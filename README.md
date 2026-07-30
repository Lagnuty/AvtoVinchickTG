# AvtoVinchickTG

Windows GUI для Telegram-only фильтрации анкет из чата/бота Дайвинчика.

В основе лежит `Lagnuty/tg-api-zapret` в папке `core`: приложение использует его Telethon-слой для входа в пользовательский Telegram-аккаунт, SOCKS5H proxy и чтение сообщений. Текущая версия приложения: `0.1.5`, ядра: `0.4.30`.

## Что уже есть

- Окно с настройками телефона, bot token, `chat_id`, исходного чата и proxy.
- Вход в Telegram по коду и 2FA.
- Запуск слушателя сообщений из `LeomatchBot` или другого указанного чата.
- Отправка подходящих анкет в ваш бот через Bot API.
- Фильтры по тексту, обязательным словам, regex, количеству слов/символов, возрасту, ссылкам, mentions и наличию фото/медиа.
- Настройки и Telegram-сессия хранятся рядом с проектом в `.data`, а в exe-сборке рядом с exe в `data`.
- Автопроверка обновлений приложения через GitHub Releases. Если вышла новая версия, появится кнопка `Доступно обновление v...`; обновление скачивает и запускает MSI-установщик.

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

## Сборка MSI

WiX Toolset ожидается здесь:

```text
D:\Documents\AIprojects\tools\wix\wix.exe
```

Сборка:

```powershell
.\build_msi.ps1
```

MSI запускается как обычный wizard и дает выбрать папку установки. Автообновление приложения использует тот же MSI, но ставит обновление в текущую папку приложения в тихом режиме.

Готовый MSI будет здесь:

```text
dist\msi\AvtoVinchickTG-0.1.5.msi
```

## Публикация обновления

Автообновление смотрит latest release в `Lagnuty/AvtoVinchickTG`.

Для релиза соберите MSI и загрузите asset:

```text
dist\msi\AvtoVinchickTG-0.1.5.msi
```

Имя asset должно содержать `AvtoVinchickTG` и иметь расширение `.msi`, например:

```text
AvtoVinchickTG-0.1.5.msi
```

Tag релиза должен быть вида `v0.1.5` или `0.1.5`. После скачивания приложение закроется, запустит `msiexec` в silent-режиме и перезапустится.
