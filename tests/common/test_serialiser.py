import unittest
from src.client.utils.serialise import Serialiser


class TestSerialiser(unittest.TestCase):
    def test_serialise_deserialise_string(self):
        serialiser = Serialiser()
        input_data = "Hello World"

        serialized_data = serialiser.serialise(input_data)
        deserialized_data = serialiser.deserialise(serialized_data)

        self.assertIsNotNone(serialized_data)
        self.assertEqual(input_data, deserialized_data)

    def test_serialise_deserialise_integer(self):
        serialiser = Serialiser()
        input_data = 474586586589769

        serialized_data = serialiser.serialise(input_data)
        deserialized_data = serialiser.deserialise(serialized_data)

        self.assertIsNotNone(serialized_data)
        self.assertEqual(input_data, deserialized_data)

    def test_serialise_deserialise_list(self):
        serialiser = Serialiser()
        input_data = ["a", "b", 3]

        serialized_data = serialiser.serialise(input_data)
        deserialized_data = serialiser.deserialise(serialized_data)

        self.assertIsNotNone(serialized_data)
        self.assertEqual(input_data, deserialized_data)

    def test_serialise_deserialise_dict(self):
        serialiser = Serialiser()
        input_data = {"age": 23, "name": "john"}

        serialized_data = serialiser.serialise(input_data)
        deserialized_data = serialiser.deserialise(serialized_data)

        self.assertIsNotNone(serialized_data)
        self.assertEqual(input_data, deserialized_data)


if __name__ == "__main__":
    unittest.main()
