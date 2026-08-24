import datetime


def now():

    print(
        datetime.datetime.now()
        .strftime("%Y-%m-%d %H:%M:%S")
    )
