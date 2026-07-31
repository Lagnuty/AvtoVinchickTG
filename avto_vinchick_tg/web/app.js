const state = { config: null, logs: [] };

const ids = [
  "phone", "bot_token", "notify_chat_id", "source_chat", "proxy_url",
  "banned_text", "required_text", "banned_regex", "required_regex",
  "min_words", "max_words", "min_chars", "max_chars", "min_age", "max_age",
  "reject_without_age", "require_photo", "reject_links", "reject_mentions", "send_rejects_to_log",
  "taste_enabled", "taste_min_score", "taste_min_samples",
  "accepted_action", "auto_skip_rejected", "auto_open_found", "ignore_ads", "forward_likes"
];

document.querySelectorAll(".nav-item").forEach((button) => {
  button.addEventListener("click", () => showView(button.dataset.view, button.textContent));
});

bind("refreshStatus", "click", refresh);
bind("clearLog", "click", () => { state.logs = []; renderLogs(); });
bind("checkProxy", "click", () => post("/api/proxy/check", { proxy_url: val("proxy_url") }));
bind("sendCode", "click", () => post("/api/telegram/send-code", collectConfig()));
bind("submitCode", "click", () => post("/api/telegram/submit-code", { code: val("code") }));
bind("submitPassword", "click", () => post("/api/telegram/submit-password", { password: val("password") }));
bind("testBot", "click", () => post("/api/bot/test", collectConfig()));
bind("findChatId", "click", findChatId);
bind("saveBot", "click", saveConfig);
bind("saveAll", "click", saveConfig);
bind("startRunner", "click", () => post("/api/runner/start", collectConfig()).then(refresh));
bind("stopRunner", "click", () => post("/api/runner/stop", {}).then(refresh));
bind("checkUpdates", "click", () => post("/api/updates/check", collectConfig()).then(refresh));
bind("installUpdate", "click", () => post("/api/updates/install", collectConfig()));
bind("importTaste", "click", importTaste);
bind("exportFiltersBtn", "click", exportFilters);
bind("importFiltersBtn", "click", () => document.getElementById("filterFile").click());
bind("filterFile", "change", importFilters);

ids.forEach((id) => {
  const el = document.getElementById(id);
  if (el) el.addEventListener("change", () => { state.config = collectConfig(); });
});

refresh();
setInterval(refresh, 2500);

function showView(name, title) {
  document.querySelectorAll(".view").forEach((view) => view.classList.toggle("active", view.id === name));
  document.querySelectorAll(".nav-item").forEach((item) => item.classList.toggle("active", item.dataset.view === name));
  document.getElementById("pageTitle").textContent = title;
}

async function refresh() {
  const data = await get("/api/status");
  state.config = data.config;
  applyConfig(data.config);
  state.logs = data.logs || [];
  document.getElementById("versionBadge").textContent = `app v${data.app_version}`;
  document.getElementById("coreBadge").textContent = `core v${data.core_version}`;
  document.getElementById("runnerStatus").textContent = data.running ? "Запущен" : "Остановлен";
  document.getElementById("runPill").textContent = data.running ? "Слушатель запущен" : "Слушатель остановлен";
  document.getElementById("tasteTotal").textContent = data.taste_samples.total;
  document.getElementById("tastePositive").textContent = data.taste_samples.positive;
  document.getElementById("tasteNegative").textContent = data.taste_samples.negative;
  document.getElementById("installUpdate").classList.toggle("hidden", !data.latest_release);
  renderLogs();
}

function applyConfig(config) {
  setVal("phone", config.phone);
  setVal("bot_token", config.bot_token);
  setVal("notify_chat_id", config.notify_chat_id);
  setVal("source_chat", config.source_chat);
  setVal("proxy_url", config.proxy_url);
  const filters = config.filters || {};
  setVal("banned_text", filters.banned_text);
  setVal("required_text", filters.required_text);
  setVal("banned_regex", filters.banned_regex);
  setVal("required_regex", filters.required_regex);
  ["min_words", "max_words", "min_chars", "max_chars", "min_age", "max_age"].forEach((id) => setVal(id, filters[id] || ""));
  ["reject_without_age", "require_photo", "reject_links", "reject_mentions"].forEach((id) => setChecked(id, !!filters[id]));
  setChecked("send_rejects_to_log", !!config.send_rejects_to_log);
  const taste = config.taste || {};
  setChecked("taste_enabled", !!taste.enabled);
  setVal("taste_min_score", taste.min_score ?? 55);
  setVal("taste_min_samples", taste.min_samples ?? 8);
  const dv = config.dv_actions || {};
  setVal("accepted_action", dv.accepted_action || "notify");
  ["auto_skip_rejected", "auto_open_found", "ignore_ads", "forward_likes"].forEach((id) => setChecked(id, !!dv[id]));
}

function collectConfig() {
  return {
    phone: val("phone"),
    bot_token: val("bot_token"),
    notify_chat_id: val("notify_chat_id"),
    source_chat: val("source_chat") || "LeomatchBot",
    proxy_url: val("proxy_url"),
    filters: {
      banned_text: val("banned_text"),
      required_text: val("required_text"),
      banned_regex: val("banned_regex"),
      required_regex: val("required_regex"),
      min_words: num("min_words"),
      max_words: num("max_words"),
      min_chars: num("min_chars"),
      max_chars: num("max_chars"),
      min_age: num("min_age"),
      max_age: num("max_age"),
      reject_without_age: checked("reject_without_age"),
      require_photo: checked("require_photo"),
      reject_links: checked("reject_links"),
      reject_mentions: checked("reject_mentions")
    },
    taste: {
      enabled: checked("taste_enabled"),
      min_score: num("taste_min_score") || 55,
      min_samples: num("taste_min_samples") || 8
    },
    dv_actions: {
      accepted_action: val("accepted_action") || "notify",
      auto_skip_rejected: checked("auto_skip_rejected"),
      auto_open_found: checked("auto_open_found"),
      ignore_ads: checked("ignore_ads"),
      forward_likes: checked("forward_likes")
    },
    send_rejects_to_log: checked("send_rejects_to_log")
  };
}

async function saveConfig() {
  await post("/api/config", collectConfig());
  await refresh();
}

async function findChatId() {
  const result = await post("/api/bot/find-chat-id", collectConfig());
  if (result.chat_id) setVal("notify_chat_id", result.chat_id);
  await saveConfig();
}

async function importTaste() {
  const file = document.getElementById("tasteFile").files[0];
  if (!file) return toast("Выберите Telegram export .zip или result.json");
  const bytes = await file.arrayBuffer();
  await fetch("/api/taste/import", {
    method: "POST",
    headers: { "X-Filename": encodeURIComponent(file.name) },
    body: bytes
  }).then(checkResponse);
  await refresh();
}

async function exportFilters() {
  const profile = await post("/api/filter-profile/export", collectConfig());
  downloadJson(profile, "avto_vinchick_filters.json");
}

async function importFilters() {
  const file = document.getElementById("filterFile").files[0];
  if (!file) return;
  const profile = JSON.parse(await file.text());
  const config = await post("/api/filter-profile/import", profile);
  state.config = config;
  applyConfig(config);
  await refresh();
}

function renderLogs() {
  const log = document.getElementById("logView");
  log.textContent = state.logs.join("\n");
  log.scrollTop = log.scrollHeight;
}

async function get(url) {
  return fetch(url).then(checkResponse);
}

async function post(url, payload) {
  const data = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload || {})
  }).then(checkResponse);
  if (data && data.error) toast(data.error);
  else toast("Готово");
  return data;
}

async function checkResponse(response) {
  const data = await response.json();
  if (!response.ok || data.error) throw new Error(data.error || response.statusText);
  return data;
}

function downloadJson(payload, filename) {
  const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  link.click();
  URL.revokeObjectURL(url);
}

function bind(id, event, handler) {
  const el = document.getElementById(id);
  if (el) el.addEventListener(event, (...args) => Promise.resolve(handler(...args)).catch((error) => toast(error.message)));
}

function val(id) { return document.getElementById(id)?.value?.trim() || ""; }
function setVal(id, value) { const el = document.getElementById(id); if (el && document.activeElement !== el) el.value = value ?? ""; }
function checked(id) { return !!document.getElementById(id)?.checked; }
function setChecked(id, value) { const el = document.getElementById(id); if (el) el.checked = !!value; }
function num(id) { return Math.max(0, Number.parseInt(val(id) || "0", 10) || 0); }

function toast(message) {
  const el = document.getElementById("toast");
  el.textContent = message;
  el.classList.remove("hidden");
  clearTimeout(toast.timer);
  toast.timer = setTimeout(() => el.classList.add("hidden"), 2800);
}
