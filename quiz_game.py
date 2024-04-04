def new_game():
  guesses = []
  correct_guesses = 0
  question_num = 1

  for key in questions:
    print("---------------------")
    print(key)
    for i in options[question_num - 1]:
      print(i)

    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)

    correct_guesses += check_answer(questions.get(key), guess)
    question_num += 1

  display_score(correct_guesses, guesses)

def check_answer(answer, guess):
  if (answer == guess):
    print("Correct!")
    return 1
  else:
    print("Wrong! :(")
    return 0

def display_score(correct, guesses):
  print("---------------------")
  print("Results")
  print("---------------------")

  print("Answers: ", end="")
  for i in questions:
    print(questions.get(i), end=" ")
  print()

  print("Guesses: ", end="")
  for i in guesses:
    print(i, end=" ")
  print()

  score = int((correct/len(questions)) * 100)

  print("Your score is: " + str(score) + "%")

def play_again():
  response = input("Do you want to play again? (yes/no): ").lower()

  if response == 'yes':
    return True
  else:
    return False

questions = {
  "Who developed the Python programming language?": "A",
  "What is the primary philosophy behind Python's design?": "C",
  "Which of the following is NOT a core data type in Python?": "B",
  "What is the syntax to comment out a line in Python?": "D"
}

options = [
  ["A. Guido van Rossum", "B. Steve Jobs", "C. Linus Torvalds", "D. Larry Page"],
  ["A. Complexity over simplicity", "B. Minimalism", "C. Readability counts", "D. More is less"],
  ["A. int", "B. char", "C. float", "D. str"],
  ["A. /* comment */", "B. // comment", "C. <!-- comment -->", "D. # comment"]
]

new_game()

while play_again():
  new_game()