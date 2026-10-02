#create 2 dictionaries and merge them and append values of same key
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merged_dict = {}
for key in dict1:
    if key in dict2:
        merged_dict[key] = dict1[key] + dict2[key]
    else:
        merged_dict[key] = dict1[key]
for key in dict2:
    if key not in dict1:
        merged_dict[key] = dict2[key]
print(merged_dict)
#append values of same key in dictionary merge_dict
for key in merged_dict:
    if key in dict1 and key in dict2:
        merged_dict[key] = [dict1[key], dict2[key]]
print(merged_dict)