import json
from inventory_report.importer.importer import Importer


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

    def import_data(path):
        return JsonImporter.readType(path)
