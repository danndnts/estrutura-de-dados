# Função para ler um vetor de 5 números inteiros
def ler_vetor():
    vetor = []
    for i in range(5):
        numero = int(input(f"Digite o número {i + 1}: "))
        vetor.append(numero)
    return vetor

# Função para exibir o vetor de forma criativa e engraçada
def exibir_vetor(vetor):
    print("\nPreparando para revelar os números mais incríveis que você já viu...\n")
    for i, numero in enumerate(vetor):
        print(f"📢 Número {i + 1}: 🌟 {numero} 🌟")
        if i == 0:
            print("Isso é só o começo... 🚀")
        elif i == 1:
            print("Você não vai acreditar no próximo... 🤯")
        elif i == 2:
            print("Espera, está ficando melhor... 🎉")
        elif i == 3:
            print("Quase lá, segure seu queixo... 😲")
        elif i == 4:
            print("Tcharam! O grande final! 🎆")

# Programa principal
def main():
    print("Bem-vindo ao show dos números incríveis! 🎪")
    vetor = ler_vetor()
    exibir_vetor(vetor)

# Executar o programa
if __name__ == "__main__":
    main()
