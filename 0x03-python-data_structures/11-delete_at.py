def delete_at(my_list=[], idx=0):
    if idx == 0 or idx >= len(my_list) - 1:
        return my_list
    else:
        new_list = []
        i = 0
        for i in range(0, len(my_list)):
            if i == idx:
                i = i + 1
            else:
                new_list.append(my_list[i])