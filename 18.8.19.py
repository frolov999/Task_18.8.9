price_all = 0
ticket = int(input('Сколько билетов вы хотите приобрести на мероприятие? '))
for age in range(ticket):
    age = int(input('Введите возраст поситтителя '))
    if age < 18:
        price_all += 0
    elif 25 > age >= 18:
        price_all += 990
    else:
        price_all += 1390
if ticket > 3:
    price_all = price_all - ((price_all / 100) * 10)
    print('Сумма к оплате', price_all, 'руб. с учетом 10%-ой скидки')
else:
    print('Сумма к оплате', price_all, 'руб.')
