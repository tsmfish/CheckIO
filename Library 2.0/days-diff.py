__author__ = 'Pavel.Malko'
def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    import datetime
    return int(str(abs(datetime.date(*date1) - datetime.date(*date2))).split(" ")[0]) if date1 != date2 else 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    assert days_diff((2014, 2, 28), (2014, 2, 28)) == 0
