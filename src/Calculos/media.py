from .basic_calculos import Basic
#from .classe import Calc_Classes as Classe

class Calc_Medias():
    def __init__(self, name, Classes):
        self.name = name
        self.classe = Classes


    def media_classes(self):
        # ---------------------------------------------------
        #             Calcula a média das classes
        # ---------------------------------------------------

        if len(self.classe.classes) <= 0:
            raise ValueError("O número de classes deve ser maior que zero.")

        for i in self.classe.classes:
            i['Med_Class'] = round((i['Min'] + i['Max']) / 2, self.classe.decimais)  # Média da classe


    def media_ponderada(self):
        # ---------------------------------------------------
        #             Calcula a média ponderada
        # ---------------------------------------------------

        if len(self.classe.classes) <= 0:
            raise ValueError("O número de classes deve ser maior que zero.")

        for i in self.classe.classes:
            i['Med_Pond'] = round(i['Freq'] * i['Med_Class'], self.classe.decimais)  # Média ponderada da classe


    def media_geral(self):
        # ---------------------------------------------------
        #             Calcula a média geral
        # ---------------------------------------------------

        if len(self.classe.classes) <= 0:
            raise ValueError("O número de classes deve ser maior que zero.")

        total_ponderado = sum(i['Med_Pond'] for i in self.classe.classes)
        media_geral = total_ponderado / self.classe.n_valores
        return round(media_geral, self.classe.decimais)


    def calc_mediana(self):
        # ---------------------------------------------------
        #             Calcula a mediana
        # ---------------------------------------------------

        if len(self.classe.classes) <= 0:
            raise ValueError("O número de classes deve ser maior que zero.")

        n = 1
        f_ant = 0

        # Implementação da mediana aqui
        for i in self.classe.classes:

            if float(i['Freq_Rel_Abs'].strip('%')) >= 50:  # Frequência relativa acumulada >= 50%
                mediana = i['Min'] + (((((self.classe.n_valores + 1) / 2) - f_ant) / i['Freq']) * self.classe.amp_classe )
                return round(mediana, self.classe.decimais)
                
            
            f_ant = i['Freq']  # Frequência relativa acumulada da classe anterior


    def calc_moda(self):
        # ---------------------------------------------------
        #             Calcula a moda
        # ---------------------------------------------------

        if len(self.classe.classes) <= 0:
            raise ValueError("O número de classes deve ser maior que zero.")

        for i in self.classe.classes:
            if i['Freq'] == max(j['Freq'] for j in self.classe.classes):
                moda = (i['Min'] + i['Max']) / 2
                return round(moda, self.classe.decimais)


    def media_quad(self):
        # ---------------------------------------------------
        #             Calcula a média quadrática
        # ---------------------------------------------------
    
        if len(self.classe.classes) <= 0:
            raise ValueError("O número de classes deve ser maior que zero.")
    
        for i in self.classe.classes:
            m = ((i['Med_Class'] - self.classe.media) ** 2)  * i['Freq']  # Média quadrática da classe
            i['Med_Quad'] = round(m, self.classe.decimais*2)  # Adiciona a média quadrática da classe à lista de classes
    