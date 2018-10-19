
# coding: utf-8

# In[68]:


# Importamos los necesario para trabajar
import csv
import matplotlib.pyplot as plt
from random import randint as num_azar
from copy import copy
from functools import total_ordering
from string import ascii_letters, digits
from math import ceil


# In[69]:


def obtener_numero(dato):
    try:
        mayor = int(dato)
    except:
        try:
            mayor = ord(dato)
        except:
            try:
                temp = 0
                for c in dato:
                    temp += ord(c)
                mayor = temp
            except:
                try:
                    return obtener_numero(dato.valor_caracteristico())
                except:
                    try:
                        cadena = str(dato)
                        return obtener_numero(cadena)
                    except:
                        raise TypeError
    return mayor


# In[70]:


# Definimos el algoritmo de ordenamiento con el que vamos a trabajar
cont = 0
def intercambia(A,x,y): #---->C 
    global cont 
    cont = cont + 1
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
def obtenerMedio(A,p,r):
    global cont
    prom = 0
    for i in A[p : r + 1]:
        cont = cont + 1
        prom = prom + obtener_numero(i) #obtener numero()"""
    prom = prom // len( A[p : r + 1])
    
    ant = None
    pos = 0
    for i in range(len(A[p : r + 1])):
        cont = cont + 1
        act = prom - obtener_numero(A[i+p])#"""obtener numero()"""
        if(ant == None or ant > abs(act)):
            ant = abs(act)
            pos = i+p
    return pos
    
def Particionar(A,p,r):
    global cont
    """
    Aquì hay que poner obtener el medio
    y =  A.index(np.percentile(A[p:r],50,interpolation='nearest')) #n por la api
    """ 
    #if(p == 0 and r == len(A)-1):
    y = obtenerMedio(A,p,r)
    intercambia(A,y,r) #n
    x=A[r] #C
    i=p-1 #C
    for j in range(p,r): #n
        if (obtener_numero(A[j])<=obtener_numero(x)): #C
            i=i+1 #C
            intercambia(A,i,j) #C
        cont = cont + 1 #C
    intercambia(A,i+1,r) #C
    return i+1 #C

# Por lo tanto es n + n
# Particionar = n

def QuickSortHector(A,p,r): 
    global cont
    if( p<r ): #C
        q=Particionar(A,p,r) #n
        QuickSortHector(A,p,q-1)# por la separación es log(n)
        QuickSortHector(A,q+1,r)# por la separación es log(n)
    cont = cont + 1
    
def QuickSortHectorb(arreglo):
    global tiempo
    global cont
    cont = 0
    QuickSortHector(arreglo,0,len(arreglo) - 1)
    tiempo += cont
    return cont


# In[71]:


#Algoritmo quick original
def partition(arr,low,high):
    global tiempo
    tiempo += 1
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
    for j in range(low , high):
        tiempo += 1
        # If current element is smaller than or
        # equal to pivot
        if   obtener_numero(arr[j]) <= obtener_numero(pivot):
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
def quickSort(arr,low,high):
    global tiempo
    tiempo += 1
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def QuickSort(A):
    global tiempo
    quickSort(A,0,len(A)-1)
    return tiempo


# In[72]:


entro = 0
def DoubleQuickSort(arreglo):
    global tiempo
    contdir = 0
    continv = 0
    for i in range(1,len(arreglo)):
        tiempo+=1
        if(arreglo[i-1]<=arreglo[i]):
            contdir+=1
            
    if(contdir==len(arreglo)-1):
        #print("entro")
        return
    #else:
     #   print(contdir,"contador")
      #  print(len(arreglo)-1)
    
    for i in range(1,len(arreglo)):
        tiempo+=1
        if(arreglo[i-1]>=arreglo[i]):
            continv+=1
            
    if(continv == len(arreglo)-1):
        for i in range(0,ceil(len(arreglo)/2)):
            tiempo+=1
            aux = arreglo[i]
            arreglo[i] = arreglo[len(arreglo) - 1 - i]
            arreglo[len(arreglo) - 1-i] = aux
        return
    cerc = 1.6 ##Nos dirá que tanto se aproximará a el valor esperado
    if(continv >= (len(arreglo)-1)//1.7 or contdir >= (len(arreglo)-1)//1.7):
        QuickSortHectorb(arreglo)
    else:
        QuickSort(arreglo)
    


# In[73]:


def graficar(x,y,color,titulo):
    plt.plot(x,y,color)
    plt.ylabel("Iteraciones")
    plt.xlabel("Cantidad de Datos")
    plt.title(titulo)
    plt.show()
    
def graficar_chidori(titulo):
    plt.ylabel("Iteraciones")
    plt.xlabel("Cantidad de Datos")
    plt.title(titulo)
    plt.show()

def graficar_quick(x, y, color, titulo):
    #y = obtener_fila(y)
    plt.plot(x, y[0], "r")
    plt.plot(x, y[1], "g")
    plt.legend(('DoubleQuickSort', 'Quick Original'), prop = {'size':10}, loc = 'upper left')
    #plt.legend(('Caso Normal'), prop = {'size':10}, loc = 'upper left')
    graficar_chidori(titulo)


# In[74]:


def probar_algoritmo(algoritmo, conjunto):
    global tiempo
    global cont
    tiempo = 0
    algoritmo(conjunto)
    return tiempo


# In[75]:



def arregloAlAzar(numero):
    """
    Funcion que permite crear un arreglo de dimension numero con puros numeros al azar
    """
    arreglo=[]
    for i in range(numero):
        arreglo.append(num_azar(1, numero))
    return arreglo


# In[83]:


def comparacion(funcion, hector):
    """
    Funcion que permite evaluar distintas opciones a una funcion dada
    """
    color=("r","g","b","k")
    caso=("Peor caso","Mejor caso","Caso promedio","Caso Especial")
    print(funcion.__name__)
    tiempo=[]
    cantidad=[]
    for j in range(4):
        tiempo=[]
        cantidad=[]
        hector_t = []
        normal = []
        for i in range(1,300):
            azar=arregloAlAzar(i)
            if j == 0:#Peor caso
                azar.sort()    
            elif j == 1: #Mejor caso
                copia=copy(azar)
                azar.sort()
                azar.reverse()
                entero=int(float(len(azar)/2))
                numero=azar[entero]
                indice=copia.index(numero)
                #print("h:",obtenerMedio(azar, 0, len(azar) - 1), "-p:",indice)
                copia[len(copia)-1],copia[indice]=copia[indice],copia[len(copia)-1]
                azar=copia
            elif j == 3:
                
                azar.sort()
                azar.reverse()
                ##elemento a invertir
                invelm = num_azar(0,len(azar)-1)
                #invelm = 0
                #print(invelm)
                azar[len(azar)-1],azar[invelm]=azar[invelm],azar[len(azar)-1]
                if(i==299):
                    print(azar,"Lista desordenada","azar peor caso")
                    #print(entro)
            azarito = copy(azar)
            if(i==299):
                print(azarito,"Lista desordenada")
            tiempo2 = probar_algoritmo(hector,azarito)
            if(i==299):
                print(azarito,"Lista ordenada")
            hector_t.append(tiempo2)
            tiempo1=probar_algoritmo(funcion,azar)
            normal.append(tiempo1)
            tiempo = [hector_t, normal]
            cantidad.append(i)
        graficar_quick(cantidad, tiempo, color[j],caso[j])
        

comparacion(QuickSort, DoubleQuickSort)

