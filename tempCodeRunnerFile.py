        while True:
            value = float(input('How much do you want to deposit? R$'))
            if value <= 0:
                print('Choose a valid amount to deposit.')
                sleep(2)
                continue
            else:
