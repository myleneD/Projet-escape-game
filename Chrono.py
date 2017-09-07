import Tkinter


class Chrono(Tkinter.Label):
    def __init__(self,root,startTime=60):
        Tkinter.Label.__init__(self,root,text='Starting...')

        self.value=startTime
        self.font=('Helvetica', 36, 'normal')
        self.__setitem__('font',self.font)
        self.after(1000,self.count)

    def formatTime(self):
        return str(self.value/60)+': '+str(self.value%60)

    def count(self):
        self.value=self.value-1
        self.__setitem__('text',self.formatTime())
        self.after(1000,self.count)

if __name__=="__main__":

    root = Tkinter.Tk()
    root.title('Chtit Chrono')
    label = Chrono(root,3600)
    label.pack()
    root.mainloop()
