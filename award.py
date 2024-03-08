# input time record when competing for all three events 
# input time for swimming
# input time for cycling
# input time for running
# calculate total time for all three
# workout which award to give

# Define award thresholds
PROVINCIAL_COLOURS_THRESHOLD = 100
PROVINCIAL_HALF_COLOURS_THRESHOLD = 105
PROVINCIAL_SCROLL_THRESHOLD = 110

swimming_time = float(input("Please enter your recorded time for swimming(minutes): "))
cycling_time = float(input("Please enter your recorded time for cycling(minutes): "))
running_time = float(input("Please enter your recorded time for running(minutes): "))

total_time = swimming_time + cycling_time + running_time
print(f"Your total time for completing the triathlon is {total_time} minutes.")

if total_time==0:
    print("You haven't participated.")
elif 0 < total_time <= PROVINCIAL_COLOURS_THRESHOLD:
    print("Congratulations! You've received Provincial Colours!")
elif PROVINCIAL_COLOURS_THRESHOLD < total_time <= PROVINCIAL_HALF_COLOURS_THRESHOLD:
    print("Congratulations! You've received Provincial Half Colours!")
elif PROVINCIAL_HALF_COLOURS_THRESHOLD < total_time <= PROVINCIAL_SCROLL_THRESHOLD:
    print("Congratulations! You've received Provincial Scroll!")
else:
    print("No award.")
    
