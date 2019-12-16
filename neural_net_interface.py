import numpy as np 
import simple_neural_net

print("Welcome")
a = str(input("Input 1: "))
b = str(input("Input 2: "))
c = str(input("Input 3: "))

nn = simple_neural_net.NeuralNetwork()

print("Output data: ")
d = nn.think(np.array([a,b,c]))
print(d) 

fb = str(input("Is the result correct?"))

if fb == 'y':
	o = open("inputs.txt", "r")
	a1 = o.read()
	o.close()
	a1 = a1.split()
	a1 = np.array([a1])
	a1 = a1.astype(int)
	a1 = a1.reshape(-1, 3)

	training_inputs = a1
	print(training_inputs)

	o = open("outputs.txt", "r")
	a1 = o.read()
	o.close()
	a1 = a1.split()
	a1 = np.array([a1])
	a1 = a1.astype(int)
	a1 = a1.reshape(-1, 1)

	training_outputs = a1

	print()
	print(training_outputs)

	training_inputs = np.append(training_inputs,np.array([[a,b,c]]).astype(int)).reshape(-1, 3)
	training_outputs = np.append(training_outputs,np.array([d]).astype(int)).reshape(-1, 1)

	a = open("outputs.txt","w")
	for i in training_outputs:
		for j in i:
			a.write(str(j)+"\n")

	a = open("inputs.txt","w")
	for i in training_inputs:
		for j in i:
			a.write(str(j)+"\n")

	a = open("weights.txt","w")
	for i in nn.synaptic_weights:
		for j in i:
			a.write(str(j)+"\n")