def tsv_to_menu(file_path, menu):
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
                    
                    menu.add_item(name, price)
                    
        print('\033c', end='')
        print(f'Successfully added item(s) from {file_path} file.\n\n')
    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except Exception as e:
        print(f'An error occurred: {e}')