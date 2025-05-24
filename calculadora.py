def calculadora():

    historico = []

    while True:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        print("Selecione a operação: ")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Resto da divisão")
        print("6 - Consultar histórico")
        print("7 - Raiz quadrada")
        print("8 - Potência(n1^n2)")
        print("9 - Usar último resultado como n1")
        print("10 - Salvar histórico em arquivo")
        print("0 - Sair")

        escolha = input("Digite sua escolha: ")

        match escolha:
            case'1':
                c = n1+n2
                print("Resultado: ", c)
                historico.append(f"{n1} + {n2} = {c}")
            case '2':
                c = n1-n2
                print("Resultado: ", c)
                historico.append(f"{n1} - {n2} = {c}")
            case'3':
                c = n1*n2
                print("Resultado: ", c)
                historico.append(f"{n1} * {n2} = {c}")
            case'4':
                if n2 != 0:
                    c = n1/n2
                    print("Resultado: ", c)
                    historico.append(f"{n1} / {n2} = {c}")
                else:
                    print("Divisão por 0")
            case'5':
                if n2 != 0:
                    c = n1%n2
                    print("Resultado: ", c)
                    historico.append(f"{n1} % {n2} = {c}")
                else:
                    print("Divisão por 0")
            case'6':
                
                print("Histórico: ", historico)
            case'0':
                print("Saindo da calculadora")
                break
            case _:
                print("Opção inválida. Tente Novamente")
                
        historico.append(c)
        if len(historico) > 5:
            historico.pop(0)

calculadora()