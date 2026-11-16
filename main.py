from pathlib import Path
from loader import load_players, load_team,
from models import League
from rules import MAX_CREDITS

BASE = Path(__file__).resolve().parent

def show_pool(players):
    by_franchise = {}
    by_role = {}
    for player in players.values():
        by_franchise[player.franchise] = by_franchise.get(player.franchise, 0) + 1
        by_role[player.role] = by_role.get(player.role, 0) + 1
    print(f"Player pool: {len(players)} players")
    print("Players by franchise:")
    for franchise in sorted(by_franchise):
        print(f"  {franchise}: {by_franchise[franchise]}")
    print("Players by role:")
    for role in sorted(by_role):
        print(f"  {role}: {by_role[role]}")

def show_team(team):
    print(f"\nTeam {team.team_name} by {team.owner}:")
    for player in team.players:
        print(f"  {player}")
    print(f"Total credits: {team.total_credits():.1f}")
    print(f"Captain: {team.captain.name}, Vice-captain: {team.vice_captain.name}")

def show_verdict(team):
    errors = team.check_rules()
    if errors:
        print("ILLEGAL:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("LEGAL")
    return errors

def main():
    players = load_players(BASE / "data" / "players.csv")
    show_pool(players)
    teams = load_teams(BASE / "data" / "sample_teams.csv", players)
    legal, illegal = [], []
    for team in teams:
        show_team(team)
        if show_verdict(team):
            illegal.append(team)
        else:
            legal.append(team)
    print(f"\nSummary: {len(legal)} legal, {len(illegal)} illegal out of {len(teams)} teams")
    print("Legal teams:")
    for team in legal:
        print(f"  {team.team_name}")
    print("Illegal teams:")
    for team in illegal:
        print(f"  {team.team_name}")

    print("\nMY TEAM (EXAMPLE: replace with your form-submitted XI)")
    my_team = load_team(BASE / "data" / "my_team.csv", players)
    if my_team is None:
        raise ValueError("data/my_team.csv must contain your team")
    show_team(my_team)
    print(f"Credits left: {MAX_CREDITS - my_team.total_credits():.1f}")
    show_verdict(my_team)

    league = League("The Dugout")
    for team in teams:
        league.add_team(team)
    league.add_team(my_team)
    print("\nLEAGUE TABLE (cheapest first)")
    print(f"{'Team':28} {'Owner':16} {'Credits':>8}  Status")
    for team in league.rank_teams():
        verdict = "ILLEGAL" if team.check_rules() else "LEGAL"
        print(f"{team.team_name:28} {team.owner:16} {team.total_credits():8.1f}  {verdict}")

if __name__ == "__main__":
    main()
