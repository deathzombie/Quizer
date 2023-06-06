import random
from string import ascii_lowercase
import pathlib

try :
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"
QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text())

def prep_ques(path,num_ques):
    ques = tomllib.loads(path.read_text())["questions"]
    num_ques = min(num_ques, len(ques))
    return random.sample(ques,num_ques)

def ans_user(ques,alts):
    print(f"\nQuestion {ques} : ")
    i = dict(zip(ascii_lowercase,alts))
    for tag, que in i.items():
        print(f"({tag})-- {que}")
    
    while (ans := input("\nChoice : ")) not in i :
        print(f"Please select one of {','.join(i)}")
    answer = i[ans]    
    return answer

def ask_usr(ques):
    c = ques["answer"]
    alts = [ques["answer"]] + ques["alts"]
    fr = ans_user(ques["question"],alts)
    if fr == c:
        print("⭐️ Correct! ⭐️")
        return 1
    else :
        print(f"{fr} is incorrect, {c} was the correct answer") 
        return 0

def run_quiz():
    ques = prep_ques(QUESTIONS_PATH,NUM_QUESTIONS_PER_QUIZ)
    score = 0
    for num,k in enumerate(ques,start=1):
        print(f"\nQuestion {num} : ")
        score += ask_usr(k)
    print(f"You got {score} out of {num} questions")

if __name__ == '__main__':
    run_quiz()