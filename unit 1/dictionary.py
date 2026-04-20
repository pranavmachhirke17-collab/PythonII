my_dict = {
    "Name": "Harsh",
    "Age": 18,
    "City": "pune"
    }

my_dict["Country"] = "india"
print( "Adding new element:",my_dict)

my_dict["Age"] = 19
print( "Updating element:", my_dict)

removed = my_dict.pop("City", None)
print("After removal:", my_dict)


new_dict = {
    "hobby": "basketball"
}
my_dict.update(new_dict)
print("Merging both dictionary :", my_dict)