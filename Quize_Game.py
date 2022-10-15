
print("welcome to quiz Game");
print("\n");

choice=input("do you want to play quize?" );

if choice.lower()!="yes":
    quit();

score=0;
que1=input("Full form of CPU ");
if que1.lower()=="central processing unit":
    score+=1;
    print("Your answer is correct.!");
else :
    print("Oops ypur answer is wrong.");
    
que2=input("Full form of OOP ");
if que2.lower()=="object oriented programming":
    score+=1;
    print("Your answer is correct.!");
else :
    print("Oops ypur answer is wrong.");
    
que3=input("Full form of DS ");
if que3.lower()=="data structure":
    score+=1;
    print("Your answer is correct.!");
else :
    print("Oops ypur answer is wrong.");
    
que4=input("Full form of OS ");
if que4.lower()=="operating system":
    score+=1;
    print("Your answer is correct.!");
else :
    print("Oops ypur answer is wrong.");
    
que5=input("Full form of CN ");
if que5.lower()=="computer networks":
    score+=1;
    print("Your answer is correct.!");
else :
    print("Oops ypur answer is wrong.");
    
print("You got ",score," out of 5");