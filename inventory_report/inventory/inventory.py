from ..reports import simple_report, complete_report


class Inventory():

    def import_data(path, type):
        switch = {
            "simple_report": simple_report,
            "complete_report": complete_report,
        }
        return switch[type](path)
