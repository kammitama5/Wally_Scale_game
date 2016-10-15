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
	                        "1)Cat\n"
	                        "2)Bear\n"
	                        "3)Truck\n"
	                        "4)Trinidad\n"
	                        "5)White House\n"
	                        "6)Sequoia Tree\n"
	                        "7)Toilet Paper\n"
	                        "8) Bag of Flour\n"
	                        "9)Space Shuttle\n"
	                        "10)Box of Cue Tips\n");
	 
		                    
	while not ((selection == "1") or (selection == "2") or (selection == "3")
		or (selection == "4") or (selection == "5") or (selection == "6") or 
		(selection == "7") or (selection == "8") or (selection == "9") or (selection == "10")):
			
		selection1 = float(selection);
	   
	 	if (selection == "1"):
	 		selection1
	 		print("hi");
	 	if (selection == "2"):
	 		selection1
	 		print("hi 3");
	 	if (selection == "4"):
	 		selection1
	 		print("hi c");
	 	if (selection == "5"):
	 		selection1
	 		print("hi d");
	 
	
	 			
	 	
	 
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
