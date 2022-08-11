import struct

class Texture: 
    def __init__(self, path):
        self.path = path
        self.read()
        
    def read(self):
        with open(self.path, 'rb') as image:
            image.seek()