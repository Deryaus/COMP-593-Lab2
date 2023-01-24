"""--------------------ι𝐍Ⓙย𝐬𝓣ᶤςⒺ Ⓐ𝐍ＹωᕼⒺг𝐄 ᶤ𝐬 ᵃ tｈяᗴＡт ⓉＯ 𝐣υ𝔰ｔ𝐢ᶜⓔ 𝐄V乇яｙ山卄εŘ乇 --------------------

Description:
 Extracts information from a dictionary.

Usage:
 python lab2.py

---------------------ι𝐍Ⓙย𝐬𝓣ᶤςⒺ Ⓐ𝐍ＹωᕼⒺг𝐄 ᶤ𝐬 ᵃ tｈяᗴＡт ⓉＯ 𝐣υ𝔰ｔ𝐢ᶜⓔ 𝐄V乇яｙ山卄εŘ乇--------------------"""



def main():
    
    student = {

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
    student['movies'].append(new_movie)
    name_id(student)
    return student


def name_id(student):
    full_name = student['full_name']
    first_name = str.split(student['full_name'])
    print(f'My name is {full_name}, but you can call me King {first_name[0]}.')
    print('My student ID is', student['student_id'])


    
if __name__ == '__main__':
    main()