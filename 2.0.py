from tkinter import *
import json
import random
import test

# начало программы
root = Tk()
root.geometry("1000x700")
with open("text.json", "r", encoding="utf-8") as json_file:
    a = json.load(json_file)

def get_random_poem(poems):#Возвращает случайное стихотворение из словаря
    poet = random.choice(list(poems.keys()))
    poem = poems[poet]
    title = random.choice(list(poem.keys()))
    return ' '.join(poem[title].splitlines())

poem = get_random_poem(a)

score = 0
mini_poem = poem[:30]  # Отображение первых 30 символов текста

new_text = Label(root, text=mini_poem, font=("Arial", 30), bg='Green',justify=LEFT)  # текст для печати,wraplength = 999
new_text.pack()  # обязательно указывать отдельно
score_label = Label(root, text="счет:" + str(score), font=("Arial", 14)) # Счет верных нажатий
score_label.pack()
count = 29
test = 0




def reset():
    global poem,score
    poem = poem
    score = 0


def ignore(event):# связывание события с функцией ignore
    return "break"



def on_key_press(event):
    global mini_poem,poem,score,count
    if event.char == mini_poem[0]:
        score += 1
        count += 1
        if count == len(poem):# отвечает за прокрутку текста при его окончании
            count = 0
            poem = get_random_poem(a)
        mini_poem = mini_poem[1:] + poem[count]
        new_text.config(text=mini_poem)
        score_label.config(text="счет:" + str(score))
    elif event.char == "<Shift>":
        ignore(event)  #игнорирования клавиши
    elif event.char != mini_poem[0]:
        score -= 1
        score_label.config(text="счет:" + str(score))


reset()
root.bind("<Key>", on_key_press)
root.bind("<Alt_L>", ignore)
root.bind("<Shift_L>", ignore)
root.bind("<Shift_R>", ignore)

# конец программы
root.mainloop()