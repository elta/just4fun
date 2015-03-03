#! /usr/bin/python
# Example of <python and tkinter programming>

from Tkinter import *

def frame(root,side):
  w=Frame(root)
  w.pack(side=side,expand=YES,fill=BOTH)
  return w

def button(root,side,text,command=None):
  w=Button(root,text=text,command=command)
  w.pack(side=side,expand=YES,fill=BOTH)
  return w

class Calculator(Frame):
  def __init__(self):
    Frame.__init__(self)
    self.pack(expand=YES,fill=BOTH)
    self.master.title("Simple Calculator")
    self.master.iconname("calcl")

    display=StringVar()
    Entry(self,relief=SUNKEN,textvariable=display).pack(side=TOP, expand=YES,fill=BOTH)

    for key in ("123","456","789","-0."):
      deyF=frame(self,TOP)
      for char in key:
        button(deyF,LEFT,char,lambda w=display,s="%s"%char: w.set (w.get()+s))

    opsF=frame(self,TOP)
    for char in "+-*/=":
      if char=='=':
        btn=button(opsF,LEFT,char)
        btn.bind("<ButtonRelease-1>",lambda e,s=self, w=display: s.clac(w),'+')
      else:
        btn=button(opsF,LEFT,char,lambda w=display,c=char: w.set (w.get()+' '+c+' '))

    clearF=frame(self,BOTTOM)
    button(clearF,LEFT,'Clr',lambda w=display: w.set(' '))

  def clac(self,display):
    try:
      display.set(eval(display.get()))
    except SyntaxError:
      display.set("ERROR")
    except ZeroDivisionError:
      display.set("ZeroDivisionError")

if __name__=="__main__":
   Calculator().mainloop()

