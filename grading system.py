#Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
#Example:
#Input grade: 87.6
#Grade/Mark: 1.75
#Description: Very Good

print ("Grading system in Polythecnic University of the Philippines")

Percentage = round(float(input("Percentage: ")))


if Percentage >= 97 and Percentage <= 100:
    print (" Grade is 1.0, Excellent")
else:
    if Percentage >= 94 and Percentage <= 96:
        print ("Grade is 1.25, Excellent")
    else:
        if Percentage >= 91 and Percentage <= 93:
            print ("Grade is 1.5, Very Good")
        else:
            if Percentage >= 88 and Percentage <= 90:
                print ("Grade is 1.75, Very Good")
            else:
                if Percentage >= 85 and Percentage <= 87:
                    print ("Grade is 2.0, Good")
                else:
                    if Percentage >= 82 and Percentage <= 84:
                        print ("Grade is 2.25, Good")
                    else:
                        if Percentage >= 79 and Percentage <= 81:
                            print ("Grade is 2.5, Satisfactory")
                        else:
                            if Percentage >= 76 and Percentage <= 78:
                                print ("Grade is 2.75, Satisfactory")
                            else: 
                                if Percentage == 75:
                                    print ("Grade is 3.0, Passing")
                                else: 
                                    if Percentage >= 65 and Percentage <=74:
                                        print ("Grade is 5.0, Failure")
                                    else:
                                        if Percentage == 0:
                                            print ("Grade is 0, either Incomplete, Withdrawn, Dropped")



print ("Done")