from .arrival_time import ArrivalTime


class AirplaneArrival:
    text_delayed = 'Самолет опаздывает. Задержка: {0}'
    text_ahead = 'Самолет прилетел раньше. Опережение: {0}'
    text_in_time = 'Самолет прилетел вовремя: {0}'

    def __init__(self, scheduled_arrival: str, actual_arrival: str):
        self.scheduled_arrival = ArrivalTime(scheduled_arrival)
        self.actual_arrival = ArrivalTime(actual_arrival)

    def get_result(self) -> str:
        if self.actual_arrival > self.scheduled_arrival:
            delay = self.actual_arrival - self.scheduled_arrival
            return self.text_delayed.format(delay)
        elif self.actual_arrival < self.scheduled_arrival:
            ahead_of_schedule = self.scheduled_arrival - self.actual_arrival
            return self.text_ahead.format(ahead_of_schedule)
        return self.text_in_time.format(self.scheduled_arrival)

    def __str__(self):
        return f'Время по расписанию: {self.scheduled_arrival} | Фактическое время: {self.actual_arrival}'

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.scheduled_arrival)}, {repr(self.actual_arrival)})'
