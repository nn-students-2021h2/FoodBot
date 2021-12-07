def all_eq(string_list: list):
    len_list = [len(i) for i in string_list]
    max_len = max(len_list)
    return [i + "_" * (max_len - len(i)) for i in string_list]


string_list = ["a", "aa*************", "aaa", "aaaa", "bbbbb", "aaaa"]
print(string_list)
print(all_eq(string_list))
