from tkinter import *
from tkinter import ttk
from colorthief import ColorThief
import easydev
from tkinter import filedialog as fd
from colormap import rgb2hex

window = Tk()
window.geometry("550x550")
window.title("Random image generator")

intro_label = Label(text="COLOR PALETTE GENERATOR", height=5, font=("Arial", 20, "bold"), fg="grey")
intro_label.pack(side=TOP)

label_frame = Frame()
label_frame.place(x=150, y=100)
input_label = Label(label_frame, text="Upload your image file here", font=("Helvetica", 10, "bold"))
input_label.pack(side=LEFT, pady=20)


def file_dialog():
    name = fd.askopenfilename()
    return name


palette_frame = Frame(width=240, height=80, bg="light grey")
palette_frame.place(x=150, y=290)

later_frame = Frame()
later_frame.place(x=140, y=260)
label_text = Label(later_frame, text="Here are the most prominent colors in the Picture:", font=("Helvetica", 10, "bold"))


class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show)
        self.widget.bind("<Leave>", self.hide)

    def show(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = ttk.Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack()

    def hide(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None


class PaletteObject:
    def __init__(self, color, row, column):
        palette_frame.place(x=50, y=300)
        self.frame = Frame(palette_frame, width=150, height=150)
        self.color = color
        self.row = row
        self.column = column

    def layout(self):
        self.frame.grid(row=self.row, column=self.column)

    def convert_rgb2hex(self):
        new_color = rgb2hex(self.color[0], self.color[1], self.color[2])
        self.frame.config(bg=new_color)
        self.hover = Tooltip(self.frame, new_color)


def uploaded_pic():
    im = ColorThief(file_dialog())

    palette = im.get_palette(color_count=2)

    label_text.pack(side=BOTTOM)

    for i in range(len(palette)):
        palette_object = PaletteObject(palette[i], 0, i)
        palette_object.convert_rgb2hex()
        palette_object.layout()


file_dialog_button = Button(label_frame, text="Upload", font=("Helvetica", 10, "bold"),
                            bg="light blue", command=uploaded_pic)
file_dialog_button.pack(side=RIGHT)

window.mainloop()
