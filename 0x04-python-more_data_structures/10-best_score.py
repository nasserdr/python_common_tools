#!/usr/bin/python3
def best_score(a_dictionary):
    if bool(a_dictionary) is False:
        return None
    else:
        max_key = list(a_dictionary.keys())[0]
        for k, v in a_dictionary.items():
            if a_dictionary[k] > a_dictionary[max_key]:
                max_key = k
        return max_key
