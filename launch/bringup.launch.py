import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg_dir = get_package_share_directory('my_robot_controller')
    nav2_dir = get_package_share_directory('nav2_bringup')

    return LaunchDescription([
        # CAN 브릿지 실행
        Node(
            package='my_robot_controller',
            executable='can_bridge_node',
            output='screen'
        ),
        # Nav2 네비게이션 실행
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(nav2_dir, 'launch', 'navigation_launch.py')),
            launch_arguments={'params_file': os.path.join(pkg_dir, 'params', 'nav2_mppi_params.yaml')}.items()
        )
    ])