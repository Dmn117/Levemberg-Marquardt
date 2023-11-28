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
