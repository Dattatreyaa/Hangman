import random
print("Lets play a game of hangman")
while():
    print("Select your Category")
    print("1-Colours (Easy)")
    print("2-Animals (Medium)")
    print("3-Cities (Hard)")
    c=int(input("Enter Your Choice: "))

    if c==1:
        word_list=("red","blue","violet","brown","white","black","yellow","green")
        word=random.choice(word_list)
        print("Category is Colours")
        x=len(word)
        print("The word is",x ,"letters long")
        word_guess=("")
        attempts=7
        while attempts>0:
            letter_guess=input("Enter a letter :")
            if letter_guess not in ("a b c d e f g h i j k l m n o p q r s t u w v x y z "):
                print("Please type an/1 alphabet")
                continue
            if letter_guess in word:
                print("Correct")
                if letter_guess in word_guess:
                    print("Letter already entered")
                    continue
                if len(word_guess)+1==len(word) :
                    print("Congrats you got the colour :",word)
                    break
                for a in range (len(word)):
                    if letter_guess==word[a]:
                        if a+1==1:
                            print(letter_guess, "is the " ,a+1,"st letter")
                            word_guess+=letter_guess
                        elif a+1==2:
                            print(letter_guess, "is the " ,a+1,"nd letter")
                            word_guess+=letter_guess
                        elif a+1==3:
                            print(letter_guess, "is the " ,a+1,"rd letter")
                            word_guess+=letter_guess
                        elif a+1>3:
                            print(letter_guess, "is the " ,a+1,"th letter")
                            word_guess+=letter_guess
            else:
                print("Wrong")
                attempts-=1
                if attempts==6:
                    print(" ______  ")
                    print("|     |  ")
                    print("|        ")
                    print("|        ")
                    print("|        ")
            
                elif attempts==5:
                    print(" ______  ")
                    print("|     |  ")
                    print("|     |  ")
                    print("|        ")
                    print("|        ")

                elif attempts==4:
                    print(" ______  ")
                    print("|     |  ")
                    print("|    /|  ")
                    print("|        ")
                    print("|        ")

                elif attempts==3:
                    print(" ______  ")
                    print("|     |  ")
                    print("|    /|\ ")
                    print("|        ")
                    print("|        ")

                elif attempts==2:
                    print(" ______  ")
                    print("|     |  ")
                    print("|    /|\ ")
                    print("|     |  ")
                    print("|        ")
                    
                elif attempts==1:
                    print(" ______  ")
                    print("|     |  ")
                    print("|    /|\ ")
                    print("|     |  ")
                    print("|    /   ")

                elif attempts==0:
                    print(" ______  ")
                    print("|     |  ")
                    print("|    /|\ ")
                    print("|     |  ")
                    print("|    /|\ ")
                    print("Game over, the colour was :",word)

    if c==2:
        word_list=("dinosaur","camel", "tiger", "leopard", "jaguar", "panther", "lizard" )
        word=random.choice(word_list)
        print("Category is Animals")
        x=len(word)
        print("The word is",x ,"letters long")
        word_guess=("")
        attempts=7
        while attempts>0:
            letter_guess=input("Enter a letter :")
            if letter_guess not in ("a b c d e f g h i j k l m n o p q r s t u w v x y z "):
                print("Please type an/1 alphabet")
                continue
            if letter_guess in word:
                print("Correct")
                if letter_guess in word_guess:
                    print("Letter already entered")
                    continue
                if len(word_guess)+1==len(word) :
                    print("Congrats you got the animal :",word)
                    break
                for a in range (len(word)):
                    if letter_guess==word[a]:
                        if a+1==1:
                            print(letter_guess, "is the " ,a+1,"st letter")
                            word_guess+=letter_guess
                        elif a+1==2:
                            print(letter_guess, "is the " ,a+1,"nd letter")
                            word_guess+=letter_guess
                        elif a+1==3:
                            print(letter_guess, "is the " ,a+1,"rd letter")
                            word_guess+=letter_guess
                        elif a+1>3:
                            print(letter_guess, "is the " ,a+1,"th letter")
                            word_guess+=letter_guess
            else:
                print("Wrong")
                attempts-=1
                if attempts==6:
                    print(" ______  ")
                    print("|     |  ")
                    print("|        ")
                    print("|        ")
                    print("|        ")
            
                elif attempts==5:
                    print(" ______  ")
                    print("|     |  ")
                    print("|     |  ")
                    print("|        ")
                    print("|        ")

                elif attempts==4:
                    print(" ______  ")
                    print("|     |  ")
                    print("|    /|  ")
                    print("|        ")
                    print("|        ")

                elif attempts==3:
                    print(" ______  ")
                    print("|     |  ")
                    print("|    /|\ ")
                    print("|        ")
                    print("|        ")

                elif attempts==2:
                    print(" ______  ")
                    print("|     |  ")
                    print("|    /|\ ")
                    print("|     |  ")
                    print("|        ")
                    
                elif attempts==1:
                    print(" ______  ")
                    print("|     |  ")
                    print("|    /|\ ")
                    print("|     |  ")
                    print("|    /   ")

                elif attempts==0:
                    print(" ______  ")
                    print("|     |  ")
                    print("|    /|\ ")
                    print("|     |  ")
                    print("|    /|\ ")
                    print("Game over, the animal was :",word)

    if c==3:
        word_list=("dubai","delhi","seoul","chennai","london","doha","istanbul","chicago")
        word=random.choice(word_list)
        print("Category is Cities")
        x=len(word)
        print("The word is",x ,"letters long")
        word_guess=("")
        attempts=7
        while attempts>0:
            letter_guess=input("Enter a letter :")
            if letter_guess not in ("a b c d e f g h i j k l m n o p q r s t u v w x y z "):
                print("Please type an/1 alphabet")
                continue
            if letter_guess in word:
                print("Correct")
                if letter_guess in word_guess:
                    print("Letter already entered")
                    continue
                if len(word_guess)+1==len(word) :
                    print("Congrats you got the city :",word)
                    break
                for a in range (len(word)):
                    if letter_guess==word[a]:
                        if a+1==1:
                            print(letter_guess, "is the " ,a+1,"st letter")
                            word_guess+=letter_guess
                        elif a+1==2:
                            print(letter_guess, "is the " ,a+1,"nd letter")
                            word_guess+=letter_guess
                        elif a+1==3:
                            print(letter_guess, "is the " ,a+1,"rd letter")
                            word_guess+=letter_guess
                        elif a+1>3:
                            print(letter_guess, "is the " ,a+1,"th letter")
                            word_guess+=letter_guess
            else:
                print("Wrong")
                attempts-=1
                if attempts==6:
                    print(" ______  ")
                    print("|     |  ")
                    print("|        ")
                    print("|        ")
                    print("|        ")
            
                elif attempts==5:
                    print(" ______  ")
                    print("|     |  ")
                    print("|     |  ")
                    print("|        ")
                    print("|        ")

                elif attempts==4:
                    print(" ______  ")
                    print("|     |  ")
                    print("|    /|  ")
                    print("|        ")
                    print("|        ")

                elif attempts==3:
                    print(" ______  ")
                    print("|     |  ")
                    print("|    /|\ ")
                    print("|        ")
                    print("|        ")

                elif attempts==2:
                    print(" ______  ")
                    print("|     |  ")
                    print("|    /|\ ")
                    print("|     |  ")
                    print("|        ")
                    
                elif attempts==1:
                    print(" ______  ")
                    print("|     |  ")
                    print("|    /|\ ")
                    print("|     |  ")
                    print("|    /   ")

                elif attempts==0:
                    print(" ______  ")
                    print("|     |  ")
                    print("|    /|\ ")
                    print("|     |  ")
                    print("|    /|\ ")
                    print("Game over, the city was :",word)
    end=input("Do you want to play again Y/N: ")
    if (end=="n" or end=="N"):
        break




