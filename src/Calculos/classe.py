import math
import pandas as pd
from .basic_calculos import Basic
from .frequencias import Calc_Frequencias as Freq
from .media import Calc_Medias as Med
from .erro import Calc_Erro as Erro

class Calc_Classes():
    def __init__(self, name, valores):
        self.name = name
        med = Med("Médias", self)
        error = Erro("Erro", self)

        self.n_valores = len(valores)  # Inicializa o número de valores
        self.n_classes = self.num_classes(valores)  # Inicializa o número de classes
        self.decimais = Basic.decimais(valores)  # Inicializa a quantidade de casas decimais
        self.amp_classe = self.amplitude_classe(valores)  # Inicializa a amplitude da classe
        self.classes = self.definir_classes(valores)  # Inicializa a lista de classes

        self.classe_build(valores)  # Constrói as classes e calcula as frequências e médias

        self.media = med.media_geral()  # Inicializa a média geral
        self.mediana = med.calc_mediana()
        self.moda = med.calc_moda()
        med.media_quad()
        self.variancia = error.variancia()
        self.desvio = error.desvio_padrao()


    def classe_build(self, valores):
        # ---------------------------------------------------
        #             Constrói as classes
        # ---------------------------------------------------

        if self.n_valores <= 0:
            raise ValueError("O número de valores deve ser maior que zero.")

        freq = Freq("Frequências", self)
        freq.frequencias(valores)
        freq.freq_absoluta()
        freq.freq_relativa()

        med = Med("Médias", self)
        med.media_classes()
        med.media_ponderada()

        
    def num_classes(self, valores) -> int:
        # ---------------------------------------------------
        #             Calcula o número de classes
        # ---------------------------------------------------

        if self.n_valores <= 0:
            raise ValueError("O número de valores deve ser maior que zero.")
        return math.ceil(self.n_valores ** 0.5)


    def amplitude_classe(self, valores) -> float:
        # ---------------------------------------------------
        #             Calcula a amplitude da classe
        # ---------------------------------------------------

        if self.n_valores <= 0:
            raise ValueError("O número de valores deve ser maior que zero.")
        return Basic.ceil(((max(valores) - min(valores))/self.n_classes), self.decimais)


    def definir_classes(self, valores):
        # ---------------------------------------------------
        #           Define os limites das classes
        # ---------------------------------------------------

        if self.n_valores <= 0:
            raise ValueError("O número de valores deve ser maior que zero.")

        amplitude = self.amp_classe

        classes = []
        Min_limit = min(valores)

        for i in range(self.n_classes):
            Max_limit = Basic.ceil(Min_limit + amplitude, self.decimais)
            classes.append({
                "Classe": int(i + 1),
                "Min": round(Min_limit, self.decimais),
                "Max": round(Max_limit, self.decimais)
            })
            Min_limit = Max_limit

        return classes