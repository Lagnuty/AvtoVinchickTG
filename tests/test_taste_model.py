from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase, main

from avto_vinchick_tg.taste_model import TasteModel


class TasteModelTest(TestCase):
    def test_live_three_does_not_train_text_model(self) -> None:
        with TemporaryDirectory() as temp_dir:
            model = TasteModel(Path(temp_dir) / "taste.json")

            self.assertFalse(model.learn("Анкета про спорт и книги, 24 года", "3"))
            self.assertEqual(model.total_samples, 0)

    def test_export_three_is_negative_description_example(self) -> None:
        with TemporaryDirectory() as temp_dir:
            export_path = Path(temp_dir) / "result.json"
            model_path = Path(temp_dir) / "taste.json"
            export_path.write_text(
                json.dumps(
                    {
                        "messages": [
                            {"text": "Катя - 24 года. Люблю спорт и книги"},
                            {"text": "1"},
                            {"text": "Маша - 25 лет. Люблю клубы"},
                            {"text": "3"},
                        ]
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )

            model = TasteModel(model_path)
            result = model.import_export(export_path)

            self.assertEqual(result.imported, 2)
            self.assertEqual(result.positive, 1)
            self.assertEqual(result.negative, 1)
            self.assertEqual(model.positive_samples, 1)
            self.assertEqual(model.negative_samples, 1)


if __name__ == "__main__":
    main()
