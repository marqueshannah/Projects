import pytest

from calculate_water import calculate_turbidity, minimum_time_threshold


def test_calculate_turbidity():

    assert calculate_turbidity([{'a': 1.2, 'b': 2.0}], 'a', 'b') == 2.4
    assert calculate_turbidity([{'a': 3.1, 'b': 1.0}], 'a', 'b') == 3.1
    assert calculate_turbidity([{'a': 5.4, 'b': 2.0}], 'a', 'b') == 10.8
    assert isinstance(calculate_turbidity([{'a': 3.142, 'b': 1.321}], 'a', 'b'), float) == True
    with pytest.raises(KeyError):
        calculate_turbidity([{'a': 1.0, 'b': 2.0}], 'c', 'd')
    with pytest.raises(KeyError):
        calculate_turbidity([{'a': 3.14}], 'a', 'b')

def test_minimum_time_threshold():
    assert minimum_time_threshold (1) == 0
    assert minimum_time_threshold(0.5) < 0
    assert round(minimum_time_threshold(1.5)) == 20
    with pytest.raises(ZeroDivisionError):
        minimum_time_threshold(0)
    with pytest.raises(TypeError):
        minimum_time_threshold('0')
