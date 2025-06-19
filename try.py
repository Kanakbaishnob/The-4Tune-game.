import random
list1 = ["You will get married soon.",
         "WOW! You working hard.Keep going.",
         "You Know, You are the most beautiful person.",
         "What do you prefer Tea or Coffee.",
         "Today is your lucky day!",
         "Books will be your best friend today.",
         "You're about to hit your goals!",
         "A surprise is coming your way!"
          ]
name=input("Enter Your Name: ")
age =int(input("Enter your age: "))

Ask1= input("Excited! Are Yor Ready for play (Yes\ No): ")
if Ask1.strip().lower() == "no":
    print("Thanks For joining.")

else:
    print(f"Wellcome {name}.Lets start.")
    for x in range(4):
        pick=input("Pick Any number (1, 2, 3, 4): ")

        if pick in ["1","2","3","4"]:
            ran_word=random.choice(list1)
            print(ran_word)
        else:
            print("Sorry! You are picking outside of the Four Option.")
    print("Thank For Playing. See You soon")


