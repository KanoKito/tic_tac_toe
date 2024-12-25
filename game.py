from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def input_rc():
    row_col = input('Введите номер строки и столбца: ').split()
    # row = int(input('Введите номер строки: '))
    # column = int(input('Введите номер столбца: '))
    return int(row_col[0]), int(row_col[1])


def main():
    game = Board()
    game.display()
    current_player = 'O'
    running = True

    while running:

        print(f'Ход делает {current_player}')
        while True:
            # В этом блоке содержатся операции, которые могут вызвать исключение.
            try:
                row, column = input_rc()
                if row < 0 or row >= game.field_size:
                    # ...выбросить исключение FieldIndexError.
                    raise FieldIndexError
                if column < 0 or column >= game.field_size:
                    # ...выбросить исключение FieldIndexError.
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    # Вот тут выбрасывается новое исключение.
                    raise CellOccupiedError
                # В метод make_move передаются те координаты, которые ввёл пользователь.
                game.make_move(row, column, current_player)
            except FieldIndexError:
                # ...выводятся сообщения...
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                continue
            except ValueError:
                # ...выводятся сообщения...
                print('Буквы вводить нельзя. Только числа. ')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
                continue
            # Если в блоке try исключения не возникло...
            else:
                # ...значит, введённые значения прошли все проверки
                # и могут быть использованы в дальнейшем.
                # Цикл прерывается.
                break
        # Тернарный оператор, через который реализована смена игроков.
        # Если current_player равен X, то новым значением будет O,
        # иначе — новым значением будет X.
        print('Ход сделан!')
        game.display()
        if game.check_win(current_player):
            print(f'Победил {current_player}.')
            game.write_out('result.txt', f'Победил {current_player}.\n')
            running = False
        elif game.is_board_full():
            print('Ничья!')
            game.write_out('result.txt', 'Ничья!\n')
            running = False
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
