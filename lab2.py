"""--------------------ι𝐍Ⓙย𝐬𝓣ᶤςⒺ Ⓐ𝐍ＹωᕼⒺг𝐄 ᶤ𝐬 ᵃ tｈяᗴＡт ⓉＯ 𝐣υ𝔰ｔ𝐢ᶜⓔ 𝐄V乇яｙ山卄εŘ乇 --------------------

Description:
 Extracts information from a dictionary and prints information about a student.

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
            },
            ] 
        }
    about_me['movies'].append({'title':  'tenet', 'genre': 'thriller'})
    name_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ('PINEAPPLE', 'PEPPERONI'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)

# Function that prints Name and student number
def name_id(about_me):
    first_name = str.split(about_me['full_name'])
    print(f'My name is ', about_me['full_name'], end=', ') 
    print(f'but you can call me King {first_name[0]}.')
    print('My student ID is', about_me['student_id'], end='.\n')

#Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizzatoppings'].extend(toppings)
    for i,t in enumerate(about_me['pizzatoppings']):
        about_me['pizzatoppings'][i] = t.lower()  
    about_me['pizzatoppings'].sort()

#Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print('\nMy favourite pizza toppings are:')
    for t in about_me['pizzatoppings']:
        print(f'- {t}')

#Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    print('\nI like to watch', end=' ')
    movie_genres = [g['genre'] for g in about_me['movies']]
    genre_list = ', '.join(movie_genres)
    x = str.split(genre_list)
    x.insert(-1, 'and')
    genre_list_edited = ' '.join((s) for s in x)
    print(genre_list_edited, end=' movies.\n')
   
#Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    print('\nSome of my favourite movies are', end=' ')
    movie_titles = [g['title'].title() for g in movie_list['movies']]
    movies = ', '.join(movie_titles)
    x = str.split(movies)
    x.insert(-1, 'and')
    movies_edited = ' '.join((s)for s in x)
    print(movies_edited, end='!')

if __name__ == '__main__':
    main()