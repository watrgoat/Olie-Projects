import math

class neuron:
	def __init__(self, weight1, weight2, activate):
		self.weight1 = weight1
		self.weight2 = weight2
		self.activate = activate

	def run(self, x1, x2, b):
		total = 0
		total += self.weight1 * x1
		total += self.weight2 * x2
		total += b
		return self.activate(total)

def sigmoid(x):
	return 1/(1+math.pow(math.e, x*-1))

weight1 = 0.9
weight2 = 0.2
bias = 0.1
n1_l1 = neuron(0.1, 1, sigmoid)
n2_l1 = neuron(0.2, .4, sigmoid)
n1_l2 = neuron(n1_l1.run(weight1, weight2, bias), n2_l1.run(weight1, weight2, bias), sigmoid)

print(n1_l2.run(weight1, weight2, bias))