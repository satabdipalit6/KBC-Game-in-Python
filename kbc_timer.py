from distutils import command
from itertools import count
from tkinter import *
from tkinter import ttk
import pygame
from PIL import Image , ImageTk
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3
import time


def main():

    win=Tk()
    app=welcome_window(win)
    win.mainloop()

class welcome_window:

    mixer.init()

    def __init__(self,root):
         self.root=root
         self.root.geometry('1366x768+0+0')
         self.root.title('Welcome Window ')
         self.root.config (bg='black')
        
        #--------------------Top Frame---------------------------------------------------------------------------------
         self.Topframe=Frame(self.root,bg='green',width=1400,height=100,highlightbackground='black',highlightthickness='5')
         self.Topframe.grid(row=0 , column= 0)

         self.firstlbl=Label(self.Topframe,text='Bhadrak Engineering School & Technology',font=('arial',25,'bold'),bg='yellow',bd=1)
         self.firstlbl.grid(row=0,column=0,padx=0,pady=0)
         self.firstlbl.place(x=400,y=10)

         self.secondlbl=Label(self.Topframe,text='Asurali,Bhadrak',font=('arial',25,'bold'),bg='yellow',bd=1)
         self.secondlbl.grid(row=1,column=0,padx=0,pady=10)
         self.secondlbl.place(x=600,y=50)
        
         #------------------Middle Frame--------------------------------------------------------------------------------
         self.midframe=Frame(self.root,bg='red',width=1400,height=500,highlightbackground='black',highlightthickness='4')
         self.midframe.grid(row=1 , column= 0)
         
         self.firstlbl=Label(self.midframe,text='Computer Science & Engineering Department',font=('arial',25,'bold'),bg='white',bd=1)
         self.firstlbl.grid(row=0,column=0,padx=0,pady=0)
         self.firstlbl.place(x=400,y=0)

         self.secondlbl=Label(self.midframe,text='Welcome To  ',font=('arial',25,'bold'),bg='white',bd=1)
         self.secondlbl.grid(row=1,column=0,padx=0,pady=10)
         self.secondlbl.place(x=620,y=40)

         self.kbc_adImage=ImageTk.PhotoImage(file='KBC_ad.png')
         self.thirdlbl=Label(self.midframe,image=self.kbc_adImage,bg='red',width= 550,height=400)
         self.thirdlbl.grid(row=1,column=0,padx=0,pady=0)
         self.thirdlbl.place(x=450,y=80)

         mixer.music.load('Kbc_Intro.wav')
         mixer.music.play()

         #----------------------------------buttom Frame----------------------------------------------------------------
         self.buttomframe=Frame(root,bg='blue',width=1400,height=300)
         self.buttomframe.grid(row=2 , column= 0)

         self.start_btn=Button (self.buttomframe,text='Lets Start',bg='yellow',fg='black',font=('arial',15,'bold'),bd=0,activebackground='black',cursor='hand2',command=self.gamewindow)
         self.start_btn.place(x=650,y=10)

    def gamewindow(self):

            self.new_window=Toplevel(self.root)
            self.app= game_window(self.new_window)
            
         #----------------Game Window-------------------------------------------------------------

class game_window:

    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)

    mixer.init()

    def select(self,event):
           

             self.ProgressbarA.place_forget()
             self.ProgressbarB.place_forget()
             self.ProgressbarC.place_forget()
             self.ProgressbarD.place_forget() 

             self.ProgressbarLabelA.place_forget()
             self.ProgressbarLabelB.place_forget()
             self.ProgressbarLabelC.place_forget()
             self.ProgressbarLabelD.place_forget()
             self.callbtn.place_forget()

             b=event.widget
             value=b['text'] 
               

             for i in range(15):  
                 
                 if value==self.correct_answers[i]:
                
                    if value== self.correct_answers[14]:
                            def close():
                                  root2.destroy()
                                  self.root.destroy() 

                            def playagain():

                                self.lifeline50btn.config(state=NORMAL,image=self.image50)
                                self.lifelineaudiencebtn.config(state=NORMAL,image=self.imageAudience)
                                self.lifelinephoneAFriendbtn.config(state=NORMAL,image=self.imagephoneAFriend)


                                root2.destroy()
                                self.questionArea.delete(1.0,END) 
                                mixer.music.load('start.wav')
                                mixer.music.play()
                                self.questionArea.insert(END,self.questions[0])
                                self.optionbtn1.config(text=self.first_option[0])
                                self.optionbtn2.config(text=self.second_option[0])
                                self.optionbtn3.config(text=self.third_option[0])
                                self.optionbtn4.config(text=self.fourth_option[0])
                                self.prizelbl.config(image=self.prizeImage)
                                
                            root2=Toplevel()
                            root2.config(bg='black')
                            root2.geometry('500x400+140+30')
                            root2.title('You won 1 crore')
                            imglbl=Label(root2,image=self.centerImage,bd=0,bg='black')
                            imglbl.pack(pady=30)
                            winLabel= Label(root2,text='U won 1 Crore...',font=('arial',40,'bold'),bg='black',fg='white')
                            winLabel.pack()
                            playagainbtn=Button(root2,text='Play Again',font=('arial',20,'bold'),bg='black',fg='white',activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=playagain)
                            playagainbtn.pack()
                            closebtn=Button(root2,text='Close',font=('arial',20,'bold'),bg='black',fg='white',activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=close)
                            closebtn.pack()
                            happyImage=PhotoImage(file='happy.png')
                            happylbl=Label(root2,image=happyImage)
                            happylbl.place(x=30,y=250)
                            happylbl1=Label(root2,image=happyImage)
                            happylbl1.place(x=400,y=250)
                            self.prizelbl.config(image=self.prizeImage15) 
                            mixer.music.load('final_mp3.mp3')
                            mixer.music.play()
                            root1.mainloop()
                            break                   
                    def quit():
                            root4.destroy()
                            self.root.destroy()
                    
                    mixer.music.load('claps.wav')
                    mixer.music.play()  
                    time.sleep(3) 
                    mixer.music.load('congo.wav')
                    mixer.music.play()   
                    
                    time.sleep(10)

                    self.questionArea.delete(1.0,END)  
                    self.questionArea.insert(END,self.questions[i+1])
                    self.optionbtn1.config(text=self.first_option[i+1])
                    self.optionbtn2.config(text=self.second_option[i+1])
                    self.optionbtn3.config(text=self.third_option[i+1])
                    self.optionbtn4.config(text=self.fourth_option[i+1])
                    self.prizelbl.config(image=self.prizeImages[i])

                    root4=Toplevel()
                    root4.config(bg='green')
                    root4.geometry('400x300+140+30')
                    root4.title('Quit')
                    Quitbtn=Button(root4,text='Do u want to Quit',font=('arial',15,'bold'),bg='yellow',fg='black',activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=quit)
                    Quitbtn.pack()
                    
                    mixer.music.load('start.wav')
                    mixer.music.play()
                    
                         
                    
                    

                 if value not in self.correct_answers:
                   

                   def tryagain():
                               self.lifeline50btn.config(state=NORMAL,image=self.image50)
                               self.lifelineaudiencebtn.config(state=NORMAL,image=self.imageAudience)
                               self.lifelinephoneAFriendbtn.config(state=NORMAL,image=self.imagephoneAFriend)

                               root1.destroy()
                               self.questionArea.delete(1.0,END)
                               mixer.music.load('start.wav')
                               mixer.music.play()
                               self.questionArea.insert(END,self.questions[0])
                               self.optionbtn1.config(text=self.first_option[0])
                               self.optionbtn2.config(text=self.second_option[0])
                               self.optionbtn3.config(text=self.third_option[0])
                               self.optionbtn4.config(text=self.fourth_option[0])
                               self.prizelbl.config(image=self.prizeImage)
                            

                   def close():
                         
                         root1.destroy()
                         self.root.destroy()
                     
                   root1=Toplevel()
                   root1.config(bg='black')
                   root1.geometry('500x400+140+30')
                   root1.title('You won 0 Rupee')
                   imglbl=Label(root1,image=self.centerImage,bd=0,bg='black')
                   imglbl.pack(pady=30)

                   loseLabel= Label(root1,text='You Lose',font=('arial',40,'bold'),bg='black',fg='white')
                   loseLabel.pack()

                   tryagainbtn=Button(root1,text='Try Again',font=('arial',20,'bold'),bg='black',fg='white',activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=tryagain)
                   tryagainbtn.pack()


                   closebtn=Button(root1,text='Close',font=('arial',20,'bold'),bg='black',fg='white',activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=close)
                   closebtn.pack()

                   mixer.music.load('wrong.wav')
                   mixer.music.play()
                   sadImage=PhotoImage(file='sad.png')
                   sadlbl=Label(root1,image=sadImage)
                   sadlbl.place(x=30,y=250)

                   
                   sadlbl1=Label(root1,image=sadImage)
                   sadlbl1.place(x=400,y=250)


                   root1.mainloop()
                   break
                 

    def lifeline50(self):
            self.lifeline50btn.config(image=self.image50X,state=DISABLED) 
            if self.questionArea.get(1.0,'end-1c') == self.questions[0]:
                mixer.music.load('50-50.mp3')
                mixer.music.play()
                self.optionbtn1.config(text='')
                self.optionbtn3.config(text='')  

            if self.questionArea.get(1.0,'end-1c') == self.questions[1]:
                mixer.music.load('50-50.mp3')
                mixer.music.play()
                self.optionbtn1.config(text='')
                self.optionbtn4.config(text='')  

            if self.questionArea.get(1.0,'end-1c') == self.questions[2]:
                mixer.music.load('50-50.mp3')
                mixer.music.play()
                self.optionbtn2.config(text='')
                self.optionbtn4.config(text='') 

            if self.questionArea.get(1.0,'end-1c') == self.questions[3]:
                mixer.music.load('50-50.mp3')
                mixer.music.play()
                self.optionbtn1.config(text='')
                self.optionbtn2.config(text='') 

            if self.questionArea.get(1.0,'end-1c') == self.questions[4]:
                mixer.music.load('50-50.mp3')
                mixer.music.play()
                self.optionbtn3.config(text='')
                self.optionbtn4.config(text='')       
            if self.questionArea.get(1.0,'end-1c') == self.questions[5]:
                mixer.music.load('50-50.mp3')
                mixer.music.play()
                self.optionbtn2.config(text='')
                self.optionbtn3.config(text='')   
            if self.questionArea.get(1.0,'end-1c') == self.questions[6]:
                mixer.music.load('50-50.mp3')
                mixer.music.play()
                self.optionbtn1.config(text='')
                self.optionbtn4.config(text='') 

            if self.questionArea.get(1.0,'end-1c') == self.questions[7]:
                mixer.music.load('50-50.mp3')
                mixer.music.play()
                self.optionbtn1.config(text='')
                self.optionbtn4.config(text='') 

            if self.questionArea.get(1.0,'end-1c') == self.questions[8]:
                mixer.music.load('50-50.mp3')
                mixer.music.play()
                self.optionbtn1.config(text='')
                self.optionbtn4.config(text='') 

            if self.questionArea.get(1.0,'end-1c') == self.questions[9]:
                mixer.music.load('50-50.mp3')
                mixer.music.play()
                self.optionbtn1.config(text='')
                self.optionbtn4.config(text='')  

            if self.questionArea.get(1.0,'end-1c') == self.questions[10]:
                mixer.music.load('50-50.mp3')
                mixer.music.play()
                self.optionbtn1.config(text='')
                self.optionbtn2.config(text='')    

            if self.questionArea.get(1.0,'end-1c') == self.questions[11]:
                mixer.music.load('50-50.mp3')
                mixer.music.play()
                self.optionbtn1.config(text='')
                self.optionbtn4.config(text='') 

            if self.questionArea.get(1.0,'end-1c') == self.questions[12]:
                mixer.music.load('50-50.mp3')
                mixer.music.play()
                self.optionbtn1.config(text='')
                self.optionbtn3.config(text='')   

            if self.questionArea.get(1.0,'end-1c') == self.questions[13]:
                mixer.music.load('50-50.mp3')
                mixer.music.play()
                self.optionbtn1.config(text='')
                self.optionbtn2.config(text='')  

            if self.questionArea.get(1.0,'end-1c') == self.questions[14]:
                mixer.music.load('50-50.mp3')
                mixer.music.play()
                self.optionbtn1.config(text='')
                self.optionbtn4.config(text='')  

    def lifelineaudiencepole(self):
            self.ProgressbarA.place(x=580,y=190)
            self.ProgressbarB.place(x=620,y=190)
            self.ProgressbarC.place(x=660,y=190)
            self.ProgressbarD.place(x=700,y=190)

            self.ProgressbarLabelA.place(x=580,y=320)
            self.ProgressbarLabelB.place(x=620,y=320)
            self.ProgressbarLabelC.place(x=660,y=320)
            self.ProgressbarLabelD.place(x=700,y=320)

            self.lifelineaudiencebtn.config(image=self.imageAudienceX,state=DISABLED) 
            if self.questionArea.get(1.0,'end-1c') == self.questions[0]:
                 mixer.music.load('audience pole.mp3')
                 mixer.music.play()
                 self.ProgressbarA.config(value=60)
                 self.ProgressbarB.config(value=20)
                 self.ProgressbarC.config(value=40)
                 self.ProgressbarD.config(value=80)
            if self.questionArea.get(1.0,'end-1c') == self.questions[1]:
                 mixer.music.load('audience pole.mp3')
                 mixer.music.play()
                 self.ProgressbarA.config(value=60)
                 self.ProgressbarB.config(value=80)
                 self.ProgressbarC.config(value=40)
                 self.ProgressbarD.config(value=30)     
            if self.questionArea.get(1.0,'end-1c') == self.questions[2]:
                 mixer.music.load('audience pole.mp3')
                 mixer.music.play()
                 self.ProgressbarA.config(value=70)
                 self.ProgressbarB.config(value=20)
                 self.ProgressbarC.config(value=40)
                 self.ProgressbarD.config(value=30) 
            if self.questionArea.get(1.0,'end-1c') == self.questions[3]:
                 mixer.music.load('audience pole.mp3')
                 mixer.music.play()
                 self.ProgressbarA.config(value=60)
                 self.ProgressbarB.config(value=10)
                 self.ProgressbarC.config(value=80)
                 self.ProgressbarD.config(value=20)   
            if self.questionArea.get(1.0,'end-1c') == self.questions[4]:
                 mixer.music.load('audience pole.mp3')
                 mixer.music.play()
                 self.ProgressbarA.config(value=60)
                 self.ProgressbarB.config(value=80)
                 self.ProgressbarC.config(value=40)
                 self.ProgressbarD.config(value=70)
            if self.questionArea.get(1.0,'end-1c') == self.questions[5]:
                 mixer.music.load('audience pole.mp3')
                 mixer.music.play()
                 self.ProgressbarA.config(value=85)
                 self.ProgressbarB.config(value=20)
                 self.ProgressbarC.config(value=40)
                 self.ProgressbarD.config(value=70) 
            if self.questionArea.get(1.0,'end-1c') == self.questions[6]:
                 mixer.music.load('audience pole.mp3')
                 mixer.music.play()
                 self.ProgressbarA.config(value=60)
                 self.ProgressbarB.config(value=80)
                 self.ProgressbarC.config(value=40)
                 self.ProgressbarD.config(value=50) 
            if self.questionArea.get(1.0,'end-1c') == self.questions[7]:
                 mixer.music.load('audience pole.mp3')
                 mixer.music.play()
                 self.ProgressbarA.config(value=20)
                 self.ProgressbarB.config(value=70)
                 self.ProgressbarC.config(value=40)
                 self.ProgressbarD.config(value=30)
            if self.questionArea.get(1.0,'end-1c') == self.questions[8]:
                 mixer.music.load('audience pole.mp3')
                 mixer.music.play()
                 self.ProgressbarA.config(value=60)
                 self.ProgressbarB.config(value=50)
                 self.ProgressbarC.config(value=80)
                 self.ProgressbarD.config(value=20)
            if self.questionArea.get(1.0,'end-1c') == self.questions[9]:
                 mixer.music.load('audience pole.mp3')
                 mixer.music.play()
                 self.ProgressbarA.config(value=10)
                 self.ProgressbarB.config(value=20)
                 self.ProgressbarC.config(value=70)
                 self.ProgressbarD.config(value=40) 
            if self.questionArea.get(1.0,'end-1c') == self.questions[10]:
                 mixer.music.load('audience pole.mp3')
                 mixer.music.play()
                 self.ProgressbarA.config(value=60)
                 self.ProgressbarB.config(value=20)
                 self.ProgressbarC.config(value=40)
                 self.ProgressbarD.config(value=80) 
            if self.questionArea.get(1.0,'end-1c') == self.questions[11]:
                 mixer.music.load('audience pole.mp3')
                 mixer.music.play()
                 self.ProgressbarA.config(value=60)
                 self.ProgressbarB.config(value=20)
                 self.ProgressbarC.config(value=80)
                 self.ProgressbarD.config(value=70)  
            if self.questionArea.get(1.0,'end-1c') == self.questions[12]:
                 mixer.music.load('audience pole.mp3')
                 mixer.music.play()
                 self.ProgressbarA.config(value=60)
                 self.ProgressbarB.config(value=20)
                 self.ProgressbarC.config(value=40)
                 self.ProgressbarD.config(value=80) 
            if self.questionArea.get(1.0,'end-1c') == self.questions[13]:
                 mixer.music.load('audience pole.mp3')
                 mixer.music.play()
                 self.ProgressbarA.config(value=60)
                 self.ProgressbarB.config(value=20)
                 self.ProgressbarC.config(value=40)
                 self.ProgressbarD.config(value=80) 
            if self.questionArea.get(1.0,'end-1c') == self.questions[14]:
                 mixer.music.load('audience pole.mp3')
                 mixer.music.play()
                 self.ProgressbarA.config(value=60)
                 self.ProgressbarB.config(value=20)
                 self.ProgressbarC.config(value=80)
                 self.ProgressbarD.config(value=40)   

    def lifelinephone(self):
             
             mixer.music.load('calling.mp3')
             mixer.music.play()
             time.sleep(3)
             mixer.music.load('Kbc Amitabh Calling.mp3')
             mixer.music.play()
             self.callbtn.place(x=70,y=260)
             self.lifelinephoneAFriendbtn.config(image=self.imagephoneAFriendX,state=DISABLED)

    def phoneclick(self):
                for i in range(15):
                     if self.questionArea.get(1.0,'end-1c') == self.questions[i]:
                          self.engine.say(f'The answer is {self.correct_answers[i]}')
                          self.engine.runAndWait()
                       

                          

    def __init__(self,root):

        self.root=root
        self.root.title("Welcome KBC GAME")   
        self.root.geometry("1366x768+0+0")
        self.root.config (bg='black')

        
                   


    #------------------------Question & options DB----------------------------------#

        self.questions = ["Q1.Which is the largest country in the world?","How many days are there in a leap year?",
             "Which one of these four birds has the longest beak and feet?",
             "What is the national currency of the United States of America (USA)?",
             "Guido van Rossum in 1991 designed which language?",
             "Finish the sequence: 9, 18, 27, _?",
             "Which one is the first fully supported 64-bit operating system?",
             "Which animal is called the king of the jungle?",
             "what time corresponds to 23:23 hours ?",
             "Which team has won most number of IPL matches ?",
             "Which is the largest planet in our Solar system?",
             "How many continents are there in the world?",
             "How many years are there in one Millenium?",
             "ipad is manufactured by?",
             "Who founded Microsoft?"] 
              

        self.first_option = ["India", "354",
                "Heron", "Euro",
                "Javascript", "36",
                "Windows 7", "Elephant", "11:23PM", "KKR",
                "Earth", "8",
                "100 years", "Google", "Monty Ritz"]
        self.second_option = ["USA", "366",
                 "Parrot", "Peso ",
                 "Python", "34",
                 "Linux", "Lion", "11.11PM", "CSK",
                 "Uranus", "5",
                 "50 years",
                 "Microsoft", "Danis Lio"]

        self.third_option = ["China", "365",
                "Crow", "Dollar",
                "Java", "30",
                "Mac", "Tiger", "7:23PM", "MI",
                "Mars", "7",
                "500 years",
                "Amazon", "Bill Gates"]

        self.fourth_option = ["Russia", "420",
                 "Pigeon", "Yen",
                 "C++", "37",
                 "Windows XP", "Cow", "9.11PM", "RCB",
                 "Jupiter",
                 "6",
                 "1000 years", "Apple",
                 "Jeff Bezos"]

        self.correct_answers = ["Russia", "366", "Heron", "Dollar", "Python", "36",
                   "Linux", "Lion", "7:23PM", "MI", "Jupiter", "7", "1000 years", "Apple",
                   "Bill Gates"]
        



        
  #----------------------------Frame Division------------------------------------------#
        self.leftframe=Frame(self.root,bg="black",padx=90,width=700,height=1500)
        self.leftframe.grid(row=0,column= 0)

        self.topframe=Frame( self.leftframe,bg="black",pady=15,width=100,height=200)
        self.topframe.grid(row=0 ,column=0)

        self.centerframe=Frame(self.leftframe,bg="black",pady=15,width=100,height=200)
        self.centerframe.grid(row=1 ,column=0)

        self.timerbtn=Button(self.root,text='B',font=('arial',15,'bold'),bg='#6c2c96',fg='white',width=2,height=1,activebackground='#6c2c96',bd=0,border=0,command=self.timerwindow)
        self.timerbtn.grid(row=0,column=0)
        

        self.buttomframe=Frame(self.leftframe,bg="black",pady=15,width=100,height=200,)
        self.buttomframe.grid(row=2 ,column=0)

        self.rightframe=Frame (root,pady=25,padx=50,bg="black",width=400,height=100)
        self.rightframe.grid (row=0,column= 1)

        
  #--------------------------LIFE LINE--------------------------------------------#
        self.image50=ImageTk.PhotoImage(file='50-50.png')
        self.image50X=ImageTk.PhotoImage(file='50-50-X.png')

        self.lifeline50btn=Button(self.topframe,image=self.image50,bg="black",bd=0,activebackground='black',width=180,height= 80,command=self.lifeline50)
        self.lifeline50btn.grid(row=0,column=0)

        self.imageAudience=ImageTk.PhotoImage(file='audiencePole.png')
        self.imageAudienceX=ImageTk.PhotoImage(file='audiencePoleX.png')

        self.lifelineaudiencebtn=Button(self.topframe,image=self.imageAudience,bg='black',bd=0,activebackground='black',width=180,height= 80,command=self.lifelineaudiencepole)
        self.lifelineaudiencebtn.grid(row=0,column=1)

        self.imagephoneAFriend=ImageTk.PhotoImage(file='phoneAFriend.png')
        self.imagephoneAFriendX=ImageTk.PhotoImage(file='phoneAFriendX.png')

        self.lifelinephoneAFriendbtn=Button(self.topframe,image=self.imagephoneAFriend,bg='black',bd=0,activebackground='black',width=180,height= 80,command=self.lifelinephone)
        self.lifelinephoneAFriendbtn.grid(row=0,column=2)

        self.callimage=ImageTk.PhotoImage(file='phone.png')
        self.callbtn=Button(root,image=self.callimage,bd=0,bg='black',activebackground='black',cursor='hand2',command=self.phoneclick)

        self.centerImage= ImageTk.PhotoImage(file='center1.png')

        logo=Label( self.centerframe,image=self.centerImage,bg='black',width= 300,height=300)
        logo.grid(row=0,column=0)
 #------------------------------Question Part------------------------------------#
        self.layImage= ImageTk.PhotoImage (file='lay.png')

        laylbl=Label(self.buttomframe,image=self.layImage,bg='black')
        laylbl.grid(row=0,column=0)
        
        self.questionArea=Text(self.buttomframe,font=('arial',18,'bold'),width=34,height=2,wrap='word',bg='black',fg='white',bd=0)
        self.questionArea.place(x=70,y=10)
        self.questionArea.insert(END,self.questions[0])
        
  #--------------------------First option----------------------------------------#      
        lblA=Label(self.buttomframe,text='A :',bg='black',fg='white',font=('arial',15,'bold'))
        lblA.place(x=60,y=110)

        self.optionbtn1=Button (self.buttomframe,text=self.first_option[0],bg='black',fg='white',font=('arial',18,'bold'),bd=0,activebackground='black',cursor='hand2')
        self.optionbtn1.place(x=100,y=100)

  #---------------------------Second option--------------------------------------#
        lblB=Label(self.buttomframe,text='B :',bg='black',fg='white',font=('arial',15,'bold'))
        lblB.place(x=330,y=110)

        self.optionbtn2=Button (self.buttomframe,text=self.second_option[0],bg='black',fg='white',font=('arial',18,'bold'),bd=0,activebackground='black',cursor='hand2')
        self.optionbtn2.place(x=360,y=100)
   #-------------------------third option-----------------------------------------#
        lblC=Label(self.buttomframe,text='C :',bg='black',fg='white',font=('arial',15,'bold'))
        lblC.place(x=60,y=190)

        self.optionbtn3=Button (self.buttomframe,text=self.third_option[0],bg='black',fg='white',font=('arial',18,'bold'),bd=0,activebackground='black',cursor='hand2')
        self.optionbtn3.place(x=100,y=180)     
    #-------------------------Fourth option----------------------------------------#
        lblD=Label(self.buttomframe,text='D :',bg='black',fg='white',font=('arial',15,'bold'))
        lblD.place(x=330,y=190)

        self.optionbtn4=Button (self.buttomframe,text=self.fourth_option[0],bg='black',fg='white',font=('arial',18,'bold'),bd=0,activebackground='black',cursor='hand2')
        self.optionbtn4.place(x=360,y=180)
    
    #------------------------Prize Details------------------------------------------#
        self.prizeImage= ImageTk.PhotoImage (file='Picture0.png')
        time.sleep(5)
        mixer.music.load('start.wav')
        mixer.music.play()
        self.prizeImage1= ImageTk.PhotoImage (file='Picture1.png')
        self.prizeImage2= ImageTk.PhotoImage (file='Picture2.png')
        self.prizeImage3= ImageTk.PhotoImage (file='Picture3.png')
        self.prizeImage4= ImageTk.PhotoImage (file='Picture4.png')
        self.prizeImage5= ImageTk.PhotoImage (file='Picture5.png')
        self.prizeImage6= ImageTk.PhotoImage (file='Picture6.png')
        self.prizeImage7= ImageTk.PhotoImage (file='Picture7.png')
        self.prizeImage8= ImageTk.PhotoImage (file='Picture8.png')
        self.prizeImage9= ImageTk.PhotoImage (file='Picture9.png')
        self.prizeImage10= ImageTk.PhotoImage (file='Picture10.png')
        self.prizeImage11= ImageTk.PhotoImage (file='Picture11.png')
        self.prizeImage12= ImageTk.PhotoImage (file='Picture12.png')
        self.prizeImage13= ImageTk.PhotoImage (file='Picture13.png')
        self.prizeImage14= ImageTk.PhotoImage (file='Picture14.png')
        self.prizeImage15= ImageTk.PhotoImage (file='Picture15.png')
        self.prizelbl=Label(self.rightframe,image=self.prizeImage,bg='black')
        self.prizelbl.grid(row=0,column=0)

        self.prizeImages=[self.prizeImage1,self.prizeImage2,self.prizeImage3,
                         self.prizeImage4,self.prizeImage5,self.prizeImage6,
                         self.prizeImage7,self.prizeImage8,self.prizeImage9,
                         self.prizeImage10,self.prizeImage11,self.prizeImage12,
                         self.prizeImage13,self.prizeImage14,self.prizeImage15]
        
        self.ProgressbarA=Progressbar(root,orient=VERTICAL,length=120)
        self.ProgressbarB=Progressbar(root,orient=VERTICAL,length=120)
        self.ProgressbarC=Progressbar(root,orient=VERTICAL,length=120)
        self.ProgressbarD=Progressbar(root,orient=VERTICAL,length=120)

        self.ProgressbarLabelA=Label(root,text='A',font=('arial',20,'bold'),bg='black',fg='white')
        self.ProgressbarLabelB=Label(root,text='B',font=('arial',20,'bold'),bg='black',fg='white')
        self.ProgressbarLabelC=Label(root,text='C',font=('arial',20,'bold'),bg='black',fg='white')
        self.ProgressbarLabelD=Label(root,text='D',font=('arial',20,'bold'),bg='black',fg='white')

        
        

     #------------------------binding button-----------------------------------------#
        
        self.optionbtn1.bind('<Button-1>',self.select)
        self.optionbtn2.bind('<Button-1>',self.select)
        self.optionbtn3.bind('<Button-1>',self.select)
        self.optionbtn4.bind('<Button-1>',self.select) 
    def timerwindow(self):

            self.new_window=Toplevel(self.root)
            self.app= timer_window(self.new_window)   
         
      
         #----------------Timer Window-------------------------------------------------------------

class timer_window:  
    

          

     def __init__(self,root):

        self.root=root
        self.root.title("Countdown Window")   
        self.root.geometry("300x250")
        self.root.config (bg='black')  


        self.secentry=Entry(root,font=('Calibri',15))
        self.secentry.place(x=60,y=30)
        self.startbtn=Button(root,text='START',font=('Calibri',14),bg='black',fg='white',command=self.countdown)
        self.startbtn.place(x=80,y=70)
        self.soundbtn=Button(root,text='Sound',font=('Calibri',14),bg='black',fg='white',command=self.sound)
        self.soundbtn.place(x=150,y=70)
        self.soundstopbtn=Button(root,text='Stop',font=('Calibri',14),bg='black',fg='white',command=self.stop_sound)
        self.soundstopbtn.place(x=220,y=70)
        self.seclbl=Label(root,text='Secs',font=('Calibri',12),bg='black',fg='white')
        self.seclbl.place(x=20,y=35)


     def countdown(self):
          
          self.startsec=self.secentry.get()
          self.secs=int(self.startsec)
          if self.secs==0:
              self.secentry.delete(0,END) 
              self.secentry.insert(END,"Time's up")
          else:
               
              print(self.secs) 
              time.sleep(1)
              self.secs -= 1
              self.secentry.delete(0,END)
              self.secentry.insert(END,self.secs)
              self.root.after(1,self.countdown)
        
     def sound(self):      
            mixer.music.load('Kbc _Clock.wav')
            mixer.music.play()
            # mixer.music.stop()
     def stop_sound(self):       
            mixer.music.stop()
            self.secs=0
            self.secentry.insert(END,"Time's up")
if __name__ == "__main__":

       main()