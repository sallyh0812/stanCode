def find_pets_dict(filename):
    """
    : param filename: str, the filename holding the text file to be processed
    : return d: dict{str, list[str]}, the dictionary that has pet’s name as key and a list of
                   adjectives as value
    """
    # Your Code Here
    d = {}
    with open(filename, 'r') as f:
        for line in f:
            data = line.split()  # ‘\n’ and extra spaces are removed
            pet_name = data[0].strip()
            adj_list = data[1].split(', ')
            # adj_list = []
            # for adj in data[1:]:
            #     if ',' in adj:
            #         adj = adj[:-1]
            #     adj_list.append(adj)
            d[pet_name] = adj_list
    return d


def find_pets(d, adjectives):
    """
    : param d: dict{str, list[str]}, the dictionary that has pet’s name as key and a list
                             of adjectives as value
    : param adjectives: list[str], the list holding adjective strings
    """
    # Your Code Here
    pets_str = ''
    for pet, adj in d.items():
        match = True
        for adjective in adjectives:
            if adjective not in adj:
                match = False
                break
        if match:
            pets_str += pet + ', '
    pets_str = pets_str[0:-2]
    print(pets_str)


def main():
    pets_dict = find_pets_dict('pets.txt')
    print(pets_dict)
    adjs = ['Fuzzy', 'Big']
    find_pets(pets_dict, adjs)


if __name__ == '__main__':
    main()
