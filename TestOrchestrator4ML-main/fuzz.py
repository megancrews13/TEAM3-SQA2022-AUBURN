import detection.constants as constants
from generation.main import generateAttack

def fuzzGenerateAttack():
    print("Start fuzzing of GenerateAttack")
    print("Finish fuzzing of GenerateAttack")

def main():
    print("Beginning Fuzzing")
    fuzzGenerateAttack()
    print("End of fuzzing")

if __name__ == "__main__":
    main()
