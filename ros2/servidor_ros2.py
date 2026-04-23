import rclpy
from rclpy.node import Node
import random

from example_interfaces.srv import SetBool

class NodoAdivino(Node):
    def __init__(self):
        super().__init__('servidor_adivinadorchis')
        self.srv = self.create_service(SetBool, 'hacer_pregunta', self.responder_callback)
        self.get_logger().info('El Nodo Adivinadorchis está listo...')

    def responder_callback(self, request, response):
        if request.data == True:
            self.get_logger().info("Se ha hecho una pregunta")
            
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

            response.message = random.choice(respuestas)
            response.success = True
            
        return response

def main(args=None):
    rclpy.init(args=args)
    nodo_adivino = NodoAdivino()
    rclpy.spin(nodo_adivino)
    rclpy.shutdown()

if __name__ == '__main__':
    main()