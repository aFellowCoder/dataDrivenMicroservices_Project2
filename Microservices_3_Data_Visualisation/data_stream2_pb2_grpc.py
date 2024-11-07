# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import data_stream2_pb2 as data__stream2__pb2


class dataStream2Stub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListFeatures = channel.unary_stream(
                '/data_stream2.dataStream2/ListFeatures',
                request_serializer=data__stream2__pb2.HelloRequest.SerializeToString,
                response_deserializer=data__stream2__pb2.GameSales.FromString,
                )
        self.SendFeatures = channel.stream_unary(
                '/data_stream2.dataStream2/SendFeatures',
                request_serializer=data__stream2__pb2.GameSales.SerializeToString,
                response_deserializer=data__stream2__pb2.HelloRequest.FromString,
                )
        self.SendOneFeature = channel.unary_unary(
                '/data_stream2.dataStream2/SendOneFeature',
                request_serializer=data__stream2__pb2.AnalysedData.SerializeToString,
                response_deserializer=data__stream2__pb2.HelloRequest.FromString,
                )


class dataStream2Servicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListFeatures(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendFeatures(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendOneFeature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_dataStream2Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListFeatures': grpc.unary_stream_rpc_method_handler(
                    servicer.ListFeatures,
                    request_deserializer=data__stream2__pb2.HelloRequest.FromString,
                    response_serializer=data__stream2__pb2.GameSales.SerializeToString,
            ),
            'SendFeatures': grpc.stream_unary_rpc_method_handler(
                    servicer.SendFeatures,
                    request_deserializer=data__stream2__pb2.GameSales.FromString,
                    response_serializer=data__stream2__pb2.HelloRequest.SerializeToString,
            ),
            'SendOneFeature': grpc.unary_unary_rpc_method_handler(
                    servicer.SendOneFeature,
                    request_deserializer=data__stream2__pb2.AnalysedData.FromString,
                    response_serializer=data__stream2__pb2.HelloRequest.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'data_stream2.dataStream2', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class dataStream2(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListFeatures(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/data_stream2.dataStream2/ListFeatures',
            data__stream2__pb2.HelloRequest.SerializeToString,
            data__stream2__pb2.GameSales.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendFeatures(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/data_stream2.dataStream2/SendFeatures',
            data__stream2__pb2.GameSales.SerializeToString,
            data__stream2__pb2.HelloRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendOneFeature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data_stream2.dataStream2/SendOneFeature',
            data__stream2__pb2.AnalysedData.SerializeToString,
            data__stream2__pb2.HelloRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)