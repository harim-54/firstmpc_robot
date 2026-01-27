import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
import can
import struct

class TrackedRobotCanBridge(Node):
    def __init__(self):
        super().__init__('can_bridge_node')
        
        # 파라미터 설정 (실제 로봇 수치로 수정)
        self.declare_parameter('track_width', 0.5)
        self.declare_parameter('wheel_radius', 0.1)
        self.L = self.get_parameter('track_width').get_value()
        self.R = self.get_parameter('wheel_radius').get_value()

        # CAN 버스 설정
        try:
            self.bus = can.interface.Bus(channel='can0', bustype='socketcan')
            self.get_logger().info("CAN Bus connected.")
        except Exception as e:
            self.get_logger().error(f"CAN Connection Failed: {e}")

        # 구독자 설정
        self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_callback, 10)
        self.create_subscription(Float32, 'flipper_pos', self.flipper_callback, 10)

    def cmd_vel_callback(self, msg):
        # 주행 제어 (RMD-X8)
        v_l = msg.linear.x - (msg.angular.z * self.L / 2.0)
        v_r = msg.linear.x + (msg.angular.z * self.L / 2.0)
        dps_l = (v_l / (2 * 3.14159 * self.R)) * 360.0
        dps_r = (v_r / (2 * 3.14159 * self.R)) * 360.0

        self.send_rmd_velocity(0x141, dps_l)
        self.send_rmd_velocity(0x142, dps_r)

    def flipper_callback(self, msg):
        # 플리퍼 제어 (MD400T)
        self.send_md_position(0x183, msg.data)

    def send_rmd_velocity(self, can_id, dps):
        speed_value = int(dps * 100)
        data = [0xA2, 0x00, 0x00, 0x00] + list(struct.pack('<i', speed_value))
        try: self.bus.send(can.Message(arbitration_id=can_id, data=data, is_extended_id=False))
        except: pass

    def send_md_position(self, can_id, degree):
        pos_value = int(degree * 10)
        data = [0x24, 0x00] + list(struct.pack('<h', pos_value)) + [0x00]*4
        try: self.bus.send(can.Message(arbitration_id=can_id, data=data, is_extended_id=False))
        except: pass

def main(args=None):
    rclpy.init(args=args)
    node = TrackedRobotCanBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()