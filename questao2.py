# Criação do dicionário com os números favoritos
numeros_favoritos = {
    "Daniel": 15,
    "Pedro": 5,
    "Lucas": 7,
    "Zinho": 10,
    "Ryan": 1
}
print("Nossos números favoritos:")
# Mostrando o nome de cada pessoa e seu número favorito
for nome, numero in numeros_favoritos.items():
    print(f"{nome}: {numero}")
