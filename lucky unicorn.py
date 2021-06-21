from random import choice
tokens = ['horse', 'unicorn', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse', 'zebra', 'donkey', 'zebra', 'donkey', 'horse']
for i in range(500):
    tokens.append('donkey')

while True:
    print('''
    ~
    *************LUCKY UNICORN**************

    Welcome to lucky unicorn where its a chance game trying to get the unicorn but not the donkey
    ~
    ''')

    valid = False
    while not valid: 
        try:
            dollars = int(input("How many credits would you like to put in today? \n"))
            if 0 < dollars <= 10:
                valid = True
            else:
                print("Please enter 1-10 credits")
        except ValueError:
            print("please enter 1-10 credits")
    print(f"you entered {dollars} credits")

    while dollars > 0:
        dollars -= 1
        token = choice(tokens)
        rewards = {'horse': 0.5,
                   'zebra': 0.5,
                   'donkey': 0,
                    'unicorn': 5}
        reward = rewards[token]
        if token == 'horse' or token =='zebra':
            print(f"congradulations you got a {token} \n you win ${reward} as a prize")
        if token == 'unicorn':
            print(f"jackpot you earned {token} \n you win ${reward} as a prize")
            
        if token == 'donkey':
            print("ohh no you lost")
            dollars += reward
            print(f"Your current winnings: {dollars}")