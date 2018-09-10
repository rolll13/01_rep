# # оператор дел
#
# # _list = [1, 2, 3]
# # print(_list)
# # del _list[0]
# # print(_list)
# # del _list
# # print(_list)
#
# # аналогично с ключами
#
#
# # функция
#
# def foo():
#     pass
#
#
# def foo_with_return():
#     return True
#
#
# def foo_with_params(param1=True, param2=True):
#     pass
#
#
# foo_with_params(False, False)
#
# foo_with_params(param2=False, param1=True)
#
# foo_with_params(False, param2=True)
#
#
# def foo_args(*args):
#     print("Foo", args)
#
#
# foo_args(1, 2, 3, 4)
#
#
# def foo_kwargs(**kwargs):
#     print('Foo kwargs', kwargs)
#
# foo_kwargs(a=1, b=2) # только именованные параметры
#
#
# def foo_args_kwargs(*args, ** kwargs):
#     print("Foo", args)
#     print('Foo kwargs', kwargs)
#
# foo_args_kwargs(1, 2, a=1, b=2)
#
#
# (lambda a,b: a + b) (1,2) # анонимная функция
#
#
# def foo_arr(_list, operation=None):
#     result = 0
#     for element in _list:
#         result = operation (result, element)
#     return result
#
# print(
#     foo_arr([1, 2, 3],
#     operation=lambda x, y: x + y)
# )

def foo1(x):
    return x**2
def foo2(x):
    return x*2
def foo3(x):
    return 2*x-1

def foo_result(x):
    if - 5 <= x <= 5:
        return foo1(x)
    elif x > 5:
        return foo2(x)
    elif x < 5:
        result = foo3(x)

for i in range(-10, 10, 1):
    print(foo_result(i))




