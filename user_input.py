available_pasta = ["pastrami", "golden_penny", "spagheti"]
name = input("please what's your name? ")
pasta = input("please which pasta would you like? ")
        
if pasta in available_pasta:
        print(f'hello {name}, we are preparing {pasta} for you'.title().strip())
else:
        print(f'hello, {name}, we dont have {pasta}')
                