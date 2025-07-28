# Easy Mad Libs Game
print("Welcome to Mad Libs!")
print("Please enter the following words:")

# Get user inputs
adjective = input("An adjective (e.g., silly): ")
animal = input("An animal: ")
verb = input("A verb (e.g., jump): ")
food = input("A food: ")
color = input("A color: ")

# Create and display the story
story = f"""
Today I saw a {adjective} {animal}!
It was {color} and kept {verb}ing.
When I offered it {food}, 
it smiled and ran away.
What a day!
"""

print("\nHere's your Mad Libs story:")
print(story)

# Save to file option
save = input("Would you like to save this story? (yes/no): ")
if save.lower() == "yes":
    with open("madlib.txt", "w") as file:
        file.write(story)
    print("Story saved as 'madlib.txt'!")
else:
    print("Okay, goodbye!")