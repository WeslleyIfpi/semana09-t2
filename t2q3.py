def anoBissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False


def dataValida(dia, mes, ano):
    if (1 <= dia <= 31) and mes in (1, 3, 5, 7, 8, 10, 12):
        return True
    elif (1 <= dia <= 30) and mes in (4, 6, 9, 11):
        return True
    elif (1 <= dia <= 28) and mes == 2:
        return True
    elif dia == 29 and mes == 2:
        return anoBissexto(ano)
    else:
        return False

def main():
    data = input('Digite uma data no formato DDMMAAAA: ')
    dia = int(data[0] + data[1])
    mes = int(data[2] + data[3])
    ano = int(data[4] + data[5] + data[6] + data[7])

    print('Data válida?')
    if ano > 0: 
        print(f' {dataValida(dia, mes, ano)}')
    else:
        print('False')
    
if __name__ == '__main__':
    main()