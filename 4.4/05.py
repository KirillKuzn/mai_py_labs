def bunny(start, finish, length):
    result = []

    def ways_possible(pos, way, jumps):
        if jumps == 0:
            if pos == finish:
                result.append(way[:])
            return
        for next_pos in [pos + 1, pos - 1, pos + 3, pos - 3]:
            if next_pos != finish or jumps == 1:
                way.append(next_pos)
                ways_possible(next_pos, way, jumps - 1)
                way.pop()

    ways_possible(start, [start], length)
    return result


def main():
    """Путешествие зайки"""
    
    result = bunny(13, 17, 2)
    print(*result, sep="\n")

    result = bunny(7, 10, 3)
    print(*result, sep="\n")


if __name__ == "__main__":
    main()
