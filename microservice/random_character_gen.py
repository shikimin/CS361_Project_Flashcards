import requests
import time
import random

while True:
    time.sleep(5)
    with open('random_character_gen.txt') as read_file:
        data = read_file.read()

    if data == "run":
        query = '''
            query ($page: Int, $perPage: Int) {
                Page(page: $page, perPage: $perPage) {
                    pageInfo {
                    total
                    perPage
                    lastPage
                    }
                    
                    characters (sort: FAVOURITES_DESC) { 
                    id
                    name { 
                        full
                    }
                    favourites
                    gender
                    dateOfBirth {
                        month
                        day
                    }
                    age
                    description
                    }
                    
                }
                }
        '''

        variables = {
            'page': 1,
            'perPage': 500
        }

        url = 'https://graphql.anilist.co'

        # Make request to API
        response = requests.post(url, json={'query': query, 'variables': variables}).json()
        response = response['data']['Page']['characters']

        # get list of character ID numbers
        id_numbers = []
        for character in response:
            id_numbers.append(character['id'])

        random_id = random.choice(id_numbers)

        with open('random_character_gen.txt','w', encoding="utf-8") as write_file:  
            write_file.write(str(random_id))