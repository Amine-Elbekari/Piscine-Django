def read_file():
    
    with open('numbers.txt', 'r') as numbers_file:
        content = numbers_file.read()
    return content

def display_numbers():
    
    content = read_file()
    numbers = [int(num) for num in content .split(',') if num.strip().isdigit()]
    for num in numbers:
        print(num)

if __name__ == '__main__':    
    display_numbers()