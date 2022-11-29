import generation.constants as constants
from generation.py_parser import checkAlgoNames
from label_perturbation_attack.knn import euc_dist
from label_perturbation_attack.knn import calculate_metrics
from label_perturbation_attack.main import call_loss

def fuzzingCheckAlgoNames():
        #inputs to try
        fuzzingValues = [12, No, {No}, [No], {0}, "///", 35]
        print ("Starting the fuzzing.")

        #looping through inputs to see if there are errors
        for inputs in fuzzingValues:
            try:
                checkAlgoNames(input)
                print ("checkAlgoNames passed with " + str(input))
            except:
                print ("checkAlgoNames failed with " + str(input))
        print ("Finished fuzzing.")

def fuzzingEuc_Dist():
           #inputs to try
           fuzzingValues1 = [-5, 7, 9, {No}, 10]
           fuzzingValues2 = [6, 12, {Yes}, {}, 0]
           print ("Start the fuzzing.")

           #looping through the inputs to look for errors
           for val1 in fuzzingValues1:
               for val2 in fuzzingValues2:
                       try:
                           euc_dist(val1, val2)
                           print ("euc_dist passed with " + str(val1) + " and " + str(val2))
                       except:
                           print ("euc_dist failed with " + str(val1) + " and " + str(val2))
           print ("Finished fuzzing.")

def fuzzingCalculate_Metrics():
           #inputs to try
           fuzzingValues = [x, "toy", 24]
           print ("Start the fuzzing.")

           #looping to search for errors
           for inputs in fuzzingValues:
               try:
                   calculate_metrics(input)
                   print ("calculate_metrics passed with " + str(input))
               except:
                   print ("calculate_metrics failed with " + str(input))
           print ("Finished fuzzing.")

def fuzzingCall_Loss():
           #inputs to try
           fuzzingValues = [("good-model-name"), (0), ({}), (None)]
           print ("Start the fuzzing.")

           #looping to search for errors
           for inputs in fuzzingValues:
               try:
                   call_loss(input)
                   print ("call_loss passed with " + str(input))
               except:
                   print ("call_loss failed with " + str(input))
           print ("Finished fuzzing.")

def main():
    fuzzingCheckAlgoNames()
    fuzzingEuc_Dist()
    fuzzingCalculate_Metrics()
    fuzzingCall_Loss()

if __name__ == "__main__":
    main()
