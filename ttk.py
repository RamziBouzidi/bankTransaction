import customtkinter
from zervicezDb import checkUzer,createUser,modifyUzer

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Frame Switching Example")
        self.geometry("400x300")
        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        
        for F in (StartPage, PageOne,Failed,Zuccezz):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage,"origin")

        

    def show_frame(self, cont,name):
        frame = self.frames[cont]
        if name == "PageOne":
            
            actualName = frame.name.get("0.0", "end")
            actualFullName = frame.fullname.get("0.0", "end")
            rezult = checkUzer(actualName,actualFullName)
            if rezult:
                frame = self.frames[Zuccezz]
                frame.mezzage = "Tranzaction Method \n "          
                frame.tkraise()
            else:
                frame = self.frames[Failed]
                frame.tkraise()
        elif name == "create":
            actualName = frame.name.get("0.0", "end")
            actualFullName = frame.fullname.get("0.0", "end")
            actualEmail = frame.email.get("0.0", "end")
            rezult = createUser(actualName,actualFullName,actualEmail,0)
            if rezult == True:
                frame = self.frames[Zuccezz]
                self.button.grid_remove()
                self.label1.grid_remove()
                self.depozit.grid_remove()
                self.withdraw.grid_remove()
                self.Loan.grid_remove()
                self.label2.grid_remove()
                self.label3.grid_remove()
                frame.mezzage = "Uzer created zuccezzfully"
                frame.tkraise()
            else:
                frame = self.frames[Failed]
                frame.mezzage = "Failed to create a uzer"

                frame.tkraise()

        elif name == "origin":
            frame.tkraise()
            print("welcome")

        elif name == "main":
            frame.tkraise()

class StartPage(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(3,weight=0)
        self.grid_rowconfigure(2,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(0,weight=1)
        
        button = customtkinter.CTkButton(self, text="Login",
                                           command=lambda: controller.show_frame(StartPage,"PageOne"))
        button.grid(row=3, column=0, padx=20, pady=20, sticky="sew",columnspan=3)
        label = customtkinter.CTkLabel(self, text="Name")
        label.grid(row=0,column = 0 ,pady=10, padx=10,sticky="w")
        self.name = customtkinter.CTkTextbox(self,height=5, corner_radius=10)
        self.name.grid(row=0,column=1,sticky="ew")
        self.fullname = customtkinter.CTkTextbox(self,height=5, corner_radius=10)
        self.fullname.grid(row=1,column=1,sticky="ew")
        self.email = customtkinter.CTkTextbox(self,height=5, corner_radius=10)
        self.email.grid(row=2,column=1,sticky="ew")
        self.label2 = customtkinter.CTkLabel(self,text="FullName")
        self.label2.grid(row=1,column = 0 ,pady=10, padx=10,sticky="w")
        self.label3 = customtkinter.CTkLabel(self, text="email")
        self.label3.grid(row=2,column = 0 ,pady=10, padx=10,sticky="w")
        self.button2 = customtkinter.CTkButton(self, text="Create",
                                           command=lambda: controller.show_frame(StartPage,"create"))
        self.button2.grid(row=4, column=0, padx=20, pady=20, sticky="sew",columnspan=3)


class PageOne(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        label = customtkinter.CTkLabel(self, text="Choose a transaction method")
        label.grid(pady=10, padx=10)
        button = customtkinter.CTkButton(self, text="Go to Start Page",
                                           command=lambda: controller.show_frame(StartPage,"main"))
        button.grid()

class Failed(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=0)
    
        super().__init__(master)
        self.mezzage = ""
        textt = customtkinter.CTkLabel(self,text=self.mezzage)
        textt.grid(row=0,column=0,padx=20, pady=20, sticky="nsew")
        button = customtkinter.CTkButton(self, text="Exit",
                                           command=lambda: controller.show_frame(StartPage,"main"))
        button.grid(row=1, column=0, padx=20, pady=20, sticky="sew",columnspan=3)

class Zuccezz(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=0)
    
        super().__init__(master)
        self.mezzage = ""
        
        
        ztatuz = customtkinter.CTkLabel(self,text= self.mezzage)
        ztatuz.grid_remove(row=0,column=0,padx=20, pady=20, sticky="nsew")
        
        



        button = customtkinter.CTkButton(self, text="Zubmit",
                                           command=lambda: controller.show_frame(StartPage,"PageOne"))
        button.grid(row=3, column=0, padx=20, pady=20, sticky="sew",columnspan=3)
        label1 = customtkinter.CTkLabel(self, text="Depozit")
        label1.grid(row=0,column = 0 ,pady=10, padx=10,sticky="w")
        self.depozit = customtkinter.CTkTextbox(self,height=5, corner_radius=10)
        self.depozit.grid(row=0,column=1,sticky="ew")
        self.withdraw = customtkinter.CTkTextbox(self,height=5, corner_radius=10)
        self.withdraw.grid(row=1,column=1,sticky="ew")
        self.Loan = customtkinter.CTkTextbox(self,height=5, corner_radius=10)
        self.Loan.grid(row=2,column=1,sticky="ew")
        self.label2 = customtkinter.CTkLabel(self,text="Withdraw")
        self.label2.grid(row=1,column = 0 ,pady=10, padx=10,sticky="w")
        self.label3 = customtkinter.CTkLabel(self, text="Loan")
        self.label3.grid(row=2,column = 0 ,pady=10, padx=10,sticky="w")
        self.button2 = customtkinter.CTkButton(self, text="Exit",
                                           command=lambda: controller.show_frame(StartPage,"main"))
        self.button2.grid(row=4, column=0, padx=20, pady=20, sticky="sew",columnspan=3)

    

if __name__ == "__main__":
    app = App()
    app.grid_columnconfigure(0, weight=1)
    app.mainloop()