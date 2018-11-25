import numpy
num = lambda x: numpy.random.choice(numpy.arange(0, 5), p = [0.15, 0.15, 0.15, 0.15, 0.4])

tensor = list(map((lambda x: num(x)), numpy.arange(0, 10001)))
print(f"Tensor: {tensor}")
