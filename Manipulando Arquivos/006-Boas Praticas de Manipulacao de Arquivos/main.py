import os, shutil

os.mkdir("nova_path")

path = r"{}".format("nova_path")

try:

    with open(f"{path}/arquivo.txt", "w", encoding="utf-8") as file:
        """
            Colocar o conteúdo no arquivo.
        """

        file.write("Texto para leitura\n")
        file.close()

    with open(f"{path}/arquivo.txt", "a", encoding="utf-8") as file:
        """
            Insirer mais conteúdo no arquivo.
        """
        file.write("--Novo texto adicionado")
        file.close()

    with open(f"{path}/arquivo.txt", "r", encoding="utf-8") as file:
        """
            Ler o conteúdo no arquivo.
        """
        print(file.read())
        file.close()

except IOError:
    print("[x] O arquivo não pode ser aberto")
    print(IOError)