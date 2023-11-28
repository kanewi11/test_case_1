from datetime import datetime, timedelta

import pytest

from airplane_arrival.exceptions import ValidationError, ArrivalTypeError
from airplane_arrival.arrival_time import ArrivalTime


def test_init_with_valid_str():
    arrival_time_str = '12:34'
    arrival_time = ArrivalTime(arrival_time_str)
    assert isinstance(arrival_time.arrival_time, datetime)


@pytest.mark.parametrize('value, exception', [(1, ValidationError),
                                              (1.1, ValidationError),
                                              ('f12:12', ValidationError),
                                              ('2:12', ValidationError),
                                              (None, ValidationError)])
def test_init_with_validation_error(value, exception):
    with pytest.raises(exception):
        ArrivalTime(value)


def test_init_with_datetime():
    dt = datetime.now()
    arrival_time = ArrivalTime(dt)
    assert arrival_time.arrival_time == dt


def test_init_with_timedelta():
    td = timedelta(hours=2, minutes=30)
    arrival_time = ArrivalTime(td)
    assert arrival_time.arrival_time == td


def test_lt_operator():
    arrival_time1 = ArrivalTime('12:00')
    arrival_time2 = ArrivalTime('13:00')
    assert arrival_time1 < arrival_time2


def test_gt_operator():
    arrival_time1 = ArrivalTime('12:00')
    arrival_time2 = ArrivalTime('11:00')
    assert arrival_time1 > arrival_time2


def test_eq_operator():
    arrival_time1 = ArrivalTime('12:00')
    arrival_time2 = ArrivalTime('12:00')
    assert arrival_time1 == arrival_time2


def test_subtraction_operator():
    arrival_time1 = ArrivalTime('14:00')
    arrival_time2 = ArrivalTime('12:30')
    result = arrival_time1 - arrival_time2
    assert isinstance(result, ArrivalTime)
    assert str(result) == '1:30:00'


@pytest.mark.parametrize('value, exception', [(1, ArrivalTypeError),
                                              (1.1, ArrivalTypeError),
                                              ('', ArrivalTypeError),
                                              (True, ArrivalTypeError),
                                              (None, ArrivalTypeError)])
def test_invalid_comparison_type(value, exception):
    arrival_time = ArrivalTime('12:00')
    with pytest.raises(exception):
        _ = arrival_time < value


def test_str_representation():
    arrival_time = ArrivalTime('15:45')
    assert str(arrival_time) == '15:45:00'
