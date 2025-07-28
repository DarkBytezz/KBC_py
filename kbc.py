print("Welcome to Kon Banega CrorePati")
questions = ("1. What is the capital of India?", "2. Who is known as the Father of the Nation in India?", "3. How many continents are there in the world?", "4. Who invented the light bulb?", "5. Which planet is known as the Red Planet?")
answers = (("a) Mumbai\nb) Kolkata\nc) Delhi\nd) Chennai"),("a) Jawaharlal Nehru \nb) Subhash Chandra Bose \nc) B. R. Ambedkar\nd) Mahatma Gandhi"),("a) 5\nb) 6\nc) 7\nd) 8"),("a) Isaac Newton\nb) Thomas Edison\nc) Albert Einstein\nd) Nikola Tesla"),("a) Earth\nb) Jupiter\nc) Mars\nd) Venus"))
money = 100
flag = True
valid_choices = ('a', 'b', 'c', 'd')
for i in range(0, 5):
    print("Question", i+1, "for",money*10,"/- :", questions[i])
    print(answers[i], "\n")
    choice = input("Enter your choice: ")
    
    while True:
        if(choice == "exit"):break
        if choice in valid_choices:
            break
        else:
            print("Invalid choice, input again")
            choice = input("Enter your choice: ")

    
    
        
    if(i == 0):
        if(choice == "c"):
            print("SAHIIII JAWAAAB....\n")
            money*=10
        else:
            print("GALAT JAWAAB....")
            flag = False
            break
    elif(i == 1):
        if(choice == "d"):
            print("SAHIIII JAWAAAB....\n")
            money*=10
        else:
            print("GALAT JAWAAB....")
            flag = False
            break
    elif(i == 2):
        if(choice == "c"):
            print("SAHIIII JAWAAAB....\n")
            money*=10
        else:
            print("GALAT JAWAAB....")
            flag = False
            break
    elif(i == 3):
        if(choice == "b"):
            print("SAHIIII JAWAAAB....\n")
            money*=10
        else:
            print("GALAT JAWAAB....")
            flag = False
            break
    else:
        if(choice == "c"):
            print("SAHIIII JAWAAAB....\n")
            money*=10
        else:
            print("GALAT JAWAAB....")
            flag = False
            break
    
    
if(not flag):
    money = 0

print("You won the prize money of: ", money)
