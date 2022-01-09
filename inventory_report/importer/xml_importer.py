import xml.etree.ElementTree as xml
from inventory_report.importer.importer import Importer
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class XmlImporter(Importer):
    def file_type(path):
        return path.split(".")[1]

    def readType(path):
        if XmlImporter.file_type(path) != "xml":
            raise ValueError("Arquivo inválido")
        file = xml.parse(path)
        keys = file.getroot()
        out = []
        for key in keys:
            temp = {}
            for attribute in key:
                temp[attribute.tag] = attribute.text
            out.append(temp)
        return out

    def import_data(path, type):
        data = XmlImporter.readType(path)
        switch = {
            "simples": SimpleReport,
            "completo": CompleteReport,
        }
        return switch[type].generate(data)
