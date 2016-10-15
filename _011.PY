# build a game where if something is on a scale, calculate how much weight
# kg vs pounds

# Prints Welcome to Wally the scale. 
# You can weigh things with me. 
# Would you like to work in kg or pounds. Choose option
# Bilingual..which want me to speak (implement library
# Please select an object to weigh from choices
# a b c d e f g  
# Tells you what you chose

def Menu():
	print("Welcome to Wally the scale.\n" 
	      "You can weigh things with me.\n");
	from time import sleep
	sleep(1.0);
	      
	print("I'm Bilingual. Should I speak in kg or pounds?");
	choice = raw_input("Pick 1 for kg or 2 for lbs :");
	
	# if entered 1, choice = choice otherwise choice = 2.2 * choice
	while not ((choice == "1") or (choice == "2")):
		choice = raw_input("This is not an option. Please try again\n");
		choice1 = float(choice);
		if (choice == "1"):
				choice1
				print("You chose kg => kilograms\n");
				sleep(1.0);
		else:
		 		(choice1 * 2.2)
		 		print("You choise lbs => pounds\n");
		 		sleep(1.0);
		 		
	#choice1 is float version of kg or pounds
		 		
	# Menu for objects to be chosen
	selection = raw_input("Please select an object to weigh from choices: "
		                    "a through j\n"
	                        "a)Cat\n"
	                        "b)Bear\n"
	                        "c)Truck\n"
	                        "d)Trinidad\n"
	                        "e)White House\n"
	                        "f)Sequoia Tree\n"
	                        "g)Toilet Paper\n"
	                        "h) Bag of Flour\n"
	                        "i)Space Shuttle\n"
	                        "j)Box of Cue Tips\n");
	 
		                    
	while not ((selection == "a") or (selection == "b") or (selection == "c")
		or (selection == "d") or (selection == "e") or (selection == "f") or 
		(selection == "g") or (selection == "h") or (selection == "i") or (selection == "j")):
			
	   
	 	if (selection == "a"):
	 		print("hi");
	 	elif (selection == "b"):
	 		print("hi 3");
	 	elif (selection == "c"):
	 		print("hi c");
	 	elif (selection == "d"):
	 		print("hi d");
	 	elif (selection == "e"):
	 		print("hi e");
	 	elif (selection == "f"):
	 		print("hi f");
	 	elif (selection == "g"):
	 		print("hi g");
	 	elif (selection == "h"):
	 		print("hi h");
	 	elif (selection == "i"):
	 		print("hi i");
	 	elif (selection == "j"):
	 		print("hi j");
	 	else:
	 		print("you picked an objec that doesn't exist");
	 	
	 			
	 	
	 
	
	 			
	 	
	 
	 #weightobject = 
	 #Cat => 4.5 kg
	 #Bear => 272 kg
	 #Truck => 2000 kg
	 #Trinidad => 5.8 x 10^9 kg
	 #White House => 10 866 217 kg
	 #Sequoia Tree => 1 200 000 kg
	 #Toilet Paper => .227 kg
	 #Bag of Flour => 1.5 kg
	 #Space Shuttle => 28945 kg
	 #Box of Cue Tips => 1 kg
	
Menu();
