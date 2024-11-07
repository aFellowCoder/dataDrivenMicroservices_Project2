from __future__ import print_function
from datetime import datetime

import grpc
import data_stream2_pb2
import data_stream2_pb2_grpc
import time
from time import perf_counter


total_number_game_sales_japan_val = 0.0

avg_sales_of_shooters_val = 0.0
shooter_games_list = []

most_sales_kid_friendly_vals = ["",""]
most_sales_kid_friendly_dict = {}

best_year_in_sales_vals = ["",""]
best_year_in_sales_dict = {}


current_date = ''

start = perf_counter()


def guide_list_features(stub):

    GameSales = data_stream2_pb2.GameSales()
    features = stub.ListFeatures(GameSales)

    for feature in features:
        total_number_game_sales_japan(feature)
        best_year_in_sales(feature)
        most_sales_kid_friendly(feature)
        avg_games_sales_of_shooters(feature)
        get_current_date(feature)



def get_current_date(feature):
    global current_date
    current_date = getattr(feature, 'releaseYear')



def total_number_game_sales_japan(feature):
    global total_number_game_sales_japan_val

    jpSales = round((float(getattr(feature, 'jpSales'))), 2)

    total_number_game_sales_japan_val += jpSales





def avg_games_sales_of_shooters(feature):
    global shooter_games_list
    global avg_sales_of_shooters_val

    global start

    end = perf_counter()
    rolling = end - start

    if rolling >= 300 and getattr(feature, 'genre') == "Shooter":
            del shooter_games_list[0]


    if getattr(feature, 'genre') == "Shooter":
        shooter_games_list.append(round((float(getattr(feature, 'globalSales'))),2))
        avg_sales_of_shooters_val = round((sum(shooter_games_list) / len(shooter_games_list)),2)





def most_sales_kid_friendly(feature):

    global most_sales_kid_friendly_vals
    global most_sales_kid_friendly_dict
    
    
    genre = getattr(feature, 'genre')
    rating = getattr(feature, 'rating')
    globalSales = round((getattr(feature, 'globalSales')), 2)

    if (rating == 'E'):

        if genre in most_sales_kid_friendly_dict:
            most_sales_kid_friendly_dict[genre] += globalSales

        else:
            most_sales_kid_friendly_dict[genre] = globalSales

        if bool(most_sales_kid_friendly_dict) != False:
            most_sales_kid_friendly_vals[0] = max(most_sales_kid_friendly_dict,
key=most_sales_kid_friendly_dict.get)
            most_sales_kid_friendly_vals[1] = str(max(most_sales_kid_friendly_dict.values()))

            




def best_year_in_sales(feature):

    global best_year_in_sales_vals
    global best_year_in_sales_dict
    
    
    salesGlobal = round((getattr(feature, 'globalSales')), 2)
    releaseYear = getattr(feature, 'releaseYear')

    if releaseYear in best_year_in_sales_dict:
        best_year_in_sales_dict[releaseYear] += salesGlobal

    else:
        best_year_in_sales_dict[releaseYear] = salesGlobal

    if bool(best_year_in_sales_dict) != False:
        best_year_in_sales_vals[0] = max(best_year_in_sales_dict,
        key=best_year_in_sales_dict.get)
        best_year_in_sales_vals[1] = str(max(best_year_in_sales_dict.values()))
    



def send_data_to_web_server(stub):
    message = generate_message()
    message_send = stub.SendOneFeature(message)


def generate_message():

    
    message = data_stream2_pb2.AnalysedData(
    analytic1 = total_number_game_sales_japan_val,
    analytic2 = shooter_games_list,
    analytic3 = most_sales_kid_friendly_vals,
    analytic4 = best_year_in_sales_vals,
    date = current_date,
    analytic2b = avg_sales_of_shooters_val,
    )
    


    return message
    
    
#Serverless function (for kubeless part) to test and see if the the rolling average is actually for 3 minutes of if it is longer due to whatever issue. And to see how much of a time difference there is. It would be added to line 39 of this file (in the for loop where the other analytics are called)

def rollongAverageTest(feature):
    
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    end = perf_counter()
    rolling = end - start

    if rolling >= 300 and getattr(feature, 'genre') == "Shooter":
            newTime = datetime.now()
            current_time2 = newTime.strftime("%H:%M:%S")
            
            return [current_time, current_time2]
            
            
            
        
	

	






def run():


    while True:

        with grpc.insecure_channel('data-stream-2-server:50059') as channel:
            stub = data_stream2_pb2_grpc.dataStream2Stub(channel)


            guide_list_features(stub)


        with grpc.insecure_channel('web-server:40051') as channel2:
            stub2 = data_stream2_pb2_grpc.dataStream2Stub(channel2)


            send_data_to_web_server(stub2)





if __name__ == '__main__':
    run()
