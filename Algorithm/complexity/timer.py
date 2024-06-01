# Find the time complexity of a function that takes a list
from timer import time_execution


@time_execution
def first_element(l):
    if len(l) == 0:
        return None
    return l[0]


if __name__ == "__main__":
    for elements in [10, 10000, 100000, 1000000]:
        print(f"For {elements} elements: ", end="")
        first_element(list(range(elements)))