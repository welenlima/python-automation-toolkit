import pandas as pd


def create_report():

    data = {
        "Produto": [
            "Notebook",
            "Mouse",
            "Teclado",
            "Monitor"
        ],
        "Quantidade": [
            5,
            10,
            8,
            3
        ],
        "Valor": [
            3500,
            80,
            150,
            900
        ]
    }

    df = pd.DataFrame(data)

    df["Total"] = df["Quantidade"] * df["Valor"]

    df.to_excel(
        "relatorio_vendas.xlsx",
        index=False
    )

    print("Relatório criado com sucesso!")


if __name__ == "__main__":
    create_report()
