import functools

def meu_decorador(funcao):
    
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("=" * 10)
        funcao(**kwargs)
        print("=" * 10)
    return envelope
    
@meu_decorador
def hello(**kwargs):
    print(f"Olá, {kwargs['nome']}!")

hello(nome = "Wallace")
print(f"Function Name: {hello.__name__}")