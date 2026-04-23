import grpc
from concurrent import futures
import random

import adivino_pb2
import adivino_pb2_grpc

class AdivinoServicer(adivino_pb2_grpc.AdivinoServicer):
    def Preguntar(self, request, context):
        print(f"Un mortal pregunta: '{request.pregunta}'")

        respuestas = [
            "Nada más no",
            "Obviooo",
            "Ok, mañana",
            "Pides mucho",
            "Pos ya que",
            "Asíi ess",
            "Mejor no te digo nada",
            "Sisisiisi"
        ]

        prediccion = random.choice(respuestas)

        return adivino_pb2.PrediccionReply(respuesta=prediccion)
    
def serve():
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    adivino_pb2_grpc.add_AdivinoServicer_to_server(AdivinoServicer(), servidor)
    servidor.add_insecure_port('[::]:50051')

    print("El Adivinadorchis está listo")
    servidor.start()
    servidor.wait_for_termination()

if __name__ == '__main__':
    serve()

        