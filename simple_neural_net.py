import numpy as np 

class NeuralNetwork():
	

	def __init__(self):
		np.random.seed(1)

		a = open("weights.txt", "r")
		a1 = a.read()
		a.close()
		a1 = a1.split()
		a1 = np.array([a1])
		a1 = a1.astype(float)
		a1 = a1.T


		self.synaptic_weights = a1
		

	def sigmoid(self, x):
		return 1 / (1 + np.exp(-x))

	def sigmoid_derivative(self, x):
		return x * (1 - x)

	def train(self, training_inputs = [[]], training_outputs = [[]], training_iterations = 0):
		
		if training_inputs == [[]]:
			a = open("inputs.txt", "r")
			a1 = a.read()
			a.close()
			a1 = a1.split()
			a1 = np.array([a1])
			a1 = a1.astype(int)
			a1 = a1.reshape(-1, 3)

			training_inputs = a1
		else:
			a = open("inputs.txt","w")
			for i in training_inputs:
				for j in i:
					a.write(str(j)+"\n")
		
		if training_outputs == [[]]:
			a = open("outputs.txt", "r")
			a1 = a.read()
			a.close()
			a1 = a1.split()
			a1 = np.array([a1])
			a1 = a1.astype(int)
			a1 = a1.reshape(-1, 1)

			training_outputs = a1
		else:
			a = open("outputs.txt","w")
			for i in training_outputs:
				for j in i:
					a.write(str(j)+"\n")

		if training_iterations == 0:
			training_iterations = 100

		a = open("weights.txt","w")
		for i in self.synaptic_weights:
			for j in i:
				a.write(str(j)+"\n")

		for iteration in range(training_iterations):

			output = self.think(training_inputs)

			error = training_outputs - output

			adjustments =np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

			self.synaptic_weights += adjustments

		a = open("weights.txt","w")
		for i in self.synaptic_weights:
			for j in i:
				a.write(str(j)+"\n")

	
				

	def think(self, inputs):

		inputs = inputs.astype(float)

		output = self.sigmoid(np.dot(inputs, self.synaptic_weights))

		return output


		

if __name__ == "__main__":

		neuralnetwork = NeuralNetwork()

		iterations = 100

		print('Current Synaptic weights ')



		print(neuralnetwork.synaptic_weights)

		

		a = open("inputs.txt", "r")
		a1 = a.read()
		a.close()
		a1 = a1.split()
		a1 = np.array([a1])
		a1 = a1.astype(int)
		a1 = a1.reshape(-1, 3)

		training_inputs = a1

		
		a = open("outputs.txt", "r")
		a1 = a.read()
		a.close()
		a1 = a1.split()
		a1 = np.array([a1])
		a1 = a1.astype(int)
		a1 = a1.reshape(-1, 1)

		training_outputs = a1

		choice = "main"

		while True:


			if choice == "main":
				print("Enter command")
				choice = str(input()).strip()
		
			if choice == "train":
				neuralnetwork.train(training_inputs, training_outputs, iterations)

				print("synaptic_weights after training: ")
				print(neuralnetwork.synaptic_weights)

			if choice == "addin":
				a = str(input("Input 1: "))
				b = str(input("Input 2: "))
				c = str(input("Input 3: "))

				training_inputs = np.append(training_inputs,np.array([[a,b,c]]).astype(int)).reshape(-1, 3)

				d = str(input("Output: "))

				training_outputs = np.append(training_outputs,np.array([d]).astype(int)).reshape(-1, 1)



				print("New situation: \ninput data = ",training_inputs)
				print("Output data= ",training_outputs)
				neuralnetwork.train(training_inputs, training_outputs, iterations)
				print("synaptic_weights after training: ")
				print(neuralnetwork.synaptic_weights)
				a = open("outputs.txt","w")
				for i in training_outputs:
					for j in i:
						a.write(str(j)+"\n")

				a = open("inputs.txt","w")
				for i in training_inputs:
					for j in i:
						a.write(str(j)+"\n")

				a = open("weights.txt","w")
				for i in neuralnetwork.synaptic_weights:
					for j in i:
						a.write(str(j)+"\n")


			if choice == "curr":
				print("Current situation: \ninput data = ",training_inputs)
				print("Output data= ",training_outputs)
				print("synaptic_weights after training: ")
				print(neuralnetwork.synaptic_weights)



			if choice == "exit":
				break

			choice = str(input()).strip()

			


		


		

		