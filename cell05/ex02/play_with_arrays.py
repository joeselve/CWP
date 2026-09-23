before = [2, 8, 9, 48, 8, 22, -12, 2]
after = []
after_after = []

for num in before:
    after.append(num + 2)

for num in after:
    if num > 5:
        after_after.append(num)

print(f"{before}")
print(f"{after_after}")