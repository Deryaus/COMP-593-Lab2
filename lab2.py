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
        'pizza_toppings': ['OLIVES', 'SAUSAGE', 'ONIONS'],
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
        'genre': 'action'
    }
    about_me['movies'].append(new_movie)
    name_id(about_me)
    print_movie_genres(about_me)

    return about_me

def name_id(about_me):
    full_name = about_me['full_name']
    first_name = str.split(about_me['full_name'])
    print(f'My name is {full_name}, but you can call me King {first_name[0]}.')
    print('My student ID is', about_me['student_id'], end='\n\n')

# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return


    
if __name__ == '__main__':
    main()