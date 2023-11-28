from .arrival_time import ArrivalTime


class AirplaneArrival:
    def __init__(self, scheduled_arrival: str, actual_arrival: str):
        self.scheduled_arrival = ArrivalTime(scheduled_arrival)
        self.actual_arrival = ArrivalTime(actual_arrival)

    def get_result(self):
        if self.actual_arrival > self.scheduled_arrival:
            delay = self.actual_arrival - self.scheduled_arrival
            return f'Самолет опаздывает. Задержка: {delay}'
        elif self.actual_arrival < self.scheduled_arrival:
            ahead_of_schedule = self.scheduled_arrival - self.actual_arrival
            return f'Самолет прилетел раньше. Опережение: {ahead_of_schedule}'
        return f'Самолет прилетел вовремя: {self.scheduled_arrival}'

    def __str__(self):
        return f'Время по расписанию: {self.scheduled_arrival} | Фактическое время: {self.actual_arrival}'

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.scheduled_arrival)}, {repr(self.actual_arrival)})'
