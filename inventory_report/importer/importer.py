from abc import ABC


class Importer(ABC):
    def import_data(self, file):
        raise NotImplementedError
