import numpy as np

class RedMulticapa:
    def __init__(self, lr, inputs=3, outputLayer=False):
        self.lr = lr
        self.inputs = inputs
        self.outputLayer = outputLayer
        self.w = np.zeros(inputs)
        for i in range(self.inputs):
            self.w[i] = np.random.uniform(-1, 1)
        self.y = np.zeros(0)
        self.GradienteLocal = 0
        self.derivatives = []
        self.a = []
        self.n = []
        self.s = []

    def Suposicion(self, p):
        return self.sigmoidal(np.dot(p, self.w))

    def sigmoidal(self, x, derivative=False):
        if derivative:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))

    def ObtenerSalida(self, p):
        self.y = self.Suposicion(p)

    def hessiana(self, CapaAnteriorY=None, CapaSiguiente=None, PuntoY=None):
        if self.outputLayer:
            sigmoidal = self.sigmoidal(self.y, True)
            error = PuntoY - self.y
            self.GradienteLocal = sigmoidal * error
        else:
            sigmoidal = self.sigmoidal(self.y, True)
            wSum = sum(CapaSiguiente.w)
            self.GradienteLocal = sigmoidal * wSum * CapaSiguiente.GradienteLocal
        for i in range(self.inputs):
            self.w[i] += self.GradienteLocal * CapaAnteriorY[i] * self.lr
            
    def jacobian(self, error):
        self.s = []
        self.derivatives = []
        num_layers = len(self.a)
        output_layer = num_layers - 1
        for i in reversed(range(1, num_layers)):
            is_output_layer = i == output_layer
            a = self.a[i] if is_output_layer else np.delete(self.a[i], 0, 0)
            d = self.sigmoidal(a)
            derivatives = np.diag(d.reshape((d.shape[0],)))
            self.derivatives = [derivatives] + self.derivatives
            if is_output_layer:
                s = np.dot(derivatives, error)
                self.s.append(s)
            else:
                weights = np.delete(self.weights[i], 0, 1)
                jacobian_matrix = np.dot(derivatives, weights.T)
                s = np.dot(jacobian_matrix, self.s[0])
                self.s = [s] + self.s

    def levemberg_marquardt(self, inputs, target):
        self.a = []
        self.n = []
        activation_values = inputs
        for w in self.weights:
            activation_values = np.insert(activation_values, 0, -1)
            activation_values = activation_values.reshape((activation_values.shape[0], 1))
            self.a.append(activation_values)
            net_inputs = np.dot(w, activation_values)
            self.n.append(net_inputs)
            activation_values = self.sigmoidal(net_inputs)
        self.a.append(activation_values)
        error = target - activation_values
        self.jacobian(error)
        self.gradient_descent(self.lr)

    def gradient_descent(self, lr):
        for i in range(len(self.weights)):
            new_w = self.weights[i] + lr * np.dot(self.s[i], self.a[i].T)
            self.weights[i] = new_w

