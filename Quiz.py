#Setting up all questions, answers and other variables
questions = 1
lives = 2
score = 5

question = ""
answer = ""

question1 = """\nWho is the best protagonist? You have {} attempt(s) remaining.
1. 'Ichigo' 
2. 'Naruto' 
3. 'Luffy'
4. 'Kirito'
5. 'Goku'
6. 'Senku'
7. 'Kaneki'
type here: """
answer1 = "luffy"

question2 = """\nWhat is the best manga? You have {} attempt(s) remaining.
1. 'One Piece'
2. 'Naruto'
3. 'Bleach'
4. 'The Seven Deadly Sins'
5. 'Sword Art Online'
6. 'Dragon Ball'
7. 'Tokyo Ghoul'
type here: """
answer2 = "one piece"

question3 = """\nSolve for 'x' answer should be in decimal form, \n'2(x + 9) - 11' You have {} attempt(s) remaining.
type here: """
answer3 = "-3.5"

question4 = """\nWho is the author of One Piece? You have {} attempt(s) remaining.
type here: """
answer4 = "eiichiro oda"

question5 = """\nWhat year did the first episode of One Piece air? You have {} attempt(s) remaining.
type here: """
answer5 = "1999"

#array for questions and answers
list_question = [question1, question2, question3, question4, question5]
list_answer = [answer1, answer2, answer3, answer4, answer5]

#Asks all question in one loop
for i in range(5):
    print("Question {}".format(questions))
    while True:
        #Checks how many loops its been and sets the question variable
        question = list_question[i]
        user = input(question.format(lives)).strip().lower()
        #Checks how many loops its been and sets the answer variable
        answer = list_answer
        if user in answer:
            print("Correct!")
            lives = 2
            break
        else:
            print("Incorrect")
            score -= 0.5
            lives -= 1
            if lives == 0:
                print("You've run out of tries, let's move on to the next question")
                lives = 2
                break
    print("\n------------------------\n")
    questions += 1
print("You got {}/5, that's {}%".format(score, round((score / 5) * 100, 2)))