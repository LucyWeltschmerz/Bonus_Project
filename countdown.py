import time


def countdown():
    t = input("Enter the time in the format h:m:s: ")
    h, m, s = map(int, t.split(':'))
    total_seconds = h * 3600 + m * 60 + s

    if total_seconds <= 0:
        print('Invalid input. Please use a time greater than 00:00:00')
        return

    while total_seconds >= 0:
        h, remainder = divmod(total_seconds, 3600)
        m, s = divmod(remainder, 60)
        time_str = f"{h:02d}:{m:02d}:{s:02d}"
        print(time_str)
        time.sleep(1)
        total_seconds -= 1
    print("Time's Up!")


if __name__ == '__main__':

    countdown()


