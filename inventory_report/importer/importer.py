import json
import csv
import xml.etree.ElementTree as xml


class Importer:
    @staticmethod
    def file_type(path):
        return path.split(".")[1]

    def JsonImporter(path):
        if Importer.file_type(path) != "json":
            raise Exception
        with open(path) as file:
            jsonFile = file.read()
            out = json.loads(jsonFile)
        return out

    def CsvImporter(path):
        if Importer.file_type(path) != "csv":
            raise Exception
        with open(path, mode="r") as csv_file:
            out = list(csv.DictReader(csv_file, delimiter=","))
        return out

    def XmlImporter(path):
        if Importer.file_type(path) != "xml":
            raise Exception
        # I got some help from: https://www.py4u.net/discuss/18657
        file = xml.parse(path)
        keys = file.getroot()
        out = []
        for key in keys:
            temp = {}
            for attribute in key:
                temp[attribute.tag] = attribute.text
            out.append(temp)
        return out
