import sys

def parse_file(file):

    content = {}
    with open(file, 'r') as periodic_file:
        lines = periodic_file.readlines()
    
        lines = list(map(lambda x: x.replace('\n', ''), lines))

        for line in lines:
            info = line.split('=')
            val = info[1].split(',')
            val = {k.strip(): v.strip() for k, v in (item.split(':') for item in val)}           
            content[info[0].strip()] = val
    return content

def generate_html_file():

    if len(sys.argv) == 2:

        html_head = """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Periodic Table</title>
        </head>
        """
        html_body = '<body style="font-family: sans-serif;">\n'
        html_content = '    <table style="border-collapse: collapse; width: 100%;">\n'
        end_html = "    </table>\n</body>\n</html>"
        infile = sys.argv[1]
        data = {}
        data = parse_file(infile)

        current_pos = 0
    
        for elemt in data:
            target_position = int(data[elemt]['position'])

            if current_pos == 0:
                html_content += "        <tr>\n"

            while current_pos < target_position:
                html_content += '            <td style="border: none;"></td>\n'
                current_pos += 1

            html_content += f"""            <td style="border: 1px solid black; padding: 10px; width: 5%; height: 160px; position: relative;">
                    <ul style="list-style: none; padding: 0; margin: 0; text-align: center;">

                        <li style="position: absolute; top: 5px; left: 5px; font-weight: bold; font-size: 14px;">
                            {data[elemt]['number']}
                        </li>

                        <li style="position: absolute; top: 5px; right: 5px; font-size: 10px; color: #555; width: 2ch; line-height: 1.2; text-align: left;">
                            {data[elemt]['electron']}
                            elc
                        </li>

                        <li style="font-size: 40px; font-weight: bold; margin-top: 25px; color: #2c3e50;">
                            {data[elemt]['small']}
                        </li>

                        <li>
                            <h4 style="margin: 5px 0; font-size: 14px;">{elemt}</h4>
                        </li>

                        <li style="font-size: 12px; font-style: italic;">
                            {data[elemt]['molar']}
                        </li>

                    </ul>
                </td>\n"""

            current_pos += 1

            if current_pos > 17:
                html_content += "        </tr>\n"
                current_pos = 0

            # if current_pos != 0:
            #     html_content += "        </tr>\n"

        with open('periodic_table.html', 'w') as file:
            file.write(html_head + html_body + html_content + end_html)

if __name__ == "__main__":
    generate_html_file()