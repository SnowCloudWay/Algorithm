def solution(spell, dic):
    for d in dic:
        if sorted(list(d)) == sorted(spell):
            return 1
    return 2