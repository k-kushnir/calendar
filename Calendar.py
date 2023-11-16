import PySimpleGUI as sg
import calendar


def create_calendar(year, month):
    # Створення календаря за вказаний рік і місяць
    cal = calendar.monthcalendar(year, month)
    header = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд']
    rows = []

    for week in cal:
        row = []
        for day in week:
            if day == 0:
                # Замінюємо 0 на порожню строку для днів, що не належать поточному місяцю
                row.append('')
            else:
                row.append(str(day))
        rows.append(row)

    # Повертаємо двовимірний список з заголовками та даними календаря
    return [header] + rows


def main():
    # Задаємо макет графічного інтерфейсу
    layout = [
        [sg.Text('Оберіть рік та місяць')],
        [sg.InputCombo([str(year) for year in range(2010, 2030)], default_value='2023', key='year'),
         sg.InputCombo([str(month) for month in range(1, 13)],
                       default_value='1', key='month'),
         sg.Button('Показати календар')],
        [sg.Table(values=[], headings=['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд'],
                  auto_size_columns=False, justification='right', num_rows=6, key='calendar')],
        [sg.Button('Вихід')]
    ]

    # Створюємо вікно із заданим макетом
    window = sg.Window('Календар', layout, resizable=True)

    while True:
        # Зчитуємо події та значення елементів інтерфейсу
        event, values = window.read()

        # Виходимо з циклу при закритті вікна або натисканні кнопки "Exit"
        if event == sg.WINDOW_CLOSED or event == 'Вихід':
            break
        elif event == 'Показати календар':
            # Обробляємо натискання кнопки "Show Calendar"
            year = int(values['year'])
            month = int(values['month'])
            cal_data = create_calendar(year, month)
            # Оновлюємо значення таблиці вікна
            window['calendar'].update(values=cal_data[1:])

    # Закриваємо вікно
    window.close()


if __name__ == '__main__':
    main()
