menu= ['Paneer Butter Masala', 'Veg Biryani', 'Masala Dosa','Cold Coffee']
print('Menu')
for i, food_name in enumerate(menu,1):
    print(f'{i}. {food_name}')
print()
user= int(input('Enter menu item number:'))
if 1<=user <= len(menu):
    selected_item= menu[user -1]
    print('You selected:', selected_item)
else:
    print('Invalid Selection! Please choose a number from the menu.')
