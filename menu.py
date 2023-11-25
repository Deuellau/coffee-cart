from item import Item

class Menu:
    def __init__(self):
        self.items = []
        
    def show(self):
        if not self.items:
            print('Menu is currently empty.\n\n')
        else:
            for index, item in enumerate(self.items):
                print(f'{index+1}. {item.name} - ${item.price}')
            print('\n')
        
    def add(self, name, price):
        name = name.title()
        price = '{:.2f}'.format(float(price))
        new_item = Item(name, price)
        self.items.append(new_item)
        print(f'\nItem {name} has been added\n\n')
        
    def delete(self, name):
        for item in self.items:
            if item.name == name.title():
                self.items.remove(item)
                print(f'\nItem {item.name} successfully deleted.\n\n')
                return 0
        
        print(f'\nItem "{name}" not found.\n\n')
        