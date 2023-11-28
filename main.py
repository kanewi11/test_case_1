from airplane_arrival import AirplaneArrival
from airplane_arrival.exceptions import ValidationError


def get_result():
    scheduled_arrival = input('Время прибытия самолета по расписанию: ')
    actual_arrival = input(f'Время фактического прибытия самолета: ')

    try:
        airplane_arrival = AirplaneArrival(scheduled_arrival, actual_arrival)
    except ValidationError as error:
        return str(error)

    return airplane_arrival.get_result()


def main():
    print('Формат времени: hh:mm\n')
    while True:
        try:
            print(get_result(), '', sep='\n')
        except (EOFError, KeyboardInterrupt):
            print('\nЗавершение программы...')
            break


if __name__ == '__main__':
    main()
