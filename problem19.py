import calendar
from helpers import Timer


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    total = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            cal = calendar.monthcalendar(year, month)
            if cal[0][6] == 1:
                total += 1
    print(total)
    timer.stop()