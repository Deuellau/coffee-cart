from item import Item

class Menu:
    def __init__(self):
        self.items = []
        self.name_set = set()
        
    def show(self):
        if not self.items:
            print('Menu is currently empty.\n\n')
        else:
            print('~~~~~ Menu ~~~~~')
            for index, item in enumerate(self.items):
                print(f'{index+1}. {item.name} - ${item.price}')
            print('\n')
        
    def add(self, name, price):
        name = name.title()
        if name not in self.name_set:
            self.name_set.add(name)
            price = '{:.2f}'.format(float(price))
            new_item = Item(name, price)
            self.items.append(new_item)
            print(f'\nItem {name} has been added\n\n')
        else:
            print(f"\nError: Duplicate item '{name}' in menu.\n\n")
            
    def add_csv(self, name, price):
        name = name.title()
        if name not in self.name_set:
            self.name_set.add(name)
            price = '{:.2f}'.format(float(price))
            new_item = Item(name, price)
            self.items.append(new_item)
            return False
        else:
            return True
        
    def delete(self, name):
        for item in self.items:
            if item.name == name.title():
                self.items.remove(item)
                self.name_set.remove(item.name)
                print(f'\nItem {item.name} deleted successfully.\n\n')
                return 0
        
        print(f'\nItem "{name}" not found.\n\n')
        
    def __eq__(self, other):
        print("__eq__ method is called")
        return self.items == other.items
        