my_dict = {'a': 1, 'b': 2, 'c': 3}

convert_to_list = "".join([f'{k}{v}' for k,v in my_dict.items()])
print(convert_to_list)

#output= a1b2c3