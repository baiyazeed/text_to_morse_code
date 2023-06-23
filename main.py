# ----------------------------------------Steps to build the Morse Code Translator in Tkinter---------------------------------------- #

# Import the necessary modules:

# Import the tkinter module as tk to create the GUI.
# Create the Morse code dictionary:

# Define a dictionary called morse_code that maps each English character to its corresponding Morse code representation.
# Define the conversion function:

# Create a function, such as convert_to_morse(), which retrieves the text entered by the user, iterates through each character, looks up its Morse code value in the dictionary, and builds the Morse code string.
# Update a label or output field to display the Morse code text.
# Create the main window:

# Use tk.Tk() to create the main window for the GUI application.
# Set the window title using window.title().
# Create the input entry field:

# Use tk.Entry() to create an input field where the user can enter English text.
# Adjust the width of the entry field using the width parameter.
# Use .pack() to place the entry field in the window layout.
# Create the "Convert" button:

# Use tk.Button() to create 2 buttons labeled "To Morse" and "To English".
# Set the command parameter to the name of the corresponding conversion function (e.g., command=convert_to_morse and command=convert_to_english).
# Use .grid() to place the button in the window layout.
# Create the output label:

# Use tk.Label() to create a label for displaying the Morse code output.
# Set the initial text of the label to an empty string or a default value.
# Set the font and any desired formatting options.
# Use .grid() to place the label in the window layout.
# Start the GUI loop:

# Use window.mainloop() to start the main loop of the GUI application.
# This loop will handle events and keep the application running until the window is closed.

# ----------------------------------------------------------------Code-------------------------------------------------------------- #


from tkinter import *

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def convert_to_morse():
    text = entry.get()
    morse_text = ''
    for char in text:
        if char.upper() in morse_code:
            morse_text += morse_code[char.upper()] + ' '
    return output_label.config(text=morse_text)
    
def convert_to_english():
    text = entry.get()
    english_text = ''
    for char in text.split():
        for key, value in morse_code.items():
            if char == value:
                english_text += key
    return output_label.config(text=english_text)

# Create the main window
window = Tk()
window.title("Morse Code Converter")
window.config(padx=30, pady=30)

# Create the input entry field
entry = Entry(window, width=100)
entry.grid(column=0, row=0, columnspan=2, padx=10, pady=1)

# Create the "Convert" button
convert_button_1 = Button(window, text="To Morse", command=convert_to_morse)
convert_button_2 = Button(window, text="To English", command=convert_to_english)
convert_button_1.grid(column=0, row=1)
convert_button_2.grid(column=1, row=1)

# Create the label for displaying the output
output_label = Label(window, text="", font=("Arial", 12), width=70)
output_label.grid(column=0, row=2, columnspan=2)

# Start the main GUI loop
window.mainloop()
