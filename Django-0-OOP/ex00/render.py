import sys
import re
import os

def get_settings_data():

    data = {}
    try:
        with open('./settings.py', 'r') as settings_file:
            # content = settings_file.readlines()
            # content = list(map(lambda x: x.replace('\n', ''), content))
            # for elemt in content:
            #     splited_elemt = elemt.split('=')
            #     value =  re.sub(r'[^a-zA-Z0-9\\n]', ' ', splited_elemt[1].strip())
            #     data[splited_elemt[0].strip()] = value.strip()
            for line in settings_file:
                line = line.strip()
                if not line or '=' not in line:
                    continue
                
                key, value = line.split('=')
                key = key.strip()
                value = value.strip().strip('"')
                data[key] = value
    except FileNotFoundError:
        print("Error: settings.py file not found")
        sys.exit(1)

    return data


def generate_cv_as_html():
    html_content = ""
    if len(sys.argv) == 2:
        
        template_file = sys.argv[1]
        
        if not os.path.isfile(template_file):
            print('Error: File not exist, please create the template file')
            sys.exit(1)
        check_file = os.path.splitext(template_file)
        if check_file[1] != ".template":
            print(f'Error: File extension must be ".template" not {check_file[1]}')
            sys.exit(1)
        
        output_file = template_file.replace('.template', '.html')
        
        settings = get_settings_data()
        try:
            with open(template_file, 'r') as file:
                content = file.read()
            
            # for val in settings:
            #     if re.search(f'{{{val}}}', line):
            #             line = re.sub(f'{{{val}}}', settings[val].strip(), line)
            #     html_content += line
            for key, val in settings.items():
                content = re.sub(f"{{{key}}}", val, content)

            with open(output_file, 'w') as myCvFile:
                myCvFile.write(content)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print('Error: Wrong number of arguments.')
        print('Usage: python render.py myCV.template')
        sys.exit(1)
generate_cv_as_html()