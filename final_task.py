import random
import psychopy.visual
from psychopy.core import wait, Clock
from psychopy import core, event
from psychopy import gui
event.globalKeys.add(key='q', modifiers=['ctrl'], func=core.quit)

# creating file for experiment
data_out = open('final_project.txt', 'a', encoding='utf-8')
data_out.write( '\t'.join(["id", "age", "gender", "condition", "trial_number", "stimulus", "response_key", "feedback"]) + "\n" )

print("file was created")

# Participant information
part_info = gui.Dlg(title = "Participant information")
identification = part_info.addField("ID: ")
age = part_info.addField("Age: ")
gender = part_info.addField("Gender: ", choices=["female", "male", "non-binary", "other"])
ok_data = part_info.show()
if part_info.OK:
    print(ok_data)
    data_out.write(str(ok_data) + "\n")
else:
    print("experiment was cancelled.")
    data_out.write("experiment was cancelled.")
    quit()

#define window and stimuli
win = psychopy.visual.Window(
            size = [1000, 800],
            units = "pix",
            fullscr = False,
            color = 'white'
)

blue_rect = psychopy.visual.Rect(
            win = win,
            units = "pix",
            width = 400, 
            height = 200,
            fillColor=["blue"],
)
blue_rect.pos = [-220, 0]

blue_red_rect = psychopy.visual.Rect(
            win = win,
            units = "pix",
            width = 400, 
            height = 200,
            fillColor=["blue"],
            lineColor=["red"],
            lineWidth = 5
)
blue_red_rect.pos = [-220, 0]

green_rect = psychopy.visual.Rect(
            win = win,
            units = "pix",
            width = 400, 
            height = 200,
            fillColor=["green"],
)
green_rect.pos = [220, 0]

green_red_rect = psychopy.visual.Rect(
            win = win,
            units = "pix",
            width = 400, 
            height = 200,
            fillColor=["green"],
            lineColor=["red"],
            lineWidth = 5
)
green_red_rect.pos = [220, 0]

orange_tri = psychopy.visual.Polygon(
            win = win,
            units = "pix",
            radius = 200,
            edges = 3,
            fillColor=["orange"],
)
orange_tri.pos = [-220, 0]

orange_green_tri= psychopy.visual.Polygon(
            win = win,
            units = "pix",
            radius = 200,
            edges = 3,
            fillColor=["orange"],
            lineColor=["green"],
            lineWidth = 5
)

orange_green_tri.pos = [-220, 0]

purple_tri = psychopy.visual.Polygon(
            win = win,
            units = "pix",
            radius = 200,
            edges = 3,
            fillColor=["purple"],
)
purple_tri.pos = [220, 0]

purple_green_tri = psychopy.visual.Polygon(
            win = win,
            units = "pix", 
            radius = 200,
            edges = 3,
            fillColor=["purple"],
            lineColor=["green"],
            lineWidth = 5
)

purple_green_tri.pos = [220, 0]

# welcome texts
welcome_text_social_1 = psychopy.visual.TextStim(win, text = "Welcome to this experiment! \n\n"
                                      "This experiment aims to better understand how people \n"
                                      "use direct and indirect information to learn. \n\n"
                                      "In the following, you will be presented with two rectangles, a green one and a blue one.  \n\n"
                                      "You choose between the two rectangles by pressing the 'k' for right \n"
                                      "and 'd' for left on the keyboard. \nn"
                                      "To help you decide, one of the rectangles will be highlighted by a red border. \n\n"
                                      "This border indicates the choices previous participants have made. \n"
                                      "This information can be pretty useful or less useful, depending on the experience of the participants. \n\n"
                                      "After you have made your choice, you will see whether it was right or wrong. \n\n"
                                      "You will be granted 10 points for every correct choice and 0 points for every incorrect choice. \n\n"
                                      "The experiments consists of 6 rounds. \n"
                                      "To win the gold prize, get at least 50 points. \n"
                                      "To win the silver prize, get at least 40 points. \n\n"
                                      "If you have understood the instructions, press space to continue.",
                                       color = "black")

welcome_text_social_2 = psychopy.visual.TextStim(win, text = "Welcome to this experiment! \n\n"
                                      "This experiment aims to better understand how people \n"
                                      "use direct and indirect information to learn. \n\n"
                                      "In the following, you will be presented with two triangles, an orange one and a purple one. \n\n"
                                      "You choose between the two triangles by pressing the 'k' for right \n"
                                      "and 'd' for left on the keyboard.\n\n"
                                      "To help you decide, one of the triangles will be highlighted by a green border. \n\n"
                                      "This border indicates the choices previous participants have made. \n"
                                      "This information can be pretty useful or less useful, depending on the experience of the participants. \n\n"
                                      "After you have made your choice, you will see whether it was right or wrong. \n\n"
                                      "You will be granted 10 points for every correct choice and 0 points for every incorrect choice.\n\n"
                                      "The experiments consists of 6 rounds. \n"
                                      "To win the gold prize, get at least 50 points. \n"
                                      "To win the silver prize, get at least 40 points. \n\n"
                                      "If you have understood the instructions, press space to continue.",
                                       color = "black")

welcome_text_nonsocial_1 = psychopy.visual.TextStim(win, text = "Welcome to this experiment! \n\n"
                                              "This experiment aims to better understand how people \n"
                                              "use direct and indirect information to learn. \n\n"
                                              "In the following, you will be presented with two rectangles, a green one and a blue one. \n\n"
                                              "You choose between the two rectangles by pressing the 'k' for right \n"
                                              "and 'd' for left on the keyboard. \n\n"
                                              "To help you decide, one of the rectangles will be highlighted by a red border. \n\n"
                                              "This choice is made by a rigged roulette wheel,  \n"
                                              "which means that this information can be pretty useful or less useful. \n\n"
                                              "After you have made your choice, you will see whether it was right or wrong.  \n\n"
                                              "You will be granted 10 points for every correct choice \n"
                                              "and 0 points for every incorrect choice.\n\n"
                                              "The experiments consists of 6 rounds.\n"
                                              "To win the gold prize, get at least 50 points.\n"
                                              "If you have understood the instructions, press space to continue.",
                                               color = "black")

welcome_text_nonsocial_2 = psychopy.visual.TextStim(win, text = "Welcome to this experiment! \n\n"
                                              "This experiment aims to better understand how people \n"
                                              "use direct and indirect information to learn. \n\n"
                                              "In the following, you will be presented with two triangles, an orange one and a purple one. \n\n"
                                              "You choose between the two triangles by pressing the 'k' for right \n"
                                              "and 'd' for left on the keyboard. \n\n"
                                              "To help you decide, one of the triangles will be highlighted. by a green border \n\n"
                                              "This choice is made by a rigged roulette wheel,  \n"
                                              "which means that this information can be pretty useful or less useful. \n\n"
                                              "After you have made your choice, you will see whether it was right or wrong. \n\n"
                                              "You will be granted 10 points for every correct choice \n"
                                              "and 0 points for every incorrect choice. \n\n"
                                              "The experiments consists of 6 rounds. \n"
                                              "To win the gold prize, get at least 50 points. \n"
                                              "If you have understood the instructions, press space to continue.",
                                               color = "black")

# randomization of groups
groups = ["social_1", "social_2", "nonsocial_1", "nonsocial_2"]
randomization = random.choice(groups)
if randomization == "social_1":
    welcome_text_social_1.draw()
    win.flip()
    event.waitKeys(keyList = ['space'])
elif randomization == "social_2":
    welcome_text_social_2.draw()
    win.flip()
    event.waitKeys(keyList = ['space'])
elif randomization == "nonsocial_1":
    welcome_text_nonsocial_1.draw()
    win.flip()
    event.waitKeys(keyList = ['space'])
else:
    welcome_text_nonsocial_2.draw()
    win.flip()
    event.waitKeys(keyList = ['space'])

print("condition: ", randomization)
data_out.write( '\t'.join([str(randomization)]) + '\n' )

instruction = psychopy.visual.TextStim(win,
                text = "Please press 'd' for left and 'k' for right.",  
                color = "black", 
                height = 25)
instruction.pos = [0, -160]

# trial run
print("the trial has started.")
trial_instruction = psychopy.visual.TextStim(win, text = "Before the experiment starts, you get a chance to practice. \n\n"
                                "This practice rounds consist of 3 trials, where you press 'd' for the left stimulus and 'k' for the right stimulus. \n\n"
                                "If you have understood the instruction, please press 'space' to continue to start the trial rounds.",
                                color = "black")
trial_instruction.draw()
win.flip()
event.waitKeys(keyList = ['space'])

# trial feedback
trial_correct = psychopy.visual.TextStim(win, text = "correct!", color = "black", height = 30)
trial_incorrect = psychopy.visual.TextStim(win, text = "incorrect!", color = "black", height = 30)

# trial stimuli presentation
if randomization == "social_1" or randomization == "nonsocial_1":
    blue_rect.draw()
    green_red_rect.draw()
    instruction.draw()
    win.flip()
    choice = event.waitKeys(keyList = ['d', 'k'])
    if 'k' in choice:
        trial_correct.draw()
        win.flip()
        wait(2)
    else:
        trial_incorrect.draw()
        win.flip()
        wait(2)
    blue_red_rect.draw()
    green_rect.draw()
    instruction.draw()
    win.flip()
    choice = event.waitKeys(keyList = ['d', 'k'])
    if 'k' in choice:
        trial_correct.draw()
        win.flip()
        wait(2)
    else:
        trial_incorrect.draw()
        win.flip()
        wait(2)
    blue_red_rect.draw()
    green_rect.draw()
    instruction.draw()
    win.flip()
    choice = event.waitKeys(keyList = ['d', 'k'])
    if 'k' in choice:
        trial_incorrect.draw()
        win.flip()
        wait(2)
    else:
        trial_correct.draw()
        win.flip()
        wait(2)
else:
    orange_tri.draw()
    purple_green_tri.draw()
    instruction.draw()
    win.flip()
    choice = event.waitKeys(keyList = ['d', 'k'])
    if 'k' in choice:
        trial_correct.draw()
        win.flip()
        wait(2)
    else:
        trial_incorrect.draw()
        win.flip()
        wait(2)
    orange_green_tri.draw()
    purple_tri.draw()
    instruction.draw()
    win.flip()
    choice = event.waitKeys(keyList = ['d', 'k'])
    if 'k' in choice:
        trial_correct.draw()
        win.flip()
        wait(2)
    else:
        trial_incorrect.draw()
        win.flip()
        wait(2)
    orange_green_tri.draw()
    purple_tri.draw()
    instruction.draw()
    win.flip()
    choice = event.waitKeys(keyList = ['d', 'k'])
    if 'k' in choice:
        trial_incorrect.draw()
        win.flip()
        wait(2)
    else:
        trial_correct.draw()
        win.flip()
        wait(2)

end_trial = psychopy.visual.TextStim(win, text = "This concludes the trial rounds. By pressing 'space' you continue to the real experiment.", color = "black", height = 25)
end_trial.draw()
win.flip()
event.waitKeys(keyList = ['space'])
print("the trial has ended.")

# experiment
print("the experiment has started.")
score = 0
trials = 0
timer = Clock()

start_experiment =psychopy.visual.TextStim(win, text = "The experiment starts in 3 seconds.", color = "black", height = 25)
start_experiment.draw()
win.flip()
wait(3)

while trials <= 5:
    # randomization of stimuli
    stimuli= ["1", "2"]
    stimulus = random.choice(stimuli)
    if randomization == "social_1" and stimulus == "1" or  randomization == "nonsocial_1" and stimulus == "1":
        blue_rect.draw()
        green_red_rect.draw()
        instruction.draw()
        win.flip()
        print("stimuli: blue_rect + green_red_rect.")
        # participants make their choice
        choice = event.waitKeys(keyList = ['d', 'k'], timeStamped = timer)
        print("choice and response time: ", choice)
        timer.reset()
    elif randomization == "social_1" and stimulus == "2" or randomization == "nonsocial_1" and stimulus == "2":
        blue_red_rect.draw()
        green_rect.draw()
        instruction.draw()
        win.flip()
        print("stimuli: blue_red_rect + green_rect.")
        # participants make their choice
        choice = event.waitKeys(keyList = ['d', 'k'], timeStamped = timer)
        print("choice and response time: ", choice)
        timer.reset()
    elif randomization == "social_2" and stimulus == "1" or randomization == "nonsocial_2" and stimulus == "1": 
        orange_tri.draw()
        purple_green_tri.draw()
        instruction.draw()
        win.flip()
        print("stimuli: orange_tri + purple_green_tri.")
        # participants make their choice
        choice = event.waitKeys(keyList = ['d', 'k'], timeStamped = timer)
        print("choice and response time: ", choice)
        timer.reset()
    else:
        orange_green_tri.draw()
        purple_tri.draw()
        instruction.draw()
        win.flip()
        print("stimuli: orange_green_triangle + purple_tri.")
        # participants make their choice
        choice = event.waitKeys(keyList = ['d', 'k'], timeStamped = timer)
        print("choice and response time: ", choice)
        timer.reset()

    # feedback is given
    feedback = ["correct!", "incorrect!"]
    random_feedback =  psychopy.visual.TextStim(win,
                                        text = random.choice(feedback),
                                        color = "black",
                                        height = 30)                            
    random_feedback.draw()
    win.flip()
    wait(2)
        
    # score is stored and feedback is printed
    if random_feedback.text == "correct!":
        score += 10
        print("feedback: correct")
        print("score: ", score)
    else:
        score += 0
        print("feedback: incorrect")        
        print("score: ", score)

    trials += 1
    print("trial: ", trials)

    data_out.write( '\t'.join([str(trials), str(stimulus), str(choice), str(random_feedback.text)]) + '\n' )

# overall feedback is given
print("overall feedback is given.")

if score >= 50:
      gold_prize = psychopy.visual.TextStim(win,
                            text = "Congratulations! You win the gold prize!", 
                            color = "black", 
                            height = 30)
      gold_prize.draw()
      win.flip()
      wait(3)
elif score == 40:
        silver_prize = psychopy.visual.TextStim(win,
                                text = "Congratulations! You win the silver prize!", 
                                color = "black",
                                height = 30)
        silver_prize.draw()
        win.flip()
        wait(3)
else:
        no_prize = psychopy.visual.TextStim(win,
                            text = "You win no prize.",
                            color = "black",
                            height = 30)
        no_prize.draw()
        win.flip()
        wait(3)

#end
end_screen = psychopy.visual.TextStim(win,
                        text = "Thank you for participating in this experiment! ",
                        color = "black",
                        height = 30)
end_screen.draw()
win.flip()
wait(5)
print("experiment has ended.")

win.close()
core.quit()
