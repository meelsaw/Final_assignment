import json
import xml.etree.ElementTree as et
import pickle
import os


class FileHandler:

    def create_json(self, output_dict):
        """
        helper method creates a json file
        :param output_dict: dict with the data to be written into json file
        :return: json file
        """
        directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        json_file_path = os.path.join(directory, "final_output.json")
        output = open(json_file_path, "w")
        json.dump(output_dict, output, indent=4, sort_keys=False)
        output.close()
        return output

    def create_xml(self, output_dict):
        """
        helper method creates a xml file
        :param output_dict: dict with the data to be written into xml file
        :return: xml file
        """
        directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        xml_doc = et.Element("data")
        for key, value in output_dict.items():
            element = et.SubElement(xml_doc, key)
            element.text = value
        xml_file = os.path.join(directory, "final_output.xml")
        tree = et.ElementTree(xml_doc)
        tree.write(xml_file, encoding='utf-8', xml_declaration=True)
        return xml_file

    def create_binary(self, output_dict):
        """
        helper method creates a binary file
        :param output_dict: dict with the data to be written into file
        :return: binary file
        """
        directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        bin_file = os.path.join(directory, "final_output.bin")
        with open(bin_file, 'wb') as binary_file:
            pickle.dump(output_dict, binary_file)
        return bin_file

    def get_request_dict(self, **kwargs):
        """
        helper method creats a dict with request details
        :param kwargs: file name and format
        :return: file object and requested format
        """
        file_obj = str()
        format_type = str()
        for key, value in kwargs.items():
            if key == "file":
                file_obj += value
            elif key == "format":
                format_type += value
        return file_obj, format_type

    def get_client_dict(self, **kwargs):
        """
        helper method prepares data to be written in the requested format
        :param kwargs: file and format type
        :return: file object, requested format and str to be written on file
        """
        file_obj, format_type = self.get_request_dict(**kwargs)
        output_dict = {"content": ""}
        with open(file_obj) as f:
            for line in f:
                output_dict["content"] += line
        return output_dict, file_obj, format_type

    def convert_file(self, **kwargs):
        """
        a method converts txt file to json/xml/binary
        :param kwargs: file and desired format
        :return: json/xml/binary file
        """
        output_dict, file_obj, format_type = self.get_client_dict(**kwargs)
        with open(file_obj) as f:
            for line in f:
                output_dict["content"] += line
        if format_type == "JSON":
            return self.create_json(output_dict)
        elif format_type == "XML":
            return self.create_xml(output_dict)
        elif format_type == "BINARY":
            return self.create_binary(output_dict)
        else:
            message = "Invalid format request"
            print(message)
            return message

    def create_txt(self, input_str):
        """
        a method writes input str into txt
        :param input_str: to be written into txt
        :return: txt file
        """
        try:
            file_name = "output_file.txt"
            with open(file_name, "w") as f:
                f.write(input_str)
                return file_name
        except Exception as e:
            return str(e)
