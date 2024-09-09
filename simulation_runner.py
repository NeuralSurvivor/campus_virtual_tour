import rclpy
from ci_agent import CIAgent
from bi_agent import BIAgent
from visitor_agent import VisitorAgent

def run_simulation():
    rclpy.init()

    # Initialize agents
    ci_agent = CIAgent('ci_agent_1')
    bi_agent = BIAgent('bi_agent_1', {'Building_Entrance': 'Host Location'})
    visitor = VisitorAgent('visitor_1', 'Building_1_Entrance')
    # Simulate visitor meeting CI agent
    visitor.meet_ci_agent(ci_agent)
    visitor = VisitorAgent('visitor_2', 'Building_2_Entrance')
    # Simulate visitor meeting CI agent
    visitor.meet_ci_agent(ci_agent)
    #rclpy.spin(ci_agent)
    rclpy.shutdown()

if __name__ == '__main__':
    run_simulation()
