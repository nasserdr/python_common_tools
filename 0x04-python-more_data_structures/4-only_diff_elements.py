def only_diff_elements(set_1, set_2):
    l1 = [x for x in set_1 if x not in set_2]
    l2 = [x for x in set_2 if x not in set_1]
    l1.extend(l2)
    return l1
