import generation.constants as constants
from generation.py_parser import checkAlgoNames
from label_perturbation_attack.knn import euc_dist

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

def main():
    fuzzingCheckAlgoNames()
    fuzzingEuc_Dist()

if __name__ == "__main__":
    main()
