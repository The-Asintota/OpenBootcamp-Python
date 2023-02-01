'''
Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de
masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es {resultado}, redondeado
con dos decimales.
'''
peso = input('¿Cuánto pesa? (kg)\n').lower()
estatura = input('¿Cuál es su estatura? (m)\n').lower()
peso = int(peso.strip('kg'))
estatura = int(estatura.strip('m'))

imc = peso / (estatura ** 2)

print('Tu índice de masa corporal es: ', imc)