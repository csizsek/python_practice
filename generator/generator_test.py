"""
TODO
"""

from generator.generator import doubles_generator_function


def test_doubles_generator_function():
    """
    TODO
    """
    for item in doubles_generator_function(range(3)):
        assert isinstance(item, int)
    assert True
