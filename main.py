from tkinter import *
from tkinter import messagebox
from pygame import mixer

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("250x300")
        self.root.maxsize(250, 300)
        mixer.init()
        self.cross_img = PhotoImage(file="img\\cross.png")
        self.circle_img = PhotoImage(file="img\\circle.png")
        self.bg_img = PhotoImage(file="img\\bg.png")
        self.player_1_score = 0
        self.player_2_score = 0
        self.i = 1
        self.btn_list = []


        Label(root, image=self.bg_img).pack()
        self.btn_1 = Button(root, bg="white", bd=0, command=lambda :self.move(self.btn_1))
        self.btn_2 = Button(root, bg="white", bd=0, command=lambda :self.move(self.btn_2))
        self.btn_3 = Button(root, bg="white", bd=0, command=lambda :self.move(self.btn_3))
        self.btn_4 = Button(root, bg="white", bd=0, command=lambda :self.move(self.btn_4))
        self.btn_5 = Button(root, bg="white", bd=0, command=lambda :self.move(self.btn_5))
        self.btn_6 = Button(root, bg="white", bd=0, command=lambda :self.move(self.btn_6))
        self.btn_7 = Button(root, bg="white", bd=0, command=lambda :self.move(self.btn_7))
        self.btn_8 = Button(root, bg="white", bd=0, command=lambda :self.move(self.btn_8))
        self.btn_9 = Button(root, bg="white", bd=0, command=lambda :self.move(self.btn_9))

        Label(root, image=self.cross_img).place(x=0, y=220)
        Label(root, image=self.circle_img).place(x=200, y=220)
        self.score_pl_1 = Label(root, text=self.player_1_score, font=("Courier 15 bold"))
        self.score_pl_2 = Label(root, text=self.player_2_score, font=("Courier 15 bold"))
        self.player_1 = Label(root, text="Player 1", font=("Courier 15 bold"), bg="blue")
        self.player_2 = Label(root, text="Player 2", font=("Courier 15 bold"), bg="white")

        self.btn_1.place(x=30, y=10, width=55, height=55)
        self.btn_2.place(x=97, y=10, width=55, height=55)
        self.btn_3.place(x=163, y=10, width=55, height=55)
        self.btn_4.place(x=30, y=77, width=55, height=55)
        self.btn_5.place(x=97, y=77, width=55, height=55)
        self.btn_6.place(x=163, y=77, width=55, height=55)
        self.btn_7.place(x=30, y=144, width=55, height=55)
        self.btn_8.place(x=97, y=144, width=55, height=55)
        self.btn_9.place(x=163, y=144, width=55, height=55)
        self.player_1.place(x=0, y=270)
        self.player_2.place(x=150, y=270)
        self.score_pl_1.place(x=60, y=230)
        self.score_pl_2.place(x=170, y=230)

    def move(self, btn):
        if btn not in self.btn_list:
            mixer.music.load("tik.mp3")
            mixer.music.play()
            if self.i%2==1:
                btn.config(image=self.cross_img)
                self.player_1.config(bg="white")
                self.player_2.config(bg="blue")
                self.i += 1

            elif self.i%2==0:
                btn.config(image=self.circle_img)
                self.player_1.config(bg="blue")
                self.player_2.config(bg="white")
                self.i+=1
            self.btn_list.append(btn)
            self.check_winner()

    def check_winner(self):
        if self.btn_1["image"]==str(self.cross_img) and self.btn_2["image"]==str(self.cross_img) and self.btn_3["image"]==str(self.cross_img) or\
            self.btn_4["image"]==str(self.cross_img) and self.btn_5["image"]==str(self.cross_img) and self.btn_6["image"]==str(self.cross_img) or\
            self.btn_7["image"]==str(self.cross_img) and self.btn_8["image"]==str(self.cross_img) and self.btn_9["image"]==str(self.cross_img) or\
            self.btn_1["image"]==str(self.cross_img) and self.btn_4["image"]==str(self.cross_img) and self.btn_7["image"]==str(self.cross_img) or\
            self.btn_2["image"]==str(self.cross_img) and self.btn_5["image"]==str(self.cross_img) and self.btn_8["image"]==str(self.cross_img) or\
            self.btn_3["image"]==str(self.cross_img) and self.btn_6["image"]==str(self.cross_img) and self.btn_9["image"]==str(self.cross_img) or\
            self.btn_3["image"]==str(self.cross_img) and self.btn_5["image"]==str(self.cross_img) and self.btn_7["image"]==str(self.cross_img) or\
            self.btn_1["image"]==str(self.cross_img) and self.btn_5["image"]==str(self.cross_img) and self.btn_9["image"]==str(self.cross_img):
            mixer.music.load("winner.mp3")
            mixer.music.play()
            self.restart_game(string="Player 1 Winner")
            
        elif self.btn_1["image"]==str(self.circle_img) and self.btn_2["image"]==str(self.circle_img) and self.btn_3["image"]==str(self.circle_img) or\
            self.btn_4["image"]==str(self.circle_img) and self.btn_5["image"]==str(self.circle_img) and self.btn_6["image"]==str(self.circle_img) or\
            self.btn_7["image"]==str(self.circle_img) and self.btn_8["image"]==str(self.circle_img) and self.btn_9["image"]==str(self.circle_img) or\
            self.btn_1["image"]==str(self.circle_img) and self.btn_4["image"]==str(self.circle_img) and self.btn_7["image"]==str(self.circle_img) or\
            self.btn_2["image"]==str(self.circle_img) and self.btn_5["image"]==str(self.circle_img) and self.btn_8["image"]==str(self.circle_img) or\
            self.btn_3["image"]==str(self.circle_img) and self.btn_6["image"]==str(self.circle_img) and self.btn_9["image"]==str(self.circle_img) or\
            self.btn_3["image"]==str(self.circle_img) and self.btn_5["image"]==str(self.circle_img) and self.btn_7["image"]==str(self.circle_img) or\
            self.btn_1["image"]==str(self.circle_img) and self.btn_5["image"]==str(self.circle_img) and self.btn_9["image"]==str(self.circle_img):
            mixer.music.load("winner.mp3")
            mixer.music.play()
            self.restart_game(string="Player 2 Winner")
            
        elif self.i==10:
            mixer.music.load("loose.mp3")
            mixer.music.play()
            self.restart_game(string="Tie Game")

    def restart_game(self, string):
        msg = messagebox.askyesno("Tic Tac Toe", string)
        if msg:
            self.btn_1["image"] = ""
            self.btn_2["image"] = ""
            self.btn_3["image"] = ""
            self.btn_4["image"] = ""
            self.btn_5["image"] = ""
            self.btn_6["image"] = ""
            self.btn_7["image"] = ""
            self.btn_8["image"] = ""
            self.btn_9["image"] = ""
            self.i = 1
            self.btn_list.clear()
            if string=="Player 1 Winner":
                self.player_1_score += 1
                self.score_pl_1["text"] = self.player_1_score
            elif string=="Player 2 Winner":
                self.player_2_score += 1
                self.score_pl_2["text"] = self.player_2_score
        else:
            root.destroy()

if __name__ == '__main__':
    root = Tk()
    obj = Game(root)
    mainloop()
