import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, threshold=0.0, max_iterations=1000):
        self.weights = np.random.rand(input_size)
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations

    def activate(self, net_input):
        return int(net_input >= self.threshold)

    def train(self, input_data, labels):
        for _ in range(self.max_iterations):
            converged = all(self._update_weights(np.array(input_vector), label) == 0 for input_vector, label in zip(input_data, labels))
            if converged:
                break

    def _update_weights(self, input_vector, label):
        error = label - self.activate(np.dot(input_vector, self.weights))
        self.weights += self.learning_rate * error * input_vector
        return error

# Example usage
input_data = [[0, 0], [0, 1], [1, 0], [1, 1]]
labels = [0, 0, 0, 1]

perceptron = Perceptron(input_size=2)
iterations = perceptron.train(input_data, labels)

print(f"Converged in {iterations} iterations")
print("Final weights:", perceptron.weights)
