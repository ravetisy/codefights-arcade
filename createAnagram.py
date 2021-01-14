def createAnagram(s, t):
    # s = sorted(s)
    # t = sorted(t)
    t_character_map = character_map(t)
    s_character_map = character_map(s)
    
    substitutions = 0
    for key in s_character_map.keys():
        if key not in t_character_map:
            substitutions += s_character_map[key]
        elif key in t_character_map.keys():
            diff = s_character_map[key] - t_character_map[key]
            if diff >= 0:
                substitutions += diff
    return substitutions


def character_map(s: str):
    map = dict()
    for character in s:
        if character in map:
            map[character] = map[character] + 1
        else:
            map[character] = 1
    return map
