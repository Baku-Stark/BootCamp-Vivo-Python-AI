import os, csv
from pathlib import Path

path = r"{}".format("nova_path")
if not Path(path).is_dir():
    os.mkdir("nova_path")

try:

    with open(f"{path}/arquivo.csv", "w", encoding="utf-8", newline='') as file:
        """
            Colocar o conteúdo no arquivo.
        """
        writer = csv.writer(file)

        writer.writerow(["Nome", "Idade"])
        writer.writerow(["Wallace", 23])
        writer.writerow(["Satoru", 29])
        writer.writerow(["Zoro", 21])
        file.close()

    with open(f"{path}/arquivo.csv", "a", encoding="utf-8", newline='') as file:
        """
            Insirer mais conteúdo no arquivo.
        """
        writer = csv.writer(file)

        writer.writerow(["Aokiji", 45])
        file.close()

    with open(f"{path}/arquivo.csv", "r", encoding="utf-8", newline='') as file:
        """
            Ler o conteúdo no arquivo.
        """
        reader = csv.reader(file)

        for idx, row in enumerate(reader):
            if idx != 0:
                print(f"Nome: {row[0]} - Idade: {row[1]}")

        file.close()

except FileNotFoundError:
    print("O arquivo não pode ser encontrado")

except IOError:
    print("[x] O arquivo não pode ser aberto")
    print(IOError)