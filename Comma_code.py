def funct(lst):
    lst_to_str = ""
    for l in lst:
        if l==lst[-1]:
            lst_to_str+= "and "+l+"."
        else:
            lst_to_str+=l+", "
    return lst_to_str

spam = ['apples', 'bananas', 'tofu', 'cats']
print(funct(spam))