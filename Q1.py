# create a python program that asks the user how far they want to travel
# if 3 or less miles → suggest bicycle
# if more than 3 but less than 300 miles → suggest motorcycle
# if 300 miles or more → suggest super car

travel_distance = int(input("Enter the distance you want to travel (in miles): \n"))

if travel_distance <= 3:
    print("Ride a bicycle")
elif 3 < travel_distance < 300:
    print("Ride a motorcycle")
else:
    print("Use a super car")
