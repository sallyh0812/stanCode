def just_do_it():
    critical_bool = False
    critical_order = 137
    elements = ['This is a simple question.']
    judge(elements, critical_bool, critical_order)
    print('CB is', critical_bool)
    critical_order = 11
    box = judge(elements, critical_bool, critical_order)
    if box:
        print(' Good job.')
    else:
        print('Good try.')


def judge(elements, critical_bool, critical_order):
    if critical_order == 137:
        if critical_bool:
            elements.append('It will test your concept.')
        else:
            elements.append('It will strengthen your Logic.')
        critical_bool = True
    else:
        for element in elements:
            print(element)
        return critical_order % 2 == 0
    print('CB is', critical_bool)
    return critical_bool


if __name__ == '__main__':
    just_do_it()
