# traffic system records speed of vehicles every 12 hours
# program reads 12 speed values and calculates the average speed

recorded_speeds = [0] * 12

for index in range(12):
    recorded_speeds[index] = float(input("Enter speed: "))

speed_sum = 0
for index in range(12):
    speed_sum += recorded_speeds[index]

average_speed = speed_sum / 12
print("Average speed =", average_speed)

if average_speed < 40:
    print("Slow traffic")
elif 40 <= average_speed <= 80:
    print("Moderate traffic")
else:
    print("Fast traffic")
