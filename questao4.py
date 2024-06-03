# Lista para armazenar as idades e alturas dos alunos
alunos = []

# Solicitar a idade e altura de 30 alunos
for i in range(30):
    print(f"Aluno {i + 1}")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura (em metros): "))
    alunos.append((idade, altura))  # Armazena uma tupla (idade, altura)

# Calcular a média de altura dos alunos
total_altura = sum(aluno[1] for aluno in alunos)
media_altura = total_altura / len(alunos)

# Determinar quantos alunos com mais de 13 anos possuem altura inferior à média
contador = sum(1 for aluno in alunos if aluno[0] > 13 and aluno[1] < media_altura)

# Imprimir o resultado
print(f"Número de alunos com mais de 13 anos e altura inferior à média: {contador}")
