from tkinter import Tk, Canvas
import random
import time



class My_button:
    def __init__(self,_id):
        self.height=None
        self.width=None
        self._id=_id
        self.bouton=None
        self.padding=10


class Handle_buttton:
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.__root=Tk()
        self.__root.title("TIC-TAC-TOE GAME")
        self.__root.geometry(f"{self.width}x{self.height}")
        self.buttons=[None  for i in range(9)]
        self.texts=[[None, None] for i in range(9)]
        #self.__root.bind("<Button-1>", lambda event: self.my_function(event))
        self.set_button()
        self.__root.mainloop()
    def set_button(self):
        k=0
        inh=self.width//3
        inv=self.height//3
       
        for i in range(3):
            for j in range(3):
                 a=j+k
                 
                 self.buttons[a]=My_button(a)
                 self.buttons[a].bouton=Canvas(self.__root,borderwidth=3, bg='yellow', height=inh, width=inv, name=f"{a}")
                 
                 self.buttons[a].bouton.bind("<ButtonPress-1>", lambda event: self.my_function(event))
                 #self.buttons[j+k].bouton.pack()
                 self.buttons[a].bouton.place( x=inh*(j), y=inv*(i))
                 time.sleep(0.03)
                 self.texts[a][0]=None
                 self.texts[a][1]=None
                 

            k+=3

    def my_function(self,event):
        
        a= str(event.widget)
        id=int(a[1])
       
        if self.texts[id][1] is not None:
            return
        else:
            random_choice=[]
            self.texts[id][0]=self.buttons[id].bouton.create_text(self.width//6, self.width//6, text="X", font="Arial 45 italic", fill="blue")
            time.sleep(0.03)
            self.texts[id][1]="X"
            for i in range(9):
                for j in range(1,5):
                    nene=self.win_failx(i,j)
                   
                    if nene:
                       return

            for i in range(9):
                if i!=id and self.texts[i][1] is None:
                   
                    random_choice.append(i)
            if len(random_choice)>0:
                
                ka=random.randrange(len(random_choice))
                dd=random_choice[ka]
                time.sleep(0.1)
                self.texts[dd][0]=self.buttons[dd].bouton.create_text(self.width//6, self.width//6, text="O", font="Arial 45 italic", fill="blue")
                time.sleep(0.1)
                self.texts[dd][1]="O"
                for i in range(9):
                   for j in range(1,5):
                       a=self.win_failo(i,j)
                       time.sleep(0.03)
                       if a:
                          return
                   
    def win_failx(self, id,x):

        if id-x>=0 and id+x<len(self.buttons):
            print(id," : ", self.texts[id][1],id-x," : ", self.texts[id-x][1], id+x," :", self.texts[id+x][1])
            if self.texts[id][1]==self.texts[id-x][1] and self.texts[id][1]==self.texts[id+x][1]:
               
                if self.texts[id][1]=="X":
                    for i in range(9):
                        self.buttons[i].bouton.delete("all")
                        time.sleep(0.05)
                    time.sleep(0.05)
                    
                    self.buttons[1].bouton.create_text(self.width//2,self.height//2, text="VOUS AVEZ GAGNE", font="Arial 35 italic", fill="green")
                    time.sleep(0.3)
                    self.buttons[1].bouton.delete("all")
                    time.sleep(0.1)
                    self.set_button()
                    time.sleep(0.02)
                    return True
                
            return False
        return False
    
    def win_failo(self, id,x):
        if id-x>0 and id+x<len(self.buttons):
            
            if self.texts[id][1]==self.texts[id-x][1] and self.texts[id][1]==self.texts[id+x][1]:
                
                if self.texts[id][1]=="O":
                    for i in range(9):
                        self.buttons[i].bouton.delete("all")
                        time.sleep(0.3)
                    time.sleep(0.3)
                    self.buttons[1].bouton.create_text(self.width//6,self.height//6, text="VOUS AVEZ PERDU", font="Arial 35 italic", fill="red")
                    
                    time.sleep(0.3)
                    self.buttons[1].bouton.delete("all")
                    time.sleep(0.02)
                    self.set_button()
                    time.sleep(0.02)
                    return True
            return False
        return False 

def main():
    result = Handle_buttton(600,600)
main()

            





    


           
   