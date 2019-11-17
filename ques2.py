chicken = int(input(" Enter the no of chicken in your form "))
cow = int(input(" Enter the no of cow in your form "))
pig = int(input(" Enter the no of pig in your form "))
legs_of_chicken = chicken *2
legs_of_cow = cow *4
legs_of_pig = pig *4
total_animals = chicken + pig + cow
total_legs = legs_of_chicken + legs_of_pig + legs_of_cow
print(" You have total" , total_animals ,"animals in your farm,")
print(" So according to it,")
print(" The total animals legs are ", total_legs)
