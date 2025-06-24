# functools_partial.py
from functools import partial

# def multiply_setup(a:float) -> float:
#     print(a,"----------> a")
#     def nested_multiply(b: float) -> float:
#         print(b,"----------> b")
#         return a * b
    
#     return nested_multiply

# multiply_setup(2)(3)

# outside_setup = multiply_setup(10)

# calling_inside_by_just_giving_param = outside_setup(30)
# print(calling_inside_by_just_giving_param)


def printing():
    print("$"*100)

# using functools
def multiplication_using_functools(a:float, b:float, name : str) -> float:
    abc = printing()
    if name:
        print(f"name is {name} with value of a is {a} and value of b is {b}")
    print(f"a is {a},'\n'b is {b}","*"*100)
    return a*b

partial_is_by_just_passing_limited_params = partial(multiplication_using_functools, 2)
print("*"*100)
fully_functioning_by_passing_remaining_params = partial(partial_is_by_just_passing_limited_params, name="ram")
print(fully_functioning_by_passing_remaining_params)
defining_b = fully_functioning_by_passing_remaining_params(3)
# print(defining_b)