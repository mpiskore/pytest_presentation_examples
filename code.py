def increment(number):
    return number + 1


def show_all_smaller_odd_positive_numbers(number):
    # python3 -> range returns a generator, not a list
    return [_ for _ in range(1, number, 2)]
