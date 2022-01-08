from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(data):
        simple_report = SimpleReport().generate(data)
        companies = [date["nome_da_empresa"] for date in data]
        stock = ""

        for company in set(companies):
            stock += (
                "- " + company + ": " + str(companies.count(company)) + "\n"
            )

        return f"{simple_report}\n\nProdutos estocados por empresa: \n{stock}"


# print(CompleteReport.generate(teste))
