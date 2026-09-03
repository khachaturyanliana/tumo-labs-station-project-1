print("Hello, Welcome to the Mad Libs!")
print("Let's create a cozy story together!")

templates = [
    "Hospital",
    "Castle",
    "Camping"
]

print("Choose a story:")

print("1. Hospital")
print("2. Camping")
print("3. Castle")


choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    print("You've selected a Hospital story!")

    number = input("Enter a number: ")
    measure_of_time = input("Enter a measure of time: ")
    mode_of_transportation = input("Enter a mode of transportation: ")
    adjective = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    noun = input("Enter a noun: ")
    color = input("Enter a color: ")
    part_of_the_body = input("Enter a part of the body: ")
    verb = input("Enter a verb: ")
    number2 = input("Enter another number: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter another noun: ")
    part_of_the_body2 = input("Enter another part of the body: ")
    verb2 = input("Enter another verb: ")
    noun4 = input("Enter another noun: ")
    adjective3 = input("Enter another adjective: ")
    silly_word = input("Enter a silly word: ")

    story = f""" 
    It was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}. The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here. There are nurses here who have {color} {part_of_the_body2}. If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor and they were wearing a {noun3} on their {part_of_the_body2}. I heard that all doctors {verb} {noun4} every day for breakfast. The most {adjective3} thing about being in the hospital is the {silly_word} {noun} ! """

    print(story)

elif choice == "2":
    print("You've selected a Camping story!")

    person = input("Enter person's name: ")
    noun = input("Enter a noun: ")
    feeling = input("Enter an adjective describing a feeling: ")
    verb = input("Enter a verb: ")
    feeling2 = input("Enter another feeling adjective: ")
    animal = input("Enter an animal: ")
    verb2 = input("Enter another verb: ")
    color = input("Enter a color: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    adverb_ly = input("Enter a adverb ending in -ly: ")
    number = input("Enter a number: ")
    measure_of_time = input("Enter a measure of time: ")
    silly_word = input("Enter a silly word: ")
    noun2 = input("Enter another noun: ")

    story = f"""
        This weekend I am going camping with {person}. I packed my lantern, sleeping bag, and {noun}. I am so {feeling} to {verb} in a tent. I am {feeling2} we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color} lake is great for {verb_ing}. Then we will {adverb_ly} hike through the forest for {number} {measure_of_time}. If I see a {color} {animal} while hiking, I am going to bring it home as a pet! At night we will tell {number} {silly_word} stories and roast {noun2} around the campfire!! """

    print(story)

elif choice == "3":
    print("You've selected a Castle story!")

    person = input("Enter person's name: ")
    adjective = input("Enter an adjective: ")
    color = input("Enter a color: ")
    animal = input("Enter an animal: ")
    place = input("Enter a place: ")
    adjective2 = input("Enter another adjective: ")
    magical_creature_plural = input("Enter a magical creature: ")
    adjective3 = input("Enter another adjective: ")
    magical_creature_plural2 = input("Enter another magical creature: ")
    room_in_a_house = input("Enter a room in a house: ")
    noun = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    noun_plural3 = input("Enter another noun: ")
    adjective4 = input("Enter another adjective: ")
    noun_plural4 = input("Enter another noun: ")
    number = input("Enter a number: ")
    measure_of_time = input("Enter a measure of time: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    adjective5 = input("Enter another adjective: ")
    noun5 = input("Enter another noun: ")

    story = f""" 
    Dear {person}, I am writing to you from a {adjective} castle in an enchanted forest. I found myself here one day after going for a ride on a {color} {animal} in {place}. There are {adjective2} {magical_creature_plural} and {adjective3} {magical_creature_plural2} here! In the {room_in_a_house} there is a pool full of {noun}. I fall asleep each night on a {noun2} of {noun_plural3} and dream of {adjective4} {noun_plural4}. It feels as though I have lived here for {number} {measure_of_time}. I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective5} {noun5}!! """

    print(story)

else:
    print("Invalid choice!")




