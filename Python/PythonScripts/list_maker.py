def list_from_user_input():
    done = False
    in_values = []
    while not done:
        while True:
            value = input()
            if not value:
                done = True
                break
            else:
                in_values.append(value)
    return in_values


def main():
    print(list_from_user_input())


if __name__ == '__main__':
    main()
