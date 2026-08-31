import data
from question_model import Question
from quiz_brain import QuizBrain

questionList = []

# Creates list of questions
for q in data.question_data:
    questionList.append(Question(q["question"], q["correct_answer"]))

# Sets up quizBrain
quiz = QuizBrain(questionList)

# Core loop
while quiz.still_has_question():
    quiz.next_question()

# End state
print("You have reached the end of the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")