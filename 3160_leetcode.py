def queryResults(limit, queries) -> list:
    result = []
    color_map = {}
    ball_map = {}

    for i, v in queries:
        if i in ball_map:
            prev_color = ball_map[i]
            color_map[prev_color] -= 1

            if color_map[prev_color] == 0:
                del color_map[prev_color]
        ball_map[i] = v

        color_map[v] = color_map.get(v, 0) + 1
        result.append(len(color_map))

    return result


queryResults(4)