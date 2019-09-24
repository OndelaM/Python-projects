swimming = int(input("Enter the time taken for swimming in minutes: "))
cycling = int(input("Enter the time taken for cycling in minutes: "))
running = int(input("Enter the time taken for running in minutes: "))

total_time = swimming + cycling + running
print(total_time)

position = int(input("Which position did you obtain in the triathlon?: (1/2/3/4)"))
                

if (total_time <= 100) and (position == 1):       
      print("Congratulations, you have received Provincial Colours")

elif (total_time <= 110) and (position == 1) or (position == 2):
      print("Congratulations, you have received Provincial Half Colours")

elif total_time <= 115:
      print("Congratulations, you have received a Provincial Scroll")

elif total_time >= 120:
      print("Congratulations, you have received a Provincial Certificate")

elif total_time > 120:
                print("Sorry no award for you!")
