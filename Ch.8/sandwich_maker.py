import pyinputplus as pyip
import time


#prices for each item in the menu
prices = {'Wheat': 1, 'White': 1, 'Sourdough': 2, 'Chicken': 2, 'Turkey': 2, 'Ham': 2, 'Tofu': 2, 'Cheddar': 1, 'Swiss': 2, 'Mozzarella': 1, 'mayo': 0.2, 'mustard' : 0.3, 'lettuce' : 0.5, 'tomato' : 0.4}

def takeOrder(num):
    order_total = []        #the total amount to pay for the whole order
    for i in range(num):
        order = []              #ingredients in the sandwich i
        sandwich_total = 0      #amount to pay for the sandwich i
        
        
        print(f'-----Sandiwch # {i+1}-----')
        
        #Type of bread
        bread = pyip.inputMenu(['White', 'Wheat', 'Sourdough'], numbered=True, prompt='Select the type of bread:\n')
        order.append(bread)
        
        #Ype of protein
        protein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True, prompt='Select the protein:\n')
        order.append(protein)
        
        #with cheese
        with_cheese = pyip.inputYesNo(prompt='Do you want to add cheese?')
        
        #type of cheese
        if with_cheese == 'yes':
            cheese = pyip.inputMenu(['Cheddar','Swiss','Mozzarella'], numbered=True, prompt='Select the type of cheese:\n')
            order.append(cheese)

        #mayo, mustard, lettuce or tomato
        extras = ['mayo', 'mustard', 'lettuce', 'tomato']

        for item in extras:
            with_extra = pyip.inputYesNo(prompt=(f'Would you like to add {item}?'))
            if with_extra == 'yes':
                order.append(item)

        #calculate the total for the sandwich ordered
        for ingredient in order:
            if ingredient in prices.keys():
                sandwich_total += prices[ingredient]
        
        order_total.append(sandwich_total)
        print(f'Sandwich {i+1}: {order} \n  Total: ${sandwich_total}')
        time.sleep(1)

    print(f'Total: ${sum(order_total)}')

#make an order
print('Welcome to El Sandwich!')
sandwiches = pyip.inputInt('How many sandwiches would you like to order? ', min=1)
takeOrder(sandwiches)




