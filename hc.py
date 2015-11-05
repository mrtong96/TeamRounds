

import random

def main():
    text = open('test_hc.csv', 'r').read()
    lines = text.split('\r')
    lines = filter(lambda x: x, lines)
    lines = map(lambda x: x.split(','), lines)
    entrants = map(lambda x: [x[0], int(x[1])], lines)

    # can change number params here to get better results at cost of computation speed
    data = run_HC_trials(entrants, 100, 200)
    #data = run_HC_trials([(i, i) for i in range(100)], 100, 200)
    for el in data:
        print el

def run_HC(people, num_trials):
    teams = people[:]
    random.shuffle(teams)
    teams = get_teams(teams)

    for j in range(num_trials):
        new_scores = map(lambda x: zip(*x)[1], teams)
        def assign_score(scores):
            if len(scores) == 3:
                return sum(scores)
            return sum(scores) * 1.5
        new_scores = map(lambda x: assign_score(x), new_scores)
        new_data = zip(teams, new_scores)
        min_team = min(new_data, key=lambda x: x[1])
        new_data.remove(min_team)
        max_team = max(new_data, key=lambda x: x[1])

        teams.remove(min_team[0])
        teams.remove(max_team[0])

        avg = (min_team[1] + max_team[1]) / 2
        players = min_team[0] + max_team[0]

        best_dist = float('inf')
        best_team = None
        if len(players) != 4:
            for i1, el1 in enumerate(players):
                for i2, el2 in enumerate(players[i1 + 1:]):
                    for el3 in players[i1 + i2 + 2:]:
                        dist = abs(avg - el1[1] - el2[1] - el3[1])
                        if dist < best_dist:
                            best_team = [el1, el2, el3]
                            best_dist = dist
        else:
            avg = (min_team[1] + max_team[1]) / 3
            for i1, el1 in enumerate(players):
                for el2 in players[i1 + 1:]:
                    dist = abs(avg - el1[1] - el2[1])
                    if dist < best_dist:
                        best_team = [el1, el2]
                        best_dist = dist
        other_team = []
        for el in players:
            if el not in best_team:
                other_team.append(el)

        teams.append(best_team)
        teams.append(other_team)
    return teams

def get_teams(teams):
    total_len = len(teams)
    out = []
    index = 0
    while index < total_len:
        if index + 6 <= total_len:
            out.append(teams[index: index + 3])
            index += 3
        elif index + 5 == total_len:
            out.append(teams[index: index + 3])
            out.append(teams[index + 3: index + 5])
            index += 5
        elif index + 4 == total_len:
            out.append(teams[index: index + 2])
            out.append(teams[index + 2: index + 4])
            index += 5
        else:
            out.append(teams[index:])
            break
    return out

def run_HC_trials(teams, num_trials, num_iter):
    best_diff = float('inf')
    best_team = None
    best_scores = None

    for i in range(num_trials):
        teams_copy = teams[:]
        result = run_HC(teams_copy, num_iter)

        def assign_score(x):
            if len(x) == 3:
                return sum(x)
            return sum(x) * 3 / 2
        scores = map(lambda x: assign_score(zip(*x)[1]), result)
        diff = max(scores) - min(scores)

        if diff < best_diff:
            best_diff, best_team = diff, result
            best_scores = scores
    return best_team, best_scores, best_diff

if __name__ == "__main__":
    main()
