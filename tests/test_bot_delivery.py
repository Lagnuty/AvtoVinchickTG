from __future__ import annotations

from pathlib import Path
from unittest import IsolatedAsyncioTestCase, TestCase, main

from avto_vinchick_tg.bot_api import build_multipart_body, build_multipart_body_files, is_photo_file
from avto_vinchick_tg.runner import VinchikRunner, combined_message_text, has_profile_description, with_answer_options
from avto_vinchick_tg.settings import AppConfig


class BotDeliveryTest(TestCase):
    def test_answer_options_are_visible(self) -> None:
        text = with_answer_options("Анкета")

        self.assertIn("1 - понравилась анкета", text)
        self.assertIn("2 - понравилась, лайк с посланием", text)
        self.assertIn("3 - не понравилась внешность", text)
        self.assertIn("4 - не понравилось описание", text)

    def test_photo_detection(self) -> None:
        self.assertTrue(is_photo_file(Path("profile.JPG")))
        self.assertFalse(is_photo_file(Path("profile.mp4")))

    def test_multipart_contains_fields_and_file(self) -> None:
        temp_file = Path("test_profile_photo.jpg")
        try:
            temp_file.write_bytes(b"image-bytes")
            body = build_multipart_body(
                "boundary",
                {"chat_id": "123", "caption": "Фото анкеты"},
                "photo",
                temp_file,
            )
        finally:
            temp_file.unlink(missing_ok=True)

        self.assertIn(b'name="chat_id"', body)
        self.assertIn(b'name="caption"', body)
        self.assertIn(b'name="photo"; filename="test_profile_photo.jpg"', body)
        self.assertIn(b"image-bytes", body)

    def test_media_group_multipart_contains_all_files(self) -> None:
        first = Path("test_profile_photo_1.jpg")
        second = Path("test_profile_photo_2.jpg")
        try:
            first.write_bytes(b"first-image")
            second.write_bytes(b"second-image")
            body = build_multipart_body_files(
                "boundary",
                {"chat_id": "123", "media": '[{"media":"attach://file0"},{"media":"attach://file1"}]'},
                {"file0": first, "file1": second},
            )
        finally:
            first.unlink(missing_ok=True)
            second.unlink(missing_ok=True)

        self.assertIn(b'name="media"', body)
        self.assertIn(b'name="file0"; filename="test_profile_photo_1.jpg"', body)
        self.assertIn(b'name="file1"; filename="test_profile_photo_2.jpg"', body)
        self.assertIn(b"first-image", body)
        self.assertIn(b"second-image", body)

    def test_combined_message_text_keeps_unique_album_captions(self) -> None:
        class Message:
            def __init__(self, text: str) -> None:
                self.message = text

        text = combined_message_text([Message("Анна, 24, Москва"), Message(""), Message("Анна, 24, Москва")])

        self.assertEqual(text, "Анна, 24, Москва")

    def test_profile_description_detection(self) -> None:
        self.assertFalse(has_profile_description(""))
        self.assertFalse(has_profile_description("Анна, 24, Москва"))
        self.assertFalse(has_profile_description("Анна, 24 - Москва"))
        self.assertTrue(has_profile_description("Анна, 24, Москва\nЛюблю дайвинг и вечерние прогулки"))
        self.assertTrue(has_profile_description("Анна, 24, Москва - люблю дайвинг"))


class DvMediaOnlyTest(IsolatedAsyncioTestCase):
    async def test_media_only_profile_is_disliked_without_notify(self) -> None:
        class Message:
            message = ""
            media = object()

        class Bot:
            sent = False

            def send_message(self, *args, **kwargs) -> None:
                self.sent = True

        class Client:
            def __init__(self) -> None:
                self.commands: list[tuple[str, str]] = []

            async def send_message(self, chat: str, command: str) -> None:
                self.commands.append((chat, command))

        logs: list[str] = []
        runner = VinchikRunner(logs.append)
        bot = Bot()
        client = Client()

        await runner._process_dv_messages([Message()], bot, client, AppConfig(source_chat="LeomatchBot"))

        self.assertEqual(client.commands, [("LeomatchBot", "3")])
        self.assertFalse(bot.sent)
        self.assertTrue(any("команда 3" in item for item in logs))

    async def test_header_only_profile_is_disliked_without_notify(self) -> None:
        class Message:
            message = "Анна, 24, Москва"
            media = object()

        class Bot:
            sent = False

            def send_message(self, *args, **kwargs) -> None:
                self.sent = True

        class Client:
            def __init__(self) -> None:
                self.commands: list[tuple[str, str]] = []

            async def send_message(self, chat: str, command: str) -> None:
                self.commands.append((chat, command))

        logs: list[str] = []
        runner = VinchikRunner(logs.append)
        bot = Bot()
        client = Client()

        await runner._process_dv_messages([Message()], bot, client, AppConfig(source_chat="LeomatchBot"))

        self.assertEqual(client.commands, [("LeomatchBot", "3")])
        self.assertFalse(bot.sent)


if __name__ == "__main__":
    main()
