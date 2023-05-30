def isSubList(numbers1, numbers2):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def main():
    numbers1 = [40, 10, 5]
    numbers2 = [10, 5, 20, 0, 40, 45, 50]

    if isSubList(numbers1, numbers2):
        print(f'{numbers1} is a Sublist of {numbers2} ')
    else:
        print(f'{numbers1} is not a Sublist of {numbers2} ')


if __name__ == '__main__':
    main()
