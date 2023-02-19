"""
TODO
"""


def doubles_generator_function(items: list[int] = range(4)) -> list[int]:
    """Generator function that takes a list of integers and yields the double of each item.

    Args:
    - items (list[int], optional): The list of integers the generator should double (default:
    range(4)).

    Yields:
    - (list[int]) The double of each item in the input list
    """
    for item in items:
        yield item * 2


# Generator expression
squares_generator_expression = (x**2 for x in range(4))

if __name__ == "__main__":
    print(type(doubles_generator_function))
    for x in doubles_generator_function():
        print(x)

    print(type(squares_generator_expression))
    for x in squares_generator_expression:
        print(x)
