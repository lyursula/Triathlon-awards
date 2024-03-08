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

#Add error handling to the user input
while True:
    swimming_input = input("Please enter your recorded time for swimming(minutes): ")
    try:
        swimming_time = float(swimming_input)  
        break
    except ValueError:
        print("Invalid input. Please enter a numerical value.") 

while True:
    cycling_input = input("Please enter your recorded time for cycling(minutes): ")
    try:
        cycling_time = float(cycling_input)
        break
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

while True:
    running_input = input("Please enter your recorded time for running(minutes): ")
    try:
        running_time = float(running_input)
        break
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

#Total time calculation        
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
    
