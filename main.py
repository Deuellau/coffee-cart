from menu import Menu
from interface import Interfaces
from file_functions import File_functions

def main():
    menu = Menu()
    File_functions.csv_to_menu('menu.csv', menu)
    userinterface = Interfaces(menu)
    
    userinterface.main_menu()
    
main()