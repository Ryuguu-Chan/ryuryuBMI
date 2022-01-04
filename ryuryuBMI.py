# for the command line arguments
# sys.argv
import sys

# for the whole mathematics
# math.pow
import math

# the final result
BMI = 0

# the helping text
HELPsyntax = "Here's the syntax\n\n[METRIC METHOD]\npython ryuryuBMI.py [weight in kg] [height in m]\n\n[NON-METRIC METHOD]\npython ryuryuBMI.py [weight in lbs] [height in m] /lbs"

# if the user type 'ryuryuBMI.py /?' -> show the help
# otherwise -> if there's more than 3 arguments (counting the ryuryuBMI.py) -> go make the calculations
# otherwise -> print the helping text as well
try:
    if (sys.argv[1] == '/?'):
        print(HELPsyntax)
    else:
        if (len(sys.argv)) >= 3:
            try:
                if (len(sys.argv) == 4 and sys.argv[3] == '/lbs'):
                    # applying the non-metric formula
                    BMI = math.trunc((703 * float(sys.argv[1])) / math.pow(float(sys.argv[2]), 2))
                else:
                    # applying the metric formula
                    BMI = math.trunc(float(sys.argv[1]) / math.pow(float(sys.argv[2]), 2))

                # checking the result based on the BMI table
                # https://cansa.org.za/files/2020/02/BMI-table-for-LRAT.jpg
                
                if (BMI <= 19):
                    print("You are Underweight!")
                elif (BMI >= 19 and BMI < 25):
                    print("You are Healthy!")
                elif (BMI >= 25 and BMI < 30):
                    print("You are Overweight!")
                elif (BMI >= 30 and BMI < 40):
                    print("You are Obese!")
                elif (BMI >= 40):
                    print("I think you will die soon!")
                else:
                    print("Something went wrong...")
            except Exception as E:
                # printing the helping text
                # print(E)
                print(HELPsyntax)
        else:
            # printing the helping text
            print(HELPsyntax)
except Exception as E :
    # print(E)
    print(HELPsyntax)