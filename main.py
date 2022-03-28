from tkinter import *
from timeit import default_timer as timer
from random_word import RandomWords
import random

window = Tk()
window.title('Typing Speed Test')
window.geometry('824x600')
window.config(bg='tan')

# TODO: initialize the variable to keep track. score, time, number of words corrct and incorrect,
# initialize variables
score = 0
misspelled_words = 0
time = 60
count_1 = 0
moving_words = ''

# Random word instead of list
# TODO: Word bank or list
r = RandomWords()
word = r.get_random_word(maxLength=9)

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


# TODO: Create the GUi to display the type test
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
window.mainloop()

