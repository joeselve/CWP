dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

def find_the_red_head(dic):
    l = []
    for i, j in dic.items():
        if j == "red":
            l.append(i)
    return l

print(find_the_red_head(dupont_family))