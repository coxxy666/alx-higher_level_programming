#!/usr/bin/python3
def no_c(my_string):
    string_without_c = []

    for c in my_string:
        if c != 'c' and c != 'C':
            string_without_c.append(c)

    return ''.join(string_without_c)
