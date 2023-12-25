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
            pets_list = line.split()  # ‘\n’ and extra spaces are removed
            name = pets_list[0]
            adj_list = pets_list[1:]
            for i in range(len(adj_list)):
                adj = adj_list[i]
                if adj.find(',') != -1:
                    # Remove comma for adj
                    adj_list[i] = adj[:len(adj) - 1]
            d[name] = adj_list
    return d


def find_pets(d, adjectives):
    """
    : param d: dict{str, list[str]}, the dictionary that has pet’s name as key and a list
                             of adjectives as value
    : param adjectives: list[str], the list holding adjective strings
    """
    # Your Code Here
    ans_s = ''
    for name, adj_list in d.items():
        count = 0
        for adj in adjectives:
            if adj in adj_list:
                count += 1
        if count == len(adjectives):
            ans_s = ans_s + name + ', '
    if len(ans_s) != 0:
        print(ans_s[: len(ans_s) - 2])  # Remove the ‘, ’ at the end
    print('')


def main():
    pets_dict = find_pets_dict('pets.txt')
    print(pets_dict)
    adjs = ['Fuzzy', 'Big']
    find_pets(pets_dict, adjs)


if __name__ == '__main__':
    main()
