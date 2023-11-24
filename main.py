from menu import Menu
from interface import interfaces
from read_tsv import tsv_to_menu

def main():
    menu = Menu()
    tsv_to_menu('menu.csv', menu)
    userinterface = interfaces(menu)
    
    userinterface.main_menu()
    
main()