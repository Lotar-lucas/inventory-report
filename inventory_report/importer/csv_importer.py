import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def file_type(path):
        return path.split(".")[1]

    def readType(path):
        if CsvImporter.file_type(path) != "csv":
            raise ValueError("Arquivo inválido")
        with open(path, mode="r") as csv_file:
            out = list(csv.DictReader(csv_file, delimiter=","))
        return out

    def import_data(path):
        return CsvImporter.readType(path)
