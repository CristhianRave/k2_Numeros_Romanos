dicUnidades = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
dicDecenas = {10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC'}
dicCentenas = {100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM'}
dicMillares = {1000:'M', 2000:'MM', 3000:'MMM'}
valores = {'I':1, 'V': 5, 'X':10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}
valores5 = { 'V': 5,  'L': 50,  'D': 500 } 
simbolosOrdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

def romano_a_arabigo(numRomano):
    numArabigo = 0
    numRepes = 1
    ultimoCaracter = ''
    for letra in numRomano: 
        #incrementamos el valor del número arábigo con el valor numérico del símbolo romano
        if letra in valores:
            numArabigo += valores[letra]
            if ultimoCaracter == '':
                pass
            elif valores[ultimoCaracter] > valores[letra]:
                numRepes = 1
            elif valores[ultimoCaracter] == valores[letra]:
                numRepes += 1
                if letra in valores5:
                    return 0

                if numRepes > 3:
                    return 0


            elif valores[ultimoCaracter] < valores[letra]:
                if numRepes > 1: # No permite repeticiones en las restas
                    return 0

                if ultimoCaracter in valores5: #No permite restas de valores de 5 (5, 50, 500)
                    return 0

                distancia = simbolosOrdenados.index(letra) - simbolosOrdenados.index(ultimoCaracter) #No permite que se resten unidades de más de un orden
                if distancia > 2:
                    return 0

                numArabigo -= valores[ultimoCaracter]*2
                numRepes = 1
        else:  #si el simbolo romano no es permitido devolvemos error (0)
            return 0

        ultimoCaracter = letra

    return numArabigo

# Descomponer valor en dígitos separando millares, centenas, decenas y unidades
def arabigo_a_romano(valor):
    if valor >= 4000:
        return 0
 
    valor = str(valor)

    millares = '0'
    centenas = '0'
    decenas  = '0'
    unidades = '0'   

    if len(valor) == 1:
        unidades = int(valor)
    elif len(valor) == 2:
        decenas =  int(valor[0]) *10
        unidades = int(valor[1])
    elif len(valor) == 3:
        centenas = int(valor[0]) *100
        decenas =  int(valor[1]) *10
        unidades = int(valor[2])
    elif len(valor) == 4:
        millares = int(valor[0]) *1000
        centenas = int (valor[1]) *100
        decenas =  int(valor[2])*10
        unidades = int(valor[3])
                
    else:
        return 0

#2.- Procesar uno a uno estos dígitos y transformarlos en su forma romana

    millares.append (dicMillares[(millares)])    
    centenas.append (dicCentenas[(centenas)])
    decenas.append  (dicDecenas[(decenas)])
    unidades.append  (dicUnidades[(unidades)])
    
#3.- Ir concatenando cada resultado en una cadena completa
    numRomano = millares + centenas + decenas + unidades

#4.- Devolverla
    return numRomano
