from std_msgs.msg import String

def send_message(node, target, message_type, data):
    publisher = node.create_publisher(String, f'/{target}/{message_type}', 10)
    msg = String()
    msg.data = str(data)
    publisher.publish(msg)

def receive_message(msg):
    return eval(msg.data)  # Convert string back to dictionary
