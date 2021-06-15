import random
import psychopy.visual
from psychopy.core import wait
from psychopy import core, event
event.globalKeys.add(key='q', modifiers=['ctrl'], func=core.quit)

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


welcome_text_social = psychopy.visual.TextStim(win, text = "Welcome to this experiment! \n"
                                      "This experiment aims to better understand how people use direct and indirect information to learn \n"
                                      "In the following, you will be presented with two rectangles, a green one and a blue one. \n"
                                      "You choose between the two rectangles by pressing the 'left' or 'right' keys on the keyboard.  \n"
                                      "After you have made your choice, you will see whether it was right or wrong.  \n"
                                      "You will be granted 10 points for every correct choice and 0 points for every incorrect choice.\n"
                                      "There will also appear a red border around either of the rectangles.\n"
                                      "This border indicates the choices previous participants have made.  \n"
                                      "This information can be pretty useful or less useful, depending on the experience of the participants. \n"
                                      "The experiments consists of 6 rounds.\n"
                                      "To win the gold prize, get at least 50 points.\n"
                                      "To win the silver prize, get at least 40 points.\n"
                                      "If you have understood the instructions, press any key to continue.",
                                      color = "black")

welcome_text_nonsocial = psychopy.visual.TextStim(win, text = "Welcome to this experiment! \n"
                                              "This experiment aims to better understand how people \n"
                                              "use direct and indirect information to learn. \n"
                                              "In the following, you will be presented with two rectangles, a green one and a blue one. \n"
                                              "You choose between the two rectangles by pressing the 'k' for right\n"
                                              "and 'd' for left on the keyboard. \n"
                                              "To help you decide, one of the rectangles will be highlighted. \n"
                                              "This choice is made by a rigged roulette wheel,  \n"
                                              "which means that this information can be pretty useful or less useful. \n"
                                              "After you have made your choice, you will see whether it was right or wrong.  \n"
                                              "You will be granted 10 points for every correct choice \n"
                                              "and 0 points for every incorrect choice.\n"
                                              "The experiments consists of 6 rounds.\n"
                                              "To win the gold prize, get at least 50 points.\n"
                                              "If you have understood the instructions, press any key to continue.",
                                              color = "black")
# randomization of groups
groups = ["social", "nonsocial"]
randomization = random.choice(groups)
if randomization == "social":
    welcome_text_social.draw()
    win.flip()
    event.waitKeys()
else:
    welcome_text_social.draw()
    win.flip()
    event.waitKeys()

sum_choices = []
sum_feedback = []
score = []
trials = 0

choice = psychopy.visual.TextStim(win, text = "Please press 'd' for the left rectangle and 'k' for the right rectangle", color = "black", height = 25)
choice.pos = [0, -160]

while trials <= 5:
    # randomization of stimuli
    stimuli= ["1", "2"]
    stimulus = random.choice(stimuli)
    if stimulus == "1":
        blue_rect.draw()
        green_red_rect.draw()
        # participants make their choice
        choice.draw()
        win.flip()
        event.waitKeys()
        wait(5)
    else:
        blue_red_rect.draw()
        green_rect.draw()
        # participants make their choice
        choice.draw()
        win.flip()
        event.waitKeys()
        win.flip()
        wait(5)

    if choice == "k" or "d":
        #feedback is given
        feedback = ["correct!", "incorrect!"]
        random_feedback =  psychopy.visual.TextStim(win, text = random.choice(feedback), color = "black", height = 30)
        random_feedback.draw()
        win.flip()
        wait(2)
        
        # answers are stored
        if choice == "k":
            sum_choices.append("k")
        else:
            sum_choices.append("d")
        
        # score and feedback is stored
        if random_feedback == "correct!":
            score.append(10)
            sum_feedback.append("correct!")
        else:
            score.append(0)
            sum_feedback.append("incorrect!")

        trials += 1
        sum_score = sum(score)

    else:
        not_valid = psychopy.visual.TextStim(window, text = "The input is not valid. Please enter 'k' or 'd'.", color = "black")
        not_valid.draw()

# participant feedback is given

if sum_score >= 50:
      gold_prize = psychopy.visual.TextStim(win, text = "Congratulations! You win the gold prize!", color = "black", height = 30)
      gold_prize.draw()
      win.flip()
      wait(3)
elif sum_score == 40:
        silver_prize = psychopy.visual.TextStim(win, text = "Congratulations! You win the silver prize!", color = "black", height = 30)
        silver_prize.draw()
        win.flip()
        wait(3)
else:
        no_prize = psychopy.visual.TextStim(win, text = "You win no prize.", color = "black", height = 30)
        no_prize.draw()
        win.flip()
        wait(3)

#end
end_screen = psychopy.visual.TextStim(win, text = "Thank you for participating in this experiment! ", color = "black", height = 30)
end_screen.draw()
win.flip()
wait(5)

# win-stay lose-shift
win_stay = []
lose_shift = []
other = []

if sum_choices[0] == "k":
    if sum_feedback[0] == "correct!":
        if sum_choices[1] == "k":   # win-stay (k - correct - k)
            win_stay.append(1)
        else:
            other.append(1)    # neither win-stay nor lose-shift (k - correct - d)
    else:
        if sum_choices[1] == "k":
            other.append(1)    # neither win-stay nor lose-shift (k - incorrect - k)
        else:
            lose_shift.append(1)    # lose shift (k - incorrect - d)
else:
    if sum_feedback[0] == "correct!":
        if sum_choices[1] == "d":   # win-stay (d - correct - d)
            win_stay.append(1)
        else:
            other.append(1)    # neither win-stay nor lose-shift (d - correct - k)
    else:
        if sum_choices[1] == "d":
            other.append(1)    # neither win-stay nor lose-shift (d - incorrect - d)
        else:
            lose_shift.append(1)    # lose shift (d - incorrect - k)

if sum_choices[1] == "k":
    if sum_feedback[1] == "correct!":
        if sum_choices[2] == "k":   # win-stay (k - correct - k)
            win_stay.append(1)
        else:
            other.append(1)    # neither win-stay nor lose-shift (k - correct - d)
    else:
        if sum_choices[2] == "k":
            other.append(1)    # neither win-stay nor lose-shift (k - incorrect - k)
        else:
            lose_shift.append(1)    # lose shift (k - incorrect - d)
else:
    if sum_feedback[1] == "correct!":
        if sum_choices[2] == "d":   # win-stay (d - correct - d)
            win_stay.append(1)
        else:
            other.append(1)    # neither win-stay nor lose-shift (d - correct - k)
    else:
        if sum_choices[2] == "d":
            other.append(1)    # neither win-stay nor lose-shift (d - incorrect - d)
        else:
            lose_shift.append(1)    # lose shift (d - incorrect - k)

if sum_choices[2] == "k":
    if sum_feedback[2] == "correct!":
        if sum_choices[3] == "k":   # win-stay (k - correct - k)
            win_stay.append(1)
        else:
            other.append(1)    # neither win-stay nor lose-shift (k - correct - d)
    else:
        if sum_choices[3] == "k":
            other.append(1)    # neither win-stay nor lose-shift (k - incorrect - k)
        else:
            lose_shift.append(1)    # lose shift (k - incorrect - d)
else:
    if sum_feedback[2] == "correct!":
        if sum_choices[3] == "d":   # win-stay (d - correct - d)
            win_stay.append(1)
        else:
            other.append(1)    # neither win-stay nor lose-shift (d - correct - k)
    else:
        if sum_choices[3] == "d":
            other.append(1)    # neither win-stay nor lose-shift (d - incorrect - d)
        else:
            lose_shift.append(1)    # lose shift (d - incorrect - k)

if sum_choices[3] == "k":
    if sum_feedback[3] == "correct!":
        if sum_choices[4] == "k":   # win-stay (k - correct - k)
            win_stay.append(1)
        else:
            other.append(1)    # neither win-stay nor lose-shift (k - correct - d)
    else:
        if sum_choices[4] == "k":
            other.append(1)    # neither win-stay nor lose-shift (k - incorrect - k)
        else:
            lose_shift.append(1)    # lose shift (k - incorrect - d)
else:
    if sum_feedback[3] == "correct!":
        if sum_choices[4] == "d":   # win-stay (d - correct - d)
            win_stay.append(1)
        else:
            other.append(1)    # neither win-stay nor lose-shift (d - correct - k)
    else:
        if sum_choices[4] == "d":
            other.append(1)    # neither win-stay nor lose-shift (d - incorrect - d)
        else:
            lose_shift.append(1)    # lose shift (d - incorrect - k)

if sum_choices[4] == "k":
    if sum_feedback[4] == "correct!":
        if sum_choices[5] == "k":   # win-stay (k - correct - k)
            win_stay.append(1)
        else:
            other.append(1)    # neither win-stay nor lose-shift (k - correct - d)
    else:
        if sum_choices[5] == "k":
            other.append(1)    # neither win-stay nor lose-shift (k - incorrect - k)
        else:
            lose_shift.append(1)    # lose shift (k - incorrect - d)
else:
    if sum_feedback[4] == "correct!":
        if sum_choices[5] == "d":   # win-stay (d - correct - d)
            win_stay.append(1)
        else:
            other.append(1)    # neither win-stay nor lose-shift (d - correct - k)
    else:
        if sum_choices[5] == "d":
            other.append(1)    # neither win-stay nor lose-shift (d - incorrect - d)
        else:
            lose_shift.append(1)    # lose shift (d - incorrect - k)


# Output
print("The participant was in the ", randomization, " group.")
print("The participant has made the following choices: ", sum_choices)
print("This is the feedback the particpant has gotten: ", sum_feedback)
print("The participant showed win-stay behavior on ", sum(win_stay), " occasions.")
print("The participant showed lose-shift behavior on ", sum(lose_shift), " occasions.")
print("The participant showed neither win-stay or lose-shift behavior on ", sum(other), " occasions.")

win.close()
core.quit()

# creating file for experiment
data_out = open(f_name, 'a', encoding='utf-8')
data_out.write( '\t'.join( [ "subject_id", "condition", "trial_number", "stimulus_shown", "response_key", "rt_start", "correct", "win-stay", "lose-shift", "isi", "date_in_ms" ] ) + "\n" )
data_out.write( '\t'.join( [ subj_id, str(condition), str(trial_num+1), resp_key, str(rt_start), str(correct), str(win_stay), str(lose_shift), str(isi), str(strftime("%Y%m%d%H%M%S", gmtime())) ] ) + '\n' )

# GL:
# the level of complexity is quite okay, but probably could be more concisely/better written
# e.g. addition to list seems unnecessary for counting, could just be a single integer
# store each trial separately!
