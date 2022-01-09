from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @staticmethod
    def readType(path):
        file_type = path.split('.')[1]
        out = []

        if(file_type == 'csv'):
            with open(path, mode='r') as csv_file:
                out = list(csv.DictReader(csv_file, delimiter=','))
            return out
        elif(file_type == 'json'):
            with open(path) as file:
                jsonFile = file.read()
                out = json.loads(jsonFile)
            return out

    def import_data(path, type):
        data = Inventory.readType(path)
        switch = {
            "simples": SimpleReport,
            "completo": CompleteReport,
        }
        return switch[type].generate(data)
