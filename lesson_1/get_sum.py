def get_sum_str(one, two, delimiter='&'):
    string_sum = str(one) + str(delimiter) + str(two)
    return string_sum.upper()


sum_string = get_sum_str('Learn', 'python')
print sum_string
