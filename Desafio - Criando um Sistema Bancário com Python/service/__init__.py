"""
    Profile 
    ---------- 
    Author : Baku - Stark 
    Info   : Application colors. 
"""

import os, re
from platform import *
  
class Colors:
    BLACK =     '\033[1;30m'
    RED =       '\033[31m'
    GREEN =     '\033[32m'
    YELLOW =    '\033[33m'
    BLUE =      '\033[34m'
    PURPLE =    '\033[35m'
    CYAN =      '\033[36m'
    WHITE =     '\033[37m'
    GRAY =      '\033[90m'
  
    BACK_RED =       '\033[1;41m'
    BACK_GREEN =     '\033[1;42m'
    BACK_YELLOW =    '\033[1;43m'
    BACK_BLUE =      '\033[1;44m'
    BACK_PURPLE =    '\033[1;45m'
    BACK_CYAN =      '\033[1;46m'
    BACK_WHITE =     '\033[1;47m'
    BACK_GRAY =      '\033[1;40m'
  
    END =       '\033[m'

class OperationalSys:
    @classmethod
    def clean_console(self) -> None:
        if system() == "Linux":
            os.system("clear")

        else:
            os.system("cls")

class RegexSys:
    @classmethod
    def model_cpf(self, cpf : str) -> str:
        cpf_model = ""

        if len(cpf) == 11:
            for index in range(0, len(cpf)):
                # print(f"{index} - {cpf[index]}")
                if index == 3 or index == 6:
                    cpf_model += f".{cpf[index]}"

                elif index == 9:
                    cpf_model += f"-{cpf[index]}"

                else:
                    cpf_model += cpf[index]

        return cpf_model

    @classmethod
    def match_cpf(self, cpf : str) -> bool:
        """
            Seguir modelo: 123.456.789-89

            args:
                cpf - String

            return:
                boolean
        """

        cpf_regex = re.compile(r"^([0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2})$")

        return True if re.match(cpf_regex, cpf) else False