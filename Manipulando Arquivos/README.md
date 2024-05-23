# Manipulando Arquivos com Python

**Python Version:**  ![Python Version](https://img.shields.io/badge/Python-3.11.2-green)

## 01 - Abrindo e Fechando um arquivo

```py
# fabrir o arquivo
with open("arquivo.txt", "w", encoding="utf-8") as file:
    file.close() # fechar o arquivo
``` 

## 02 - Lendo Um Arquivo

```py
with open("arquivo.txt", "r", encoding="utf-8") as file:
    """
        Ler o conteúdo no arquivo.
    """
    print(file.read())
    file.close()
```

## 03 - Escrevendo Em Um Arquivo

```py
with open("arquivo.txt", "w", encoding="utf-8") as file:
    """
        Colocar o conteúdo no arquivo.
    """

    file.write("Texto para leitura\n")
    file.close()

with open("arquivo.txt", "a", encoding="utf-8") as file:
    """
        Insirer mais conteúdo no arquivo.
    """
    file.write("--Novo texto adicionado")
    file.close()
```