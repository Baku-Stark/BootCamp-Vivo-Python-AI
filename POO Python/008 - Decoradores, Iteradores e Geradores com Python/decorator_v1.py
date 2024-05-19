class Decorator:
    @staticmethod
    def calculadora(operador : str):
        def soma(a, b):
            return a + b
        
        def subtrair(a, b):
            return a - b
        
        def multiplicar(a, b):
            return a * b
        
        def dividir(a, b):
            return a // b
        
        def potencia(a, b):
            return a ** b
        
        match operador:
            case "soma":
                return soma(5, 5)
            
            case "subtrair":
                return subtrair(15, 5)
            
            case "multi":
                return multiplicar(5, 5)
            
            case "div":
                return dividir(5, 5)
            
            case "pot":
                return potencia
            
print(Decorator.calculadora("soma"))
print(Decorator.calculadora("subtrair"))
print(Decorator.calculadora("multi"))
print(Decorator.calculadora("div"))
print(Decorator.calculadora("pot")(5, 2)) # 25

print('')
def meu_decorador(funcao):
    def envelope():
        print("=" * 10)
        funcao()
        print("=" * 10)
    return envelope
    
@meu_decorador
def ola_mundo():
    print("Olá, mundo!")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()