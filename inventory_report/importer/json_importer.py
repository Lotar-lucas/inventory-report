import json
from inventory_report.importer.importer import Importer
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class JsonImporter(Importer):
    def file_type(path):
        return path.split(".")[1]

    def readType(path):
        if JsonImporter.file_type(path) != "json":
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            jsonFile = file.read()
            out = json.loads(jsonFile)
        return out

    def import_data(path, type):
        data = JsonImporter.readType(path)
        switch = {
            "simples": SimpleReport,
            "completo": CompleteReport,
        }
        return switch[type].generate(data)
