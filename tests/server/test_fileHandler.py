import unittest
import os
from src.server.utils.file_handler import FileHandler


class TestFileHandler(unittest.TestCase):

    def setUp(self):
        self.file_handler = FileHandler()

    def test_create_json(self):
        # test if create_json method creates a JSON file
        output_dict = {"content": "value1"}
        json_file_path = self.file_handler.create_json(output_dict)
        self.assertTrue(os.path.isfile(json_file_path))
        # clean up
        os.remove(json_file_path)

    def test_create_xml(self):
        # test if create_xml method creates an XML file
        output_dict = {"content": "value1"}
        xml_file_path = self.file_handler.create_xml(output_dict)
        self.assertTrue(os.path.isfile(xml_file_path))
        # clean up
        os.remove(xml_file_path)

    def test_create_binary(self):
        # test if create_binary method creates a binary file
        output_dict = {"content": "value1"}
        bin_file_path = self.file_handler.create_binary(output_dict)
        self.assertTrue(os.path.isfile(bin_file_path))
        # clean up
        os.remove(bin_file_path)

    def test_get_request_dict(self):
        # test if get_request_dict method constructs a dict correctly
        request_dict, format_type = self.file_handler.get_request_dict(file="file.txt", format_type="JSON")
        self.assertEqual(request_dict, "file.txt")
        self.assertEqual(format_type, "JSON")

    def test_get_client_dict(self):
        # test if get_client_dict method prepares data correctly for writing
        input_str = "Hello, world!"
        with open("input.txt", "w") as f:
            f.write(input_str)
        client_dict, file_obj, format_type = self.file_handler.get_client_dict(file="input.txt", format_type="JSON")
        self.assertEqual(client_dict, {"content": input_str})
        self.assertEqual(file_obj, "input.txt")
        self.assertEqual(format_type, "JSON")
        # clean up
        os.remove("input.txt")

    def test_convert_file_json(self):
        # test if convert_file method correctly converts to JSON
        input_str = '{"key1": "value1", "key2": "value2"}'
        with open("input.txt", "w") as f:
            f.write(input_str)
        json_file_path = self.file_handler.convert_file(file="input.txt", format_type="JSON")
        self.assertTrue(os.path.isfile(json_file_path))
        # clean up
        os.remove("input.txt")
        os.remove(json_file_path)

    def test_create_txt(self):
        # test if create_txt method creates a text file with the input string
        input_str = "Hello, world!"
        txt_file_path = self.file_handler.create_txt(input_str)
        self.assertTrue(os.path.isfile(txt_file_path))
        with open(txt_file_path, "r") as f:
            content = f.read()
        self.assertEqual(content, input_str)
        # clean up
        os.remove(txt_file_path)


if __name__ == '__main__':
    unittest.main()
