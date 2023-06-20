def get_address():
    return "Mirpur DOHS"


def get_name():
    return "Next solution Lab"


def get_info():
    name = get_name()
    address = get_address()
    return name, address


print(get_info()[0])
