import random


def calculate_luhn_check_digit(partial_imei):
    """Вычисляет контрольную цифру IMEI по алгоритму Луна"""
    digits = [int(d) for d in partial_imei]
    total = 0
    for i, digit in enumerate(digits):
        if i % 2 == 0:
            total += digit
        else:
            doubled = digit * 2
            total += doubled if doubled < 10 else doubled - 9
    check_digit = (10 - (total % 10)) % 10
    return check_digit


def generate_valid_imei(tac):
    """Генерирует валидный IMEI на основе TAC"""
    random_part = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    imei_without_check = tac + random_part
    check_digit = calculate_luhn_check_digit(imei_without_check)
    return imei_without_check + str(check_digit)


def main():
    """Основная функция скрипта"""
    models = {
        '0': {'name': 'Teyes CC3 2K', 'tac': '86104505'},
        '1': {'name': 'Samsung Galaxy Tab A9+', 'tac': '35573736'},
        '2': {'name': 'Samsung Galaxy Fold', 'tac': '35409010'},
        '3': {'name': 'Samsung Galaxy S10', 'tac': '35172510'},
        '4': {'name': 'Samsung Galaxy S7', 'tac': '35815207'},
        '5': {'name': 'Samsung Galaxy S5', 'tac': '35255806'},
        '6': {'name': 'Huawei P30 Lite', 'tac': '86159504'},
        '7': {'name': 'Huawei Mate X5', 'tac': '86502606'},
        '8': {'name': 'Honor 8', 'tac': '86192303'},
    }

    print("Выберите устройство для генерации IMEI:")
    for key, model in models.items():
        print(f"{key}. {model['name']}")

    while True:
        choice = input("Введите номер устройства (1-4): ").strip()
        if choice in models:
            selected_model = models[choice]
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    # Генерируем два IMEI
    tac = selected_model['tac']
    imei1 = generate_valid_imei(tac)
    imei2 = generate_valid_imei(tac)

    # Записываем в файл IMEI0
    with open('IMEI0', 'w') as f:
        f.write(imei1 + '\n')
        f.write(imei2 + '\n')

    print(f"\nСгенерированы IMEI для {selected_model['name']}:")
    print(imei1)
    print(imei2)
    print(f"\nФайл 'IMEI0' успешно создан!")


if __name__ == "__main__":
    main()