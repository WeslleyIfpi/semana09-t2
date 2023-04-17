def decompoeNumero(numero):
    centena = numero // 100
    dezena = (numero % 100) // 10
    unidade = (numero % 100) % 10

    return centena, dezena, unidade

def porExtenso(numero):
    if numero == 0:
        return ''
    elif numero == 1:
        return 'uma'
    elif numero == 2:
        return 'duas'
    elif numero == 3:
        return 'três'
    elif numero == 4:
        return 'quatro'
    elif numero == 5:
        return 'cinco'
    elif numero == 6:
        return 'seis'
    elif numero == 7:
        return 'sete'
    elif numero == 8:
        return 'oito'
    elif numero == 9:
        return 'nove'

def escreva(numero):
    saida = ''
    centena, dezena, unidade = decompoeNumero(numero)
   
    saida += porExtenso(centena)
    if centena  == 1:
        saida += ' centena'
    elif centena > 1: 
        saida += ' centenas'

    if (dezena > 0 and centena > 0 and unidade > 0):
        saida += ', '
    elif unidade > 0 or (unidade == 0 and dezena > 0 and centena > 0):
        saida += ' e '

    saida += porExtenso(dezena)
    if dezena  == 1:
        saida += ' dezena'
    elif dezena > 1: 
        saida += ' dezenas'
    
    if unidade > 0 and dezena > 0:
        saida += ' e '

    saida += porExtenso(unidade)
    if unidade == 1:
        saida += ' unidade'
    elif unidade > 1: 
        saida += ' unidades'

    saida += '.'

    return saida




def main():
    numero = int(input())
    print(escreva(numero))

if __name__ == '__main__':
    main()