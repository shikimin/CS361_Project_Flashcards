# Microservice ReadMe
A microservice that generates a random character from the [AniList API](https://anilist.gitbook.io/anilist-apiv2-docs/).

## Requirements
The following modules must be imported:
```
import requests
import time
import random
```

## Requesting and Receiving Data
This microservice uses a .txt file (random_character_gen.txt) as a communication pipe. 
To **request** data from the microservice, the word “run” must be written into random_character_gen.txt. 
An example of how this can be done using user input is below:
```
import time

response = input("Enter 1 to generate a random character. Enter 2 to exit.\n")
if response == "1":
    # Write into txt file
    with open('random_character_gen.txt', 'w') as write_random_char:
        write_random_char.write("run")
    time.sleep(5)

    # Read character ID number from txt file
    with open('random_character_gen.txt') as read_random_char:
        read_data = read_random_char.read()
        print(read_data)
elif response == "2":
    quit()
else:
    print("That's not a valid number")
```
If the microservice detects “run” in the .txt file, it will make a call to the AniList API and draw a 
random ID number for one of its 50 most popular anime characters. It will then write the ID number in the .txt file. 

As seen above, it is then up to the main application to **receive** the data by opening and reading the data from the .txt file. 

**Note:** It is up to the user/main application to determine when the microservice should start running (e.g. at the same time as main app startup or right before data is requested); 
all that matters is that it is running when the main app requests data.

## UML Sequence Diagram
![UML Sequence Diagram for Random Character Generator microservice](/microservice/random_character_gen_UML_diagram.png)
