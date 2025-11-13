import random
import logging
from datetime import datetime

def setup_basic_logging():
    """Базовая настройка системы логирования"""
    # Создаем форматер с датой, временем, уровнем и сообщением
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)-8s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Настраиваем основной логгер
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Очищаем существующие обработчики (чтобы избежать дублирования)
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Файловый обработчик
    file_handler = logging.FileHandler('program.log', encoding='utf-8', mode='a')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    # Добавляем обработчики к логгеру
    logger.addHandler(file_handler)

    return logger

# Инициализация логирования
logger = setup_basic_logging()

def log_program_start():
    """Логирование начала работы программы"""
    logger.info("=" * 50)
    logger.info("ПРОГРАММА ЗАПУЩЕНА")
    logger.info(f"Время запуска: {datetime.now()}")
    logger.info("=" * 50)

def log_program_end():
    """Логирование завершения работы программы"""
    logger.info("=" * 50)
    logger.info("ПРОГРАММА ЗАВЕРШЕНА")
    logger.info(f"Время завершения: {datetime.now()}")
    logger.info("=" * 50)

def log_user_input(input_type, value):
    """Логирование ввода пользователя"""
    logger.info(f"ВВОД [{input_type}]: {value}")

def log_program_output(output_type, value):
    """Логирование вывода программы"""
    logger.info(f"ВЫВОД [{output_type}]: {value}")

def log_operation(operation, details):
    """Логирование операций программы"""
    logger.info(f"ОПЕРАЦИЯ [{operation}]: {details}")

def log_error(error_msg, context=""):
    """Логирование ошибок"""
    logger.error(f"ОШИБКА [{context}]: {error_msg}")


log_program_start()
N = input('Допишите число до которого можно загадывать: от 1 до ')
log_program_output('Диалог с пользователем','Допишите число до которого можно загадывать: от 1 до ')
log_user_input('Значение N',N)
log_operation('Проверка введённых данных',f'Проверка N({N})')
while True:
    if N.isdigit():
        N = int(N)
        x = random.randint(1, N)
        log_operation(f'Получаем число от 1 до {N} (загаданное число)',x)
        break
    else:
        log_error('Введённое число должно состоять из цифр(1234567890), быть больше 0 и быть целым ',f'Неверные данные для N({N})')
        N = input('Введённое число должно состоять из цифр(1234567890), быть больше 0 и быть целым ')
        log_user_input('Значение N', N)

k = input('Введите число попыток на отгадывание: ')
log_program_output('Диалог с пользователем','Введите число попыток на отгадывание: ')
log_user_input('Значение k',k)
log_operation('Проверка введённых данных', f'Проверка k({k})')
while True:
    if k.isdigit():
        k = int(k)
        break
    else:
        log_error('Введённое число должно состоять из цифр(1234567890), быть больше 0 и быть целым ',f'Неверные данные для k({k})')
        k = input('Введённое число должно состоять из цифр(1234567890), быть больше 0 и быть целым ')
        log_user_input('Значение k', k)

if k==0:
    log_operation('Проверка числа попыток', k)
    print('У вас нет попыток')
    log_program_output('Конечные данные','У вас нет попыток')
else:
    lose = True
    answer = input('Какое число было загадано? ')
    log_program_output('Диалог с пользователем', 'Какое число было загадано? ')
    log_user_input('Значение answer', answer)
    while (lose and k > 1):
        log_operation('Проверка введённых данных', f'Проверка answer ({answer})')
        if answer.isdigit():
            answer=int(answer)
            if (answer < 1 or answer > N):
                log_error(f'Введённое число выходит за допустимый диапазон от 1 до {N} ',f'Неверные данные для answer({answer})')
                answer=input(f'Введённое число выходит за допустимый диапазон от 1 до {N} ')
                log_user_input('Значение answer', answer)
            else:
                log_operation('Проверка ответа и загаданного числа',f'Ответ:{answer}, загадано:{x}')
                if answer == x:
                    lose = False
                elif answer > x:
                    answer = (input('Загаданное число меньше '))
                    k -= 1
                    log_program_output('Диалог с пользователем','Загаданное число меньше ')
                    log_user_input('Новое значение answer', answer)
                    log_operation('Уменьшение количества попыток',k)
                else:
                    answer = (input('Загаданное число больше '))
                    k -= 1
                    log_program_output('Диалог с пользователем', 'Загаданное число больше ')
                    log_user_input('Новое значение answer', answer)
                    log_operation('Уменьшение количества попыток', k)
        else:
            log_error(f'Введённое число должно состоять из цифр(1234567890), быть в диапазоне от 1 до {N} и быть целым ',
                      f'Неверные данные для answer({answer})')
            answer=input(f'Введённое число должно состоять из цифр(1234567890), быть в диапазоне от 1 до {N} и быть целым ')
            log_user_input('Значение answer', answer)

    if int(answer) == x:
        lose = False
        log_operation('Проверка последнего ответа',f'Ответ:{answer}, загадано:{x}')
    if lose:
        print('Попытки закончились')
        log_program_output('Конечные данные', 'Попытки закончились')
    else:
        print('Вы угадали')
        log_program_output('Конечные данные', 'Вы угадали')

log_program_end()
