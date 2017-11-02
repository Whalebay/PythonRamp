import time
import math

OldVariable = 0.9
NewVariable = 0.5

IntermidiateVariable = OldVariable
if OldVariable < NewVariable:
    while IntermidiateVariable < NewVariable:
        print(float(IntermidiateVariable) ,"NewVariable=", float(NewVariable))
        IntermidiateVariable = IntermidiateVariable + 0.01
        print(float(IntermidiateVariable) ,"NewVariable=", float(NewVariable))
        time.sleep(0.00001)
    
if OldVariable > NewVariable:
    while IntermidiateVariable > NewVariable:
        print(float(IntermidiateVariable) ,"NewVariable=", float(NewVariable))
        IntermidiateVariable = IntermidiateVariable - 0.01
        print(float(IntermidiateVariable) ,"NewVariable=", float(NewVariable))
        time.sleep(0.00001)

print("Finished")
