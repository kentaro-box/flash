import random
import tkinter


class Learning():
    # tao ra cua so chuong trinh
    def run(self):
        self.root = tkinter.Tk()
        self.root.configure(background='pink')
        self.root.title("学習開始")
        self.root.geometry("600x1000")
        self.welcome_window()
        self.question_list = []
        self.number = 0
        self.score = 0
        self.root.mainloop()

    # tao ra list tu dien
    def dict(self):
        self.questionsDict = {
            "apple": "りんご",
            "banana":  "バナナ",
            "peach": "もも",
            "orange": "オレンジ",
            "avocado": "アボカド",
        }
        print(self.number)
        self.number += 1
        # question_list = []
        self.key_list = list(self.questionsDict.keys())
        self.val_list = list(self.questionsDict.values())


        question = random.choice(self.key_list)
        if question not in self.question_list:
            pass
        else:
            while question in self.question_list:
                question = random.choice(self.key_list)

        # làm cho question với question_list có độ dài bằng nhau thì hàm sẽ tự động kết thúc
        self.question_list.append(question)
        print(self.question_list)
        print(question)
        self.questions_window(question)

    # tao nut "学習を始める"
    def welcome_window(self):
        self.button = tkinter.Button(self.root, text = "学習開始", font = ("times New Roman", 24), command = self.startBtn)
        self.button.place(x = 650, y = 650)
    # tao nut "答える"
    def questions_window(self, question):
        self.button1 = tkinter.Button(text = "答え",font = ("times New Roman", 24), command = self.clickBtn)
        self.button1.place(x = 650, y = 650)
    # tao o entry de nhap data
        self.entry = tkinter.Entry(width = 60)
        self.entry.place(x = 400, y = 500)
    #
        self.trueAnswer = self.questionsDict[question]
    # tao ra dong "答えれそーなら答えてね"
        self.label = tkinter.Label(self.root, text="答えれそーならなら答えてね", font=("times New Roman", 30))
        self.label.place(x = 500, y = 100)

    #
        self.label1 = tkinter.Label(self.root, text = question, font=("times New Roman", 50))
        self.label1.place(x = 600, y = 400)
# tạo nút mở
    def startBtn(self):
        self.button.destroy()
        self.dict()

    def clickBtn(self):
        self.entryString = self.entry.get()
        self.entry.destroy()
        self.button1.destroy()
        self.label.destroy()
        self.label1.destroy()
        self.checkAnswer()
    
    def correctBtn(self):
        self.label2.destroy()
        self.button2.destroy()
        self.dict()

    def incorrectBtn(self):
        self.label3.destroy()
        self.label4.destroy()
        self.button3.destroy()
        self.dict()
    
    def scoreBtn(self, currentWindow):
        if currentWindow == "正解":
            self.label2.destroy()
            self.button5.destroy()
            self.entry.destroy()
        else:
            self.label3.destroy()
            self.label4.destroy()
            self.button6.destroy()
            self.entry.destroy()
        
        self.label5 = tkinter.Label(self.root, text = f"点数は {self.score}",font=("times New Roman", 50))
        self.label5.place(x= 600, y = 400)

    def correctAnswer(self):
        self.label2 = tkinter.Label(self.root, text = "正解!!", font=("times New Roman", 60))
        self.label2.place(x =  610, y =  350)
        self.score += 1
        if self.number == 5:
            currentWindow = "正解"
            self.button5 = tkinter.Button(text = "score", command = lambda: self.scoreBtn(currentWindow))
            self.button5.place(x = 250, y = 500)
        else:
            self.button2 = tkinter.Button(text = "次へ", font=("times New Roman", 30),command = self.correctBtn)
            self.button2.place(x = 650, y = 600)
        
    def incorrectAnswer(self, correctAnswer):
        self.label3 = tkinter.Label(self.root, text = "不正解\n>:<", font=("System", 50))
        self.label3.place(x = 200, y = 200)
        self.label4 = tkinter.Label(self.root, text = f"正解の答え: {correctAnswer}", font=("System", 50))
        self.label4.place(x = 200, y = 300)
        if self.number == 5:
            currentWindow = "incorrect"
            self.button6 = tkinter.Button(text = "score", command = lambda: self.scoreBtn(currentWindow))
            self.button6.place(x = 250, y = 500)
        else:
            self.button3 = tkinter.Button(text = "次へ", command = self.incorrectBtn)
            self.button3.place(x = 250, y = 500)

    def checkAnswer(self):
        if self.entryString == self.trueAnswer:
            self.correctAnswer()
        else:
            self.incorrectAnswer(self.trueAnswer)


def main():
    Learning().run()

if __name__ == "__main__":
    main()
