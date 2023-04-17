def calculaMorango(morangoKg):
    if morangoKg <= 5:
        return morangoKg * 2.5
    else:
        return morangoKg * 2.2
    
def calculaMaca(macaKg):
    if macaKg <= 5:
        return macaKg * 1.8
    else:
        return macaKg * 1.5

def calculaDesconto(morangoKg, macaKg, subtotal):
    if (morangoKg + macaKg >= 8) or subtotal > 25.00:
        return subtotal * 0.9
    else:
        return subtotal

def main():
    morangoKg = float(input('Quantidade de morangos em Kg: '))
    macaKg = float(input('Quantidade de maçãs em Kg: '))
     
    precoMorango = calculaMorango(morangoKg)
    precoMaca = calculaMaca(macaKg)
    subtotal = precoMorango + precoMaca

    total = (f'Total: {calculaDesconto(morangoKg, macaKg, subtotal):.2f}')
    print(total)

if __name__ == '__main__':
    main()

