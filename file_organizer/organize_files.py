import os
import shutil


def organize_folder(folder):

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):

            extension = filename.split(".")[-1]

            destination = os.path.join(folder, extension)

            os.makedirs(destination, exist_ok=True)

            shutil.move(file_path, destination)


if __name__ == "__main__":

    folder = input("Digite o caminho da pasta: ")

    organize_folder(folder)

    print("Arquivos organizados com sucesso!")
