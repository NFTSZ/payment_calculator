price = float(input('Enter the product price: $'))
print('Choose a payment method: ')
print('[1] Cash\n[2] Cash with card\n[3] Installments with card')
option = int(input('> '))

# Installment area according to payment option [3]
if option == 3:
    print('Enter the number of installments: ')
    print('[2x], [3x], [4x], [5x]')
    installments = int(input('> '))

    # Analyze the number of installments and include interest
    if installments == 2:
        two_installments = price / 2
        print('2 installments of ${:.2f} with no interest'.format(two_installments))
    elif installments == 3:
        three_installments = price / 3 # monthly installments
        interest = (20/100) * price # 20% interest on the price
        print('3 installments of ${:.2f} with ${:.2f} interest. Total: ${:.2f} per month'.format(three_installments, interest, three_installments + interest))
        # ''three_installments + interest'' includes the interest in the monthly installment
    elif installments == 4:
        four_installments = price / 4
        interest = (20/100) * price
        print('4 installments of ${:.2f} with ${:.2f} interest. Total: ${:.2f} per month'.format(four_installments, interest, four_installments + interest))
    elif installments == 5:
        five_installments = price / 5
        interest = (20/100) * price
        print('5 installments of ${:.2f} with ${:.2f} interest. Total: ${:.2f} per month'.format(five_installments, interest, five_installments + interest))

# Analyze and apply discounts
elif option == 1:
    discount = (10/100) * price # 10% discount on the price
    print('From ${:.2f} to ${:.2f} with 10% discount'.format(price, price - discount))
elif option == 2:
    discount = (5/100) * price # 5% discount on the price
    print('From ${:.2f} to ${:.2f} with 5% discount'.format(price, price - discount))
else: 
    print('Invalid option.') # In case the user inputs a number for an unavailable option
