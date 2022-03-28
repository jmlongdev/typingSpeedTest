from tkinter import *
from random_word import RandomWords
import random
from tkinter import messagebox

window = Tk()
window.title('Typing Speed Test')
window.geometry('824x600')
window.config(bg='tan')

# initialize variables
score = 0
misspelled_words = 0
time = 10
count_1 = 0
moving_words = ''

r = RandomWords()
word = r.get_random_word(maxLength=9)


def given_time():
    global time, score, misspelled_words
    if time > 11:
        pass
    else:
        time_count_label.config(fg='red')
    if time > 0:
        time -= 1
        time_count_label.config(text=time)
        time_count_label.after(1000, given_time)
    else:
        game_instruction_label.config(text='Hit = {} | Miss = {} | Total Score = {}'.format(score, misspelled_words, score-misspelled_words))
        reset_board = messagebox.askretrycancel('Notification', 'Do you want to play again?')
        if reset_board:
            score = 0
            misspelled_words = 0
            time = 60
            score_count_label.config(text=score)
            time_count_label.config(text=time)
            random_word_label.config(text=word)
            game_instruction_label.place(x=135, y=500)
            start_label.place(x=290, y=65)

            word_entry.delete(0, END)


def game(event):
    global score, misspelled_words
    if time == 10:
        given_time()
    game_instruction_label.place_forget()
    start_label.place_forget()
    if word_entry.get() == random_word_label:
        score += 1
        score_count_label.configure(text=score)
    else:
        misspelled_words += 1
    word = r.get_random_word(maxLength=9)
    random_word_label.config(text=word)
    word_entry.delete(0, END)


def moving_text():
    # animates the top text to move
    global count_1, moving_words
    floating_text = 'Typing Test'
    if count_1 >= len(floating_text):
        count_1 = 0
        moving_words = ''
    moving_words += floating_text[count_1]
    count_1 += 1
    moving_words_label.configure(text=moving_words)
    moving_words_label.after(150, moving_text)


moving_words_label = Label(window, text='', font=('arial', 25, 'italic bold'), fg='purple', width=40)
moving_words_label.place(x=10, y=10)
# create function that animates the title
moving_text()

start_label = Label(window, text='Start Typing', font=('arial', 30, 'italic bold'), bg='black', fg='white')
start_label.place(x=290, y=65)

random_word_label = Label(window, text=word, font=('arial', 45, 'italic bold'), fg='green')
random_word_label.place(x=250, y=260)

score_label = Label(window, text='Your Score:', font=('arial', 25, 'italic bold'), fg='red')
score_label.place(x=20, y=120)

score_count_label = Label(window, text=score, font=('arial', 25, 'italic bold'), fg='blue')
score_count_label.place(x=115, y=180)

timer_label = Label(window, text='Time Left:', font=('arial', 25, 'italic bold'), fg='red')
timer_label.place(x=600, y=120)

time_count_label = Label(window, text=time, font=('arial', 25, 'italic bold'), fg='blue')
time_count_label.place(x=660, y=180)

word_entry = Entry(window, font=('arial', 25, 'italic bold'), bd=10, justify='center')
word_entry.place(x=225, y=370)
word_entry.focus_set()

game_instruction_label = Label(window, text='Hit enter button after typing the word', font=('arial', 25, 'italic bold'), fg='grey')
game_instruction_label.place(x=135, y=500)

window.bind('<Return>', game)

window.mainloop()

