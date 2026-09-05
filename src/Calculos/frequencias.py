from .basic_calculos import Basic
#from .classe import Calc_Classes as Classe

class Calc_Frequencias():
    def __init__(self, name, Classes):
        self.name = name
        self.classe = Classes

    def frequencias(self, valores) -> list:
        # ---------------------------------------------------
        #             Calcula as frequências
        # ---------------------------------------------------

        if len(self.classe.classes) <= 0:
            raise ValueError("O número de classes deve ser maior que zero.")

        for i in self.classe.classes:
            aux = 0
            for j in valores:
                if i['Min'] <= j < i['Max']:
                    aux += 1
            i['Freq'] = int(aux)

    def freq_absoluta(self):
        # ---------------------------------------------------
        #             Calcula a frequência absoluta
        # ---------------------------------------------------

        if len(self.classe.classes) <= 0:
            raise ValueError("O número de classes deve ser maior que zero.")

        aux = 0
        for i in self.classe.classes:
            aux += i['Freq']  # Frequência
            i['Freq_Abs'] = int(aux)

    def freq_relativa(self):
        # ---------------------------------------------------
        #             Calcula a frequência relativa
        # ---------------------------------------------------

        if len(self.classe.classes) <= 0:
            raise ValueError("O número de classes deve ser maior que zero.")

        
        for i in self.classe.classes:
            i['Freq_Rel'] = str(round(i['Freq'] * 100 / self.classe.n_valores, self.classe.decimais)) + "%" # Frequência relativa em Porcentagem (%)
            i['Freq_Rel_Abs'] = str(round(i['Freq_Abs'] * 100 / self.classe.n_valores, self.classe.decimais)) + "%"  # Frequência relativa absoluta em Porcentagem (%)
