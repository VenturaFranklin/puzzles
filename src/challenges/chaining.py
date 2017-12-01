from functools import partial


class add(int):
    def __init__(self, number):
        self.sum = number

    def __call__(self, number):
        new_sum = self.sum + number
        return add(new_sum)


# def add(number, sum=0, parent=True):
#     sum += number
#     print("My number", number, "My Sum", sum)
#     new_add = partial(add, sum=sum, parent=False)
#     if parent:
#         return number
#     else:
#         return new_add


if __name__ == "__main__":
    assert add(1) == 1
    assert add(1)(2) == 3
    assert add(1)(2)(3) == 6
# add = partial(test_add)
