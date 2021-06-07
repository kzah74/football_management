from .models import Match
import datetime


def get_all_pairs(qs):
    index = 1
    pairs = []
    for element1 in qs:
        for element2 in qs[index:]:
            pair = (element1, element2)
            pairs.append(pair)
        index += 1
    return pairs


def generate_matches(qs):
    all_matches = get_all_pairs(qs)
    date = datetime.date.today() + datetime.timedelta(days=1)
    while len(all_matches) > 0:
        teams_for_today = []
        matches_for_today = []
        matches_left_over = []
        for match in all_matches:
            if (match[0] in teams_for_today) or (match[1] in teams_for_today):
                matches_left_over.append(match)
            else:
                matches_for_today.append(match)
                teams_for_today.append(match[0])
                teams_for_today.append(match[1])
        all_matches = matches_left_over

        for pair in matches_for_today:
            visitor, host = pair
            visitor = pair[0]
            host = pair[1]

            match = Match(visitor=visitor, host=host, date=date)
            match.save()
        
        date += datetime.timedelta(days=1)
