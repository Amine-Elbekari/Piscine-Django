import sys

def get_capital_city():
    
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
    
    if len(sys.argv) == 2:
        state = sys.argv[1]
        if state in states:
            abbrev = states[state]
            if abbrev in capital_cities:
                print(capital_cities[abbrev])
        else:
            print('Unknown state')

if __name__ == '__main__':
    get_capital_state()