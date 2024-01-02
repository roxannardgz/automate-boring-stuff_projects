## Fantasy Game Inventory
import pprint

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

#print items in the inventory
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        
        item_total += v #total of items
    print("Total number of items: " + str(item_total))
    
    
displayInventory(stuff)
