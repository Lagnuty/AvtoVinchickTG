# AvtoVinchickTG

Windows GUI для Telegram-only фильтрации анкет из чата/бота Дайвинчика.

В основе лежит `Lagnuty/tg-api-zapret` в папке `core`: приложение использует его Telethon-слой для входа в пользовательский Telegram-аккаунт, SOCKS5H proxy и чтение сообщений. Текущая версия приложения: `0.1.1`, ядра: `0.4.30`.

## Что уже есть

- Окно с настройками телефона, bot token, `chat_id`, исходного чата и proxy.
- Вход в Telegram по коду и 2FA.
- Запуск слушателя сообщений из `LeomatchBot` или другого указанного чата.
- Отправка подходящих анкет в ваш бот через Bot API.
- Фильтры по тексту, обязательным словам, regex, количеству слов/символов, возрасту, ссылкам, mentions и наличию фото/медиа.
- Настройки и Telegram-сессия хранятся рядом с проектом в `.data`, а в exe-сборке рядом с exe в `data`.

## Запуск из исходников

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -U pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

Если `python` не установлен глобально, положите portable Python в:

```text
D:\Documents\AIprojects\tools\python\python.exe
```

## Как пользоваться

1. Создайте Telegram-бота через BotFather и вставьте token.
2. Напишите своему боту любое сообщение, затем нажмите `Найти chat_id`.
3. Укажите телефон Telegram-аккаунта и proxy вида `socks5h://host:port`.
4. Нажмите `Отправить код`, введите код, затем `Войти по коду`. Если включен 2FA, введите пароль и нажмите `Войти с 2FA`.
5. Настройте фильтры и нажмите `Запуск`.

## Сборка exe

```powershell
.\build_exe.ps1
```

Готовый файл будет здесь:

```text
dist\AvtoVinchickTG\AvtoVinchickTG.exe
```
