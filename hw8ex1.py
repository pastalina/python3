# Задание 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько
# рукопожатий было?

n = int(input("Введите количество друзей: "))

graph = []
for i in range(n):
    row = [1] * n
    row[i] = 0
    graph.append(row)

handshakes = 0
for row in graph:
    for i in row:
        handshakes += i / 2

print(f"Всего было произведено рукопожатий: {int(handshakes)} ")
