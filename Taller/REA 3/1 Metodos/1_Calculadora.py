# Ayuda niño revisar operaciones fundamentales
"""
Elaborar un algoritmo  que ayude a un niño a revisar sus tareas 
referentes a las operaciones aritméticas fundamentales: sumar, restar, 
multiplicar y dividir.  
El proceso es el siguiente: Se ofrecerá un menú de opciones para 
escoger lo que desea hacer  de acuerdo con el siguiente formato: 

TE PUEDO AYUDAR A:
1: SUMAR
2: RESTAR
3: MULTIPLICAR
4: DIVIDIR
5: FIN
OPCION: 

En caso de el niño seleccione la opción 1; está indicando que desea 
revisar operaciones de sumar, enseguida se debe establecer un proceso 
interactivo para que el niño introduzca los dos números a sumar y su resultado, 
luego que el computador le indique si la suma está correcta o incorrecta; 
en seguida le pregunte si desea revisar otra suma, si es así, 
deberá repetir todo el proceso para revisar la siguiente suma. 
Y así con las demás operaciones. 

Ejemplo:      
5 + 3 = 7       la suma es incorrecta     
5 + 3 = 8       la suma es  correcta 

"""

# Se crea la clase que contendra los datos por teclado
class AyudaNino:
    
    # Se inicializa el metodo constructor
    def __init__(self,n1,n2,resultado):
        
        # La palabra reservada (self) para nombrar el parametro del metodo
        self.n1 = n1
        self.n2 = n2
        self.resultado = resultado

    # Se inicia la funcion sumar
    def sumar(self):
        
        # La variable (total) almacenara la operacion de la suma
        total = self.n1 + self.n2
        """
        Con el bucle if se confirmara que la suma ingresada sea correcta y 
        con la palabra reservada (return) se busca dictar si la sentencia 
        se cumple o no
        """ 
        if total == resultado:
            return True
        else:
            return False
        
    # Se inicia la funcion de restar 
    def restar(self):
        
        # La variable (total) almacenara la operacion de la resta
        total = self.n1 - self.n2
        
        """
        Con el bucle if se confirmara que la resta ingresada sea correcta y 
        con la palabra reservada (return) se busca dictar si la sentencia 
        se cumple o no
        """         
        if total == resultado:
            return True
        else:
            return False

    # Se inicia la funcion de multiplicar 
    def multiplicar(self):

        # La variable (total) almacenara la operacion de la multiplicacion        
        total = self.n1 * self.n2
        
        """
        Con el bucle if se confirmara que la multiplicacion ingresada sea 
        correcta y con la palabra reservada (return) se busca dictar 
        si la sentencia se cumple o no
        """         

        # La variable (total) almacenara la operacion de la multiplicacion        
        if total == resultado:
            return True
        else:
            return False

    # Se inicia la funcion de dividir
    def dividir(self):
        
        """
        Por medio del bucle if se analiza para saber si la divicion se puede
        o no se puede hacer ya que si el divisor es cero (0) la operacion
        es imposible 
        """
        if self.n2 != 0:
            
            # La variable (total) almacenara la operacion de la division        
            total = self.n1 / self.n2
            
            """    
            Con el bucle if se confirmara que la division ingresada sea 
            correcta y con la palabra reservada (return) se busca dictar 
            si la sentencia se cumple o no
            """
            if total == resultado:
                return True
            else:
                return False
        else:
            print("No se puede dividir por cero (0)")
            return False
        
# Se crea una funcion que almacenara el menu desplegado por pantalla 
def menu():
    print("TE PUEDO AYUDAR A: \n \
    1: SUMAR\n \
    2: RESTAR\n \
    3: MULTIPLICAR\n \
    4: DIVIDIR\n \
    5: FIN")

"""
Al iniciar el bucle while directamente se pedira directamente al 
usuario los datos necesarios para hacer la secuenta poo con sus respectivos
llamados entre herencias 
"""
while True:
    
    # Se llama a la funcion (menu)
    menu()
    
    # Se pedira la opcion correspondiente al menu dado
    opcion = int(input("Opcion: "))
    
    """
    Se desplegara una serie de bucles anidados los cuales llevaran las 
    respectivas funciones de sus metodos de clase 
    """
    
    # Si la opcion es 5 (FIN) se dara un break para finalizar el programa
    if opcion == 5:
        print("Ayuda finalizada")
        break
    
    if opcion == 1:
        
        """
        Se inicia la variable que dara inicio al bucle while el cual 
        llevara consigo la serie de sentencias requeridas segun la opcion dada
        por el usuario
        """
        desea = 'S'
        while desea == 'S':
            
            # Por mensaje en pantalla se da a conocer al usuario 
            # la operacion a realizar
            print("\t***__ Te ayudo a sumar __***")
            
            # Las variables almacenaran numeros de tipo float y su resultado
            num1 = float(input("Primer numero: "))
            num2 = float(input("Segundo numero: "))
            resultado = float(input("Resultado: "))
            
            # En esta variable se hara el llamado a la clase principal
            verificador = AyudaNino(num1,num2,resultado)
            
            """
            Si el verificador es para sumar se usara su metodo para comprobar
            si el umero dado es correcto o si esta mal la operacion
            """
            if verificador.sumar():
                print("LA SUMA ES CORRECTA")
            else:
                print("LA SUMA ES INCORRECTA")
            
            # Se pregunta al usuario si quiere volver a efectuar la suma
            desea = input("Desea hacer otra suma? (S/N) ")
            
            # Se pone el caracter ingresado en mayuscula para ahorrar codigo
            desea = desea.capitalize()
            
            """
            Si el usuario no desea seguir en suma se cerrada este metodo 
            y se retornara al metodo (menu)
            """
            while desea == 'N':
                print("Fin de la ayuda")
                break
            
    if opcion == 2:
        """
        Se inicia la variable que dara inicio al bucle while el cual 
        llevara consigo la serie de sentencias requeridas segun la opcion dada
        por el usuario
        """
        desea = 'S'
        while desea == 'S':
            # Por mensaje en pantalla se da a conocer al usuario 
            # la operacion a realizar
            print("\t***__ Te ayudo a restar __***")
            
            # Las variables almacenaran numeros de tipo float y su resultado
            num1 = float(input("Primer numero: "))
            num2 = float(input("Segundo numero: "))
            resultado = float(input("Resultado: "))
            
            # En esta variable se hara el llamado a la clase principal
            verificador = AyudaNino(num1,num2,resultado)
            
            """
            Si el verificador es para restar se usara su metodo para comprobar
            si el umero dado es correcto o si esta mal la operacion
            """
            if verificador.restar():
                print("LA RESTA ES CORRECTA")
            else:
                print("LA RESTA ES INCORRECTA")

            # Se pregunta al usuario si quiere volver a efectuar la suma
            desea = input("Desea hacer otra resta? (S/N) ")

            # Se pone el caracter ingresado en mayuscula para ahorrar codigo
            desea = desea.capitalize()
            
            """
            Si el usuario no desea seguir en suma se cerrada este metodo 
            y se retornara al metodo (menu)
            """
            while desea == 'N':
                print("Fin de la ayuda")
                break
    if opcion == 3:
        """
        Se inicia la variable que dara inicio al bucle while el cual 
        llevara consigo la serie de sentencias requeridas segun la opcion dada
        por el usuario
        """
        desea = 'S'
        while desea == 'S':
            # Por mensaje en pantalla se da a conocer al usuario 
            # la operacion a realizar
            print("\t***__ Te ayudo a multiplicar __***")
            
            # Las variables almacenaran numeros de tipo float y su resultado
            num1 = float(input("Primer numero: "))
            num2 = float(input("Segundo numero: "))
            resultado = float(input("Resultado: "))
            
            # En esta variable se hara el llamado a la clase principal
            verificador = AyudaNino(num1,num2,resultado)
            
            """
            Si el verificador es para multiplicar se usara su metodo para comprobar
            si el umero dado es correcto o si esta mal la operacion
            """
            if verificador.multiplicar():
                print("LA MULTIPLICACION ES CORRECTA")
            else:
                print("LA MULTIPLICACION ES INCORRECTA")

            # Se pregunta al usuario si quiere volver a efectuar la suma
            desea = input("Desea hacer otra multiplicacion? (S/N) ")

            # Se pone el caracter ingresado en mayuscula para ahorrar codigo
            desea = desea.capitalize()
            
            """
            Si el usuario no desea seguir en suma se cerrada este metodo 
            y se retornara al metodo (menu)
            """
            while desea == 'N':
                print("Fin de la ayuda")
                break
            
    if opcion == 4:
        """
        Se inicia la variable que dara inicio al bucle while el cual 
        llevara consigo la serie de sentencias requeridas segun la opcion dada
        por el usuario
        """
        desea = 'S'
        while desea == 'S':
            # Por mensaje en pantalla se da a conocer al usuario 
            # la operacion a realizar
            print("\t***__ Te ayudo a dividir __***")
            
            # Las variables almacenaran numeros de tipo float y su resultado
            num1 = float(input("Primer numero: "))
            num2 = float(input("Segundo numero: "))
            resultado = float(input("Resultado: "))
            
            # En esta variable se hara el llamado a la clase principal
            verificador = AyudaNino(num1,num2,resultado)
            
            """
            Si el verificador es para dividir se usara su metodo para comprobar
            si el umero dado es correcto o si esta mal la operacion
            """
            if verificador.dividir():
                print("LA DIVISION ES CORRECTA")
            else:
                print("LA DIVISION ES INCORRECTA")
                
            # Se pregunta al usuario si quiere volver a efectuar la suma
            desea = input("Desea hacer otra division? (S/N) ")
            
            # Se pone el caracter ingresado en mayuscula para ahorrar codigo
            desea = desea.capitalize()
            
            """
            Si el usuario no desea seguir en suma se cerrada este metodo 
            y se retornara al metodo (menu)
            """
            while desea == 'N':
                print("Fin de la ayuda")
                break