import random

computer_score=0
user_score=0
options=["rock","paper","scissors"]
while(True):
    user_input=input("Choose between rock,paper,scissors\n")
    computer_choice=random.choice(options)
    user_input=user_input.lower()
    if user_input=="rock" and computer_choice=="paper":
        print(f"your choice:{user_input} computer_choice:{computer_choice}")
        print("computer win")
        computer_score+=1
        print(f'''score
              user:{user_score} computer:{computer_score}''')
    elif user_input=="rock" and computer_choice=="scissors":
        print(f"your choice:{user_input} computer_choice:{computer_choice}")
        print("user win")
        user_score+=1
        print(f'''score
              user:{user_score} computer:{computer_score}''')
    elif user_input=="rock" and computer_choice=="rock":
        print(f"your choice:{user_input} computer_choice:{computer_choice}")
        print("Draw")
        print(f'''score
              user:{user_score} computer:{computer_score}''')
    elif user_input=="paper" and computer_choice=="paper":
        print(f"your choice:{user_input} computer_choice:{computer_choice}")
        print("Draw")
        print(f'''score
              user:{user_score} computer:{computer_score}''')
    elif user_input=="paper" and computer_choice=="scissors":
        print(f"your choice:{user_input} computer_choice:{computer_choice}")
        print("computer win")
        computer_score+=1
        print(f'''score
              user:{user_score} computer:{computer_score}''')
    elif user_input=="paper" and computer_choice=="rock":
        print(f"your choice:{user_input} computer_choice:{computer_choice}")
        print("User win")
        user_score+=1
        print(f'''score
              user:{user_score} computer:{computer_score}''')
    elif user_input=="scissors" and computer_choice=="rock":
        print(f"your choice:{user_input} computer_choice:{computer_choice}")
        print("computer win")
        computer_score+=1
        print(f'''score
              user:{user_score} computer:{computer_score}''')
    elif user_input=="scissors" and computer_choice=="paper":
        print(f"your choice:{user_input} computer_choice:{computer_choice}")
        print("User win")
        user_score+=1
        print(f'''score
              user:{user_score} computer:{computer_score}''')
    elif user_input=="scissors" and computer_choice=="scissors":
        print(f"your choice:{user_input} computer_choice:{computer_choice}")
        print("Draw")
        print(f'''score
              user:{user_score} computer:{computer_score}''')
    