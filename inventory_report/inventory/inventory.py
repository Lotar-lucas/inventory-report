from inventory_report.importer.importer import Importer
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory(Importer):
    @staticmethod
    def readType(path):
        file_type = path.split(".")[1]

        if file_type == "csv":
            return Importer.CsvImporter(path)
        elif file_type == "json":
            return Importer.JsonImporter(path)
        else:
            return Importer.XmlImporter(path)

    def import_data(path, type):
        data = Inventory.readType(path)
        switch = {
            "simples": SimpleReport,
            "completo": CompleteReport,
        }
        return switch[type].generate(data)
