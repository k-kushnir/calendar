import datetime


def print_calendar(year, month):
    try:
        cal = datetime.date(year, month, 1)
    except ValueError:
        print("Введіть коректні значення року і місяця.")
        return

    print(f"Календар на {cal.strftime('%B')} {year}:")
    print("Пн Вт Ср Чт Пт Сб Нд")

    # Знайти день тижня першого дня місяця
    start_day = datetime.date(year, month, 1)

    # Визначити відступ перед першим днем
    offset = start_day.weekday()

    # Визначити кількість днів у місяці
    if month == 12:
        days_in_month = (datetime.date(year + 1, 1, 1) - start_day).days
    else:
        days_in_month = (datetime.date(year, month + 1, 1) - start_day).days

    # Друк календаря
    for day in range(1, days_in_month + 1):
        if day == 1:
            print(" " * 3 * offset, end="")
        print(f"{day:2d} ", end="")
        if (day + offset) % 7 == 0:
            print()


if __name__ == "__main__":
    year = int(input("Введіть рік: "))
    month = int(input("Введіть місяць (1-12): "))
    print_calendar(year, month)
