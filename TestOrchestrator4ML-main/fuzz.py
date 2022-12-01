import traceback
import detection.constants as constants

from typing import Any, List

<<<<<<< HEAD

from dataclasses import dataclass


from detection import py_parser
from label_perturbation_attack import knn
from generation import main
from label_perturbation_attack import main
from label_perturbation_attack.knn import euc_dist, predict
from label_perturbation_attack.main import call_loss, call_prob
from generation.main import generateUnitTest

def fuzzingCheckAlgoNames(fuzzing):

           algo_list = fuzzing.value1

           if not algo_list:
              checkAlgoNames()
           else:
              print ("Wrong input")

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
=======
from detection.py_parser import checkAlgoNames
from label_perturbation_attack.knn import euc_dist, predict
from generation.attack_model import calculate_k
from generation.py_parser import getImport

def fuzz(method, fuzzing_arguments: List[Any]):
    for arguments in fuzzing_arguments:
        try:
            result = method(*arguments)
        except Exception as exc:
            print(f"FUZZ: {method.__name__} FAILED")
            traceback.print_exc()
        else:
            print(f"FUZZ: {method.__name__} PASSED ({result})")
>>>>>>> e428023ed2582763f29975fb006bf6f5c52339a0


if __name__ == "__main__":
    fuzz_targets = [
        (

            checkAlgoNames, [
                 (0,),
                 (None,),
                 (2.4456,),
                 (333,),
                 ("sugar",),
            ]
        ),
        (
            euc_dist, [
                 ("dog", "cat"),
                 (None, 12),
                 ("bad", "good"),
                 ("yes", "no"),
                 (10, None),
            ]
        ),
        (
            predict, [
                 ("name", "person"),
                 (0, 4),
                 ({}, "Section"),
                 ("none", 445),
                 ("yes", "no"),
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
            getImport, [
                 ("simple", "complex"),
                 (0, 3),
                 ({}, []),
                 (6, 10),
                 ("sqa", "prject"),
            ]
        )
    ]
    for method, fuzzing_arguments in fuzz_targets:
        fuzz(method, fuzzing_arguments)
