from datetime import datetime, timedelta

date_today = datetime.today()

date_min_birthday = datetime.today() - timedelta(days=365.25 * 9)

date_birthday = datetime(2013, 8, 5)

print('сегодняшняя дата', date_today.date())
print('минимальная дата', date_min_birthday.date())
print('дата рождения   ', date_birthday.date())
print('*' * 20, '\n')

if date_birthday > date_min_birthday:
    print(f'Your age({date_birthday}) is too young.')
else:
    print('OK!')

print('*' * 20, '\n')


user_age_day = (date_today - date_birthday).days

user_age_year = int(user_age_day / 365.25)

print('возраст: ', user_age_year)

