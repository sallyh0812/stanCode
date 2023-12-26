FILENAME = 'name.txt'


def get_dict():
    all_d = {}
    with open(FILENAME, 'r') as f:
        all_d['female'] = {}
        all_d['male'] = {}
        for line in f:
            line = line.strip().split(', ')
            year = line[0]
            female = line[1:6]
            male = line[6:]
            for i in range(5):
                if female[i] in all_d['female']:
                    all_d['female'][female[i]] += 5 - i
                else:
                    all_d['female'][female[i]] = 5 - i
                if male[i] in all_d['male']:
                    all_d['male'][male[i]] += 5 - i
                else:
                    all_d['male'][male[i]] = 5 - i
    return all_d


def main():
    print(get_dict())


if __name__ == '__main__':
    main()
