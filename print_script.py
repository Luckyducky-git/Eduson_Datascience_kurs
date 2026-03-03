import re



def is_valid_phone_number(phone: str):
    """
    Проверяет валидность введённого номера сотового телефона.

    Условия валидности:
    - длина номера (без учёта необязательного знака '+') должна быть 11 символов;
    - начинается с '+' (опционально), затем '7' или '8';
    - далее следуют цифры, которые могут быть разделены '-' или пробелом.

    Args:
        phone (str): Строка с номером телефона для проверки.

    Returns:
        bool: True, если номер валиден, False — в противном случае.

    Examples:
        >>> is_valid_phone_number('+79991234567')
        True
        >>> is_valid_phone_number('89991234567')
        True
        >>> is_valid_phone_number('+7 999 123 45 67')
        True
        >>> is_valid_phone_number('+7-999-123-45-67')
        True
        >>> is_valid_phone_number('7999123456')  # слишком короткий
        False
        >>> is_valid_phone_number('+19991234567')  # не 7 и не 8 после +
        False
    """
    if not isinstance(phone, str):
        return False

    # Удаляем пробелы и дефисы для подсчёта длины цифр
    cleaned_phone = re.sub(r'[\s-]', '', phone)

    # Проверяем длину (с учётом возможного '+' в начале)
    if cleaned_phone.startswith('+'):
        if len(cleaned_phone) != 12:
            return False
        digits_part = cleaned_phone[1:]  # убираем '+'
    else:
        if len(cleaned_phone) != 11:
            return False
        digits_part = cleaned_phone

    # Проверяем, что оставшаяся часть состоит только из цифр
    if not digits_part.isdigit():
        return False

    # Проверяем, что номер начинается с 7 или 8
    if digits_part[0] not in ('7', '8'):
        return False

    return True



# Пример использования и тестирования
if __name__ == '__main__':
    test_cases = [
        '+79991234567',
        '89991234567',
        '+7 999 123 45 67',
        '+7-999-123-45-67',
        '7999123456',      # слишком короткий
        '+19991234567',  # не 7 и не 8 после +
        'abc12345678',   # не цифры
        '+7 999-123 abc', # смешанные символы
        '',              # пустая строка
        '  +79991234567  ',  # с пробелами по краям
    ]

    for number in test_cases:
        result = is_valid_phone_number(number)
        print(f'{number!r} -> {result}')