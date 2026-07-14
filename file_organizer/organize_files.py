from pathlib import Path
import shutil


def organize_files(folder):

    folder = Path(folder)

    if not folder.exists():
        print("Pasta não encontrada.")
        return

    extensions = {
        ".pdf": "PDFs",
        ".jpg": "Imagens",
        ".png": "Imagens",
        ".xlsx": "Planilhas",
        ".csv": "Dados",
        ".txt": "Textos"
    }

    for file in folder.iterdir():

        if file.is_file():

            folder_name = extensions.get(
                file.suffix.lower(),
                "Outros"
            )

            destination = folder / folder_name

            destination.mkdir(exist_ok=True)

            shutil.move(
                str(file),
                str(destination / file.name)
            )

            print(f"Movido: {file.name}")


if __name__ == "__main__":

    path = input(
        "Digite o caminho da pasta: "
    )

    organize_files(path)
