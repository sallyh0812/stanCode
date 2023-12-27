FILENAME = 'company.txt'


def floor_distribution() -> dict:
    d = {}
    with open(FILENAME, 'r') as f:
        for line in f:
            if line != '\n':
                floor, room, company = line.split()
                floor, room = int(floor), int(room)
                if floor in d:
                    if company in d[floor]:
                        d[floor][company].append(room)
                        d[floor][company] = sorted(d[floor][company])
                    else:
                        d[floor][company] = [room]
                else:
                    d[floor] = {company: [room]}
    return d


def find_company(d: dict, name: str) -> None:
    ans = ""
    for floor, company_dict in d.items():
        if name in company_dict:
            for room in company_dict[name]:
                ans += f"{floor}-{room}, "
    print(ans[:-2])


def main():
    print(floor_distribution())
    find_company(floor_distribution(), 'stanCode')


if __name__ == '__main__':
    main()
