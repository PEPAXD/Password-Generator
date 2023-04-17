import string
import tkinter
import customtkinter
import random

#CHARACTERS
def characters():

    #LETTERS, DIGITS AND SPECIAL-CHARACTERS
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    lettersLower = ""
    lettersUpper = ""

    #SEPARETE UPPER AND LOWER LETTERS
    for caracter in letters:
        if caracter.islower():
            lettersLower += caracter
        else:
            lettersUpper += caracter

    #RETURN ARRAY-CHARACTERS
    arrayCharacters = lettersUpper, lettersLower, special, digits
    return arrayCharacters

#CHECK SWITCH
def characterChecks(arrayCharacters, switch):

    charactersPassword = ""

    lettersUpper = arrayCharacters[0]
    lettersLower = arrayCharacters[1]
    digits = arrayCharacters[2]
    special = arrayCharacters[3]

    #CHECK BOOLEANS
    if switch[0].get() == "on":
        charactersPassword += lettersUpper

    if switch[1].get() == "on":
        charactersPassword += lettersLower

    if switch[2].get() == "on":
        charactersPassword += digits

    if switch[3].get() == "on":
        charactersPassword += special

    #RETURN NEW-CHARACTER STRING
    return charactersPassword

#SLIDER NUMBER
def lenPasswordUser(longPassword, characters):

    pwd = ""
    while len(pwd)<longPassword:

        newChar = random.choice(characters)
        pwd += newChar

    return pwd

#GENERATE AND PRINT RANDOM-PASSWORD
def generatepassword(charactersPassword, lenNumber):

    #CREATE A RANDOM-CHARACTERS PASSWORD
    pwd = ""
    while len(pwd)<lenNumber:

        newChar = random.choice(charactersPassword)
        pwd += newChar

    return pwd

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window appearance
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        # configure window size
        self.geometry(f"{400}x{450}")
        self.resizable(False, False)

        # configure window title
        self.title("Password-Generator 'By Mauro Pepa'")

        # create canvas
        self.frame = customtkinter.CTkFrame(master=self, corner_radius=30)
        self.frame.pack(fill="both", expand=True)
        self.frame.place(relx=0.07, rely=0.07, relwidth=0.87, relheight=0.87)

        # TEXT-LABEL
        self.label = customtkinter.CTkLabel(master=self.frame, text="PASSWORD GENERATOR", font=("Arial Black", 22, "underline"))
        self.label.place(relx=0.5, rely=0.08, anchor=tkinter.CENTER)

        # def switches
        switch_characters = characters()
        def switch_event(index):
            def event():
                characterspassword = characterChecks(switch_characters, switch_vars)
                return characterspassword
            return event


        # array control switches
        switch_vars = [customtkinter.StringVar(value="on") for _ in range(4)]
        for i in range(4):
            switch = customtkinter.CTkSwitch(master=self.frame, text=switch_characters[i], command=switch_event(i),
                                             variable=switch_vars[i], onvalue="on", offvalue="off")
            switch.place(relx=0.15, rely=0.2 + i * 0.1, anchor=tkinter.W)

        # create slider variables longPassword
        def slider_event(value):
            value = int(value)
            numberslider.configure(text=str(value))

            # Calcula la posición relativa del valor en el rango de 1 a 64
            # donde 1 es el extremo izquierdo (rojo) y 64 es el extremo derecho (verde)
            position = (value - 1) / 32

            # Interpola los valores de los componentes RGB para obtener el color
            red = int(255 * (1 - position))
            green = int(255 * position)
            blue = 0

            # Convierte los valores RGB en una cadena hexadecimal para usar como color
            color = f"#{red:02x}{green:02x}{blue:02x}"

            # Configura el color del progreso del slider
            self.slider.configure(progress_color=color)

        # numberslider
        numberslider = customtkinter.CTkLabel(master=self.frame, text="16", font=("Arial", 18))
        numberslider.place(relx=0.5, rely=0.62, anchor=tkinter.CENTER)

        self.slider = customtkinter.CTkSlider(master=self.frame, from_=1, to=32, command=slider_event)
        self.slider.place(relx=0.5, rely=0.67, anchor=tkinter.CENTER)


        # print password
        def click_button():
            lenNumberPassword = int(self.slider.get())
            characterspassword = characterChecks(characters(), switch_vars)
            password = generatepassword(characterspassword, lenNumberPassword)

            self.entry.delete(0, tkinter.END)  # Limpia el cuadro de entrada
            self.entry.insert(0, password)  # Inserta el texto en el cuadro de entrada
            self.entry.justify = tkinter.CENTER

        # create button
        self.button = customtkinter.CTkButton(master=self.frame, text="GENERATE PASSWORD", command=click_button)
        self.button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        # create text-entry
        self.entry = customtkinter.CTkEntry(master=self.frame, placeholder_text=("*"*50), width=250, height=30, corner_radius=8)
        self.entry.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

app = App()
app.mainloop()
