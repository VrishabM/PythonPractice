def list_tuple_generator(str):
    my_list = str.split(",")
    my_tuple = tuple(my_list)
    return my_list, my_tuple


inp = input("Enter string seperated values : ")
mlist, mtuple = list_tuple_generator(inp)
print("List -> ", mlist, "\nTuple -> ", mtuple)
