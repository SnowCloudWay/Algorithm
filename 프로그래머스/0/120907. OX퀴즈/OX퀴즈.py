def solution(quiz):
    answer = []
    for i in quiz:
        quizSplit = i.split()
        if quizSplit[1] == "+":
            result = int(quizSplit[0]) + int(quizSplit[2])
        elif quizSplit[1] == "-":
            result = int(quizSplit[0]) - int(quizSplit[2])
        if result == int(quizSplit[4]):
            answer.append("O")
        else:
            answer.append("X")
    return answer