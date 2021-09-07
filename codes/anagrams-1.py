# print group all the anagrams in this array of strings
# str1 = ['ate', 'eat', 'tea', 'bit', 'fit', 'abcd', 'bcda']
# Expected output: [ ('ate', 'eat', 'tea'), ('abcd','bcda')]


final_dict = {}

def update_dict(newstring):
    sorted_string = ''.join(sorted(list(newstring)))
    # Take sorted string as key of final_dict
    if sorted_string in final_dict:
        final_dict[sorted_string].append(newstring)
    else:
        final_dict[sorted_string] = [newstring]



if __name__ == "__main__":
    str1 = ['ate', 'eat', 'tea', 'bit', 'fit', 'abcd', 'bcda']
    for i in range(len(str1)):
        update_dict(str1[i])
    print(final_dict)
    print("set of all anagrams:")
    for k, v in final_dict.items():
        if len(v)>1:
            print(tuple(v))