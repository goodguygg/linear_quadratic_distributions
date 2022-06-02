import sympy as sp

def aLin(ratio, N):
    a = sp.Symbol('a')
    f = (a - (a - 1) * 1/N) - ratio
    return sp.solve(f)[0]

def kNLin(ratio, N):
    a = aLin(ratio, N)
    kN = N - (a-1)/(a+1)
    return kN

def fiLin(i, ratio, N):
    a = aLin(ratio, N)
    kN = kNLin(ratio, N)
    fi = (1/kN) * ((2*a/(a + 1)) - (2*(a - 1)/(a + 1)) * (i/N))
    return fi

def listFiLin(ratio, N):
    # returns list of values of all mlm leg links with "ratio" being the ratio between last and first link and "N" being the number of links within the chain
    list = []
    for i in range(1, N + 1):
        list.append(fiLin(i, ratio, N))
    return list
