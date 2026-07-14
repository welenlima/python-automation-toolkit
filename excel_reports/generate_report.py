import pandas as pd


def create_report(input_file, output_file):

    # Ler dados de vendas
    df = pd.read_csv(input_file)

    # Criar coluna de faturamento
    df["Faturamento"] = (
        df["Quantidade"] * df["Valor"]
    )

    # Criar resumo
    summary = {
        "Total de vendas": len(df),
        "Faturamento total": df["Faturamento"].sum(),
        "Produto mais vendido": (
            df.groupby("Produto")["Quantidade"]
            .sum()
            .idxmax()
        )
    }

    # Transformar resumo em tabela
    summary_df = pd.DataFrame(
        [summary]
    )

    # Exportar relatório Excel
    with pd.ExcelWriter(output_file) as writer:
        df.to_excel(
            writer,
            sheet_name="Vendas",
            index=False
        )

        summary_df.to_excel(
            writer,
            sheet_name="Resumo",
            index=False
        )

    print("Relatório criado com sucesso!")


if __name__ == "__main__":

    create_report(
        "vendas.csv",
        "relatorio_vendas.xlsx"
    )
