from inventory_report.reports.simple_report import SimpleReport
from datetime import datetime
import statistics


class CompleteReport(SimpleReport):
    def generate(data):
        today = datetime.today().strftime("%Y-%m-%d")
        dates = [date["data_de_fabricacao"] for date in data]
        validity = [
            date["data_de_validade"]
            for date in data
            if date["data_de_validade"] >= today
        ]
        companies = [date["nome_da_empresa"] for date in data]
        stock = ""
        for company in set(companies):
            stock += (
                "- " + company + ": " + str(companies.count(company)) + "\n"
            )
        return (
            "Data de fabricação mais antiga: "
            + min(dates)
            + "\nData de validade mais próxima: "
            + min(validity)
            + "\nEmpresa com maior quantidade de produtos estocados: "
            + statistics.mode(companies)
            + "\n\nProdutos estocados por empresa:\n"
            + stock
            + '\n'
        )
