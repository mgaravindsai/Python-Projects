def displayInventory(inventory):
    item = 0
    print("Inventory:")
    for itm,val in inventory.items():
        print(val , itm)
        item+=val
    print("Total number of items: "+ str(item))


def addToInventory(inventory,addedItems):
    for i in addedItems:
        if i in inv.keys():
            inv[i]+=1
        else:
            inv[i] = 1

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
displayInventory(inv)