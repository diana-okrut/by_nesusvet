"""
https://www.codewars.com/kata/alphabet-war
"""
left_side = {'s': 1,
             'b': 2,
             'p': 3,
             'w': 4,
             'y': 1,
             }
right_side = {'z': 1,
              'd': 2,
              'q': 3,
              'm': 4,
              'y': 3,
              }
central = {'a': 1,
           'o': 1,
           'u': 1,
           'e': 1,
           'i': 1,
           'y': 1,
           }


def counting_of_points(battlefield: str, army: dict):
    counter = 0
    for letter in battlefield:
        if letter in army:
            counter += army[letter]
    return counter


def determination_of_winners(text):
    if text == '':
        return "Let's fight again!"

    left_side_points = counting_of_points(text, left_side)
    right_side_points = counting_of_points(text, right_side)
    central_points = counting_of_points(text, central)

    results = {'Left side': left_side_points,
               'Right side': right_side_points,
               'Central': central_points,
               }
    pairs = []
    for name, score in results.items():
        pairs.append((score, name))
    winners_list = sorted(pairs, reverse=True)
    first_place = winners_list[0]
    second_place = winners_list[1]
    if first_place[0] == second_place[0]:
        answer = "Let's fight again!"
    else:
        answer = f'{first_place[1]} wins!'
    return answer
