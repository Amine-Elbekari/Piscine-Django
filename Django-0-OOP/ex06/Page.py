from elem import Elem, Text
from elements import *


class Page:
    def __init__(self, class_instance):
        self.class_instance = class_instance
    def is_valid(self):
        
        node = self.class_instance
        valid = False
        valid_classes = (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text)
        body_div_valid_elements = (Div, H1, H2, Table, Ul, Ol, Span, Text)
        if not isinstance(node, valid_classes):
            return False
        if not isinstance(node, Html):
            return False
        if len(node.content) == 2:
            if not isinstance(node.content[0], Head) or \
                not isinstance(node.content[1], Body):
                 return False
            # Head Check
            if len(node.content[0].content) == 1:
                valid = True
                if isinstance(node.content[0].content[0], Title):
                    if node.content[0].content[0].content and len(node.content[0].content[0].content) == 1:
                        
                        if not isinstance(node.content[0].content[0].content[0], Text):
                            return False
                    else:
                        return False
                else:
                    return False
            elif len(node.content[0].content) == 2:
                print(f"THIS IS HEAD CONTENT: {node.content[0].content[1]}")
                valid = True
                if not isinstance(node.content[0].content[0], Title) or \
                    not isinstance(node.content[0].content[1], Meta):
                        return False
                if node.content[0].content[0].content and len(node.content[0].content[0].content) == 1:
                    if not isinstance(node.content[0].content[0].content[0], Text):
                        return False
                else:
                    return False
                if not node.content[0].content[1].attr:
                    return False
            else:
                return False
            # Body Check
            if len(node.content[1].content) > 0:
                valid = True
                for elm in node.content[1].content:
                    if isinstance(elm, body_div_valid_elements):
                        if isinstance(elm, Div):
                            if elm.content:
                                for elm_div in elm.content:
                                    if isinstance(elm_div, body_div_valid_elements):
                                        if isinstance(elm_div, H1):
                                            if elm_div:
                                                if len(elm_div.content) != 1:
                                                    return False
                                            else:
                                                return False
                                        if isinstance(elm_div, H2):
                                            if elm_div:
                                                if len(elm_div.content) != 1:
                                                    return False
                                            else:
                                                return False
                                        if isinstance(elm_div, Ul):
                                            if elm_div:
                                                if len(elm_div.content) != 1:
                                                    return False
                                            else:
                                                return False
                                        if isinstance(elm_div, Ol):
                                            if elm_div:
                                                if len(elm_div.content) >= 1:
                                                    print(len(elm_div.content))
                                            else:
                                                return False
                                        if isinstance(elm_div, Span):
                                            if elm_div:
                                                if len(elm_div.content) == 1:
                                                    if not isinstance(elm_div.content[0], Text) and \
                                                        not isinstance(elm_div.content[0], P):
                                                        return False
                                                    if isinstance(elm_div.content[0], P):
                                                        if elm_div.content[0].content:
                                                            if len(elm.content[0].content) == 1:
                                                                if not isinstance(elm.content[0].content[0], Text):
                                                                    return False
                                                            else:
                                                                return False   
                                                        else:
                                                            return False
                                                else:
                                                    return False    
                                            else:
                                                return False
                                        continue
                                    else:
                                        return False
                            else:
                                return False
                        if isinstance(elm, H1):
                            if elm:
                                if len(elm.content) != 1:
                                        return False
                            else:
                                    return False
                        if isinstance(elm, H2):
                            if elm:
                                if len(elm.content) != 1:
                                    return False
                            else:
                                return False
                        if isinstance(elm, Ul):
                            if elm:
                                if len(elm.content) != 1:
                                    return False
                            else:
                                return False
                        if isinstance(elm, Ol):
                            if elm:
                                if len(elm.content) != 1:
                                    return False
                            else:
                                return False
                        if isinstance(elm, Span):
                            if elm:
                                if len(elm.content) == 1:
                                    if not isinstance(elm.content[0], Text) and \
                                        not isinstance(elm.content[0], P):
                                        return False
                                    if isinstance(elm.content[0], P):
                                        if elm.content[0].content:
                                            if len(elm.content[0].content) == 1:
                                                if not isinstance(elm.content[0].content[0], Text):
                                                    return False
                                            else:
                                                return False
                                        else:
                                            return False
                                else:
                                    return False
                            else:
                                return False
                        continue
                    else:
                        return False
            else:
                return False
        else:
            return False
        return valid
if __name__ == "__main__":
    # H1, H2, Div, Table, Ul, Ol, Span, or Text
    try:
        t = Html([Head([Title(Text('f'))]), Body([Div([H1(Text('Y')), H2(Text('Y')), Ul(Text('Y')), Ol(Text('Y'))]), H1(Text('Y')), H2(Text('Y')), Table(),Ul(Text('Y')), Ol(Text('Y')), Span(P(Text('TEXT'))), Text('I AM INSIDE BODY')])])
        a = Page(t)
        print(a.is_valid())
    except Exception as e:
        print(e)