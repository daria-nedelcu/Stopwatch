# template for "Stopwatch: The Game"

import simplegui

# define global variables

tenths = 0
points = 0
stops = 0
timer_is_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    global D
    
    A = t // 600
    B = (t % 600) // 100
    C = ((t % 600) % 100) // 10
    D = ((t % 600) % 100) % 10
    
    return str(A) + ':' + str(B) + str(C) + '.' + str(D)    

    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_button():
    
    global timer_is_running
    timer.start()
    timer_is_running = True
    
def stop_button():
    
    global timer_is_running
    global points
    global stops
    
    timer.stop()
    
    if(timer_is_running):
        stops += 1
        if (D == 0):
            points += 1
            
    timer_is_running = False
    
def reset_button():
    
    global tenths
    global points
    global stops
    tenths = 0
    points = 0
    stops = 0
    timer.stop()
    

# define event handler for timer with 0.1 sec interval

def stopwatch():
    global tenths
    tenths += 1
    
# define draw handler

def printing_stopwatch(canvas):
    
    canvas.draw_text(format(tenths), (100,150), 50, "White")
    score = str(points) + ' / ' + str(stops)
    canvas.draw_text(score, (250,20), 20, "Red")
    
# create frame

frame = simplegui.create_frame("Stopwatch: The Game", 300, 300)

# register event handlers

frame.add_button('Start', start_button, 150)
frame.add_button("Stop", stop_button, 150)
frame.add_button("Reset", reset_button, 150)
frame.set_draw_handler(printing_stopwatch)
timer = simplegui.create_timer(100, stopwatch)

# start frame

frame.start()

# Please remember to review the grading rubric
