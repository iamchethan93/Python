# Create a program to stimulate KBC question and answers. As the user answers 
# we need to identify if the question is right or wrong and then update the winnings accordingly.

#Logic
# question is asked and user answer needs to be validated. Create a dict with question and answers. 

#If the user answers correctly add 5k amount to winnings variable. iterate via loop and when answer does not match exit and display the winings.


questions_answers = {
    "Who was the 1st PM of India" : "JN",
    "Father of the nation" : "MG",
    "Best batsman ever" : "VK",
    "Name of your pet" : "Peddu"
}


def kbc_game():
    winnings = 0
    for key,value in questions_answers.items():
        print(key)
        answer = input("Enter your answer:")
        if answer != value:
            print(f"Unfortunately the answer is wrong. Your game ends here")
            break
        else:
            winnings= winnings+5000
    print(f"Your total winnings is {winnings}")

kbc_game()