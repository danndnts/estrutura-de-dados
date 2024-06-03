# Lista para armazenar as médias dos alunos
medias = []

# Solicitar as notas de 10 alunos
for i in range(10):
    print(f"Aluno {i+1}")
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a nota {j+1}: "))
        notas.append(nota)
    
    # Calcular a média das notas do aluno
    media = sum(notas) / len(notas)
    medias.append(media)

# Contar o número de alunos com média maior ou igual a 7.0
alunos_com_media_alta = sum(1 for media in medias if media >= 7.0)

# Imprimir o resultado
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_com_media_alta}")
