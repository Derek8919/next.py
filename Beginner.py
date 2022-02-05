# print('x'*10)
# name = input('What is your name? ')
# favorite_color = input('What is your favorite color? ')
# print(f"Hi, {name} likes {favorite_color}")
# weight = input('Enter your weight L(bs): ')
# kgs = int(weight) * 0.45
# print(f'Your weight in Kgs is: {str(kgs)}')
# text = '''Python for beginners is special for beginners
#  surely for beginners'''
# print(text.replace('beginners','absolute beginners'))
# print(text)
# print(text.upper())
# print(text.title())
# print(text.lower())
# print(text.find('i'))
# if statements
# is_hot = True
# is_cold = False
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of cold water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day enjoy")
#
# print('Have pleasure!')
# price = 1000000
# has_good_credit = True
# has_high_income = True
# has_criminal_record = False
# if has_good_credit:
#     down_payment = price * 0.1
# else:
#     down_payment = price * 0.2
# print(f'Down payment for customer is {down_payment}')
# if has_high_income and not has_criminal_record:
#     print('Eligible')
# else:
#     print('Ineligible')
name = input('What is your name?' )
if len(name) < 3:
    print('Name character should be more than 3 characters')
elif len(name) > 50:
    print('Name character should be less than 50 characters')
else:
    print('Your name is lovely')