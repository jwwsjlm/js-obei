# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import obei_pb2 as obei__pb2


class GreeterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.obeiHKIIUU9O618PPTHPM = channel.unary_unary(
                '/obei.Greeter/obeiHKIIUU9O618PPTHPM',
                request_serializer=obei__pb2.jsStr.SerializeToString,
                response_deserializer=obei__pb2.ret.FromString,
                )


class GreeterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def obeiHKIIUU9O618PPTHPM(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'obeiHKIIUU9O618PPTHPM': grpc.unary_unary_rpc_method_handler(
                    servicer.obeiHKIIUU9O618PPTHPM,
                    request_deserializer=obei__pb2.jsStr.FromString,
                    response_serializer=obei__pb2.ret.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'obei.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def obeiHKIIUU9O618PPTHPM(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/obei.Greeter/obeiHKIIUU9O618PPTHPM',
            obei__pb2.jsStr.SerializeToString,
            obei__pb2.ret.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)