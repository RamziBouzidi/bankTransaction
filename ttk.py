import customtkinter

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
        
        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        """Raises the desired frame to the top"""
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.grid_columnconfigure(0,weight=1)
        button = customtkinter.CTkButton(self, text="Login/Create",
                                           command=lambda: controller.show_frame(PageOne))
        button.grid(row=3, column=0, padx=20, pady=20, sticky="ew",columnspan=3)
        label = customtkinter.CTkLabel(self, text="Name")
        label.grid(row=0,column = 0 ,pady=10, padx=10,sticky="w")
        label2 = customtkinter.CTkLabel(self,text="FullName")
        label2.grid(row=1,column = 0 ,sticky="w")
        label3 = customtkinter.CTkLabel(self, text="email")
        label3.grid(row=2,column = 0 ,sticky="w")

        
       
        

class PageOne(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        label = customtkinter.CTkLabel(self, text="Page One")
        label.pack(pady=10, padx=10)
        button = customtkinter.CTkButton(self, text="Go to Start Page",
                                           command=lambda: controller.show_frame(StartPage))
        button.pack()

if __name__ == "__main__":
    app = App()
    app.grid_columnconfigure(0, weight=1)
    app.mainloop()