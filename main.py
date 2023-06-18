import json
import pandas as pd
import team

handles = 'handles.txt'
teamCounts = [1, 1]
teamSize = 3

userList = []
with open(handles, 'r') as file:
    for line in file:
        line = line.strip()
        userList.append(line)

df = team.createDF(userList)
rdf = df.copy()

for teamCount in teamCounts:
    teams, rdf = team.assemble(df, rdf, teamCount, teamSize, verbose=False)
    print(json.dumps(teams, indent=2))
    with open('bestTeams.txt', 'w') as file: file.write(teams_json)


# Restart
teamCounts = [2]
rdf = df.copy()

for teamCount in teamCounts:
    teams, rdf = team.assemble(df, rdf, teamCount, teamSize, verbose=False)
    print(json.dumps(teams, indent=2))
    with open('bestTeams.txt', 'w') as file: file.write(teams_json)