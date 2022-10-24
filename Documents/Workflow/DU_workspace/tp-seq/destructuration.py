# Remplacer les ... par une seule instruction
# sans écrire de constantes littérales (1, 2...)
# Le programme doit s'exécute sans aucune erreur
s = [1, 2, 3, 4]

c0, b0, a0, d0 = s

assert a0 == 3 and b0 == 2 and c0 == 1 and d0 == 4

a1, *b1 = s

assert a1 == 1 and b1 == [2, 3, 4]

b2, *c2, a2 = s

assert a2 == 4 and b2 == 1 and c2 == [2, 3]

*b3, c3, a3 = s

assert a3 == 4 and b3 == [1, 2] and c3 == 3

print('ok')