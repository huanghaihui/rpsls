# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

import random

def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return -1
    
def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'number_to_name ERROR!'
    
def rpsls(player_choice):
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5,1)
    comp_choice = number_to_name(comp_number)
    
    diff = (player_number - comp_number)%5
    
    print 'Player chooses ' + player_choice
    print 'Computer chooses ' + comp_choice
    
    if diff == 0:
        print 'Player and Computer tie!'
    elif diff >=3:
        print 'Computer wins!'
    elif diff <=2:
        print 'Player wins!'
    else:
        print 'ERROR!!!'
       
    print ''
        
rpsls('rock')
rpsls('Spock')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')

