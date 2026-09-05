import math

class Basic():
    def __init__(self, name):
        self.name = name

    @staticmethod
    def decimais(valores) -> int:
        # ---------------------------------------------------
        #  Define a quantidade de casas decimais necessárias
        # ---------------------------------------------------

        num_str = str(max(valores))
        if '.' in num_str:
            return len(num_str.split('.')[1])
        return 0


    @staticmethod
    def ceil(x, precision=0):
        # ---------------------------------------------------
        #          Arredonda para cima com precisão
        # ---------------------------------------------------

        factor = 10 ** precision
        return math.ceil(x * factor) / factor