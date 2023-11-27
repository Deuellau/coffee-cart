from item import Item

class Menu:
    def __init__(self):
        self.items = []
        self.name_set = set()
        
    def in_menu(self, name):
        if name in self.name_set:
            return True
        else:
            return False
        
    def show(self):
        if not self.items:
            print('Menu is currently empty.\n\n')
        else:
            for index, item in enumerate(self.items):
                print(f'{index+1}. {item.name} - ${item.price}')
            print('\n')
        
    def add(self, name, price, csv): 
        name = name.title()
        if not self.in_menu(name):
            self.name_set.add(name)
            price = '{:.2f}'.format(float(price))
            new_item = Item(name, price)
            self.items.append(new_item)
            if csv:
                return False
            else:
                print('\033c', end='')
                print(f'Item {name} has been added\n\n')
        else:
            if csv:
                return True
            else:
                print('\033c', end='')
                print(f"\nError: Duplicate item '{name}' in menu.\n\n")
                
    def edit(self, name, new_name, price):
        for item in self.items:
            if item.name == name.title():
                item.name = new_name
                item.price = '{:.2f}'.format(float(price))
                self.name_set.remove(name)
                self.name_set.add(new_name)
                print('\033c', end='')
                print(f'Item {new_name} edited successfully.\n\n')
        
    def delete(self, name):
        for item in self.items:
            if item.name == name.title():
                self.items.remove(item)
                self.name_set.remove(item.name)
                print('\033c', end='')
                print(f'Item {item.name} deleted successfully.\n\n')
                return 0
        print('\033c', end='')
        print(f'\nItem "{name}" not found.\n\n')
        
    def __eq__(self, other):
        print("__eq__ method is called")
        return self.items == other.items
        