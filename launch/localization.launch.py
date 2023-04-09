import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    package_name = 'wubot'
    ekf_params_file = os.path.join(get_package_share_directory(
        package_name), 'config', 'ekf.yaml')
    return LaunchDescription([

        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[ekf_params_file])
    ])
