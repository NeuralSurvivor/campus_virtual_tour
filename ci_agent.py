import rclpy
from rclpy.node import Node
from agent_communication import send_message, receive_message

class CIAgent(Node):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.current_location = 'Campus Entrance'
        self.destination = None
        self.visitor = None

    def escort_visitor(self, visitor, destination):
        self.visitor = visitor
        self.destination = destination
        # Simulate escorting to the building
        self.get_logger().info(f'Escorting {self.visitor} to {self.destination}.')
        # Request navigation from the BI agent
        self.request_navigation(self.destination)

    def request_navigation(self, building):
        send_message(self, building, 'navigation_request', {'visitor': self.visitor})

    def handle_bi_response(self, msg):
        response = receive_message(msg)
        if response['status'] == 'success':
            self.get_logger().info(f"Received path to host: {response['path']}")
        else:
            self.get_logger().info(f"Access denied by {response['bi_agent']}")
