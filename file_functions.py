import csv

class File_functions:
    def csv_to_menu(self, file_path, menu):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

                for line in lines:
                    values = line.strip().split(',')

                    if len(values) == 2:
                        name, price_str = values
                        name = name.title()

                        try:
                            price = float(price_str)
                        except ValueError:
                            continue
                        
                        menu.add(name, price)
                        
            print('\033c', end='')
            print(f'Successfully added item(s) from {file_path} file.\n\n')
        except FileNotFoundError:
            print(f'File not found: {file_path}')
        except Exception as e:
            print(f'An error occurred: {e}')
            
    def menu_to_csv(self, file_path, menu):
        try:
            with open(file_path, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                for item in menu.items:
                    csv_writer.writerow([item.name, item.price])
            print('\nMenu saved successfully.\n\n')
        except FileNotFoundError:
            print('Error: The specified file was not found.')
        except Exception as e:
            print(f'An error occurred: {e}')