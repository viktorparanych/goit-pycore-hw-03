# Функція яка допоможе вам визначати, кого з колег потрібно привітати. 
# Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.
from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.05.05"},
    {"name": "Jane Smith", "birthday": "1990.05.03"}
]
def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d"). date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until = (birthday_this_year - today).days

        if 0 <= days_until <= 7:
            congratulation_date = birthday_this_year


            day_of_week = congratulation_date.weekday()                                                                                                         
            if day_of_week == 5:
                congratulation_date += timedelta(days=2)
            elif day_of_week == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    return upcoming_birthdays
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)