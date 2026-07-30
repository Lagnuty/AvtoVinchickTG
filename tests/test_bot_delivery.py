from __future__ import annotations

from pathlib import Path
from unittest import TestCase, main

from avto_vinchick_tg.bot_api import build_multipart_body, is_photo_file
from avto_vinchick_tg.runner import with_answer_options


class BotDeliveryTest(TestCase):
    def test_answer_options_are_visible(self) -> None:
        text = with_answer_options("Анкета")

        self.assertIn("1 - лайк", text)
        self.assertIn("2 - лайк с посланием", text)
        self.assertIn("3 - пропустить", text)

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


if __name__ == "__main__":
    main()
