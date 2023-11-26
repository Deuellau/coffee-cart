class Interfaces:
    def __init__(self, menu, files):
        self.menu = menu
        self.files = files
        self.modified = False
        
    def option_handler(self, valid_options):
        while True:
            option = input('Option: ')
            if option.lower() not in valid_options:
                print('\nInvalid Input')
            else:
                break
        print('\n\n')
        return option


    def main_menu(self):
        while True:
            self.modified = False
            print('===== Main Menu =====')
            print("\nPlease select an option:")
            print("1. View menu")
            print("2. Modify menu")
            print('Type Q to quit')
            options_lst = ['1', '2', 'q']
            option = self.option_handler(options_lst)

            if option.lower() == 'q':
                break
            elif option == '1':
                self.view_menu()
            elif option == '2':
                self.modify_menu()
                


    def view_menu(self):
        self.menu.show()
            
    def modify_menu(self):
        while True:
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
                if self.modified:
                    self.modify_save_option()
                break
        
        
    def modify_add(self):
        print('Adding item to menu.')
        while True:
            name = input('Enter item name: ')
            if name.isdigit():
                print('Item name invalid.')
            else:
                break
            
        while True:
            price = input('Enter item price: $')
            if not (price.replace('.', '', 1).isdigit() and price.count('.') <= 1):
                print('Item price invalid')
            else:
                break

        self.menu.add(name, price)
        self.modified = True
        
    def modify_delete(self):
        print('Deleting item from menu.')
        print('\nMenu items:')
        self.menu.show()
        name = input('Enter item name to delete: ')
        self.menu.delete(name)
        self.modified = True
        
    def modify_save_option(self):
        print('Do you want to save changes made to menu?') #TODO: check if menu is edited
        print('\nPress Y to save and exit.')
        print('Press any key to exit without saving.')
        option = input("")
        if option.lower() == 'y':
            self.files.menu_to_csv('menu.csv', self.menu)