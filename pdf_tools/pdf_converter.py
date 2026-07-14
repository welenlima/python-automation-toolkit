from pathlib import Path


def list_pdf_files(folder):

    folder_path = Path(folder)

    pdf_files = list(folder_path.glob("*.pdf"))

    print("Arquivos PDF encontrados:")

    for pdf in pdf_files:
        print(pdf.name)


if __name__ == "__main__":

    folder = input("Digite a pasta: ")

    list_pdf_files(folder)
