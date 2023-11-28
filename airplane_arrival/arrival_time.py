import re
from typing import Union
from datetime import datetime, time, timedelta

from .exceptions import ValidationError, ArrivalTypeError


class ArrivalTime:
    _PATTERN = re.compile('[0-9]{2}:[0-9]{2}')
    _FORMAT = '%H:%M'

    def __init__(self, arrival_time: Union[str, datetime, timedelta]):
        if not isinstance(arrival_time, (datetime, timedelta)):
            self._check_valid_arrival(arrival_time)
            self.arrival_time = self._str_to_time_obj(arrival_time)
        else:
            self.arrival_time = arrival_time

    def _check_valid_arrival(self, arrival: str) -> None:
        if not isinstance(arrival, str) or not self._PATTERN.fullmatch(arrival):
            raise ValidationError

    def _str_to_time_obj(self, arrival: str) -> datetime:
        return datetime.strptime(arrival, self._FORMAT)

    @classmethod
    def __verify_data(cls, other) -> datetime:
        if not isinstance(other, (time, ArrivalTime)):
            raise ArrivalTypeError

        return other if isinstance(other, (time, datetime)) else other.arrival_time

    def __lt__(self, other: Union['ArrivalTime', time]) -> bool:
        other_time = self.__verify_data(other)
        return self.arrival_time < other_time

    def __gt__(self, other: Union['ArrivalTime', time]) -> bool:
        other_time = self.__verify_data(other)
        return self.arrival_time > other_time

    def __eq__(self, other: Union['ArrivalTime', time]) -> bool:
        other_time = self.__verify_data(other)
        return self.arrival_time == other_time

    def __sub__(self, other) -> 'ArrivalTime':
        other_time = self.__verify_data(other)
        return ArrivalTime(self.arrival_time - other_time)

    def __str__(self) -> str:
        if isinstance(self.arrival_time, timedelta):
            return str(self.arrival_time)
        return str(self.arrival_time.time())

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.arrival_time)})'

