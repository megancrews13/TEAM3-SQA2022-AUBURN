import traceback
from typing import Any, List

from detection.py_parser import checkAlgoNames
from label_perturbation_attack.knn import euc_dist, calculate_k
from label_perturbation_attack.main import call_loss
from generation.main import generateUnitTest

def fuzz(method, fuzzing_arguments: List[Any]):
    for arguments in fuzzing_arguments:
        try:
            result = method(*arguments)
        except Exception as exc:
            print(f"FUZZ: {method.__name__} FAILED")
            traceback.print_exc()
        else:
            print(f"FUZZ: {method.__name__} PASSED ({result})")


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
