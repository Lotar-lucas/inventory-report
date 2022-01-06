from datetime import datetime
import statistics


class SimpleReport:
    def generate(data):
        today = datetime.today().strftime("%Y-%m-%d")
        dates = [date["data_de_fabricacao"] for date in data]
        validity = [
            date["data_de_validade"]
            for date in data
            if date["data_de_validade"] >= today
        ]
        company = [date["nome_da_empresa"] for date in data]
        return (
            "Data de fabricação mais antiga: "
            + min(dates)
            + "\nData de validade mais próxima: "
            + min(validity)
            + "\nEmpresa com maior quantidade de produtos estocados: "
            + statistics.mode(company)
            + '\n'
        )
