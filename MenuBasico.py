import os

while True:
    os.system("cls")
    print("seja bem-vindo")
    print("(0) sair")
    print("(1) abrir calculadora")
    print("(2) desligar computador")
    print("(3) trocar cor (azul)")
    opcao = input()
    if opcao == "0":
        break
    elif opcao == "1":
        os.system("calc")
    elif opcao == "2":
        os.system("shutdown/s")
    elif opcao == "3":
        os.system("color 3")