import pandas

state_name = input("Enter the state name: ").title()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

if state_name in states_list:
    print("Yes")
else:
    print("no")
