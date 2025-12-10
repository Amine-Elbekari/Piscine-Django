from collections import defaultdict

def convert_to_dic():

    d = [
    ('Hendrix' , '1942'),
    ('Allman' , '1946'),
    ('King' , '1925'),
    ('Clapton' , '1945'),
    ('Johnson' , '1911'),
    ('Berry' , '1926'),
    ('Vaughan' , '1954'),
    ('Cooder' , '1947'),
    ('Page' , '1944'),
    ('Richards' , '1943'),
    ('Hammett' , '1962'),
    ('Cobain' , '1967'),
    ('Garcia' , '1942'),
    ('Beck' , '1944'),
    ('Santana' , '1947'),
    ('Ramone' , '1948'),
    ('White' , '1975'),
    ('Frusciante', '1970'),
    ('Thompson' , '1949'),
    ('Burton' , '1939')
    ]


    var_to_dict = {}
    # Using a loop
    # for val, key in d:
    #     if key not in var_to_dict:
    #         var_to_dict[key] = []
    #     var_to_dict[key].append(val)

    # for key, val in var_to_dict.items():
    #     print(f"{key}: {' '.join(val)}")

    # Use setdefault method is the best
    for val, key in d:
        var_to_dict.setdefault(key, []).append(val)    
    print(*[f"{key} : {' '.join(val)}" for key, val in var_to_dict.items()], sep="\n")

if __name__ == '__main__':
    convert_to_dic()