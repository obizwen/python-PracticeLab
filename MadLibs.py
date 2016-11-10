'''
	This python lets users to input their own words,
  and make a funny (or strange) story.
'''

print "The Mad Libs has started"
ch_name = raw_input("Give a name for your character:")
print "We will need 3 adjective words"
adj1 = raw_input("Adjective 1:")
adj2 = raw_input("Adjective 2:")
adj3 = raw_input("Adjective 3:")

print "We will also need 3 verbs"
verb1 = raw_input("Verb 1:")
verb2 = raw_input("Verb 2:")
verb3 = raw_input("Verb 3:")

print "We will also need 4 nouns"
noun1 = raw_input("Noun 1:")
noun2 = raw_input("Noun 2:")
noun3 = raw_input("Noun 3:")
noun4 = raw_input("Noun 4:")

print "Now, please give me some others"
animal = raw_input("an animal")
food = raw_input("a food")
fruit = raw_input("a fruit")
number = raw_input("a number")
superhero = raw_input("a superhero name")
country = raw_input("a country")
dessert = raw_input("a dessert")
year = raw_input("a year")

#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print STORY % (adj1, ch_name, verb1, adj2, noun1, noun2, animal, food, verb2, noun3, fruit, adj3, ch_name, verb3, number, ch_name, superhero, superhero, ch_name, country, ch_name, dessert, ch_name, year, noun4)