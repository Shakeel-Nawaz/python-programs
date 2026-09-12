"""
Merging of Dictionary, if entries found common, add the values
"""

def merge_dict(dict1,dict2):
    dict_copied = dict1.copy()
    for key, val in dict2.items():
        dict_copied[key] = dict_copied.get(key,0) + val
    return dict_copied


d1 = {'a':1,'b':2}
d2 = {'c':1,'a':2,'e':9,'t':6}
print(merge_dict(d1,d2))