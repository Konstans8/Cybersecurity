import re


def check_password_strength(password):
    # Установим минимальные требования к паролю
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
    repeat_error = bool(
        re.search(r"(.)\1\1", password)
    )  # Проверка на 3 подряд идущих одинаковых символа

    # Составляем список ошибок
    errors = {
        "Длина пароля меньше 8 символов": length_error,
        "Отсутствуют цифры": digit_error,
        "Отсутствуют заглавные буквы": uppercase_error,
        "Отсутствуют строчные буквы": lowercase_error,
        'Отсутствуют специальные символы (!@#$%^&*(),.?":{}|<>)': symbol_error,
        "Повторяются символы 3 и более раз подряд": repeat_error,
    }

    # Выводим результаты
    if not any(errors.values()):
        print("Пароль надежный!")
    else:
        print("Пароль не удовлетворяет следующим требованиям:")
        for error, has_error in errors.items():
            if has_error:
                print(f"- {error}")


# Пример использования
password = input("Введите пароль для проверки: ")
check_password_strength(password)
