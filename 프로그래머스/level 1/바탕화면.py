def solution(wallpapaer):
    a = []
    b = []
    for i, row in enumerate(wallpapaer):
        for j, col in enumerate(row):
            if col == "#":
                a.append(i)
                b.append(j)
    
    return [min(a), min(b), max(a)+1, max(b)+1]