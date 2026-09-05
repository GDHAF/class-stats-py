import sys
import csv
import pandas as pd
import matplotlib.pyplot as plt
from src.Calculos.classe import Calc_Classes





def main():

    #Uso do arquivo CSV para entrada de dados
    path = input("Digite o caminho do arquivo CSV:")
    with open(path, 'r') as file:
        reader = csv.reader(file)
        n_valores = [float(row[0] + "." + row[1]) for row in reader]


    print("-------------------------------------")
    print("Definindo classes:")
    classe = Calc_Classes("Exemplo", n_valores)

    print("-------------------------------------")
    print("Definindo Frequências e Médias:")

    for i, classe_info in enumerate(classe.classes):
        print(f"Classe {i + 1}: [{classe_info['Min']}, {classe_info['Max']}] - Frequência: {classe_info['Freq']} - Frequência Absoluta: {classe_info['Freq_Abs']} - Frequência Relativa: {classe_info['Freq_Rel']} - Frequência Relativa Absoluta: {classe_info['Freq_Rel_Abs']} - Média da Classe: {classe_info['Med_Class']} - Média Ponderada: {classe_info['Med_Pond']} - Média Quadrática: {classe_info['Med_Quad']}")

    print("-------------------------------------")
    print(f"Média Geral: {classe.media}")
    print(f"Mediana: {classe.mediana}")
    print(f"Moda: {classe.moda}")
    print(f"Variância: {classe.variancia}")
    print(f"Desvio Padrão: {classe.desvio}")

    summary = (
        f"Média Geral: {classe.media}\n"
        f"Mediana: {classe.mediana}\n"
        f"Moda: {classe.moda}\n"
        f"Variância: {classe.variancia}\n"
        f"Desvio Padrão: {classe.desvio}"
    )

    df = pd.DataFrame(classe.classes)

    # Criando a imagem referente ao DataFrame e ao resumo estatístico
    fig, ax = plt.subplots(figsize=(12, 6))  # Set the figure size
    ax.axis('off')

    plt.text(0.01, 0.95, summary, transform=ax.transAxes, fontsize=12, verticalalignment='top', fontfamily='monospace')


    # Criar a tabela com os dados do DataFrame
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', bbox=[0, 0, 1, 0.65])

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    for key, cell in table.get_celld().items():
        cell.set_linewidth(0.5)
        # Highlight headers with a light gray background color
        if key[0] == 0:
            cell.set_facecolor('#eaeaea')


    # Salvar a imagem criada em formato .PNG
    plt.savefig('resultado_estatistico.png', bbox_inches='tight', dpi=300)
    print("A imagem 'resultado_estatistico.png' foi criada com sucesso.")

if(__name__ == "__main__"):
    main()
        
        