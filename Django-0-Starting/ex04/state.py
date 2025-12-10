import sys

def get_state_capital():
    
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO",
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver",
    }
    
    #print(capital_cities)
    if len(sys.argv) == 2:
        
        capital = sys.argv[1]
        found_state = ''

        capital_to_abbrv = {val:key for key, val in capital_cities.items()}
        if capital in capital_to_abbrv:
            found_cap_abbrv = capital_to_abbrv[capital]
            if found_cap_abbrv:
                abbrev_to_state = {val:key for key, val in states.items()}
                found_state = abbrev_to_state[found_cap_abbrv]
                print(found_state)
        else:
            print('Unknown state')
    

if __name__ == '__main__':
    get_state_capital()