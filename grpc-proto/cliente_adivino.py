import grpc
import adivino_pb2
import adivino_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as canal:
        stub = adivino_pb2_grpc.AdivinoStub(canal)

        mi_pregunta = "¿Será que pasé el CENEVAL?"
        print(f"Yo: {mi_pregunta}")

        peticion = adivino_pb2.PreguntaRequest(pregunta=mi_pregunta)
        respuesta = stub.Preguntar(peticion)

        print(f"El adivinadorchis dice: {respuesta.respuesta}")

if __name__ == '__main__':
    run()