from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:

    def import_data(path, type):
        with open(path, mode='r') as csv_file:
            data = list(csv.DictReader(csv_file, delimiter=','))
        switch = {
            "simples": SimpleReport,
            "completo": CompleteReport,
        }
        return switch[type].generate(data)
