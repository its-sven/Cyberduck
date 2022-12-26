import random
import os

banner = """
Welcome to Your
  _____       _     _                  _            _    
 |  __ \     | |   | |                | |          | |   
 | |__) |   _| |__ | |__   ___ _ __ __| |_   _  ___| | __
 |  _  / | | | '_ \| '_ \ / _ \ '__/ _` | | | |/ __| |/ /
 | | \ \ |_| | |_) | |_) |  __/ | | (_| | |_| | (__|   < 
 |_|  \_\__,_|_.__/|_.__/ \___|_|  \__,_|\__,_|\___|_|\_\ 
                                                                                
                                                                                        
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠔⠒⠒⠒⠒⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⠀⠀⠀⠀⠀⣼⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⢁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⠀⠀⠀⠀⡠⠐⠀⡲⣺⣶⣦⣄⠀
⠀⠀⠀⠀⡠⠏⠉⠑⢺⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⣀⠠⠋⢀⢠⣾⣿⣿⣻⣿⣿⠃
⠀⠀⠀⡼⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⡔⠁⢣⡗⠒⣾⣿⣿⣿⣿⡿⠛⠀⠀
⠀⠀⡰⠃⠀⠀⠀⠀⠀⠀⠡⡀⠀⠀⠀⠀⠀⠀⠡⢄⡀⠋⠿⣿⣿⣿⣿⣿⡧⠀⠀⠀
⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠑⠄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠐⠺⣿⠿⠉⠀⠀⠀⠀
⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⡀⠀⠀
⣿⡐⠠⠐⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀
⡇⠀⠀⠀⠁⠀⠀⠀⠀⠈⠐⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆
⢸⡆⠀⠰⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆
⠘⡏⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⡆
⠀⠹⡆⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃
⠀⠀⠉⠻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠃⠀
⠀⠀⠀⠀⠀⠁⠂⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⡴⠊⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠐⠢⠤⠄⢀⣀⣀⣀⠀⠤⠤⠤⠒⠒⠉⠀⠀⠀⠀                                                                                                                

-Best Proplem solver on Earth.

"""

print(banner)



languages = ["English", "German", "French", "Spanish", "Italian"]

# Prompt the user to select a language
print("Select a language from the following list:")
for i, lang in enumerate(languages):
    print(str(i + 1) + ". " + lang)

selected_lang_num = int(input("Enter the number of your selected language: "))

if selected_lang_num > 5:
  print("Error")
  exit()

selected_lang = languages[selected_lang_num - 1]

os.system('clear')

# Print the selected language
print("You selected: " + selected_lang) 

print("\n")

# Output depending on the selection
if selected_lang == "English":

    answer = "N"
    while answer == "N":
        text = input("Explain your problem in as much detail as possible to the rubber ducky: \n\n")

        os.system('clear')

    # List of pre-fabricated texts
        prefab_texts = ["So your problem is:\n" + text + "\n\nrigth?", 
                "Why don't you read that again?\n\n" + text, 
                "Are you sure the answer isn't already in your problem description?\n\n" + text]

    # Choose a random pre-fabricated text from the list
        random_text = random.choice(prefab_texts)

    # Print the random text
        print(random_text)


        while answer == "N" or "n":
            answer = input("\n\nDid that help? [Y/N]")
            if answer == "Y" or "y":
                print("Glad I could help\n-Your Rubberduck")
                continue
    
            elif answer == "N" or "n":
                print("Try again:\n")

            else:
                print("Error")




elif selected_lang == "German":

    text = input("Erkläre dein Problem so detailliert wie möglich der Gummiente: \n\n\n")

    os.system('clear')

    # List of pre-fabricated texts
    prefab_texts = ["Dein Problem ist also:\n" + text + "\n\nRichtig?", 
                "Lies dir das doch noch mal durch:\n\n" + text, 
                "Bist du sicher, dass die Antwort nicht schon in deiner Problembeschreibung steht?\n\n" + text]

    # Choose a random pre-fabricated text from the list
    random_text = random.choice(prefab_texts)

    # Print the random text
    print(random_text)

    input("\n\nHat das weitergeholfen? [J/N]")


elif selected_lang == "French":

    text = input("Explique ton problème de manière aussi détaillée que possible au canard en caoutchouc: \n\n\n")

    os.system('clear')

    # List of pre-fabricated texts
    prefab_texts = ["Ton problème est donc:\n" + text + "\n\nCorrect?", 
                "Relis-le:\n\n" + text, 
                "Es-tu sûr que la réponse ne se trouve pas déjà dans la description de ton problème?\n\n" + text]

    # Choose a random pre-fabricated text from the list
    random_text = random.choice(prefab_texts)

    # Print the random text
    print(random_text)


elif selected_lang == "Spanish":

    text = input("Explica tu problema con el mayor detalle posible al patito de goma: \n\n\n")

    os.system('clear')

    # List of pre-fabricated texts
    prefab_texts = ["Así que tu problema es:" + text + "\n\n¿Verdad?", 
                "¿Por qué no lees eso otra vez?\n\n" + text, 
                "¿Está seguro de que la respuesta no está ya en la descripción de su problema?\n\n" + text]

    # Choose a random pre-fabricated text from the list
    random_text = random.choice(prefab_texts)

    # Print the random text
    print(random_text)


elif selected_lang == "Italian":

    text = input("Spiegate il problema nel modo più dettagliato possibile alla paperella di gomma: \n\n\n")

    os.system('clear')

    # List of pre-fabricated texts
    prefab_texts = ["Quindi il problema è:" + text + "\n\nGiusto?", 
                "Perché non lo rileggi?\n\n" + text, 
                "Siete sicuri che la risposta non sia già presente nella descrizione del problema?\n\n" + text]

    # Choose a random pre-fabricated text from the list
    random_text = random.choice(prefab_texts)

    # Print the random text
    print(random_text)

else:
    print("Invalid selection.")


input("Press Enter to end the program")
exit()
