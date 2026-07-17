def generate_square(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        result.append('*' * i)
    return result[::-1]

for row in generate_square(5):
    print(row)