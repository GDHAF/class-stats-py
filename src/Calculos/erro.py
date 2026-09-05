from .basic_calculos import Basic

class Calc_Erro():
    def __init__(self, name, Classes):
        self.name = name
        self.classe = Classes


    def variancia(self):
        # ---------------------------------------------------
        #             Calcula a variância
        # ---------------------------------------------------

        if self.classe.n_valores <= 0:
            raise ValueError("O número de valores deve ser maior que zero.")

        total_quad = sum(i['Med_Quad'] for i in self.classe.classes)

        return round(total_quad / self.classe.n_valores, self.classe.decimais*2)

    def desvio_padrao(self):
        # ---------------------------------------------------
        #             Calcula o desvio padrão
        # ---------------------------------------------------

        if self.classe.n_valores <= 0:
            raise ValueError("O número de valores deve ser maior que zero.")

        return round(self.variancia() ** 0.5, self.classe.decimais*2)
