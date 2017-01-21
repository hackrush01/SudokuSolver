import tkinter as tk
from utility import getPuzzlePos



# puzzle = [
#          [8,0,9,  2,0,0,  0,3,0],
#          [2,0,0,  9,8,0,  0,0,7],
#          [0,0,0,  1,6,0,  0,2,8],

#          [0,0,8,  4,0,0,  0,0,3],
#          [6,0,0,  0,0,0,  0,0,8],
#          [5,0,0,  0,0,2,  4,0,0],
         
#          [3,0,0,  0,4,5,  0,0,0],
#          [4,0,0,  0,3,2,  0,0,6],
#          [0,5,0,  0,0,6,  2,0,5]
#           ]

# qPuzzle = [[0 for _ in range(9)] for _ in range(9)]

def outputGUI(solvedPuzzle):
    master = tk.Tk()
    master.resizable(False, False)
    master.title("Sudoku")
    dummyImg = tk.PhotoImage()

    colour1 = 'teal'
    colour2 = 'beige'
    colour = colour1

    # global colour

    for block in range(9):

        colour = colour1 if colour == colour2 else colour2
        
        for box in range(9):

            gridRow = int(int((block / 3)) * 3 + (box / 3))
            gridCol = int(int((block % 3)) * 3 + (box % 3))

            number = solvedPuzzle[block][box] if not solvedPuzzle[block][box] == 0 else ' '

            tk.Label(master, bg=colour, fg='black', image=dummyImg,
             relief='ridge', width=50, height=50,
             compound='center', text=number,
             font=('Helvetica', 20)
             ).grid(row=gridRow, column=gridCol)

    master.mainloop()

# def inputGUI():

#     global master, colour, colour1, colour2
#     labels = []

#     for block in range(9):

#         labels.append([])

#         colour = colour1 if colour == colour2 else colour2
        
#         for box in range(9):

#             gridRow = int(int((block / 3)) * 3 + (box / 3))
#             gridCol = int(int((block % 3)) * 3 + (box % 3))

#             labels[block].append(tk.Label(master, bg=colour, fg='indian red', image=dummyImg,
#                                     relief='ridge', width=50, height=50,
#                                     compound='center',
#                                     font=('Helvetica', 20)
#                                     ))
#             labels[block][box].grid(row=gridRow, column=gridCol)
#             labels[block][box].bind("<Button-1>", boxClick)
#             labels[block][box].bind("<Key>", keyPress)

#         tk.Button(master, compound='center', text='Solve', font=('Helvetica', 20),
#             command=btnClick).grid(row=9, rowspan=3, column=3, columnspan=3, pady=15)

#     master.mainloop()

#     return qPuzzle


# def boxClick(event):
#     event.widget.focus_set()


# def keyPress(event):

#     global qPuzzle

#     if event.char in "123456789":
#         grid_info = event.widget.grid_info()
#         row = int(grid_info["row"])
#         col = int(grid_info["column"])
#         number = event.char

#         event.widget.config(text=number)

#         block, box, number = getPuzzlePos(row, col, number)

#         qPuzzle[block][box] = int(number)

#     elif event.keycode in [22, 119]:
#         event.widget.config(text='')


# def btnClick():
    #     master.quit()

# inputGUI()