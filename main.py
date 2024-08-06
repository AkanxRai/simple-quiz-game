import quiz

print("Welcome to my quiz game!")

playing = input("Do you want to play my 'How much you know Akanksh' Quiz?\n").lower()
if playing != "yes":
    print("Oh... Hope to see you again 😢")
    exit(0)

print("Great! Let's get on with the quiz then...")
name = input("First, type your beautiful name: ")
print(f"I gladly welcome you, {name}")
print("""Here are some things you need to know...
      - There will be 5 questions. 
      - Enter your answer by typing the option number (e.g., type 1 and press enter).
      - Each question will have different points. 
      - In the end, a rating out of 10 will be given.
Let's see how much you know of me 😁""")
input("Press enter after you have read the instructions.")
q1_ans = int(input("""Would they ever be open to a long-distance relationship?
      1) Yes
      2) No
Enter the number of your choice: """))

q2_ans = int(input("""What is their favorite sex position?
      1) Doggy style
      2) Missionary
      3) Tit suck and fuck
      4) Cow girl
Enter the number of your choice: """))

q3_ans = int(input("""How do they like to be apologized to? (Most preferable)
      1) Gifts
      2) Physical apology (hugs, hold hands, etc.)
      3) BJ
      4) Food
Enter the number of your choice: """))

q4_ans = int(input("""How do they like to receive love? (Most preferable)
      1) Gifts
      2) Physical
      3) Verbal
      4) Text Messaging
Enter the number of your choice: """))

q5_ans = int(input("""What is their principle?
      1) Never break your word.
      2) Never borrow money.
      3) Help and be kind.
      4) Be self-sufficient
Enter the number of your choice: """))

print("Thank you for completing the quiz!")

rating = quiz.run_quiz(q1_ans, q2_ans, q3_ans, q4_ans, q5_ans)

print("Your Final rating is:", rating)
if rating > 8:
    print(f"Damn {name}! You know me well.")
elif rating > 5:
    print(f"I guess you understand me a little, {name}.")
else:
    print(f"It is very sad that you don't understand me at all, {name}.")
print("See you soon... Bye!")
