preco = float(input('Insira o preço do produto: R$'))
print('Escolha uma forma de pagamento: ')
print('[1] À vista\n[2] À vista no cartão\n[3] Dividido no cartão')
opcao = int(input('> '))

# área de parcelas de acordo com o pagamento nº [3]
if opcao == 3:
    print('Informe em quantas parcelas vai dividir: ')
    print('[2x], [3x], [4x], [5x]')
    parcelas = int(input('> '))

# analisa o número de parcelas e inclui os juros
    if parcelas == 2:
        duas = preco / 2
        print('2 vezes de R${:.2f} sem juros'.format(duas))
    elif parcelas == 3:
        tres = preco / 3 # parcelas mensais
        juros = (20/100) * preco # juros de 20% no preço
        print('3 vezes de R${:.2f} com juros de R${:.2f}. Total: R${:.2f} por mês'.format(tres, juros, tres + juros)) 
        # ''tres + juros'' inclui os juros na parcela mensal 
    elif parcelas == 4:
        quatro = preco / 4
        juros = (20/100) * preco
        print('4 vezes de R${:.2f} com juros de R${:.2f}. Total: R${:.2f} por mês'.format(quatro, juros, quatro + juros))
    elif parcelas == 5:
        cinco = preco / 5
        juros = (20/100) * preco
        print('5 vezes de R${:.2f} com juros de R${:.2f}. Total: R${:.2f} por mês'.format(cinco, juros, cinco + juros))

# analisa e adiciona os descontos
elif opcao == 1:
    desc = (10/100) * preco # desconto de 10 % no preço
    print('De R${:.2f} por R${:.2f} com 10% de desconto'.format(preco, preco - desc))
elif opcao == 2:
    desc = (5/100) * preco # desconto de 5% no preço
    print('De R${:.2f} por R${:.2f} com 5% de desconto'.format(preco, preco - desc))
else: 
    print('Opção inválida.') # caso o input do usúario seja um número cuja opção não disponível
