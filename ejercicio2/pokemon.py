import csv
import operator
import pandas as pd   


#pokemon = csv.reader(open('/Users/juanlu_navarro/Documents/Carrera Juan/programacion/EvaluacionTema4/ejercicio2/pokemon (1).csv'), delimiter=',')
#next(pokemon)
pokemon = pd.read_csv('/Users/juanlu_navarro/Documents/Carrera Juan/programacion/EvaluacionTema4/ejercicio2/pokemon (1).csv',header=None,skiprows=1)

class Nodo:
    def __init__(self,  numero = None, nombre=None, tipo1 = None, tipo2 = None, total = None,HP = None, attack=None, defense = None, SpA = None, SpD = None,Speed = None, Generation=None, Legendary = None, izq = None, der = None):
        self.nombre = nombre
        self.numero = numero
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.total = total
        self.HP = HP
        self.attack = attack
        self.defense = defense
        self.SpA = SpA
        self.SpD = SpD
        self.Speed = Speed
        self.Generation = Generation
        self.Legendary = Legendary
        self.izq = izq
        self.der = der

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s '%(self.numero, self.nombre, self.tipo1,self.tipo2, self.total, self.HP, self.attack, self.defense, self.SpA, self.SpD, self.Speed, self.Generation, self.Legendary)
    
class aBinarios:
    def __init__(self):
        self.raiz=None
    def agregar(self, elemento,orden):
        if self.raiz == None:
            self.raiz = elemento
        else:
            aux = self.raiz
            padre = None
            while aux != None:
                padre = aux
                if(orden == 'numero'):
                    if int(elemento.numero) >= int(aux.numero):
                        aux = aux.der 
                    else:
                        aux = aux.izq 
                
                if(orden == 'nombre'):
                    if elemento.nombre >= aux.nombre:
                        aux = aux.der 
                    else:
                        aux = aux.izq 
                 
                if(orden == 'tipo'):
                    if str(elemento.tipo) >= str(aux.tipo):
                        aux = aux.der 
                    else:
                        aux = aux.izq  
                        
            if(orden == 'numero'):    
                if int(elemento.numero) >= int(padre.numero):
                        padre.der =elemento
                else:
                        padre.izq =elemento 
            
            if(orden == 'nombre'):    
                if str(elemento.nombre) >= str(padre.nombre):
                        padre.der =elemento
                else:
                        padre.izq =elemento 
            
            if(orden == 'tipo'):    
                if str(elemento.tipo1) >= str(padre.tipo1):
                        padre.der =elemento
                else:
                        padre.izq =elemento 
                        
    def buscarNum(raiz, eleccion):
        pos = None
        if (raiz is not None):
            if raiz.numero == eleccion :
                pos = raiz
                print(raiz)
                print(pos)
            elif (raiz.izq is not None) and ( eleccion < raiz.izq.numero):
                    pos = aBinarios.buscarNum(raiz.izq, eleccion)
            else:
                    pos = aBinarios.buscarNum(raiz.der, eleccion)
        return pos    
    
    def buscarNombre(raiz, eleccion, lista):
        if (raiz is not None):
            if eleccion in raiz.nombre:
                lista.append(raiz)
            if (raiz.izq is not None):
                    aBinarios.buscarNombre(raiz.izq, eleccion, lista)
            if (raiz.der is not None):
                    aBinarios.buscarNombre(raiz.der, eleccion, lista)
               
    def porNumero(self, elemento):
        if elemento!= None:
            print(elemento)
            self.porNumero(elemento.izq)
            self.porNumero(elemento.der)

    def porNombre(self, elemento):
        if elemento!= None:
            self.porNombre(elemento.izq)
            print(elemento)
            self.porNombre(elemento.der)
            
    def porTipo(self, elemento):
        if elemento!= None:
            self.porTipo(elemento.izq)
            print(elemento)
            self.porTipo(elemento.der)    
    def getRaiz(self):
        return self.raiz
    
def cargarArbol(ab,pokemonPar,orden):
    for i in range(0,pokemonPar.shape[0]):
        nod = Nodo(pokemonPar[0][i], pokemonPar[1][i], pokemonPar[2][i],pokemonPar[3][i], pokemonPar[4][i], pokemonPar[5][i],pokemonPar[6][i], pokemonPar[7][i], pokemonPar[8][i],pokemonPar[9][i], pokemonPar[10][i], pokemonPar[11][i], pokemonPar[12][i])
        ab.agregar(nod,orden)
        
    
        

if __name__ == '__main__':
    ab = aBinarios()
    
    while(True):
        print('---menu---\n'+
              '1.Árbol por número\n'+
              '2.Árbol por nombre\n'+
              '3.Árbol por tipo\n'+
              '4.Orden por número\n'+
              '5.Orden por nombre\n'+
              '6.Orden por tipo\n'+
              '7.Buscar datos por su número de pokemon\n'+
              '8.Buscar datos por nombre de pokemon\n')
        
        num = input('Elige: ')
        if num == '1':
            cargarArbol(ab,pokemon,'numero')
        elif num == '2':
            cargarArbol(ab,pokemon,'nombre')
        elif num == '3':
            cargarArbol(ab,pokemon,'tipo')      
        elif num == '4':
            ab.porNumero(ab.getRaiz())
        elif num == '5':
            print(ab)
            ab.porNombre(ab.getRaiz())
        elif num == '6':
            ab.porTipo(ab.getRaiz())      
        elif num == '7':
            cargarArbol(ab,pokemon,'numero')
            eleccion = int(input('Seleccione un número del 1 al 721: '))
            if eleccion >= 0 or eleccion <= 721:
                salida = aBinarios.buscarNum(ab.getRaiz(), eleccion)
                print(salida)
            else:
                break
        elif num == '8':
            cargarArbol(ab,pokemon,'nombre')
            eleccion = str(input('Introduzca los caracteres a buscar: '))
            print(eleccion)
            if(eleccion.isdigit()==False):
                lista = []
                aBinarios.buscarNombre(ab.getRaiz(), eleccion, lista)
                for i in lista:
                    print(i)
            else:
                break
                          
            
            
            
            


    






                            