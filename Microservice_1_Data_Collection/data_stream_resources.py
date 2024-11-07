import data_stream_pb2


def read_game_data():

    feature_list = []

    file = open("metacritic_games.csv", 'r')

    while True:
        line = file.readline().rstrip().split(',')

        if line[0] == '':
            break

        feature = data_stream_pb2.Game(
        name = line[0],
        platform = line[1],
        developer = line[2],
        publisher = line[3],
        genre = line[4],
        releaseDate = line[5],
        criticPositive = int(line[6]),
        criticNeutral = int(line[7]),
        criticNegative = int(line[8]),
        metascore = int(line[9]),
        )

        feature_list.append(feature)


    file.close()

    return feature_list
