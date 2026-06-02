import unittest
from pathlib import Path


class TestContent(unittest.TestCase):
    def test_text_contains_expected_phrase(self) -> None:
        text = Path("test.txt").read_text(encoding="utf-8")
        self.assertIn("un beau garcon", text)


if __name__ == "__main__":
    unittest.main()
