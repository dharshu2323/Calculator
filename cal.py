import tkinter as tk
from unicodedata import digit

LIGHT_GRAY = "#F5F5F5"
font=("Comic Sans MS", 12)  
fon=("Comic Sans MS", 24)  



class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("CALCULATOR")
        self.total_expression = ""
        self.current_expression = ""
        
        self.display_frame = self.create_frame()  # Create the display frame first
        self.total_label, self.label = self.create_display_label()
        self.digits={
            7:(1,1),8:(1,2),9:(1,3),4:(2,1),5:(2,2),6:(2,3),1:(3,1),2:(3,2),3:(3,3),0:(4,1),'.':(4,2)        }
        self.operations={"/":"\u00F7","*":"\u00D7","-":"-","+":"+"}
        self.display_button = self.create_button()
        self.display_button.rowconfigure(0,weight=1)
        for x in range(1,5):
                self.display_button.rowconfigure(x,weight=1)
                self.display_button.columnconfigure(x,weight=1)
        self.digit_button()
        self.create_operator_button()
        self.special()
        self.bindkey()
    def bindkey(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event,digit=key: self.add_exp(digit))
        for key in self.operations:
            self.window.bind(str(key), lambda event,operator=key: self.append(operator))

    def special(self):
        self.clear()
        self.equal()
        self.sqrt_btn()
        self.square()
    
    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,bg="#000",fg="#204080" ,font=fon, padx=24)
        total_label.pack(expand=True, fill="both")
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="#000",fg="#204080", font=fon,padx=32)
        label.pack(expand=True, fill="both")
        return total_label, label

    def create_frame(self):
        frame = tk.Frame(self.window, height=20, bg="#082152")
        frame.pack(expand=True, fill="both")
        return frame
    def add_exp(self,value):
        self.current_expression+=str(value)
        self.update()

    def digit_button(self):
        for digit,grid_value in self.digits.items():
            button=tk.Button(self.display_button,text=str(digit),bg="#000",fg="#204080",borderwidth=1,font=font,command=lambda x=digit:self.add_exp(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)
    def append(self,operaotr):
        self.current_expression+=operaotr
        self.total_expression+=self.current_expression
        self.current_expression=""
        self.total()
        self.update()
        

    def create_operator_button(self):
        i=0
        for operator,symbol in self.operations.items():
            button=tk.Button(self.display_button,text=symbol,bg="#000",fg="#204080",borderwidth=2,font=font,command=lambda x=operator:self.append(x))
            button .grid(row=i,column=4,sticky=tk.NSEW)
            i+=1

    def create_button(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    def cll(self):
        self.total_expression=""
        self.current_expression=""
        self.total()
        self.update()
    def clear(self):
        button=tk.Button(self.display_button,text="C",bg="#000",fg="#204080",borderwidth=2,font=font,command=self.cll)
        button .grid(row=0,column=1,sticky=tk.NSEW)
    def sq(self):
        self.current_expression=eval(f"{self.current_expression}**2")
        self.update()
    def square(self):
        button=tk.Button(self.display_button,text="x\u00b2",bg="#000",fg="#204080",borderwidth=2,font=font,command=self.sq)
        button .grid(row=0,column=2,sticky=tk.NSEW)
    def sqrt(self):
        self.current_expression=str(eval(f"{self.current_expression}**0.5"))
        self.update()
    def sqrt_btn(self):
        button=tk.Button(self.display_button,text="\u221ax",bg="#000",fg="#204080",borderwidth=2,font=font,command=self.sqrt)
        button .grid(row=0,column=3,sticky=tk.NSEW)
    def evaluate(self):
        self.total_expression+=self.current_expression
        self.update()
        try:
            self.current_expression=eval(str(self.total_expression))
            self.total_expression=""
        except Exception as e:
            self.current_expression="Error"
        finally:
            self.update()
    def equal(self):
        button=tk.Button(self.display_button,text="=",bg="#000",fg="#204080",borderwidth=2,font=font,command=self.evaluate)
        button .grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)
    def total(self):
        expression=self.total_expression
        for operator,symbol in self.operations.items():
            expression=expression.replace(operator,f'{symbol}')

        self.total_label.config(text=expression)
    def update(self):
        self.label.config(text=self.current_expression)



    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    cal = Calculator()
    cal.run()
