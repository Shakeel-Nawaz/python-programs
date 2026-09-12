"""
Merging of Dictionary, if entries found common, add the values

Logic:
1. Take Copy of 1st Dictionary
2. Iterate Over 2nd Dictionary's Items
3. Use Get Method with "Key of 2nd Dict and Default value 0 " and Add Value of 2nd Dict
3. Evaluate   CopiedDict[Key from 2nd Dict]  =  CopiedDictionary.get(Key from 2nd Dict,0) + Value
"""

def merge_dict(dict1,dict2):
    dict_copied = dict1.copy()
    for key, val in dict2.items():
        dict_copied[key] = dict_copied.get(key,0) + val
    return dict_copied


d1 = {'a':1,'b':2}
d2 = {'c':1,'a':2,'e':9,'t':6}
print(merge_dict(d1,d2))