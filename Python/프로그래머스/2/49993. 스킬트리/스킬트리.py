def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        filtered_skill = "".join([s for s in tree if s in skill])
        if skill.startswith(filtered_skill):
            answer += 1
    return answer