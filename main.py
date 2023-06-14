
print("Welcome To My First Game")
name = input("What is Your Name ")
age = int(input("What is your Age "))

health = 10

if age >= 18 :
  print("You are Old enough to Play!")
  
  wants_to_play = input("Do you Want to Play ? ").lower()
  if wants_to_play == "yes" :
    print("you are Staring with",health, "Health")
    print("Lets Play")
    
    left_or_right = input("First Choice... (left/right)? ")
    if left_or_right == 'left' :
      ans = input("Nice... You Follow the Path and Reach a Lake... Do You Swim Across or go around (across/around)? ")
      
      if ans == "around" :
        print("You went around Reached Other Side of Lake")
      elif ans == 'across' :
        print("You managed to get across, but were bit by a fish and lost 5 Health.")
        health -= 5
      
      ans = input("You notice a house and a river, Which do You go to (house/river) ?") 
      if ans == 'house':
        print("You Go to the house and greated By owner...He doesn't like You and you lost 5 health")
        
        if health <= 0 :
          print("You now have Have 0 health and you lost the Game...")
        else :
          print("You have Survived...You Win.")
      else :
        print("You fell in the river and Lost..") 
     
    else :
      print("You fell down And Lost...")
  else :
    print("Cya.....")  
else :
  print("You are Not Old Enough!!!")