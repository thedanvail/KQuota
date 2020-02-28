import datetime

def Quota():
    start = datetime.datetime.strptime('19.2.2020 19:00:00,00', '%d.%m.%Y %H:%M:%S,%f')
    conv_start = start.timestamp()
    dt = datetime.datetime.now()
    conv_dt = dt.timestamp()
    kq = conv_dt - conv_start
    quota = kq / 30

    print(int(quota))

if __name__ == "__main__":
    Quota()