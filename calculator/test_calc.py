import subprocess
import sys
import unittest
from pathlib import Path


class CalculatorTest(unittest.TestCase):
    def test_retries_after_invalid_first_number(self):
        script = Path(__file__).with_name("calc.py")
        result = subprocess.run(
            [sys.executable, str(script)],
            input="abc\n2\n+\n3\nn\n",
            capture_output=True,
            text=True,
            timeout=5,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Please enter a valid number.", result.stdout)
        self.assertEqual(result.stdout.count("Enter First Number:"), 2)
        self.assertRegex(result.stdout, r"Result:\s+5\.0\b")


if __name__ == "__main__":
    unittest.main()