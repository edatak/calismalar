class Question:
    def __init__(self, text , chocies, answer):
        self.text = text
        self.chocies = chocies
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer



# print(q1.checkAnswer("Python"))
# print(q2.checkAnswer("C#"))

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1} : {question.text}")

        for q in question.chocies:
            print("-" + q )

        answer = input("Cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1


    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    def showScore(self):
        print("score: ", self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz bitti")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100, "*"))
        



q1 = Question("En iyi programlama dili hangisidir?" , ["C#" , "Python" , "Javascript" , "Java"] , "Python")
q2 = Question("En popüler programlama dili hangisidir?" , ["Python" , "C#"  , "Java", "Javascript"] , "Python")
q3 = Question("En çok kazandıran programlama dili hangisidir?" , ["Javascript" , "Python" , "C#" , "Java"] , "Python")
q4 = Question("En çok sevilen programlama dili hangisidir?" , ["Javascript" , "Python" , "C#" , "Java"] , "Python")
q5 = Question("En kolay programlama dili hangisidir?" , ["Javascript" , "Python" , "C#" , "Java"] , "Python")
questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions)

quiz.displayQuestion()
quiz.loadQuestion()
