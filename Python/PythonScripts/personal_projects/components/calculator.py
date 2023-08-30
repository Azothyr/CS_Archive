from azothyr_tools.functions.math_funcs import calculate_geometric_progression as calc_geo_progress


class Calculator:
    pass


def print_geo_iter(out_name, _iter):
    print(out_name, '-'*5)
    for i, val in enumerate(_iter, 1):
        print(f"Iter {i} = {round(val)}")
    print('-'*10)


def print_geo_iter(out_name, _iter):
    print(out_name, '-'*5)
    for i, val in enumerate(_iter, 1):
        print(f"Iter {i} = {round(val)}")
    print('-'*10)


def main():
    iterations = 12
    cost = calc_geo_progress(100, iterations, 2)
    regen = calc_geo_progress(4, iterations, 2)
    damage = calc_geo_progress(2, iterations, 2)
    defense = calc_geo_progress(1, iterations, 2)
    atk_spd = calc_geo_progress(20, iterations, 2)
    # print_geo_iter('cost', cost)
    # print_geo_iter('regen', regen)
    # print_geo_iter('damage', damage)
    # print_geo_iter('defense', defense)
    # print_geo_iter('atk_spd', atk_spd)
    for i in range(iterations):
        print(f'{i+1}> C:{cost[i]}, R:{regen[i]}, Dam:{damage[i]}, Def:{defense[i]}, AS:{atk_spd[i]}')


if __name__ == '__main__':
    main()
