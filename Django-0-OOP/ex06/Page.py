from elem import Elem, Text
from elements import *


class Page:
    def __init__(self, class_instance):
        self.class_instance = class_instance
    def is_valid(self):
        
        # The if else is not a good solution so i am gonna use dict of tuples
        node = self.class_instance
        valid = False
        allowed_elements = {
            Html: (Head, Body),
            Head: (Title, Meta),
            Body: (H1, H2, Div, Table, Ul, Ol, Span, Text, Br, Hr, Img),
            Div: (H1, H2, Div, Table, Ul, Ol, Span, Text, Br, Hr, Img),
            Table: (Tr,),
            Tr: (Th, Td),
            Th: (Text,),
            Td: (Text,),
            Ul: (Li,),
            Ol: (Li,),
            Li: (Text,),
            H1: (Text,),
            H2: (Text,),
            Title: (Text,),
            Span: (Text, P),
            P: (Text,)
        }
        if not isinstance(node, Html) or len(node.content) != 2:
            return False
        if not isinstance(node.content[0], Head) or\
            not isinstance(node.content[1], Body):
            return False
        if len(node.content[0].content) == 1:
            if isinstance(node.content[0].content[0], Title):
                valid = True
        elif len(node.content[0].content) == 2:
            if isinstance(node.content[0], Title) and isinstance(node.content[1], Meta):
                valid = True
        if not valid:
            return False
        
        body = node.content[1]
        nodes_to_check = [body]
        while len(nodes_to_check) > 0:
            
            current_node = nodes_to_check.pop(0)
            if isinstance(current_node, (Text, Br, Hr, Meta, Img)):
                continue
            current_type = type(current_node)
            if current_type not in allowed_elements:
                return False
            allowed_children_type = allowed_elements[current_type]

            current_children = current_node.content
            if current_children:
                for child in current_children:
                    if not isinstance(child, allowed_children_type):
                        print('ds')
                        return False
                    nodes_to_check.append(child)
            else:
                return False
        return valid
        
if __name__ == "__main__":
    # H1, H2, Div, Table, Ul, Ol, Span, or Text
    try:
        t = Html([Head([Title(Text('f'))]), Body([Div([H1(Text('Y')), H2(Text('Y')), Ul([Li(Text('ds')), Li(Text('fdfd'))]), Ol(Li(Text('sd')))]), H1(Text('Y')), Br(),H2(Text('Y')), Table(Tr(Td(Text("sdsd")))),Ul(Li(Text('asdsd'))), Ol(Li(Text('xxx'))), Span(P(Text('TEXT'))), Text('I AM INSIDE BODY')])])
        a = Page(t)
        # print(f'{t}')
        print(a.is_valid())
    except Exception as e:
        print(e)