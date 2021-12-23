import numpy as np


class RNN:
    def __init__(self, Wx, Wh, b):
        self.parms = [Wx, Wh, b]
        self.grads = [np.zeros_like(Wx), np.zeros_like(Wh), np.zeros_like(b)]
        self.cache = None
    
    def forward(self, x, h_prev):
        Wx, Wh, b = self.parms
        t= np.matmul(h_prec, Wh) + 
