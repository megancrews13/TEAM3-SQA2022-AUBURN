import traceback
from typing import Any, List

from detection.py_parser import checkAlgoNames
from label_perturbation_attack.knn import euc_dist, calculate_k
from label_perturbation_attack.main import call_loss
from generation.main import generateUnitTest

<<<<<<< HEAD
def fuzz(method, fuzzing_arguments: List[Any]):
    for arguments in fuzzing_arguments:
        try:
            result = method(*arguments)
        except Exception as exc:
            print(f"FUZZ: {method.__name__} FAILED")
            traceback.print_exc()
        else:
            print(f"FUZZ: {method.__name__} PASSED ({result})")
=======

from detection import py_parser
from label_perturbation_attack import knn
from generation import main
from label_perturbation_attack import main


def fuzzingCheckAlgoNames(fuzzing):

           algo_list = fuzzing.value1

           if not algo_list:
              checkAlogNames()
           else:
              print ("Wrong input")

def fuzzingEuc_Dist():
           #inputs to try
           fuzzingValues1 = [-5, 7, 9, {No}, 10]
           fuzzingValues2 = [6, 12, {Yes}, {}, 0]
           print ("Start the fuzzing.")

           #looping through the inputs to look for errors damage ignore
           for val1 in fuzzingValues1:
               for val2 in fuzzingValues2:
                       try:
                           euc_dist(val1, val2)
                           print ("euc_dist passed with " + str(val1) + " and " + str(val2))
                       except:
                           print ("euc_dist failed with " + str(val1) + " and " + str(val2))
           print ("Finished fuzzing.")

def fuzzingPredict(fuzzing):

           predictions = fuzzing.value2

           if not predictions:
              predict()
           else:
              print ("Wrong input")


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


def fuzzingGenerateUnitTest():
           #inputs to try damage
           fuzzingValues1 = ["simple", 0, ([]), 6]
           fuzzingValues2 = ["complex", 3, ({}), 10]
           print ("Start the fuzzing.")

           #looping to search for errors
           for val1 in fuzzingValues1:
               for val2 in fuzzingValues2:
                   try:
                      generateUnitTest(val1, val2)
                      print ("generateUnitTest passed with " + str(val1) + "and " + str(val2))
                   except:
                      print ("generateUnitTest failed with " + str(val1) + "and " + str(val2))
           print ("Finished fuzzing.")

@dataclass
class fuzzingValues():

      value1 = "The cow jumped over the moon"
      value2 = "23869035345"


def main():
    fuzzing = fuzzingValues()

    fuzzingCheckAlgoNames(fuzzing)
    fuzzingEuc_Dist()
    fuzzingPredict(fuzzing)
    fuzzingCall_Loss()
    fuzzingGenerateUnitTest()
>>>>>>> b4de6e8f865b0868ac55263d9f6ff73b2819eac5


if __name__ == "__main__":
    fuzz_targets = [
        (

            checkAlgoNmes, [
                 (0,),
                 (Zero,),
                 (2.4456,),
                 ({Yes},),
                 ([Yes],),
            ]
        ),
        (
            euc_dist, [
                 (-5, 6),
                 (7, 12),
                 ("bad", "good"),
                 ("yes", "no"),
                 (10, 0),
            ]
        ),
        (
            call_loss, [
                 ("name"),
                 (0,),
                 ({}),
                 ("none"),
                 ("yes"),
            ]
        ),
        (
            calculate_k, [
                 ({}),
                 (None, 3),
                 (None, "project"),
                 (None, 555),
                 (None, "december"),
            ]
        ),
        (
            generateUnitTest, [
                 ("simple", "Complex"),
                 (0, 3),
                 ({}, []),
                 (6, 10),
                 ("sqa", "prject"),
            ]
        )
    ]
    for method, fuzzing_arguments in fuzz_targets:
        fuzz(method, fuzzing_arguments)
