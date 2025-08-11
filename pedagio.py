l, d = map(int, input().split())
k, p = map(int, input().split())

pedagios = l // d
value = l * k + pedagios * p
print(f"{value:.0f}")
