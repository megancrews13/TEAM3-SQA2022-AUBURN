import traceback
import detection.constants as constants
from typing import Any, List

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
