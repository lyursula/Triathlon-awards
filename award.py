# input time record when competing for all three events 
# input time for swimming
# input time for cycling
# input time for running
# calculate total time for all three
# workout which award to give
swimming_time = float(input("Please enter your recorded time for swimming(minutes): "))
cycling_time = float(input("Please enter your recorded time for cycling(minutes): "))
running_time = float(input("Please enter your recorded time for running(minutes): "))

total_time = swimming_time + cycling_time + running_time
print(f"Your total time for completing the triathlon is {total_time} minutes.")

if total_time==0:
    print("You haven't participated.")
elif (total_time >0) and (total_time <= 100):
    print("Congratulations! You've received Provincial Colours!")
elif (total_time >=101) and (total_time <=105):
    print("Congratulations! You've received Provincial Half Colours!")
elif (total_time >=106) and (total_time <=110):
    print("Congratulations! You've received Provincial Scroll!")
else:
    print("No award.")
