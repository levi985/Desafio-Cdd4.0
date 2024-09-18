m = 5 
while m == 5:
    n1 = float(input("Digite o primeiro número "))
    n2 = float(input("Digite o segundo número "))
    m = int(input("O que deseja fazer? 1-somar, 2-subtrair, 3-mutiplicar, 4-dividir, 5-inserir um novo número, 6-sair"))
    
    if m == 1:
        soma = n1 + n2
        print(f"A soma entre {n1} e {n2} é {soma}")
    elif m == 2 :
        subtracao = n1 - n2
        print(f"A subração entre entre {n1} e {n2} é {subtracao}")

    elif m == 3: 
        mutiplicacao = n1 * n2 
        print(f"A mutiplicação entre {n1} e {n2} é {mutiplicacao}")

    elif m == 4: 
        divisao = n1 / n2 
        print(f"A divisão entre {n1} e {n2} é {divisao}")

    elif m == 5:
        m=5
    else: 
        print("Você saiu do programa")
