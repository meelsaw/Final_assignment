import json
import xml.etree.ElementTree as et
import pickle


class FileHandler:

    def convert_file(self, **kwargs):
        file_obj = str()
        format_type = str()
        for key, value in kwargs.items():
            if key == "file_name":
                file_obj += value
            elif key == "format":
                format_type += value
        output_dict = {"content": ""}
        with open(file_obj) as f:
            for line in f:
                output_dict["content"] += line
        if format_type == "JSON":
            final_output = open("final_output.json", "w")
            json.dump(output_dict, final_output, indent=4, sort_keys=False)
            final_output.close()
            return final_output
        elif format_type == "XML":
            xml_doc = et.Element("data")
            for key, value in output_dict.items():
                element = et.SubElement(xml_doc, key)
                element.text = value
            xml_file_path = 'final_output.xml'
            tree = et.ElementTree(xml_doc)
            tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)
            return xml_file_path
        elif format_type == "BINARY":
            bin_file_path = 'final_output.bin'
            with open(bin_file_path, 'wb') as binary_file:
                pickle.dump(output_dict, binary_file)
            return bin_file_path
        else:
            message = "Invalid format request"
            print(message)
            return message

    def create_txt(self, input_str):
        try:
            file_name = "output_file.txt"
            with open(file_name, "w") as f:
                f.write(input_str)
                return file_name
        except Exception as e:
            return str(e)
