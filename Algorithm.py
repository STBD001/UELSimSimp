import random

# Define the pots
pot_1 = {'AS Roma': 'ITA', 'Manchester United': 'ENG', 'FC Porto': 'POR', 'Ajax Amsterdam': 'NLD',
         'Rangers': 'SCO', 'Eintracht Frankfurt': 'GER', 'Lazio': 'ITA', 'Tottenham': 'ENG', 'Slavia Praga': 'CZE'}

pot_2 = {'Real Sociedad': 'ESP', 'AZ Alkmaar': 'NLD', 'SC Braga': 'POR', 'Olympiakos': 'GRE',
         'Olympique Lyon': 'FRA', 'PAOK': 'GRE', 'Fenerbahce': 'TUR', 'Maccabi Tel Awiw': 'ISR', 'Ferencvárosi TC': 'HUN'}

pot_3 = {'Karabach Agdam': 'AZE', 'Galatasaray': 'TUR', 'FK Bodø/Glimt': 'NOR', 'Viktoria Pilzno': 'CZE', 'Royale Union Saint-Gilloise': 'BEL',
         'Dynamo Kijów': 'UKR', 'Łudogorec Razgrad': 'BUL', 'FC Midtjylland': 'DEN', 'Malmö FF': 'SWE'}

pot_4 = {'Athletic Bilbao': 'ESP', 'TSG Hoffenheim': 'GER', 'OGC Nice': 'FRA', 'RSC Anderlecht': 'BEL',
         'FC Twente': 'NED', 'Besiktas': 'TUR', 'FCSB': 'RUM', 'FK RFS': 'SWE', 'IF Elfsborg': 'SWE'}

all_teams = {**pot_1, **pot_2, **pot_3, **pot_4}


def draw_simplified():
    matches = {team: [] for team in all_teams}
    pots = [pot_1, pot_2, pot_3, pot_4]
    num_opponents = 8

    for team in all_teams:
        while len(matches[team]) < num_opponents:
            possible_opponents = []
            for pot in pots:
                if team in pot:
                    continue
                possible_opponents += [
                    opponent for opponent in pot
                    if all_teams[opponent] != all_teams[team] and len(matches[opponent]) < num_opponents
                       and opponent not in matches[team]  # Ensure no duplicate opponents
                ]


            if not possible_opponents:
                return draw_simplified()


            opponent = random.choice(possible_opponents)
            matches[team].append(opponent)
            matches[opponent].append(team)

    return matches


def print_matches(matches):
    for team, opponents in matches.items():
        print(f"{team} zagra przeciwko: {', '.join(opponents)}\n")