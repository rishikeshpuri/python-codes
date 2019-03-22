def new_string(str):

    first=str[:1]
    last=str[-1:]
    middle=str[1:-1]
    return last+middle+first

print(new_string('python'))