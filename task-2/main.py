strings = ["gg gg gg", "abbbbbb", "www"]


def filter_strings(filter_func: callable, strings_list: list) -> list:
    return [x for x in strings_list if x not in list(filter(filter_func, strings_list))]


if __name__ == "__main__":
    print(filter_strings(lambda x: " " in x, strings))
    print(filter_strings(lambda x: x.startswith("a"), strings))
    print(filter_strings(lambda x: len(x) < 5, strings))
