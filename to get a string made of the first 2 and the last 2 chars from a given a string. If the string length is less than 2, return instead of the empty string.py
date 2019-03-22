def len_string(str):
    if len(str)<2:
        return "empty"
    return str[0:2]+str[-2:]
print(len_string('w3resource'))
print(len_string('w3'))
print(len_string('w'))