with open("arquivo.txt", "w") as file:
    """
        Colocar o conteúdo no arquivo.
    """

    file.write("Texto para leitura\n")
    file.close()

with open("arquivo.txt", "a") as file:
    """
        Insirer mais conteúdo no arquivo.
    """
    file.write("--Novo texto adicionado")
    file.close()