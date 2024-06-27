import ctypes
import os

class BlueScreenDLL:
    def __init__(self, dll_path):
        self.dll = ctypes.CDLL(dll_path)
        self.dll.start.argtypes = []
        self.dll.start.restype = None

    def start(self):
        self.dll.start()

def start():
    dll_path = os.path.abspath("bst.dll")
    bluesd = BlueScreenDLL(dll_path)
    bluesd.start()
