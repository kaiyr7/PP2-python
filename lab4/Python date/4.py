from datetime import datetime, timedelta
def diff():
    d1=datetime.now()
    d2=timedelta(4)
    d=d1-d2
    return d.total_seconds()