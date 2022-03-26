import random
import time
import enquiries
import glob
import os


def start_quiz(path, quiz_name, qa_order):
    with open(path+"/"+quiz_name, "r") as f:
        l = f.read().split("\n\n")
        random.shuffle(l)
        total_len = len(l)
        while len(l) > 0:
            try:
                # Choose a random QA pair and parse Q and A from it
                rand_ind = random.randint(0, len(l))
                q = l[rand_ind].split("\nA:")[0][2:]
                a = l[rand_ind].split("\nA:")[1]

                if qa_order == "Answer-Question":  # Switch Q and A if asked for
                    temp = a
                    a = q
                    q = temp

                # Print a new question
                print("\n----------------------\n", (total_len - len(l)+1),
                      "/", total_len, "\n", q, "\n")
                i = input(
                    "press y if you know and any button if you didn't: \n\n")

                # Remove question if user says he/she knew
                if i == "y":
                    l.remove(l[rand_ind])
                print("\n", a, "\n")
                time.sleep(2)
            except Exception as e:
                print(e)


# Show all txt files as quizzes options
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)
options = [file for file in glob.glob("*.txt")]
choice = enquiries.choose('Choose one of these quizzes: ', options)

# Choose whether Q-A or A-Q
qa_order = enquiries.choose('Which quiz mode do you want: ', [
                            "Question-Answer", "Answer-Question"])

start_quiz(path, choice, qa_order)
