from avto_vinchick_tg.filters import FilterSettings, evaluate_profile, extract_age
from avto_vinchick_tg.core_update import is_newer_version, parse_version_py
from avto_vinchick_tg.app_update import choose_windows_asset, normalize_tag


def test_extract_age_prefers_age_marker():
    assert extract_age("Маша, 23 года\nлюблю дайвинг") == 23


def test_rejects_banned_text_and_short_profile():
    settings = FilterSettings(banned_text=["астрология"], min_words=5)

    result = evaluate_profile("20 лет, астрология", settings)

    assert not result.accepted
    assert any("астрология" in reason for reason in result.reasons)
    assert any("слов" in reason for reason in result.reasons)


def test_accepts_profile_matching_required_regex():
    settings = FilterSettings(min_age=18, max_age=30, required_regex=[r"\bpython\b"])

    result = evaluate_profile("Катя, 24 года. Пишу на Python и люблю спорт.", settings)

    assert result.accepted
    assert result.age == 24


def test_parse_core_version():
    assert parse_version_py('__version__ = "0.4.30"') == "0.4.30"


def test_detect_newer_core_version():
    assert is_newer_version("0.4.30", "0.4.29")
    assert not is_newer_version("0.4.29", "0.4.29")


def test_normalize_app_release_tag():
    assert normalize_tag("v0.1.2") == "0.1.2"


def test_choose_windows_installer_asset():
    asset = choose_windows_asset(
        [
            {"name": "tool.exe", "browser_download_url": "https://example.test/tool.exe"},
            {
                "name": "AvtoVinchickTG-Setup-0.1.2.exe",
                "browser_download_url": "https://example.test/AvtoVinchickTG-Setup-0.1.2.exe",
            },
        ]
    )

    assert asset["name"] == "AvtoVinchickTG-Setup-0.1.2.exe"
