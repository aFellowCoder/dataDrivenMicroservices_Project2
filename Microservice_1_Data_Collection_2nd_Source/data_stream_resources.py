import data_stream2_pb2


def read_game_data():

    feature_list = []

    file = open("Video_Games_Sales_as_at_22_Dec_2016.csv", 'r')

    while True:
        line = file.readline().rstrip().split(',')

        if line[0] == '':
            break


        feature = data_stream2_pb2.GameSales(
        name = line[0],
        platform = line[1],
        releaseYear = line[2],
        genre = line[3],
        americaSales = float(line[4]),
        euSales = float(line[5]),
        jpSales = float(line[6]),
        otherSales = float(line[7]),
        globalSales = float(line[8]),
        rating = line[9],
        )

        feature_list.append(feature)


    file.close()

    return feature_list
