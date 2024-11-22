""" Файл для хранения вспомогательных функций бота """


def generate_array(number: int) -> str:
    """Generate array
    Функция, которая создаёт строку прогресса пользователя

    Args:
        number (int): прогресс на данный момент
    return:
        progress (str): Строка с прогрессом
    """
    array = []
    for i in range(8):
        if i == number:
            array.append("🧑🏼‍💻")
        elif i > number:
            array.append("📝")
        else:
            array.append("💯")
    return ''.join(array)
