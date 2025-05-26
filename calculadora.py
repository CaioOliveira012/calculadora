import math

def calculadora():
    historico = []
    while True:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        print("\nSelecione a operação: ")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Resto da divisão")
        print("6 - Consultar histórico")
        print("7 - Raiz quadrada de n1")
        print("8 - Potência (n1^n2)")
        print("9 - Salvar histórico em arquivo")
        print("0 - Sair")

        escolha = input("Digite sua escolha: ")

        match escolha:
            case '1':
                c = n1 + n2
                print("Resultado:", c)
                historico.append(f"{n1} + {n2} = {c}")
            case '2':
                c = n1 - n2
                print("Resultado:", c)
                historico.append(f"{n1} - {n2} = {c}")
            case '3':
                c = n1 * n2
                print("Resultado:", c)
                historico.append(f"{n1} * {n2} = {c}")
            case '4':
                if n2 != 0:
                    c = n1 / n2
                    print("Resultado:", c)
                    historico.append(f"{n1} / {n2} = {c}")
                else:
                    print("Erro: divisão por zero.")
                    continue
            case '5':
                if n2 != 0:
                    c = n1 % n2
                    print("Resultado:", c)
                    historico.append(f"{n1} % {n2} = {c}")
                else:
                    print("Erro: divisão por zero.")
                    continue
            case '6':
                print("\nHistórico:")
                for item in historico:
                    print(item)
                continue
            case '7':
                if n1 >= 0:
                    c = math.sqrt(n1)
                    print("Resultado: √", n1, "=", c)
                    historico.append(f"√{n1} = {c}")
                else:
                    print("Erro: raiz quadrada de número negativo.")
                    continue
            case '8':
                c = n1 ** n2
                print("Resultado:", c)
                historico.append(f"{n1} ^ {n2} = {c}")
            case '9':
                try:
                    with open("historico_calculadora.txt", "w") as arquivo:
                        for item in historico:
                            arquivo.write(item + "\n")
                    print("Histórico salvo com sucesso em 'historico_calculadora.txt'")
                except:
                    print("Erro ao salvar arquivo.")
                continue
            case '0':
                print("Saindo da calculadora.")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                continue

        historico.append(c)
        if len(historico) > 5:
            historico.pop(0)

calculadora()
