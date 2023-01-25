"""--------------------ι𝐍Ⓙย𝐬𝓣ᶤςⒺ Ⓐ𝐍ＹωᕼⒺг𝐄 ᶤ𝐬 ᵃ tｈяᗴＡт ⓉＯ 𝐣υ𝔰ｔ𝐢ᶜⓔ 𝐄V乇яｙ山卄εŘ乇 --------------------

Description:
 Extracts information from a dictionary.

Usage:
 python lab2.py

---------------------ι𝐍Ⓙย𝐬𝓣ᶤςⒺ Ⓐ𝐍ＹωᕼⒺг𝐄 ᶤ𝐬 ᵃ tｈяᗴＡт ⓉＯ 𝐣υ𝔰ｔ𝐢ᶜⓔ 𝐄V乇яｙ山卄εŘ乇--------------------"""
def main():
    about_me = {

        'full_name': 'Geoff Smith',
        'student_id': 10256979,
        'pizzatoppings': ['OLIVES', 'SAUSAGE', 'ONIONS'],
        'movies': [
            {
                'title': 'gladiator',
                'genre': 'action'

            },
            {
                'title': 'interstellar',
                'genre': 'science fiction'
            }
            ] 
        }

    new_movie = {
        'title': 'tenet',
        'genre': 'thriller'
    }
    about_me['movies'].append(new_movie)
    name_id(about_me)
    print_movie_genres(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ('PINEAPPLE', 'PEPPERONI'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)

def name_id(about_me):
    full_name = about_me['full_name']
    first_name = str.split(about_me['full_name'])
    print(f'My name is {full_name}, but you can call me King {first_name[0]}.')
    print('My student ID is', about_me['student_id'], end='\n')

#Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizzatoppings'].extend(toppings)
    for i,t in enumerate(about_me['pizzatoppings']):
        about_me['pizzatoppings'][i] = t.lower()  
    about_me['pizzatoppings'].sort()

#Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print('\nMy favourite pizza toppings are:')
    for t in about_me['pizzatoppings']:
        print(f'- {t}')

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    print('\nI like to watch ', end='')
    #for i,g in enumerate(about_me['movies']):
    #    if i < len(about_me['movies']) -1:
    #        print(f'{g["genre"]}, ', end='')
    #    else:
    #        print(f'{g["genre"]} ')

    movie_genres = [g['genre'] for g in about_me['movies']]
    genre_list = ', '.join(movie_genres)
    x = 'and'
    genre_list.insert(-1, x)
    print(genre_list)
   
# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    print('\nSome of my favourite movies are ', end='')
    for i,m in enumerate(movie_list['movies']):
        if i < len(movie_list['movies']) -1:
            print(f'{m["title"]}, ', end='')
        else:
            print(f'{m["title"]} ')

if __name__ == '__main__':
    main()