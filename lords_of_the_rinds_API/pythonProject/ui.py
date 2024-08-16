from tkinter import *
from lodr_brain import LodrBrain

THEME_COLOR = "#275363"

class LodrInterface:

    def __init__(self, lodr_brain: LodrBrain):
        self.lodr = lodr_brain

        self.window = Tk()
        self.window.title("Lord of the Rings Dialogs")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.image_names()


        self.canvas = Canvas(width=400, height=400, bg="white")
        self.quote_text = self.canvas.create_text(
            200,
            200,
            width=200,
            text="Some Lord of the rings text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))

        # image_canvas = PhotoImage(file="image/hobbit.png")
        # self.canvas.create_image(200, 200, image=image_canvas)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        image = PhotoImage(file="image/lotr.png")
        self.lotr_button = Button(width=400, height=100,image=image, highlightthickness=0, command=self.button_pressed)
        self.lotr_button.grid(row=2, column=0)


        self.get_next_dialog()


        self.window.mainloop()

    def get_next_dialog(self):
        quote_text = self.lodr.next_quote()
        self.canvas.itemconfig(self.quote_text, text=quote_text)

    def button_pressed(self):
        self.get_next_dialog()