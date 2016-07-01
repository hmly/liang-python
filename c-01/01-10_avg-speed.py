def avg_speed(dist2, time):
    return dist2 / 1.6 / (time[0] + time[1] / 60 + time[2] / 3600)


distance = 14
time2 = (0, 45, 30)  # hour, min, sec

print("average speed: %.3f" % avg_speed(distance, time2))
