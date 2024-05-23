with open("arquivo.txt", "r") as file:
    """
        Ler o conteúdo no arquivo.
    """
    print(file.read())
    file.close()