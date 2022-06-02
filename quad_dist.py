import sympy as sp

def aQuad(ratio, N):
    a = sp.Symbol('a')
    f = ((a - 1) * pow((1/N - 1), 2) + 1) - ratio
    return sp.solve(f)[0]

def kNQuad(ratio, N):
    a = aQuad(ratio, N)
    kN = (2/(a+1)) * N + (((a-1) * (N - 1) * (2 * N - 1)) / ((a+1) * 3 * N))
    return kN

def fiQuad(i, ratio, N):
    a = aQuad(ratio, N)
    kN = kNQuad(ratio, N)
    fi = (1/kN) * (((2 * (a - 1)) / (a + 1)) * pow((i/N - 1), 2) + 2 / (a + 1))
    return fi

def listFiQuad(ratio, N):
    # returns list of values of all mlm leg links with "ratio" being the ratio between last and first link and "N" being the number of links within the chain
    list = []
    for i in range(1, N + 1):
        list.append(fiQuad(i, ratio, N))
    return list
