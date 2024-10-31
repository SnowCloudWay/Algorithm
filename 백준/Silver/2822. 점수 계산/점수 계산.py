import sys

scores = list(map(int, sys.stdin.read().splitlines()))
s_scores = sorted(scores)
scores_idx = []

sys.stdout.write(str(sum(s_scores[3:]))+'\n')
for num in s_scores[3:]:
    scores_idx.append(scores.index(num)+1)
print(' '.join(map(str, (sorted(scores_idx)))))
