from numpy import random
from math import isclose
from pprint import pprint
import copy
from tqdm import tqdm

CITY = 'Manchester City'
ARSENAL = 'Arsenal'
NEWCASTLE = 'Newcastle'
MANCHESTER_UNITED = 'Manchester United'
LIVERPOOL = 'Liverpool'
TOTTENHAM = 'Tottenham'
ASTON_VILLA = 'Aston Villa'
BRIGHTON = 'Brighton Hove Albion'
BRENTFORD = 'Brentford FC'
FULHAM = 'Fulham'
CRYSTAL_PALACE = 'Crystal Palace'
CHELSEA = 'Chelsea'
BOURNEMOUTH = 'Bournemouth'
WOLVES = 'Wolverhampton Wanderers'
WEST_HAM = 'West Ham United'
LEEDS = 'Leeds United'
NOTT = 'Nottingham Forest'
LEICESTER = 'Leicester City'
EVERTON = 'Everton FC'
SOUTHAMPTON = 'Southampton FC'


def calculate_possibilities(upcoming_matches, current_points, metadata):
    if len(upcoming_matches) == 0:
        metadata['n_possibilities'] += 1
        print("{:e}".format(metadata['n_possibilities']))
        return

    current_match = upcoming_matches[0]
    # first team wins
    winner = current_match[0]
    current_points[winner] += 3
    calculate_possibilities(upcoming_matches=upcoming_matches[1:], current_points=current_points, metadata=metadata)

    # second team wins
    winner = current_match[1]
    current_points[winner] += 3
    calculate_possibilities(upcoming_matches=upcoming_matches[1:], current_points=current_points, metadata=metadata)

    # A draw
    team_1 = current_match[0]
    team_2 = current_match[1]
    current_points[team_1] += 1
    current_points[team_2] += 1
    calculate_possibilities(upcoming_matches=upcoming_matches[1:], current_points=current_points, metadata=metadata)


def get_top_4(final_points):
    all_points = sorted(list(set([points for team, points in final_points.items()])), reverse=True)
    top_4_qual_points = all_points[3]
    teams_for_top_4 = [team for team, points in final_points.items() if points >= top_4_qual_points]
    return teams_for_top_4


def calculate_possibility(upcoming_matches, current_points, metadata):
    if len(upcoming_matches) == 0:
        # metadata['top_4'] = get_top_4(current_points)
        return

    current_match = upcoming_matches[0]
    possibility = random.choice([current_match[0], current_match[1], None],
                                p=[current_match[2][0], current_match[2][1], current_match[2][2]])

    # A draw
    if not possibility:
        team_1 = current_match[0]
        team_2 = current_match[1]
        metadata['matches_result'].append([(team_1, team_2, 'Draw')])
        current_points[team_1] += 1
        current_points[team_2] += 1

    # A winner
    else:
        current_points[possibility] += 3
        metadata['matches_result'].append([(current_match[0], current_match[1], possibility)])

    return calculate_possibility(upcoming_matches=upcoming_matches[1:], current_points=current_points,
                                 metadata=metadata)


def simulate_results(upcoming_matches, points, n_times=1000000):
    metadata = {
        'matches_result': []
    }

    top_4_teams_count = dict()
    for _ in tqdm(range(n_times)):
        current_points = copy.deepcopy(points)
        calculate_possibility(upcoming_matches=upcoming_matches, current_points=current_points,
                              metadata=copy.deepcopy(metadata))
        top_4_teams = get_top_4(current_points)
        for top_4_team in top_4_teams:
            if top_4_team not in top_4_teams_count:
                top_4_teams_count[top_4_team] = 0

            top_4_teams_count[top_4_team] += 1

    probs = [(top_4_team, 100 * count/n_times) for top_4_team, count in top_4_teams_count.items()]
    pprint(sorted(probs, key=lambda x: x[1], reverse=True))
    print("\n")
    pprint(top_4_teams_count)


def main():
    current_points = {
        CITY: 76,
        ARSENAL: 75,
        NEWCASTLE: 65,
        MANCHESTER_UNITED: 63,
        LIVERPOOL: 56,
        TOTTENHAM: 54,
        ASTON_VILLA: 54,
        BRIGHTON: 52,
        BRENTFORD: 50,
        FULHAM: 45,
        CRYSTAL_PALACE: 40,
        CHELSEA: 39,
        BOURNEMOUTH: 39,
        WOLVES: 37,
        WEST_HAM: 34,
        LEEDS: 30,
        NOTT: 30,
        LEICESTER: 29,
        EVERTON: 28,
        SOUTHAMPTON: 24
    }

    upcoming_matches = [
                        # 34
                        (LEICESTER, EVERTON, (0.1, 0.1, 0.8)), (ARSENAL, CHELSEA, (0.7, 0.1, 0.2)),

                        # 28
                        (LIVERPOOL, FULHAM, (0.7, 0.1, 0.2)), (CITY, WEST_HAM, (0.7, 0.1, 0.2)),
                        (BRIGHTON, MANCHESTER_UNITED, (0.4, 0.2, 0.4)),

                        # 35
                        (BOURNEMOUTH, CHELSEA, (0.4, 0.2, 0.4)), (CITY, LEEDS, (0.8, 0.1, 0.1)),
                        (WOLVES, ASTON_VILLA, (0.1, 0.7, 0.2)), (TOTTENHAM, CRYSTAL_PALACE, (0.7, 0.1, 0.2)),
                        (LIVERPOOL, BRENTFORD, (0.7, 0.1, 0.2)), (NEWCASTLE, ARSENAL, (0.3, 0.3, 0.4)),
                        (WEST_HAM, MANCHESTER_UNITED, (0.2, 0.3, 0.5)), (FULHAM, LEICESTER, (0.3, 0.3, 0.4)),
                        (BRIGHTON, EVERTON, (0.7, 0.1, 0.2)), (NOTT, SOUTHAMPTON, (0.3, 0.3, 0.4)),

                        # 36
                        (LEEDS, NEWCASTLE, (0.2, 0.7, 0.1)), (SOUTHAMPTON, FULHAM, (0.3, 0.3, 0.4)),
                        (CHELSEA, NOTT, (0.3, 0.3, 0.4)), (ASTON_VILLA, TOTTENHAM, (0.4, 0.3, 0.3)),
                        (MANCHESTER_UNITED, WOLVES, (0.4, 0.2, 0.4)), (CRYSTAL_PALACE, BOURNEMOUTH, (0.3, 0.3, 0.4)),
                        (EVERTON, CITY, (0.1, 0.8, 0.1)), (BRENTFORD, WEST_HAM, (0.3, 0.3, 0.4)),
                        (ARSENAL, BRIGHTON, (0.55, 0.35, 0.1)), (LEICESTER, LIVERPOOL, (0.1, 0.8, 0.1)),

                        # 25
                        (NEWCASTLE, BRIGHTON, (0.45, 0.35, 0.2)),

                        # 37
                        (TOTTENHAM, BRENTFORD, (0.5, 0.3, 0.2)), (LIVERPOOL, ASTON_VILLA, (0.45, 0.25, 0.3)),
                        (WOLVES, EVERTON, (0.3, 0.3, 0.4)), (BOURNEMOUTH, MANCHESTER_UNITED, (0.3, 0.4, 0.3)),
                        (FULHAM, CRYSTAL_PALACE, (0.3, 0.3, 0.4)), (NOTT, ARSENAL, (0.05, 0.7, 0.25)),
                        (WEST_HAM, LEEDS, (0.3, 0.3, 0.4)), (BRIGHTON, SOUTHAMPTON, (0.7, 0.1, 0.2)),
                        (CITY, CHELSEA, (0.6, 0.1, 0.3)), (NEWCASTLE, LEICESTER, (0.7, 0.1, 0.2)),

                        # 32
                        (BRIGHTON, CITY, (0.25, 0.45, 0.3)), (MANCHESTER_UNITED, CHELSEA, (0.3, 0.3, 0.4)),

                        # 38
                        (ASTON_VILLA, BRIGHTON, (0.35, 0.35, 0.3)), (EVERTON, BOURNEMOUTH, (0.3, 0.3, 0.4)),
                        (LEEDS, TOTTENHAM, (0.3, 0.4, 0.3)), (BRENTFORD, CITY, (0.2, 0.7, 0.1)),
                        (MANCHESTER_UNITED, FULHAM, (0.5, 0.3, 0.2)), (CHELSEA, NEWCASTLE, (0.3, 0.5, 0.2)),
                        (LEICESTER, WEST_HAM, (0.3, 0.3, 0.4)), (ARSENAL, WOLVES, (0.8, 0.1, 0.1)),
                        (SOUTHAMPTON, LIVERPOOL, (0.1, 0.7, 0.2)), (CRYSTAL_PALACE, NOTT, (0.3, 0.3, 0.4))]

    # check
    for match in upcoming_matches:
        assert isclose(sum(match[-1]), 1, abs_tol=1e-3), f"Issue with prob : {match[0]}, {match[1]} : {sum(match[-1])}"

    # simulate_results(upcoming_matches=upcoming_matches, points=current_points, n_times=100000)

    metadata = {
        'n_possibilities': 0
    }
    current_points = copy.deepcopy(current_points)
    calculate_possibilities(upcoming_matches[:5], current_points, metadata)
    print(metadata, current_points)


if __name__ == '__main__':
    main()
