player_scores={}
with open("scores.csv","r") as f:
    for line in f:
        player,_,score=line.split(",")
        score=int(score.strip())
        if player in player_scores:
            player_scores[player].append(score)
        else:
            player_scores[player] = [score]
print(player_scores)
for player,score_list in player_scores.items():
    min_value=min(score_list)
    max_value=max(score_list)
    avg_score=sum(score_list)/len(score_list)
    print(f"{player}==> Min:{min_value},Max:{max_value},Average={avg_score}")

