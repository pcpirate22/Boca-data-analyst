matches = [
    {"matchday": 1,  "date": "2026-01-25", "opponent": "Deportivo Riestra",     "score_for": 1, "score_against": 0, "home": True},
    {"matchday": 2,  "date": "2026-01-28", "opponent": "Estudiantes",           "score_for": 1, "score_against": 2, "home": False},
    {"matchday": 3,  "date": "2026-02-01", "opponent": "Newell's Old Boys",     "score_for": 2, "score_against": 0, "home": True},
    {"matchday": 4,  "date": "2026-02-08", "opponent": "Velez Sarsfield",       "score_for": 1, "score_against": 2, "home": False},
    {"matchday": 5,  "date": "2026-02-15", "opponent": "Platense",              "score_for": 0, "score_against": 0, "home": True},
    {"matchday": 6,  "date": "2026-02-20", "opponent": "Racing Club",           "score_for": 0, "score_against": 0, "home": True},
    {"matchday": 8,  "date": "2026-02-28", "opponent": "Gimnasia Mendoza",      "score_for": 1, "score_against": 1, "home": True},
    {"matchday": 7,  "date": "2026-03-04", "opponent": "Lanus",                 "score_for": 3, "score_against": 0, "home": False},
    {"matchday": 9,  "date": "2026-05-02", "opponent": "Central Cordoba (SdE)", "score_for": 2, "score_against": 1, "home": False},
    {"matchday": 10, "date": "2026-03-11", "opponent": "San Lorenzo",           "score_for": 1, "score_against": 1, "home": True},
    {"matchday": 11, "date": "2026-03-15", "opponent": "Union Santa Fe",        "score_for": 1, "score_against": 1, "home": False},
    {"matchday": 12, "date": "2026-03-22", "opponent": "Instituto Cordoba",     "score_for": 2, "score_against": 0, "home": True},
    {"matchday": 13, "date": "2026-04-02", "opponent": "Talleres Cordoba",      "score_for": 1, "score_against": 0, "home": False},
    {"matchday": 14, "date": "2026-04-11", "opponent": "Independiente",         "score_for": 1, "score_against": 1, "home": True},
    {"matchday": 15, "date": "2026-04-19", "opponent": "River Plate",           "score_for": 1, "score_against": 0, "home": False},
    {"matchday": 16, "date": "2026-04-23", "opponent": "Defensa y Justicia",    "score_for": 4, "score_against": 0, "home": False},
]

def is_win(match):
    return match["score_for"] > match["score_against"]

def is_draw(match):
    return match["score_for"] == match["score_against"]

def is_loss(match):
    return match["score_for"] < match["score_against"]


def home_matches(matches):
    return [m for m in matches if m["home"]]

def away_matches(matches):
    return [m for m in matches if not m["home"]]


def win_home(matches):
    return sum(1 for m in home_matches(matches) if is_win(m))

def win_away(matches):
    return sum(1 for m in away_matches(matches) if is_win(m))

def win_rate(matches):
    return sum(1 for m in matches if is_win(m)) / len(matches)

def goals_for(matches):
    return sum(m["score_for"] for m in matches)

def goals_against(matches):
    return sum(m["score_against"] for m in matches)

def goal_difference(matches):
    return goals_for(matches) - goals_against(matches)

def avg_goals_for(matches):
    return goals_for(matches) / len(matches)

def avg_goals_against(matches):
    return goals_against(matches) / len(matches)

print("Matches:", len(matches))
print("Home matches:", len(home_matches(matches)))
print("Away matches:", len(away_matches(matches)))
print("Wins:", sum(1 for m in matches if is_win(m)))
print("Draws:", sum(1 for m in matches if is_draw(m)))
print("Losses:", sum(1 for m in matches if is_loss(m)))
print("Home wins:", win_home(matches))
print("Away wins:", win_away(matches))

print("Win rate (overall):", win_rate(matches))
print("Win rate (home):", win_rate(home_matches(matches)))
print("Win rate (away):", win_rate(away_matches(matches)))

print("Goals for (overall):", goals_for(matches))
print("Goals for (home):", goals_for(home_matches(matches)))
print("Goals for (away):", goals_for(away_matches(matches)))

print("Goals against (overall):", goals_against(matches))
print("Goals against (home):", goals_against(home_matches(matches)))
print("Goals against (away):", goals_against(away_matches(matches)))

print("Goal difference (overall):", goal_difference(matches))
print("Goal difference (home):", goal_difference(home_matches(matches)))
print("Goal difference (away):", goal_difference(away_matches(matches)))

print("Avg goals for (overall):", avg_goals_for(matches))
print("Avg goals for (home):", avg_goals_for(home_matches(matches)))
print("Avg goals for (away):", avg_goals_for(away_matches(matches)))

print("Avg goals against (overall):", avg_goals_against(matches))
print("Avg goals against (home):", avg_goals_against(home_matches(matches)))
print("Avg goals against (away):", avg_goals_against(away_matches(matches)))