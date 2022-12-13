
def getCount(a, b):
    m, n = len(a), len(b)
    look = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(n + 1):
        look[0][i] = 0
    for i in range(m + 1):
        look[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if a[i - 1] == b[j - 1]:
                look[i][j] = look[i - 1][j - 1] + look[i - 1][j]
            else:
                look[i][j] = look[i - 1][j]
    return look[m][n]


a = 'bienvenido a creed and bear'
b = 'bienbienvenido a creeandedandbear and beaar'

print('count:', getCount(b, a))

c = 'hola'
d = 'Un oso cogió un hilo dental para limpiar sus dientes'

print('count:', getCount(d, c))

e = 'papaya'
f = 'me gustan las peras'

print('count:', getCount(f, e))

h = 'But man is not made for defeat'
i = 'But man is not made for defeat… A man can be destroyed but not defeated.'

print('count:', getCount(i, h))

j = 'Hell is empty'
k = 'Hellhelly is emptyempty and all the devils are here.'

print('count:', getCount(k, j))

l = 'who refuses to be what he is.'
m = 'Man is the only creaturecreature who refuses to bebe what he isss.'

print('count:', getCount(m, l))


