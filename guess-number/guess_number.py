import random
def  find_number(x):
    print('=====================')
    print('WELCOME TO THE GAME')
    print('=====================')
    
    random_number = random.randint(1, x)

    prediction = 0

    while prediction != random_number:
        prediction = int(input(f'CHOOSE A NUMBER BETWEEN ONE AND {x}: '))
        if prediction < random_number:
            print('VERY LOW NUMBER')
        else:
            print('VERY BIG NUMBER')

    print(f'CONGRATULATIONS THE NUMBER IS {random_number}') 


choose_number = int(input('CHOOSE ONE NUMBER: '))
find_number(choose_number)