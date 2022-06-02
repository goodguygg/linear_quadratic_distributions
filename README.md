# linear_quadratic_distributions
This is a set of functions which allow user to input a size of a set and a ratio between the first and last value of the set. The function returns a set of values which holds the ratio true and the sum of all value is equal to 1.

For example I need a set of numbers of size 10 with ratio between the first and last value being 4.

In order to get a distribution I would call 

N = 10
ratio = 4

print(listFiLin(ratio, N))

[0.160000000000000, 0.146666666666667, 0.133333333333333, 0.120000000000000, 0.106666666666667, 0.0933333333333333, 0.0800000000000000, 0.0666666666666667, 0.0533333333333333, 0.0400000000000000]

print(listFiQuad(ratio, N))

[0.194594594594595, 0.163963963963964, 0.136936936936937, 0.113513513513514, 0.0936936936936937, 0.0774774774774775, 0.0648648648648649, 0.0558558558558558, 0.0504504504504504, 0.0486486486486487]

feel free to use something like

a = 0
for i in listFi:
    a += i
print(a)

to check the validity, and submit any issues if there is a provlem.
