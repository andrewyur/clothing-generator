"""The Clothing class contains information on,
color, weight, layering priority."""
class Clothing:
    def __init__(self, c, w, l):

        self.color = c
        self.weight = w
        self.layerReq = l

class Tops(Clothing):
    def __init__(self, ):