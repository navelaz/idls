import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool

class NodoJugador(Node):
    def __init__(self):
        super().__init__('cliente_jugador')
        self.cliente = self.create_client(SetBool, 'hacer_pregunta')
        
        while not self.cliente.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Buscando al Gran Adivinadorchis...')
            
        self.peticion = SetBool.Request()

    def preguntar(self):
        self.peticion.data = True
        self.future = self.cliente.call_async(self.peticion)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)
    nodo_jugador = NodoJugador()
    
    input("Piensa en una pregunta de Sí/No y presiona ENTER ")
    
    nodo_jugador.get_logger().info('Adivinadorchis pensando...')
    respuesta = nodo_jugador.preguntar()
    
    nodo_jugador.get_logger().info(f'El destino dice: {respuesta.message}')
    
    nodo_jugador.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()