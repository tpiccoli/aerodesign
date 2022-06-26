Utilização do programa 'airfoils_curves_graphs.py'
@tpiccoli
#---------------------

Programa para geração de gráficos relacionando coeficientes aerodinâmicos de aerofólios com o ângulo de inclinação, e para auxiliar
na obtenção da equação para região linear. Desenvolvido exlusivamente para estudos de aeronave para a competição estudantil SAE Aerodesign.

Executar o arquivo preferencialmente em um interpretador Python - Anaconda, VSCode, IDLE, PyCharm, etc.

1 - Os dados de coeficientes dos aerofólios devem estar em arquivos .csv. Você pode usar o site AirFoilTools para obter os coeficientes de aerofólios em formato .csv;
2 - Salvar os arquivos contendo os coeficientes na mesma pasta em que está salvo o código;
3 - Para alterar o caminho dos arquivos .csv e intervalo de leitura, alterar essas propriedades nas linhas dedicadas para leitura pelo Pandas DataFrame (linhas 16 a 32);
4 - Para deixar o código limpo, podem ser excluidas ou suprimidas as linhas 37 a 118, conforme necessidade.
5 - Alterar variáveis das linhas 154 e 155 conforme necessidade - suprimir linhas abaixo caso não seja necessário a geração da função da região linear;
6 - Variável "pontos_del" na linha 185 utilizada para remover manualmente os pontos a serem desconsiderados da região linear;
7 - Executar o código.

OBS: Separador decimal - PONTO.

-------------------------------------------------------------------------------------------------------------------------------------------------
Code for generating graphs relating airfoil airfoils to pitch angle, and to obtain the equation for linear region. 
Developed exclusively for aircraft studies for the SAE Aerodesign university competition.


Run the file preferably in a Python interpreter - Anaconda, VSCode, IDLE, PyCharm, etc.

1 - The airfoil coefficient data must be in .csv files. You can use the AirFoilTools website to get the airfoil coefficients in .csv format;
2 - Save the files containing the coefficients in the same folder where the code is saved;
3 - To change the path of the .csv files and reading range in file, change these properties in the lines dedicated to reading by Pandas DataFrame (lines 16 to 32);
4 - To make the code clean, lines 37 to 118 can be deleted or suppressed, as needed.
5 - Change variables in lines 154 and 155 as needed - suppress lines below if it is not necessary to generate the linear region function;
6 - Variable "pontos_del" in line 185 used to manually remove the points (by index) to be disregarded from the linear region. Useful for remove points scattered outside the region;
7 - Run the code.

NOTE: Decimal separator - DOT.