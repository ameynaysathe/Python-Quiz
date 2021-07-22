def give_options(x,y,z):
    print("a):", x)
    print("b):", y)
    print("c):", z)

print("Hello! Welcome to my Python Quiz" "\n" "Note: These are the basic questions of python" "\n" "All Questions carries 10 marks each")
ans = input("Are you ready to play (yes/no): ")
score = 0
total_questions = 5

correct_ans =["#this is a comment", "my-var", "int = int(5)", ".py","print(type(x))"]

if ans.lower() == "yes":

    print("Question- How do you insert COMMENTS in Python code? ")
    give_options("//this is a comment", "#this is a comment", "//this is a comment//" )
    ans=input("Answer: ")
    if ans.lower() == correct_ans[0]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")

    print("Question- Which one is NOT a legal variable name? ")
    give_options("my_var", "my-var", "myvar")
    ans = input("Answer: ")
    if ans.lower() == correct_ans[1]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")

    print("Question- How do you create a variable with the numeric value 5? ")
    give_options("int = str(5.0)", "int = char(5)", "int = int(5)")
    ans = input("Answer: ")
    if ans.lower() == correct_ans[2]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")

    print("Question- What is the correct file extension for Python files? ")
    give_options(".py", ".pyth", "pyth")
    ans = input("Answer: ")
    if ans.lower() == correct_ans[3]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")

    print("Question- What is the correct syntax to output the type of a variable or object in Python? ")
    give_options("print(typeof(x))", "print(type(x))", "print(x.type)")
    ans = input("Answer: ")
    if ans.lower() == correct_ans[4]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")

i = score*10
if i <= 20:
    print("oops, your score is ",i,"/ 50 better luck next time.")
elif i == 30:
    print("wow! you scored ",i,"/ 50 you are quiet smart.")
elif i == 40:
    print("Wow! you scored",i,"/50 you are Awesome")
else:
    print("Congratulations! it's a perfect ",i,"/ 50 you are Intelligent.")