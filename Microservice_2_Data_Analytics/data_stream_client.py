from __future__ import print_function

import grpc
import data_stream_pb2
import data_stream_pb2_grpc
import time
from time import perf_counter


total_number_of_must_plays_val = [0,0,0,0]

all_metascores_of_nintendo_exclusives_list = []
all_metascores_of_playstation_exclusives_list = []
all_metascores_of_xbox_exclusives_list = []
all_metascores_of_pc_first_party_titles_list = []

avg_metascore_of_exclusives_val = [0,0,0]

most_loved_genre_vals = ['','','','',]

most_loved_genre_on_playstation_dict = {}
most_loved_genre_on_xbox_dict = {}
most_loved_genre_on_nintendo_dict = {}
most_loved_genre_on_pc_dict = {}


lowest_scoring_metacritic_game_per_platform_val = ['no console released yet' , "",
 'no console released yet' , "", 'no console released yet' ,
  "", 'no console released yet' , ""]

current_date = ''

start = perf_counter()


def guide_list_features(stub):

    game = data_stream_pb2.Game()
    features = stub.ListFeatures(game)

    for feature in features:
        total_number_of_must_plays(feature)
        lowest_scoring_metacritic_game(feature)
        most_loved_genres(feature)
        avg_metascore_of_exclusives(feature)
        get_current_date(feature)



def get_current_date(feature):
    global current_date
    current_date = getattr(feature, 'releaseDate')



def total_number_of_must_plays(feature):
    global total_number_of_must_plays_val

    platform = getattr(feature, 'platform')

    if (platform == 'PS' or platform == 'PS2' or platform == 'PS3' or platform == 'PS4') and (getattr(feature, 'metascore') >= 90):
        total_number_of_must_plays_val[0] += 1

    elif (platform == 'XBOX' or platform == 'X360' or platform == 'XONE') and (getattr(feature, 'metascore') >= 90):
        total_number_of_must_plays_val[1] += 1

    elif (platform == 'WII' or platform == 'Switch' or platform == 'WIIU' or platform == 'N64' or platform == 'GC') and (getattr(feature, 'metascore') >= 90):
        total_number_of_must_plays_val[2] += 1

    elif (platform == 'PC') and (getattr(feature, 'metascore') >= 90):
        total_number_of_must_plays_val[3] += 1



def avg_metascore_of_exclusives(feature):
    global all_metascores_of_nintendo_exclusives_list
    global all_metascores_of_playstation_exclusives_list
    global all_metascores_of_xbox_exclusives_list



    global start

    end = perf_counter()
    rolling = end - start

    if rolling >= 300:

        if getattr(feature, 'publisher') == "Nintendo":
            del all_metascores_of_nintendo_exclusives_list[0]

        elif ((getattr(feature, 'publisher') == "Sony Online Entertainment") or (getattr(feature, 'publisher') == "Sony Interactive Entertainment") or (getattr(feature, 'publisher') == "SCEA") or (getattr(feature, 'publisher') == "SCEE")) and (getattr(feature, 'platform') != "PC"):
            del all_metascores_of_playstation_exclusives_list[0]

        elif (getattr(feature, 'publisher') == "Microsoft Game Studios") and (getattr(feature, 'platform') != "PC"):
            del all_metascores_of_xbox_exclusives_list[0]



        # for i in range(0,10):
        #     all_metascores_of_nintendo_exclusives_list.remove(i)
        #     all_metascores_of_playstation_exclusives_list.remove(i)
        #     all_metascores_of_xbox_exclusives_list.remove(i)

    global avg_metascore_of_exclusives_val

    if getattr(feature, 'publisher') == "Nintendo":
        all_metascores_of_nintendo_exclusives_list.append(int(getattr(feature, 'metascore')))
        avg_metascore_of_exclusives_val[0] = round(sum(all_metascores_of_nintendo_exclusives_list) / len(all_metascores_of_nintendo_exclusives_list))

    elif ((getattr(feature, 'publisher') == "Sony Online Entertainment") or (getattr(feature, 'publisher') == "Sony Interactive Entertainment") or (getattr(feature, 'publisher') == "SCEA") or (getattr(feature, 'publisher') == "SCEE")) and (getattr(feature, 'platform') != "PC"):
        all_metascores_of_playstation_exclusives_list.append(int(getattr(feature, 'metascore')))
        avg_metascore_of_exclusives_val[1] = round(sum(all_metascores_of_playstation_exclusives_list) / len(all_metascores_of_playstation_exclusives_list))

    elif (getattr(feature, 'publisher') == "Microsoft Game Studios") and (getattr(feature, 'platform') != "PC"):
        all_metascores_of_xbox_exclusives_list.append(int(getattr(feature, 'metascore')))
        avg_metascore_of_exclusives_val[2] = round(sum(all_metascores_of_xbox_exclusives_list) / len(all_metascores_of_xbox_exclusives_list))



def most_loved_genres(feature):
    global most_loved_genre_vals

    global most_loved_genre_on_playstation_dict
    global most_loved_genre_on_xbox_dict
    global most_loved_genre_on_nintendo_dict
    global most_loved_genre_on_pc_dict

    game_genre = str(getattr(feature, 'genre'))
    game_metascore = int(getattr(feature, 'metascore'))
    platform = getattr(feature, 'platform')

    if (platform == 'PS' or platform == 'PS2' or platform == 'PS3' or platform == 'PS4') and (game_metascore >= 90):

        if game_genre in most_loved_genre_on_playstation_dict:
            most_loved_genre_on_playstation_dict[game_genre] += 1

        else:
            most_loved_genre_on_playstation_dict[game_genre] = 1

        if bool(most_loved_genre_on_playstation_dict) != False:
            most_loved_genre_vals[0] = max(most_loved_genre_on_playstation_dict,
            key=most_loved_genre_on_playstation_dict.get)


    elif (platform == 'XBOX' or platform == 'X360' or platform == 'XONE') and (game_metascore >= 90):

        if game_genre in most_loved_genre_on_xbox_dict:
            most_loved_genre_on_xbox_dict[game_genre] += 1

        else:
            most_loved_genre_on_xbox_dict[game_genre] = 1

        if bool(most_loved_genre_on_xbox_dict) != False:
            most_loved_genre_vals[1] = max(most_loved_genre_on_xbox_dict,
            key=most_loved_genre_on_xbox_dict.get)


    elif (platform == 'WII' or platform == 'WIIU' or platform == 'Switch' or platform == 'N64' or platform == "GC") and (game_metascore >= 90):

        if game_genre in most_loved_genre_on_nintendo_dict:
            most_loved_genre_on_nintendo_dict[game_genre] += 1

        else:
            most_loved_genre_on_nintendo_dict[game_genre] = 1

        if bool(most_loved_genre_on_nintendo_dict) != False:
            most_loved_genre_vals[2] = max(most_loved_genre_on_nintendo_dict,
            key=most_loved_genre_on_nintendo_dict.get)


    elif (platform == 'PC') and (game_metascore >= 90):

        if game_genre in most_loved_genre_on_pc_dict:
            most_loved_genre_on_pc_dict[game_genre] += 1

        else:
            most_loved_genre_on_pc_dict[game_genre] = 1

        if bool(most_loved_genre_on_pc_dict) != False:
            most_loved_genre_vals[3] = max(most_loved_genre_on_pc_dict,
            key=most_loved_genre_on_pc_dict.get)



def lowest_scoring_metacritic_game(feature):
    global lowest_scoring_metacritic_game_per_platform_val


    platform = getattr(feature, 'platform')

    if (platform == 'PS' or platform == 'PS2' or platform == 'PS3' or platform == 'PS4'):
        if lowest_scoring_metacritic_game_per_platform_val[1] == "":
            lowest_scoring_metacritic_game_per_platform_val[1] = str(getattr(feature, 'metascore'))
            lowest_scoring_metacritic_game_per_platform_val[0] = getattr(feature, 'name')


        elif getattr(feature, 'metascore') < int(lowest_scoring_metacritic_game_per_platform_val[1]):
            lowest_scoring_metacritic_game_per_platform_val[1] = str(getattr(feature, 'metascore'))
            lowest_scoring_metacritic_game_per_platform_val[0] = getattr(feature, 'name')


    elif (platform == 'XBOX' or platform == 'X360' or platform == 'XONE'):
        if lowest_scoring_metacritic_game_per_platform_val[3] == "":
            lowest_scoring_metacritic_game_per_platform_val[3] = str(getattr(feature, 'metascore'))
            lowest_scoring_metacritic_game_per_platform_val[2] = getattr(feature, 'name')


        elif getattr(feature, 'metascore') < int(lowest_scoring_metacritic_game_per_platform_val[3]):
            lowest_scoring_metacritic_game_per_platform_val[3] = str(getattr(feature, 'metascore'))
            lowest_scoring_metacritic_game_per_platform_val[2] = getattr(feature, 'name')



    elif (platform == 'WII' or platform == 'Switch' or platform == 'WIIU' or platform == 'N64' or platform == 'GC'):

        if lowest_scoring_metacritic_game_per_platform_val[5] == "":
            lowest_scoring_metacritic_game_per_platform_val[5] = str(getattr(feature, 'metascore'))
            lowest_scoring_metacritic_game_per_platform_val[4] = getattr(feature, 'name')


        elif getattr(feature, 'metascore') < int(lowest_scoring_metacritic_game_per_platform_val[5]):
            lowest_scoring_metacritic_game_per_platform_val[5] = str(getattr(feature, 'metascore'))
            lowest_scoring_metacritic_game_per_platform_val[4] = getattr(feature, 'name')


    elif (platform == 'PC'):

        if lowest_scoring_metacritic_game_per_platform_val[7] == "":
            lowest_scoring_metacritic_game_per_platform_val[7] = str(getattr(feature, 'metascore'))
            lowest_scoring_metacritic_game_per_platform_val[6] = getattr(feature, 'name')


        elif getattr(feature, 'metascore') < int(lowest_scoring_metacritic_game_per_platform_val[7]):
            lowest_scoring_metacritic_game_per_platform_val[7] = str(getattr(feature, 'metascore'))
            lowest_scoring_metacritic_game_per_platform_val[6] = getattr(feature, 'name')


def send_data_to_web_server(stub):
    message = generate_message()
    message_send = stub.SendOneFeature(message)


def generate_message():

    message = data_stream_pb2.AnalysedData(
    analytic1 = total_number_of_must_plays_val,
    analytic2 = lowest_scoring_metacritic_game_per_platform_val,
    analytic3 = most_loved_genre_vals,
    analytic4 = avg_metascore_of_exclusives_val,
    date = str(current_date),
    analytic4a = all_metascores_of_nintendo_exclusives_list,
    analytic4b = all_metascores_of_playstation_exclusives_list,
    analytic4c = all_metascores_of_xbox_exclusives_list,
    )

    return message






def run():


    while True:

        with grpc.insecure_channel('data-stream-1-server:50051') as channel:
            stub = data_stream_pb2_grpc.dataStreamStub(channel)

                #print("-------------- ListFeatures --------------")
            guide_list_features(stub)
                #print("Total number of Must-Plays:",total_number_of_must_plays_val)
                #print("Average score of Nintendo First Part Titles:",avg_metascore_of_exclusives_val)
                #print("Lowest Metascore Game:", lowest_scoring_metacritic_game_per_platform_val[0])
                #print("Score:", lowest_scoring_metacritic_game_per_platform_val[1])
                #print("Most Loved PS4 Genre:", most_loved_genre_vals)

                #print("Dict:", most_loved_genre_on_playstation_dict)


        with grpc.insecure_channel('web-server:40051') as channel2:
            stub2 = data_stream_pb2_grpc.dataStreamStub(channel2)

            # print("-------------- Web Server --------------")
            send_data_to_web_server(stub2)





if __name__ == '__main__':
    run()
