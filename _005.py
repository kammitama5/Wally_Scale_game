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
	raw_input("Welcome to Wally the scale.\n" 
	      "You can weigh things with me.\n");
	      
	print("I'm Bilingual. Should I speak in kg or pounds?");
	choice = raw_input("Pick 1 for kg or 2 for lbs");
	
	# if entered 1, choice = choice otherwise choice = 2.2 * choice
	choice1 = float(choice);
	if (choice == "1"):
		choice1;
		raw_input("You chose kg => pounds");
	elif (choice == "2"):
		 (choice1 * 2.2)
		 raw_input("You choise lbs => pounds");
	else:
		choice = raw_input("This is not an option. Please try again");
	

	weighobject = raw_input("Please select an object to weigh from choices: "
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

