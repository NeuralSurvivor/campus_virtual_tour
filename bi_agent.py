import rclpy
from rclpy.node import Node
from agent_communication import send_message, receive_message

class BIAgent(Node):
    def __init__(self, name, building_map):
        super().__init__(name)
        self.building_map = building_map
        self.current_location = 'Building Entrance'

    def provide_navigation(self, msg):
        request = receive_message(msg)
        visitor = request['visitor']
        # Check if visitor is authorized
        if self.is_authorized(visitor):
            path = self.get_navigation_path()
            send_message(self, 'CI Agent', 'navigation_response', {'status': 'success', 'path': path})
        else:
            send_message(self, 'CI Agent', 'navigation_response', {'status': 'denied'})

    def get_navigation_path(self):
        # Logic for pathfinding within the building map
        return ['Building Entrance', 'Host Location']

    def is_authorized(self, visitor):
        # Check visitor's authorization to access the building
        return True
