nome = input("Digite o seu nome;")

idade = int(input("Qua a sua idade?"))

print(f"Bem vindo {nome}, voce tem {idade} anos.")

print("Como posso te ajudar hoje")

def menu ():
    print("1 - Bebidas")
    print("2 - Salgados")
    print("3 - Doces")

    opc_user=int(input("Digite o número a opção desejada:"))

    if opc_user == 1:
        print("Temos coca, fanta e guaraná")

    elif opc_user == 2:
        print("Temos coxinha, risole e empadão")

    elif opc_user == 3:
        print("Temos brigadeiro")

    else:
        print("Opção incorreta! Digite um número de 1 a 3")