i, j = 0, 0
while i <= 10:
    print(f"Table de {i}: ", end = "")
    while j <= 10:
        print(f"{i * j}", end = " ")
        j += 1
    print()
    j = 0
    i += 1