import csv
from collections import Counter


def get_team_names_by_id():
    points_by_teams = {}
    with open('teams.csv') as teams:
        for row_dict in csv.DictReader(teams):
            team_id, team_name = row_dict['id'], row_dict['name']
            points_by_teams[int(team_id)] = team_name
    return points_by_teams


def get_most_frequent_winner_team_id():
    iterable = []
    with open('matches.csv') as matches:
        for row_dict in csv.DictReader(matches):
            score_a, score_b = map(int, row_dict['score'].split(':'))
            if score_a > score_b:
                iterable.append(int(row_dict['team_a']))
            elif score_b > score_a:
                iterable.append(int(row_dict['team_b']))

    counter = Counter(iterable)
    return counter.most_common(1)[0][0]


def get_most_frequent_goals_team_id():
    iterable = []
    # Changes allowed from here ===
    with open('matches.csv') as matches:
        for row_dict in csv.DictReader(matches):
            score_a, score_b = map(int, row_dict['score'].split(':'))
            iterable.extend([int(row_dict['team_a'])] * score_a)
            iterable.extend([int(row_dict['team_b'])] * score_b)
    # Changes allowed till here ===
    counter = Counter(iterable)
    return counter.most_common(1)[0][0]

def get_subtract_frequent_winners():
    iterable = []
    with open('matches.csv') as matches:
        for row_dict in csv.DictReader(matches):
            score_a, score_b = map(int, row_dict['score'].split(':'))
            if score_a > score_b:
                iterable.append(int(row_dict['team_a']))
            elif score_b > score_a:
                iterable.append(int(row_dict['team_b']))
    # Changes allowed till here ===
    counter = Counter(iterable)
    return counter.most_common(2)[0][1]- counter.most_common(2)[1][1]

def get_most_frequent_winner_team_id__in_2016():
    iterable = []
    with open('matches.csv') as matches:
        for row_dict in csv.DictReader(matches):
            if '2016' in row_dict['date']:
                score_a, score_b = map(int, row_dict['score'].split(':'))
                if score_a > score_b:
                    iterable.append(int(row_dict['team_a']))
                elif score_b > score_a:
                    iterable.append(int(row_dict['team_b']))

    counter = Counter(iterable)
    list_of_winners = []
    for pair in counter.most_common(10):
        list_of_winners.append(pair[0])

    return list_of_winners

if __name__ == "__main__":
    name_by_id = get_team_names_by_id()
    # print(name_by_id)
    team_id = get_most_frequent_winner_team_id()
    # print(team_id)
    print(1, name_by_id[team_id])
    team_id = get_most_frequent_goals_team_id()
    print(2, name_by_id[team_id])
    winner_substract = get_subtract_frequent_winners()
    print(3, winner_substract)
    winners_in_2016 = get_most_frequent_winner_team_id__in_2016()
    for el in winners_in_2016:
        print(4, name_by_id[el])


# sqlite3 football.db
