def to_lower_case(s):
    return s.lower()


def to_upper_case(s):
    return s.upper()


string_list = 'HeLLo  EVEryBody'.split()
print(list(map(to_lower_case, string_list)))
print(list(map(to_upper_case, string_list)))
