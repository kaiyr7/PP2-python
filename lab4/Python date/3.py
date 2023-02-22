from datetime import datetime
def datetomicroseconds():   
    return datetime.now().replace(microsecond=0)