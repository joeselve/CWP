inp = input("")

result = ""
for cha in inp:
    if cha.islower() is True:
        result += cha.upper()
    elif cha.isupper() is True:
        result += cha.lower()
    else:
        result += cha

print(result)