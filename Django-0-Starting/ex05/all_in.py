import sys

def process_arg(arg, states, capital_cities):

    if arg in states:
        abbrev = states[arg]
        if abbrev in capital_cities:
            return f"{capital_cities[abbrev]} is the capital of {arg}"
    
    capital_to_abbrv = {val:key for key, val in capital_cities.items()}
    if arg in capital_to_abbrv:
        found_cap_abbrv = capital_to_abbrv[arg]
        if found_cap_abbrv:
            abbrev_to_state = {val:key for key, val in states.items()}
            return f"{arg} is the capital of {abbrev_to_state[found_cap_abbrv]}"
        
        
    
    return f"{arg} is neither a capital city nor a state"

def all_in():
    
    output = []
    
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
        
        args_list = [elemt.strip() for elemt in sys.argv[1].split(',') if elemt.strip()]
        for arg in args_list:
           output.append(process_args_list(arg.title(), states, capital_cities))
    
        print(*output, sep='\n')            

if __name__ == '__main__':
    all_in()