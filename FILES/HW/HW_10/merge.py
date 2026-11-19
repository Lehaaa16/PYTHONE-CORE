import list


def merge_lists(list1, list2):
    return list1 + list2


l1 = list.make()
print()
l2 = list.make()
print(f"Об'єднаний список: {merge_lists(l1, l2)}")
