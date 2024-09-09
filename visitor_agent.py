import rclpy
from rclpy.node import Node

class VisitorAgent(Node):
    def __init__(self, name, destination):
        super().__init__(name)
        self.name=name
        self.destination = destination

    def meet_ci_agent(self, ci_agent):
        self.get_logger().info(f"Meeting {ci_agent} for escort to {self.destination}.")
        ci_agent.escort_visitor(self.name, self.destination)
