while True:
    print('Who are you?')
    name=input()
    if name != 'Lilly':
        continue
    print('Hello Lilly. What is the password?')
    password = input()
    if password == 'swordfish':
        break
print('access granted.')
    
