from menu import Menu
from interface import Interfaces
from file_functions import File_functions

def main():
    menu = Menu()
    files = File_functions()
    
    files.csv_to_menu('menu.csv', menu)
    userinterface = Interfaces(menu, files)
    
    userinterface.main_menu()

main()