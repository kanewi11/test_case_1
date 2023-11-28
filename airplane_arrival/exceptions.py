class ArrivalException(Exception):
    DETAIL = 'Неизвестная ошибка'

    def __init__(self, *args):
        super().__init__(self.DETAIL, *args)

    def __str__(self):
        return self.DETAIL


class ValidationError(ArrivalException):
    DETAIL = 'Проверьте формат записи: чч:мм'


class ArrivalTypeError(ArrivalException):
    DETAIL = 'Операнд справа должен иметь тип time или ArrivalTime'
