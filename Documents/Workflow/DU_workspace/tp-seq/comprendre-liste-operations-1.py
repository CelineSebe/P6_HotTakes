s = []
s.append(2)             # s ?
s.insert(0, 4)          # s ?
s.insert(20, 7)         # s ?
s[1] = 'd'              # s ?
s[2] /= s[2]            # s ?
s.count(1)              # ?
s[0], s[1] = s[1], s[0] # s ?

p, _, d = s             # p ? _ ? d ?
premier, *suite = s     # premier ? suite ?

b = [False, True]
s.extend(b)             # s ?

x = s.pop(1)            # x ? s ?

s2 = [2, 3, 5]
i, s2[i], x = s2        # i ? s2 ? x ?

s.append(s2)            # s ?
s2.append(s)            # s2 ? s ?

t = tuple(b)            # t ?
s = list('Fin.')        # s ? s2 ?
