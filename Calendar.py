import datetime
import PySimpleGUI as sg


def print_calendar(year, month):
    try:
        year = int(year)
        month = int(month)
        cal = datetime.date(year, month, 1)
    except ValueError:
        sg.popup_error("Введіть коректні значення року і місяця.")
        return

    calendar_text = f"Календар на {cal.strftime('%B')} {year}:\n"
    calendar_text += "{:2s} {:2s} {:2s} {:2s} {:2s} {:2s} {:2s}".format(
        "Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Нд\n")

    # Знайти день тижня першого дня місяця
    start_day = datetime.date(year, month, 1)

    # Визначити відступ перед першим днем
    offset = start_day.weekday()

    # Визначити кількість днів у місяці
    if month == 12:
        days_in_month = (datetime.date(year + 1, 1, 1) - start_day).days
    else:
        days_in_month = (datetime.date(year, month + 1, 1) - start_day).days

    # Додавання днів до рядка календаря
    current_line = " " * 3 * offset
    for day in range(1, days_in_month + 1):
        current_line += f"{day:2d} "
        if (day + offset) % 7 == 0:
            calendar_text += current_line + "\n"
            current_line = ""
    return calendar_text


def program():
    layout = [
        [sg.Text("Введіть рік:"), sg.InputText(key="year")],
        [sg.Text("Введіть місяць (1-12):"), sg.InputText(key="month")],
        [sg.Button("Показати календар"), sg.Button("Вийти")],
        [sg.Output(size=(30, 10), key="output")],
    ]

    window = sg.Window("Календар", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Вийти":
            break

        if event == "Показати календар":
            year = values["year"]
            month = values["month"]
            window["output"].update("")
            window["output"].print(print_calendar(year, month))

    window.close()


if __name__ == "__main__":
    program()
