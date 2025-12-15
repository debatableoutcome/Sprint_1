time_str = '1h 45m,360s,25m,30m 120s,2h 60s'

def time_calc(value):
    time_split = value.replace(',', ' ').split()
    mins = []
    for time in time_split:
        if 'h' in time:
            minutes = int(time[:-1]) * 60

        elif 's' in time:
            minutes = int(time[:-1]) / 60

        elif 'm' in time:
            minutes = int(time[:-1])
        mins.append(minutes)
    sum_minutes = int(sum(mins))
    print(sum_minutes)

if __name__ == '__main__':
    time_calc(time_str)