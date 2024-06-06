from pydantic import *
from typing import Annotated

class Atleta(BaseModel):
    nome  : Annotated[str, Field(description="Nome do atleta", examples="Baku Stark", max_lenght=50)]
    cpf   : Annotated[str, Field(description="CPF do atleta", examples="123.456.789.12", max_lenght=11)]
    idade : Annotated[int, Field(description="Idade do atleta", max_lenght=2)]
    peso  : Annotated[PositiveFloat, Field(description="Peso do atleta", examples="75.6")]
    altura: Annotated[PositiveFloat, Field(description="Peso do atleta", examples="1.78")]
    sexo  : Annotated[str, Field(description="Sexo do atleta", examples="M", max_lenght=1)]