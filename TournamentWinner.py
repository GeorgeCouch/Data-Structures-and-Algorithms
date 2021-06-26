def tournamentWinner(competitions, results):
    teamScores = {}
    for i in range(len(competitions)):
        newResult = results[i]
        if(newResult == 0):
            newResult = 1
        elif(newResult == 1):
            newResult = 0
        teamScores[competitions[i][newResult]] = 0
        print(teamScores)
    return ""

competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0,0,1]

print(competitions[0][1])
tournamentWinner(competitions, results)
