# -*- coding: utf-8 -*-
"""
Created on Mon May 16 10:48:20 2022

@author: Tiago Piccoli

Cálculos de coeficientes de sustentação e arrasto para perfis aerodinâmicos.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df1=pd.read_csv('xf-naca0010-il-500000.csv',sep=',',header=0, usecols=['Alpha','Cl','Cd','Cm'])
#Cálculos das funções lineares
def regiao_linear(incl):
    global i_removidos
    mediana = np.median(incl)
    #calcular desvio padrão da amostra
    dv_p=np.std(incl) #cálculo do desvio padrão
    #refinar valores eliminando m que estejam fora do range do desvpad
    i=0
    i_removidos=[] #para eliminar dos valores de x 
    for m in incl:
        if m < mediana+dv_p/40 and m > mediana-dv_p/40: #valores que atendem ao critério de refinamento
            i=i+1
        else:
            i_removidos.append(i)
            i=i+1

#-------------------------------
def inclinacao(x,y): #retorna lista de coeficientes angulares (m) para cada x
    global incl
    incl=[]
    i=0
    for x_0 in x:
        m = (x[i+1]-x[i])/(y[1+i]-y[i])
        i=i+1
        incl.append(int(m))
        if i==len(x)-1:
            break
    return incl
#-------------------------------------
def indice(n,y):
    c=0
    for i in y:
        if i==n:
            return c
        else:
            c=c+1
            pass

angulos=np.array(df1['Alpha'])
cl=np.array(df1['Cl']) 
#roda função inclinação, para obter lista dos m 
regiao_linear(inclinacao(angulos,cl)) #refinamento e calculo do m úteis

ang_lin = np.delete(angulos,i_removidos)
cl_lin = np.delete(cl,i_removidos)

i=1
i_ang_esparsos=[]
while i<len(ang_lin):
    dim=abs(ang_lin[i-1]-ang_lin[i])    
    i=i+1
    if dim>0.75:
        i_ang_esparsos.append(i)
    else:
        pass
 
ang_lin=np.delete(ang_lin,i_ang_esparsos)
cl_lin=np.delete(cl_lin,i_ang_esparsos)        

#determinar linha aproximada entr o cl. min e cl. max - função linear
#retornar posição de máx cl e min cl
m=((max(cl)-min(cl))/(angulos[indice(max(cl),cl)]-angulos[indice(min(cl),cl)])) #inclinação geral entre o intervalo de ângulos - 
y_m=[]
b=cl[indice(0,angulos)]
for x in angulos:
    y=m*x+b
    y_m.append(y)

'''
#AJUSTE PARA EQUIVALER ORIGEM À ZERO - suprimir caso necessário
aj=y_m[0]-cl[0]
aj2=y_m[29]-cl[29] #compensar 'barriga' próximo aos -5°

b=b-aj-aj2
y_m.clear()
for x in angulos:
    y=m*x+b
    y_m.append(y)
'''

print('Função linear f(x):',m,'x + ',b)

'''Espaco para caso deseje deletar manualmente pontos que não foram removidos pela função'''
pontos_del=[0,1,2,3,4,5,6,7,8,9,10,19]
if not pontos_del:
    pass
else:
    ang_lin=np.delete(ang_lin,pontos_del)
    cl_lin=np.delete(cl_lin,pontos_del)
#-----------
#geração das funções e plotagem dos gráficos para EPPLER 423
func_lin = np.polyfit(ang_lin,cl_lin,1).round(decimals=4) #gera regressão
legend1='Função linear para seção linear'
plt.plot(ang_lin,cl_lin,'^', label =legend1)
plt.plot(angulos,cl, label='Curva Cl')
plt.plot(angulos,y_m, label='Cl linear')
plt.title('Curvas Cl, Perfil Naca10')
plt.grid()
plt.legend()
plt.show()

print('-----------')
print('A função que atende à região linear é: f(x)=', func_lin[0] ,'x + ',func_lin[1]) 
print('A função aproximação é:',round(m,4),'x+ ',b)   

#bloco de notas
#diferenca=y_m[29]-cl[29]
