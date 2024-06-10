real = float(input('How much money do you have in your wallet? R$ '))
dollar = real / 5.00  # Considering the current exchange rate of 1 USD = 5 BRL
euro = real / 6.00  # Considering the current exchange rate of 1 EUR = 6 BRL

print('I have R$ {:.2f}. With this amount, you can buy approximately US$ {:.2f}.'.format(real, dollar))
print('I have R$ {:.2f}. With this amount, you can buy approximately € {:.2f}.'.format(real, euro))

