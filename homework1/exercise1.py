#  функція яка розраховує кількість днів між заданою датою і поточною датою.


from datetime import date, datetime, timedelta


def get_days_from_today(date):
    try:
        converted_date = datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.today().date()
        delta = (today_date - converted_date).days
        return delta
    except ValueError:
    
        print("Неправильний формат дати!")
        return None

print(get_days_from_today("2020-10-09"))