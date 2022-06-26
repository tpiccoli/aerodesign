# -*- coding: utf-8 -*-
"""
Created on Mon May 16 10:48:20 2022

@author: Tiago Piccoli

Cálculos de coeficientes de sustentação e arrasto para perfis aerodinâmicos.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#leitura dos arquivos contendo cada perfil de asa por coordenadas unitárias, em csv.
#depois criar arquivo separado para git e dropbox com caminhos genéricos

df1=pd.read_csv('xf-e423-il-200000.csv',sep=',',header=9, usecols=['Alpha','Cl','Cd','Cm'])
df2=pd.read_csv('xf-e423-il-500000.csv',sep=',',header=9, usecols=['Alpha','Cl','Cd','Cm'])
df3=pd.read_csv('xf-naca4412-il-200000.csv',sep=',',header=9, usecols=['Alpha','Cl','Cd','Cm'])
df4=pd.read_csv('xf-naca4412-il-500000.csv',sep=',',header=9, usecols=['Alpha','Cl','Cd','Cm'])
df5=pd.read_csv('xf-naca23021-il-200000.csv',sep=',',header=9, usecols=['Alpha','Cl','Cd','Cm'])
df6=pd.read_csv('xf-naca23021-il-500000.csv',sep=',',header=9, usecols=['Alpha','Cl','Cd','Cm'])
df7=pd.read_csv('xf-s1210-il-200000.csv',sep=',',header=9, usecols=['Alpha','Cl','Cd','Cm'])
df8=pd.read_csv('xf-s1210-il-500000.csv',sep=',',header=9, usecols=['Alpha','Cl','Cd','Cm'])
df9=pd.read_csv('xf-s1223-il-200000.csv',sep=',',header=9, usecols=['Alpha','Cl','Cd','Cm'])
df10=pd.read_csv('xf-s1223-il-500000.csv',sep=',',header=9, usecols=['Alpha','Cl','Cd','Cm'])

#utilizar linhas abaixo para geração de perfis com RE= 1e6
df11=pd.read_csv('xf-naca23021-il-1000000.csv',sep=',',header=9, usecols=['Alpha','Cl','Cd','Cm'])
df12=pd.read_csv('xf-s1210-il-1000000.csv',sep=',',header=9, usecols=['Alpha','Cl','Cd','Cm'])
df13=pd.read_csv('xf-s1223-il-1000000.csv',sep=',',header=9, usecols=['Alpha','Cl','Cd','Cm'])
df14=pd.read_csv('xf-e423-il-1000000.csv',sep=',',header=9, usecols=['Alpha','Cl','Cd','Cm'])
df15=pd.read_csv('xf-naca4412-il-1000000.csv',sep=',',header=9, usecols=['Alpha','Cl','Cd','Cm'])

#geração dos gráficos

'''
#geração dos gráficos 'Cl x Alpha de Perfis - (RE = 200.000)
ax = df1.plot(x='Alpha',y='Cl', label='E423',kind='line',title='Cl x Alpha de Perfis - (RE = 200.000)')
df3.plot(ax=ax,x='Alpha',y='Cl',label='NACA-4412-il', kind='line')
df5.plot(ax=ax,x='Alpha',y='Cl',label='NACA-23021-il', kind='line')
df7.plot(ax=ax,x='Alpha',y='Cl',label='SELLIG-1210-il', kind='line')
df9.plot(ax=ax,x='Alpha',y='Cl',label='SELLIG-1223-il', kind='line')
#plt.savefig('Cl x Alpha de Perfis - RE 200000.jpg')
plt.show()

#geração dos gráficos 'Cl x Alpha de Perfis - (RE = 500.000)
ax = df2.plot(x='Alpha',y='Cl', label='E423',kind='line',title='Cl x Alpha de Perfis - (RE = 500.000)')
df4.plot(ax=ax,x='Alpha',y='Cl',label='NACA-4412-il', kind='line')
df6.plot(ax=ax,x='Alpha',y='Cl',label='NACA-23021-il', kind='line')
df8.plot(ax=ax,x='Alpha',y='Cl',label='SELLIG-1210-il', kind='line')
df10.plot(ax=ax,x='Alpha',y='Cl',label='SELLIG-1223-il', kind='line')
#plt.savefig('Cl x Alpha de Perfis - RE 500000.jpg')
plt.show()

#geração dos gráficos 'Cd x Alpha de Perfis - (RE = 200.000)
ax = df1.plot(x='Alpha',y='Cd', label='E423',kind='line',title='Cd x Alpha de Perfis - (RE = 200.000)')
df3.plot(ax=ax,x='Alpha',y='Cd',label='NACA-4412-il', kind='line')
df5.plot(ax=ax,x='Alpha',y='Cd',label='NACA-23021-il', kind='line')
df7.plot(ax=ax,x='Alpha',y='Cd',label='SELLIG-1210-il', kind='line')
df9.plot(ax=ax,x='Alpha',y='Cd',label='SELLIG-1223-il', kind='line')
#plt.savefig('Cd x Alpha de Perfis - RE 200000.jpg')
plt.show()

#geração dos gráficos 'Cd x Alpha de Perfis - (RE = 500.000)
ax = df2.plot(x='Alpha',y='Cd', label='E423',kind='line',title='Cd x Alpha de Perfis - (RE = 500.000)')
df4.plot(ax=ax,x='Alpha',y='Cd',label='NACA-4412-il', kind='line')
df6.plot(ax=ax,x='Alpha',y='Cd',label='NACA-23021-il', kind='line')
df8.plot(ax=ax,x='Alpha',y='Cd',label='SELLIG-1210-il', kind='line')
df10.plot(ax=ax,x='Alpha',y='Cd',label='SELLIG-1223-il', kind='line')
#plt.savefig('Cd x Alpha de Perfis - RE 500000.jpg')
plt.show()


#geração dos gráficos 'Cm x Alpha de Perfis - (RE = 200.000)
ax = df1.plot(x='Alpha',y='Cm', label='E423',kind='line',title='Cm x Alpha de Perfis - (RE = 200.000)')
df3.plot(ax=ax,x='Alpha',y='Cm',label='NACA-4412-il', kind='line')
df5.plot(ax=ax,x='Alpha',y='Cm',label='NACA-23021-il', kind='line')
df7.plot(ax=ax,x='Alpha',y='Cm',label='SELLIG-1210-il', kind='line')
df9.plot(ax=ax,x='Alpha',y='Cm',label='SELLIG-1223-il', kind='line')
#plt.savefig('Cm x Alpha de Perfis - RE 200000.jpg')
plt.show()

#geração dos gráficos 'Cm x Alpha de Perfis - (RE = 500.000)
ax = df2.plot(x='Alpha',y='Cm', label='E423',kind='line',title='Cm x Alpha de Perfis - (RE = 500.000)')
df4.plot(ax=ax,x='Alpha',y='Cm',label='NACA-4412-il', kind='line')
df6.plot(ax=ax,x='Alpha',y='Cm',label='NACA-23021-il', kind='line')
df8.plot(ax=ax,x='Alpha',y='Cm',label='SELLIG-1210-il', kind='line')
df10.plot(ax=ax,x='Alpha',y='Cm',label='SELLIG-1223-il', kind='line')
#plt.savefig('Cm x Alpha de Perfis - RE 500000.jpg')
plt.show()


#geração dos gráficos (Cl,Cd,Cm) x Alpha de Perfis - (RE = 1.000.000)
#curvas cl
ax = df11.plot(x='Alpha',y='Cl', label='NACA-23021-il',kind='line',title='Cl x Alpha de Perfis - (RE = 1.000.000)')
df12.plot(ax=ax,x='Alpha',y='Cl',label='SELLIG-1210-il', kind='line')
df13.plot(ax=ax,x='Alpha',y='Cl',label='SELLIG-1223-il', kind='line')
df14.plot(ax=ax,x='Alpha',y='Cl',label='E423', kind='line')
df15.plot(ax=ax,x='Alpha',y='Cl',label='NACA-4412-il', kind='line')
#plt.savefig('Cl x Alpha de Perfis - RE 1e6.jpg')
plt.show()

#curvas Cd
ax = df11.plot(x='Alpha',y='Cd', label='NACA-23021-il',kind='line',title='Cd x Alpha de Perfis - (RE = 1.000.000)')
df12.plot(ax=ax,x='Alpha',y='Cd',label='SELLIG-1210-il', kind='line')
df13.plot(ax=ax,x='Alpha',y='Cd',label='SELLIG-1223-il', kind='line')
df14.plot(ax=ax,x='Alpha',y='Cd',label='E423', kind='line')
df15.plot(ax=ax,x='Alpha',y='Cd',label='NACA-4412-il', kind='line')
#plt.savefig('Cd x Alpha de Perfis - RE 1e6.jpg')
plt.show()

#curvas Cm
ax = df11.plot(x='Alpha',y='Cm', label='NACA-23021-il',kind='line',title='Cm x Alpha de Perfis - (RE = 1.000.000)')
df12.plot(ax=ax,x='Alpha',y='Cm',label='SELLIG-1210-il', kind='line')
df13.plot(ax=ax,x='Alpha',y='Cm',label='SELLIG-1223-il', kind='line')
df14.plot(ax=ax,x='Alpha',y='Cm',label='E423', kind='line')
df15.plot(ax=ax,x='Alpha',y='Cm',label='NACA-4412-il', kind='line')
#plt.savefig('Cm x Alpha de Perfis - RE 1e6.jpg')
plt.show()

'''

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

angulos=np.array(df1['Alpha'])
e423_cl=np.array(df1['Cl']) 
#roda função inclinação, para obter lista dos m 
regiao_linear(inclinacao(angulos,e423_cl)) #refinamento e calculo do m úteis
#foi gerado i _removidos
#1 - Relacionar valores removidos com o vetor de ângulos
ang_lin = np.delete(angulos,i_removidos)
cl_lin = np.delete(e423_cl,i_removidos)
#incl_med=sum(incl)/len(incl)
#print(ang_lin)


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
#print(ang_lin)
#fazer função da região linear


'''Espaco para caso deseje deletar manualmente pontos que não foram removidos pela função'''
#----
pontos_del=[0,1,2]
ang_lin=np.delete(ang_lin,pontos_del)
cl_lin=np.delete(cl_lin,pontos_del)
#-----------
func_lin = np.polyfit(ang_lin,cl_lin,1).round(decimals=4) #gera regressão
legend1='f(x)='+str((func_lin[0]))+'x + '+str(func_lin[1])
plt.plot(ang_lin,cl_lin,'o', label =legend1)
plt.plot(angulos,e423_cl, label='Curva Cl')
plt.title('Curva Cl, Perfil Eppler 423')
plt.legend()
plt.show()

print('-----------')
print('A função que atende à região linear é: f(x)=', func_lin[0] ,'x + ',func_lin[1])    

