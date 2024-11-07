from concurrent import futures
import logging
import math
import time

import grpc
import data_stream2_pb2
import data_stream2_pb2_grpc
import data_stream_resources

ITERATOR = 0

class dataStreamServicer2(data_stream2_pb2_grpc.dataStream2Servicer):

    def __init__(self):
        self.db = data_stream_resources.read_game_data()

    def ListFeatures(self, request, context):


        global ITERATOR

        count = 0
        for i in range(0,10):

            yield self.db[ITERATOR]
            ITERATOR+=1
        time.sleep(2)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_stream2_pb2_grpc.add_dataStream2Servicer_to_server(dataStreamServicer2(), server)
    server.add_insecure_port('[::]:50059')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
