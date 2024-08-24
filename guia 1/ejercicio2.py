"""" Cuadrado de un binomio Plantear un script directamente en el shell de Python, que permita mostrar,
 para dos valores 𝑎 y 𝑏, que: Un binomio al cuadrado (suma) esigual al cuadrado del primer término, más el doble
producto del primero por el segundo más el cuadrado del segundo. """


a=int(input("ingrese un numero entero: "))#ingreso del primer numero
b=int(input("ingrese otro numero entero: "))#ingreso del segundo numero
primer_termino=a*a;#formula del primer termino
segundo_termino=2*a*b;#formula del segundo termino
tercer_termino=b*b;#formula del tercer termino
cuadrado=primer_termino+segundo_termino+tercer_termino;#resultado del cuadrado
print("El cuadrado de un binomio de a: ",a,"y b: ",b,"es: ",cuadrado)#muestro por pantalla el resultado


"""___________________________________________________________________________________________
                                PRUEBA DE ESCRITORIO
______________________________________________________________________________________________
ENTRADA                         
______________________________________________________________________________________________
ingrese un numero entero :2
ingrese otro numero entero: 3
______________________________________________________________________________________________
PROCESO
______________________________________________________________________________________________
primer_termino=2*2
segundo_termino=2*2*3
tercer_termino=3*3
______________________________________________________________________________________________

SALIDA
______________________________________________________________________________________________
el cuadrado de un binomio de a: 2 y b: 3 es: 25
______________________________________________________________________________________________"""

