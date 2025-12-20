from path import Path

def create_folder():

    dir_name = Path("my_folder")
    status = False
    try:
        dir_name.mkdir()
        status = True
        print(f'Directory {dir_name} created successfully')
    except FileExistsError:
        print(f'Directory {dir_name} already exist')
    except PermissionError:
        print(f'Permission denied: Unable to create {dir_name}')
    except Exception as e:
        print(f'Error: {e}')
    return (status, dir_name)

def create_file():
    status, dir_name = create_folder()
    file_name = 'file.txt'
    file_path = f'{dir_name}/{file_name}'
    if status:
        try:
            with open(file_path, 'w') as file:
                file.write('Create some stuff inside this file')
                print(f'\nFile {file_name} created with some content\n')
        except Exception as e:
            print(f'Error: {e}')
    return (status, file_path)

def read_file():

    status, file_to_read = create_file()
    if status:
        try:
            with open(file_to_read, 'r') as read_file:
                content = read_file.read()
                print(f'\nThe {file_to_read} content is:\n {content}\n')
        except Exception as e:
            print('Error: {e}')

if __name__ == "__main__":
    read_file()
