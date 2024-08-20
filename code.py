from tkinter import*
from tkinter import messagebox

class atm:
    def __init__(self, root):
        self.root=root
        blank_space = " "
        self.root.title = (110 * blank_space + "Atm System" )
        self.root.geometry("800x760+280+0")
        self.root.configure(background='grey')
#=====================================FRAME=====================================#
        MainFrame = Frame(self.root, bd=20, width=760, height =700 , relief=RIDGE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd=7, width=734, height =300 , relief=RIDGE)
        TopFrame1.grid(row=1, column=0, padx=12)
        
        TopFrame2 = Frame(MainFrame, bd=7, width=734, height =300 , relief=RIDGE)
        TopFrame2.grid(row=0, column=0, padx=0)

        TopFrame2Left = Frame(TopFrame2, bd=5, width=190, height =300 , relief=RIDGE)
        TopFrame2Left.grid(row=0, column=0, padx=3)

        TopFrame2Mid = Frame(TopFrame2, bd=5, width=200, height =300 , relief=RIDGE)
        TopFrame2Mid.grid(row=0, column=1, padx=3)

        TopFrame2Right = Frame(TopFrame2, bd=5, width=190, height =300 , relief=RIDGE)
        TopFrame2Right.grid(row=0, column=2, padx=3)

#=====================================FUNCTIONS=====================================#
        def enter_Pin() :
            pinNo = self.txtReceipt.get("1.0","end-1c")
            if ((pinNo == str("2213")) or (pinNo == str("1234")) or (pinNo == str("4323"))) :
                self.txtReceipt.delete("1.0",END)
                
                self.txtReceipt.insert(END,'\t\t        ATM' + "\n\n\n\n")
                self.txtReceipt.insert(END,'Withdraw Cash\t\t\t Account Details' + "\n\n\n\n")
                self.txtReceipt.insert(END,'Cash With Receipt\t\t\t Deposit' + "\n\n\n\n")
                self.txtReceipt.insert(END,'Balance\t\t\t New Pin' + "\n\n\n\n")
            

                self.btnArrowL1=Button(TopFrame2Right,width=160, height=60, state=NORMAL,
                command=AcoountDetails,image=self.img_arrow_Right).grid(row=0,column=0,padx =2, pady =2)

                self.btnArrowL2=Button(TopFrame2Right,width=160, height=60, state=NORMAL,
                command=deposit,image=self.img_arrow_Right).grid(row=1 ,column=0, padx =2, pady =2)
        
                self.btnArrowL3=Button(TopFrame2Right,width=160, height=60, state=NORMAL,
                                       command=request_new_pin,
                image=self.img_arrow_Right).grid(row=2,column=0, padx =2, pady =2)
        
                self.btnArrowL4=Button(TopFrame2Right,width=160, height=60, state=NORMAL,
                                       command=statement,
                image=self.img_arrow_Right).grid(row=3,column=0, padx =2, pady =2)

         #====================================================================================================#
         
                self.btnArrowL1=Button(TopFrame2Left,width=160, height=60, state=NORMAL,
                command=withdrawcash,image=self.img_arrow_Left).grid(row=0 ,column=0, padx =2, pady =2)

                self.btnArrowL2=Button(TopFrame2Left,width=160, height=60, state=NORMAL,
                command=withdrawcash,image=self.img_arrow_Left).grid(row=1 ,column=0, padx =2, pady =2)
        
                self.btnArrowL3=Button(TopFrame2Left,width=160, height=60, state=NORMAL,
                                       command=balance,
                image=self.img_arrow_Left).grid(row=2,column=0, padx =2, pady =2)
        
                self.btnArrowL4=Button(TopFrame2Left,width=160, height=60, state=NORMAL,
                                       command=statement,
                image=self.img_arrow_Left).grid(row=3,column=0, padx =2, pady =2)
            else: 
                self.txtReceipt.delete("1.0",END)
                self.txtReceipt.insert(END,'Invalid Pin Number' + "\n\n")
        
      
        def clear():
            self.txtReceipt.delete("1.0",END)
            self.btnArrowL1=Button(TopFrame2Left,width=160, height=60, state=DISABLED,
            image=self.img_arrow_Left).grid(row=0 ,column=0, padx =2, pady =2)

            self.btnArrowL2=Button(TopFrame2Left,width=160, height=60, state=DISABLED,
            image=self.img_arrow_Left).grid(row=1 ,column=0, padx =2, pady =2)
        
            self.btnArrowL3=Button(TopFrame2Left,width=160, height=60, state=DISABLED,
            image=self.img_arrow_Left).grid(row=2,column=0, padx =2, pady =2)
        
            self.btnArrowL4=Button(TopFrame2Left,width=160, height=60, state=DISABLED,
            image=self.img_arrow_Left).grid(row=3,column=0, padx =2, pady =2)
        #=====================================UPPER CLICKABLE BUTTONS OF ATM==========================================#
            self.img_arrow_Right = PhotoImage(file ="rArrow.png")
         
            self.btnArrowL1=Button(TopFrame2Right,width=160, height=60, state=DISABLED,
            image=self.img_arrow_Right).grid(row=0 ,column=0, padx =2, pady =2)

            self.btnArrowL2=Button(TopFrame2Right,width=160, height=60, state=DISABLED,
            image=self.img_arrow_Right).grid(row=1 ,column=0, padx =2, pady =2)
        
            self.btnArrowL3=Button(TopFrame2Right,width=160, height=60, state=DISABLED,
            image=self.img_arrow_Right).grid(row=2,column=0, padx =2, pady =2)
        
            self.btnArrowL4=Button(TopFrame2Right,width=160, height=60, state=DISABLED,
            image=self.img_arrow_Right).grid(row=3,column=0, padx =2, pady =2)
        
        def insert0():
            value0 = 0
            self.txtReceipt.insert(END,value0)

        def insert1():
            value1 = 1
            self.txtReceipt.insert(END,value1)

        def insert2():
            value2 = 2
            self.txtReceipt.insert(END,value2)

        def insert3():
            value3 = 3
            self.txtReceipt.insert(END,value3)

        def insert4():
            value4 = 4
            self.txtReceipt.insert(END,value4)

        def insert5():
            value5 = 5
            self.txtReceipt.insert(END,value5)
        
        def insert6():
            value6 = 6
            self.txtReceipt.insert(END,value6)

        def insert7():
            value7 = 7
            self.txtReceipt.insert(END,value7)

        def insert8():
            value8 = 8
            self.txtReceipt.insert(END,value8)

        def insert9():
            value9 = 9
            self.txtReceipt.insert(END,value9)

        def cancel():
            Cancel = messagebox.askyesno("ATM","Confirm if you want to cancel")
            if Cancel > 0:
                self.root.destroy()
                return
        
        def withdrawcash():
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.focus_set()

        def AcoountDetails():
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'Account Name= Mohammad Shahid\n')
            self.txtReceipt.insert(END,'Account Number= xxxxxxxxxxxxxxx\n')
            self.txtReceipt.insert(END,'Balance= $1296')

            self.txtReceipt.focus_set()

        def deposit():
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'This option is currently unavialable \n')
            self.txtReceipt.focus_set()

        def request_new_pin():
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\t\tWelcome to iBank\n\n')
            self.txtReceipt.insert(END,'New Pin will be send to your home address\n')
            
        def balance(): 
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\t\tWelcome to iBank\n\n')
            self.txtReceipt.insert(END,'$1296' + "\n")
           
        def statement(): 
            pinNo1 = self.txtReceipt.get("1.0" , "end-1c")
            pinNo2 = str(pinNo1)
            pinNo3 = float(pinNo2)
            pinNo4 = float(1296 - pinNo3)
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\n\t' + str(pinNo4) + "\t\t")
            self.txtReceipt.insert(END,'$1296' + "\n")
            self.txtReceipt.insert(END,'\t\t\t\n\n     Account Balance $' + str(pinNo4)+"\t\t\n\n")
            
        #==============================Widget=====================================#
        self.txtReceipt = Text(TopFrame2Mid, height = 17, width =42,bd=12,font=('arial',9,'bold'))
        self.txtReceipt.grid(row=0,column=0)

        self.img_arrow_Left = PhotoImage(file ="1Arrow.png")
        
        self.btnArrowL1=Button(TopFrame2Left,width=160, height=60, state=DISABLED,
        command=withdrawcash,image=self.img_arrow_Left).grid(row=0 ,column=0, padx =2, pady =2)

        self.btnArrowL2=Button(TopFrame2Left,width=160, height=60, state=DISABLED,
        command=withdrawcash,image=self.img_arrow_Left).grid(row=1 ,column=0, padx =2, pady =2)
        
        self.btnArrowL3=Button(TopFrame2Left,width=160, height=60, state=DISABLED,  
                               command=balance,
        image=self.img_arrow_Left).grid(row=2,column=0, padx =2, pady =2)
        
        self.btnArrowL4=Button(TopFrame2Left,width=160, height=60, state=DISABLED,
                               command=statement,
        image=self.img_arrow_Left).grid(row=3,column=0, padx =2, pady =2)
        
        #=====================================UPPER CLICKABLE BUTTONS OF ATM==========================================#
         
        self.img_arrow_Right = PhotoImage(file ="rArrow.png")
        
        self.btnArrowR1=Button(TopFrame2Right,width=160, height=60, state=DISABLED,
        command=AcoountDetails,image=self.img_arrow_Right).grid(row=0 ,column=0, padx =2, pady =2)

        self.btnArrowR2=Button(TopFrame2Right,width=160, height=60, state=DISABLED,
        command=deposit,image=self.img_arrow_Right).grid(row=1 ,column=0, padx =2, pady =2)
        
        self.btnArrowR3=Button(TopFrame2Right,width=160, height=60, state=DISABLED,
                               command=request_new_pin,
        image=self.img_arrow_Right).grid(row=2,column=0, padx =2, pady =2)
        
        self.btnArrowR4=Button(TopFrame2Right,width=160, height=60, state=DISABLED,
                               command=statement,
        image=self.img_arrow_Right).grid(row=3,column=0, padx =2, pady =2)
        #=====================================PIN NUMBER BUTTONS==========================================#
         
        self.img1 = PhotoImage(file ="one.png")
        
        self.btn1=Button(TopFrame1,width=160, height=60,command=insert1,
        image=self.img1).grid(row=2 ,column=0, padx =6, pady =4)
        
        self.img2 = PhotoImage(file ="two.png")

        self.btn2=Button(TopFrame1,width=160, height=60,command=insert2,
        image=self.img2).grid(row=2,column=1, padx =6, pady =4)
        
        self.img3 = PhotoImage(file ="three.png")
        
        self.btn3=Button(TopFrame1,width=160, height=60,command=insert3,
        image=self.img3).grid(row=2,column=2, padx =6, pady =4)
        
        self.imgCE = PhotoImage(file ="cancel.png")
        
        self.btnCancel=Button(TopFrame1,width=160, height=60,command=cancel,
        image=self.imgCE).grid(row=2,column=3, padx =6, pady =4)
        #==================================================================================#
        self.img4 = PhotoImage(file ="four.png")
        
        self.btn4=Button(TopFrame1,width=160, height=60,command=insert4,
        image=self.img4).grid(row=3,column=0, padx =6, pady =4)
        
        self.img5 = PhotoImage(file ="five.png")
        
        self.btn5=Button(TopFrame1,width=160, height=60,command=insert5,
        image=self.img5).grid(row=3,column=1, padx =4, pady =4)
        
        self.img6 = PhotoImage(file ="six.png")
        
        self.btn6=Button(TopFrame1,width=160, height=60,command=insert6,
        image=self.img6).grid(row=3,column=2, padx =4, pady =4)
        
        self.imgCl = PhotoImage(file ="clear.png")
        
        self.btnClear=Button(TopFrame1,width=160, height=60,command=clear,
        image=self.imgCl).grid(row=3,column=3, padx =4, pady =4)
        #======================================================================# 
        self.img7 = PhotoImage(file ="seven.png")
        
        self.btn7=Button(TopFrame1,width=160, height=60,command=insert7,
        image=self.img7).grid(row=4,column=0, padx =6, pady =4)
        
        self.img8 = PhotoImage(file ="eight.png")
        
        self.btn8=Button(TopFrame1,width=160, height=60,command=insert8,
        image=self.img8).grid(row=4,column=1, padx =6, pady =4)
        
        self.img9 = PhotoImage(file ="nine.png")
        
        self.btn9=Button(TopFrame1,width=160, height=60,command=insert9,
        image=self.img9).grid(row=4,column=2, padx =6, pady =4)
        
        self.imgEnter = PhotoImage(file ="Enter.png")
        
        self.btnEnter=Button(TopFrame1,width=160, height=60,command= enter_Pin,
        image=self.imgEnter).grid(row=4,column=3, padx =6, pady =4)
        #======================================================================# 
        self.imgSp1 = PhotoImage(file ="empty.png")
        
        self.btnSp1=Button(TopFrame1,width=160, height=60,
        image=self.imgSp1).grid(row=5,column=0, padx =6, pady =4)
        
        self.imgZero = PhotoImage(file ="zero.png")
        
        self.btnZero=Button(TopFrame1,width=160, height=60,command=insert0,
        image=self.imgZero).grid(row=5,column=1, padx =6, pady =4)
        
        self.imgSp2 = PhotoImage(file ="empty.png")
        
        self.btnSp2=Button(TopFrame1,width=160, height=60,
        image=self.imgSp2).grid(row=5,column=2, padx =6, pady =4)
        
        self.imgSp3 = PhotoImage(file ="empty.png")
        
        self.btnSp3=Button(TopFrame1,width=160, height=60,
        image=self.imgSp3).grid(row=5,column=3, padx =6, pady =4)
        

if __name__=='__main__':
    root= Tk()
    application = atm(root)
    root.mainloop()
        
        