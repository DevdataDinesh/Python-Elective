teams = {}
while True:
    team_name = input("Enter team name (or 'done' to finish): ")
    if team_name == "done":
        break
    wins = int(input("Enter number of wins: "))
    losses = int(input("Enter number of losses: "))
    teams[team_name] = [wins, losses]
print("Names of all teams:")
for team in teams:
    print(team)
wins = [team[0] for team in teams.values()]
max_wins = max(wins)
winning_teams = [team for team in teams if teams[team][0] == max_wins]
print(f"\nName of the team(s) with the highest wins: {', '.join(winning_teams)}")
losses = [team[1] for team in teams.values()]
max_losses = max(losses)
losing_teams = [team for team in teams if teams[team][1] == max_losses]
print(f"\nName of the team(s) with the highest losses: {', '.join(losing_teams)}")
team_name = input("\nEnter the team name for win percentage: ")
if team_name in teams:
    win_percentage = teams[team_name][0] / (teams[team_name][0] + teams[team_name][1])
    print(f"Win percentage of {team_name} is {win_percentage * 100:.1f}%")
else:
    print(f"{team_name} is not in the list of teams.")