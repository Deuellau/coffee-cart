import csv

class File_functions:
    def csv_to_menu(self, file_path, menu):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                item_count = 0
                duplicate_items = ''
                
                for line in lines:
                    values = line.strip().split(',')

                    if len(values) == 2:
                        name, price_str = values

                        try:
                            price = float(price_str)
                        except ValueError:
                            continue
                        
                        duplicate = menu.add_csv(name, price)
                        
                        if duplicate:
                            duplicate_items += name + ', '
                        else:
                            item_count += 1
                        
                item_s_char = ''    
                if item_count > 1:
                    item_s_char = 's'
                    
            print('\033c', end='')
            if item_count > 0:
                print(f'Successfully added {item_count} item{item_s_char} from {file_path} file.')
            elif duplicate_items:
                print(f'Duplicate Items: {duplicate_items[:len(duplicate_items)-2]}.')
            else:
                print('No items imported from file')
            print('\n')
            
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