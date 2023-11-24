class interfaces:
    def __init__(self, menu):
        self.menu = menu
        
    def option_handler(self, valid_options):
        while True:
            option = input('Option: ')
            if option.lower() not in valid_options:
                print('\nInvalid Input')
            else:
                break
        print('\n')
        return option
        
    def main_menu(self):
        while True:
            print('===== Main Menu =====')
            print("\nPlease select an option:")
            print("1. View menu")
            print("2. Modify menu")
            print('Type Q to quit')
            options_lst = ['1', '2', 'q']
            option = self.option_handler(options_lst)

            if option.lower() == 'q':
                return 0
            elif option == '1':
                self.view_menu()
            elif option == '2':
                self.modify_menu()
            
    def view_menu(self):
        self.menu.show_menu()
            
    def modify_menu(self):
        print('===== Modify Menu =====')
        print('\nModify options:')
        print('1. Add item')
        print('2. Edit item')
        print('3. Delete item')
        print('4. Back to main menu')
        options_lst = ['1', '2', '3', '4']
        option = self.option_handler(options_lst)

        if option == '1':
            self.modify_add()
        elif option == '3':
            self.modify_delete()
        else:
            return 0
        
    def modify_add(self):
        print('Adding item to menu')
        while True:
            name = input('Enter item name: ')
            if name.isdigit():
                print('Item name invalid')
            else:
                break
            
        while True:
            price = input('Enter item price: $')
            if not (price.replace('.', '', 1).isdigit() and price.count('.') <= 1):
                print('Item price invalid')
            else:
                break

        self.menu.add_item(name, price)
        
    def modify_delete(self):
        print('Deleting item to menu')
        name = input('Enter item name:')
        self.menu.delete_item(name)