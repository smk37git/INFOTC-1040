# Sebastian Main -- Midterm Project

def get_user_time():
    time = input("What is the current time in 12-hour format (hh:mmam / hh:mmpm): ")
    
    time_split = time.split(":")
    hour = int(time_split[0])
    minute = int(time_split[1][:2])
    cycle = time[5:]
    
    while hour < 00 or hour > 12:
        time = input("Invalid Hour -- What is the current time in 12-hour format (hh:mmam / hh:mmpm): ")
        time_split = time.split(":")
        hour = int(time_split[0])
        minute = int(time_split[1][:2])
        cycle = time[5:]
    
    while minute < 00 or minute > 59:
        time = input("Invalid Minutes -- What is the current time in 12-hour format (hh:mmam / hh:mmpm): ")
        time_split = time.split(":")
        hour = int(time_split[0])
        minute = int(time_split[1][:2])
        cycle = time[5:]
    
    return time
    
def get_user_day():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day = input("What day of the week is it: ")
    if day in days:
        return day, days
    else:
        print("Invalid day, please try again.")
        return get_user_day()
    
    
def get_user_timer():
    timer = input("What is the length of the timer (hh:mm): ")
    return timer

def calculate_timer(time, day, days):
    # TIMER
    timer = get_user_timer()
    timer_split = timer.split(":")
    timer_hour = int(timer_split[0])
    timer_minute = int(timer_split[1])
    
    while timer_hour < 00 or timer_hour > 23:
        timer = input("Invalid Hours -- What is the length of the timer (hh:mm): ")
        timer_split = timer.split(":")
        timer_hour = int(timer_split[0])
        timer_minute = int(timer_split[1])
        
    while timer_minute < 00 or timer_minute > 59:
        timer = input("Invalid Minutes -- What is the length of the timer (hh:mm): ")
        timer_split = timer.split(":")
        timer_hour = int(timer_split[0])
        timer_minute = int(timer_split[1])
        
    # INPUT_TIME
    time_split = time.split(":")
    hour = int(time_split[0])
    minute = int(time_split[1][:2])
    cycle = time[5:]
    
    # Calculate new time
    total_minutes = hour * 60 + minute + timer_hour * 60 + timer_minute
    new_cycle = cycle
    if total_minutes >= 720:
        if cycle == "am":
            new_cycle = "pm"
        else:
            cycle = "am"
            
    new_hour = (hour + timer_hour)
    new_minute = (minute + timer_minute)
    if new_minute >= 60:
        new_hour += 1
        new_minute -= 60
    if new_minute < 10:
        new_minute = "0" + str(new_minute)
            
    new_hour = new_hour % 12
    if new_hour == 0:
        new_hour = 12
        
        
    # New Day
    day_index = days.index(day)
    days_passed = total_minutes // (24 * 60)
    new_day_index = (day_index + days_passed) % 7
    new_day = days[new_day_index]
        


    # OUTPUT 
    new_time = str(new_hour) + ":" + str(new_minute)
    print("The new time is: "+ new_time + cycle + ", " + str(new_day))
    

def main():
    time = get_user_time()
    day, days = get_user_day()
    calculate_timer(time, day, days)
    
main()