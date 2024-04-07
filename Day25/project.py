from turtle import Screen,Turtle
import turtle 
import pandas as pd

t = Turtle()
screen = Screen()
screen.title('US STATE GAME')
image = 'blank_states_img.gif'
screen.addshape(image)
t.shape(image)

state_data = pd.read_csv('50_states.csv')
state_list = state_data['state'].to_list()
guessed_state = []
left_state =[]
while len(guessed_state)<50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess the State",prompt="What's the another state name? =").title()
    if answer_state == 'Exit':
        missing_list = [state for state in state_list if (state not in guessed_state)]
        # for state in state_list:
        #     if state not in guessed_state:
        #         left_state.append(state)
        # print(left_state)
        new_data = pd.DataFrame(missing_list)
        new_data.to_csv('states_to_learn2.csv')
        break
    if answer_state in state_list:
        t = Turtle()
        guessed_state.append(answer_state)
        t.hideturtle()
        t.penup()
        state = state_data[state_data['state']==answer_state]
        t.goto(int(state['x'].iloc[0]),int(state['y'].iloc[0]))
        t.write(answer_state)


#mistakes I did here 
#could not think how to add mssing states into left state although little bit dimag chala but still couldn't reach to destination
#could not think how to find a user answer in state list 

#things I learnt today 
#write a comment that thing you want to do and then move forward 


        

