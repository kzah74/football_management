import datetime

def dates(lst):
    dates = []
    for x in range(len(lst)):
        dates.append((datetime.date.today() + datetime.timedelta(days=x)).strftime('%d-%m-%Y'))
    del dates[0]
    return dates


def all_pairs(lst):
    index = 1
    pairs = []
    for element1 in lst:
        for element2 in lst[index:]:
            pair = (element1, element2)
            pairs.append(pair)
        index += 1
    return pairs

def distinct_pairs(lst):
    all_matches = all_pairs(lst)
    possible_dates = dates(all_matches)
    program_matches = {}
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

        program_matches[possible_dates[0]] = matches_for_today
        del possible_dates[0]
    return program_matches
