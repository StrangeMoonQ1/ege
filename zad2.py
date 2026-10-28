print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (x or (not(y)) or ((not(z)) and w)) == 0:
                    print(x, y, z, w)
# Памятка
# ∨ = or, ∧ = and, → = <=, ≡ = ==, ¬ = not.