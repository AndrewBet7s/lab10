##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

#main house
rectangle = drawpad.create_rectangle(200,200,500,500, fill='red')
#roof
line = drawpad.create_line(200,200,350,100)

line = drawpad.create_line(350,100,500,200)
#door
rectangle = drawpad.create_rectangle(300,500,400,350, fill='brown')
#windows
rectangle = drawpad.create_rectangle(450,250,400,300, fill='light blue')

rectangle = drawpad.create_rectangle(300,300,250,250, fill='light blue')
#door knob
rectangle = drawpad.create_rectangle(390,420,370,440, fill='grey')
#chimeney
line = drawpad.create_line(500,200,500,100)

line = drawpad.create_line(500,100,460,100)

line = drawpad.create_line(460,175,460,100)
#lawn
rectangle = drawpad.create_rectangle(0,500,600,800, fill='green')

root.mainloop()