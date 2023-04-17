
def apuracao(q1, q2, q3, q4, q5):
    lista = [q1, q2, q3, q4, q5]
    qtd = lista.count('S')

    if qtd == 5:
        return 'Assassino'
    elif  3 <= qtd <= 4:
        return 'Cúmplice'
    elif qtd == 2: 
        return 'Suspeito'
    else:
        return 'Inocente'

def main():
    questao1 = input("Telefonou para a vítima ?").upper().strip()
    questao2 = input("Esteve no local do crime ?").upper().strip()
    questao3 = input("Mora perto da vítima ?").upper().strip()
    questao4 = input("Devia para a vítima ?").upper().strip()
    questao5 = input("Já trabalhou com a vítima ?").upper().strip()

    decisao = apuracao(questao1, questao2, questao3, questao4, questao5)

    print(f'Você é: {decisao}')

if __name__ == '__main__':
    main()