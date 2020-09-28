#archivo original
def sumar(a,b): 
    resultado= a+b
    return resultado

def restar(a,b): 
    resultado= a-b
    return resultado

def main(): 
    numero1= int(input('primer numero: '))
    numero2= int(input('escribe el segundo numero: '))
    suma= sumar(numero1, numero2)
    print(suma)
    resta= restar(numero1, numero2)
    print(resta)


if __name__ == "__main__":
    main()