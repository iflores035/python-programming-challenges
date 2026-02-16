'''
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
'''

for i in range (1, 101):
    
    res3 = i%3
    res5 = i%5
    
    if res3 == 0  and res5 == 0:
        print('fizzbuzz')

    elif res5 == 0:
        print('buzz')
        
    elif res3 == 0:
        print('fizz')
    
    else:
        print(i)
