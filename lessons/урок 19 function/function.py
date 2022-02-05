from func1 import input_list
from func2 import print_list
# def user_func():
#     print('hello')
# user_func()
""" ДЛЯ КОММЕНТАРИЕВ ИСПОЛЬЗУЮТСЯ КОВЫЧКИ """


def new_list(lst):
    if lst is None:
        lst = [111, 'viktor', 'barinov']
    else:
        lst.clear()
        input_list(lst)
    return lst



def main():
    user_list = [13, 'name', 'lastname']
    print_list(user_list)

    user_list[0] = 21
    user_list[1] = 'ilhom'
    user_list[2] = 'eshonqulov'

    print_list(user_list)

    # input_list(user_list)

    print_list(user_list)

    empty_list = []
    new_list(empty_list)
    print_list(empty_list)

    new_list(user_list)
    print_list(user_list)

""" в main функцию записывается всё тело"""
if __name__ == '__main__':
    main()
































