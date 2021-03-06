"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если
фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите
численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

income = int(input('Введите значение выручки: '))
expenses = int(input('Введитете значение издержек: '))

profit = income - expenses

if income > expenses:
    print('Фирма работает в прибыль')
    print(f'Рентабельность выручки составляет: {profit / income}')
    workers = int(input('Введите количество сотрудников: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника сотавляет: {profit / workers}')
else:
    print('Фирама работает в убыток')
