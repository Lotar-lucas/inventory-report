from ..reports import simple_report, complete_report
import csv


class Inventory():

    def import_data(path, type):
        with open(path, mode='r') as csv_file:
            data = list(csv.DictReader(csv_file, delimiter=','))

        switch = {
            "simple_report": simple_report,
            "complete_report": complete_report,
        }
        return switch[type](data)
