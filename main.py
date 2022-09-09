import random
import tkinter

questionsDict = {
  "apple" :"りんご",
  "banana": "バナナ",
  "peach":"もも",
  "orange": "オレンジ"
}

correctCount = 0
count = 0
answerButton = ""
answer = ""
entryTxt = ""
answerTxt = ""
decisionLabel = ""
nextButton = ""
key = ""
answerLabel = ""
usedKey = []

# スタートボタン動作
def start():
  startButton.destroy()
  setAnswerButton()
  makeLabel()
  setEntryForm()
  settingQuestion()

def setAnswerButton():
  global answerButton
  answerButton = tkinter.Button(text="答える", width=19, command=check)
  answerButton.place(x=42, y=300)

def makeNextButton():
  global nextButton
  if answerButton:
    answerButton.destroy()
  if count == len(questionsDict):
    nextButton = tkinter.Button(text="スコア", width=19, command=end)
    nextButton.place(x=42, y=300)
  else:
    nextButton = tkinter.Button(text="次へ", width=19, command=settingQuestion)
    nextButton.place(x=42, y=300)
  # 入力値の初期化  
  entryTxt.delete(0, tkinter.END)
  
# ラベルの作成
def makeLabel():
  label = tkinter.Label(root, text="答えれそーなら答えてね♪", font = ("System", 18))
  # 表示と表示場所
  label.place(x=45, y=20)

# 入力フォーム設置
def setEntryForm():
  global entryTxt, answerTxt
  entryTxt = tkinter.Entry(width=21, bg='#F0F8FF', fg='#FF4500')
  # 配置
  entryTxt.place(x=45, y=200)
  
# 回答をチェック
def check():
  global answer, answerTxt, decisionLabel, correctCount, entryTxt, answerLabel
  answerTxt = entryTxt.get()
  print("check:答え", answer, "入力値", answerTxt)

  if answer.replace(' ', '') == answerTxt.replace(' ', ''):
    decisionLabel = tkinter.Label(root, text="正解！！", font = ("System", 84))
    decisionLabel.place(x=46, y=150)
    correctCount += 1

  else:
    decisionLabel = tkinter.Label(root, text="不正解\n(☍﹏⁰)｡", font = ("System", 64))
    answerLabel = tkinter.Label(root, text="正解は,「"+answer+"」だよ", font = ("System", 21))
    decisionLabel.place(x=46, y=70)
    answerLabel.place(x=20, y=240)

  makeNextButton()

# 終了用の関数
def end():
  canvas = tkinter.Canvas(root, width=300, height=400)
  canvas.pack()
  decisionLabel = tkinter.Label(root, text="End", font = ("System", 12))
  decisionLabel.place(x=50, y=200)
  message = f"正解数は{len(questionsDict)}問中、{correctCount}問でした！"
  correctLabel = tkinter.Label(root, text=message, font = ("System", 15))
  correctLabel.place(x=50, y=200)
  

def settingQuestion():
  global count, questionsDict, answer, entryTxt, decisionLabel, usedKey
  setAnswerButton()
  if nextButton:
      nextButton.destroy()
      decisionLabel.destroy()
  if answerLabel:
      answerLabel.destroy()

  print(count , len(questionsDict))
  key = random.choice(list(questionsDict.keys()))
  while key in usedKey:
    key = random.choice(list(questionsDict.keys()))
  print(usedKey)
  print(key)
  answer = questionsDict[key]
  print(key)
  print(usedKey)
  usedKey.append(key)
  questionLabel = tkinter.Label(root, text=key, width=10, font = ("System", 39))
  questionLabel.place(x=20, y=150)
  count += 1

root = tkinter.Tk()
root.title("単語帳")
root.geometry("300x400")

# スタートボタン設置
startButton = tkinter.Button(
  text="学習を始める", 
  fg='#ff0000',
  bg='#f0e68c', 
  width= 20,
  height=2,
  command=start
  )
startButton.place(x=42, y=300)

root.mainloop()