import unittest


class TestString(unittest.TestCase):
    def test_should_capitalize_string(self):
        string = "hello"
        expected_value = "Hello"
        self.assertEqual(string.capitalize(), expected_value)

    def test_should_upper_string(self):
        string = "hello"
        expected_value = "HELLo"
        self.assertEqual(string.upper(), expected_value)

    def test_should_trim_string(self):
        string = "  hello "
        expected_value = "hello"
        self.assertEqual(string.strip(), expected_value)


if __name__ == "__main__":
    unittest.main()
