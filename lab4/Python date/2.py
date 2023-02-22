from datetime import date,timedelta
def yesterday():
    return (date.today()-timedelta(1))
def today():
    return date.today()
def tomorrow():
    return (date.today()+timedelta(1))
