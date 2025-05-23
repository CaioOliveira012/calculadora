def calculadora():
    while True:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        print("Selecione a operação: ")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        escolha = input("Digite sua escolha: ")

        match escolha:
            case'1':
                print("Resultado: ")
            case '2':
                print("Resultado: ")
            case'3':
                print("Resultado: ")
            case'4':
                print("Resultado: ")
            case'0':
                print("Saindo da calculadora")
                break
            case _:
                print("Opção inválida. Tente Novamente")
calculadora()