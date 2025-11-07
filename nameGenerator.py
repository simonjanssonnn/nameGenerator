import random

# läs in namn fil listan
with open(r"names.txt") as file:
    list_names = file.read().splitlines()

# fråga användaren om inställningar
include_numbers = input("Vill du ha siffror i ditt användarnamn? (ja/nej): ").lower().strip()
username_length_input = input("Välj ett ensiffrigt nummer för hur långt ditt namn ska vara: ")

# gör om string till en integer

try:

    username_length = int(username_length_input)
except ValueError:
    username_length = 2
    print("VARNING: Ogiltig inmatning, sätter automatiskt längden till 2")



# hitta namn med rätt längd och appenda den till en tom lista
final_name = []
for i in list_names:
    if len(i) == username_length:
        final_name.append(i)

# lägg till siffror om användaren vill det
try:

    if include_numbers == "ja":
        random_number = random.randint(1, 999)
    elif include_numbers == "nej":
        random_number = ""
    else:
        raise ValueError
except ValueError:
    random_number = ""
    print("VARNING: Ingenting givet, sätter slumpat nummer till ingenting")


print(random.choice(final_name), random_number)


