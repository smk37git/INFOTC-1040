# Sebastian Main
# Problem #2
def get_season(month):
    if month > 0 and month < 3:
        return "\033[1m" + "Winter."
    elif month == 12:
        return "\033[1m" + "Winter."
    elif month > 2 and month < 6:
        return "\033[1m" + "Spring."
    elif month > 5 and month < 9:
        return "\033[1m" + "Summer."
    elif month > 8 and month < 12:
        return "\033[1m" + "Fall."
    elif month > 12 or month < 1:
        return "\033[1m" + "Invalid month."
    elif month == 0 or month < 0:
        return "\033[1m" + "Invalid month."

def main():
    month = int(input("Please enter a month (as an integer): "))
    season = get_season(month)
    print("Month " + str(month) + " is " + str(season))

main()

    