import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    package_name = 'wubot'
    imu_params_file = os.path.join(get_package_share_directory(
        package_name), 'config', 'imu_params.yaml')
    return LaunchDescription([

        Node(
            package='bno055',
            executable='bno055',
            output='screen',
            parameters=[{
                imu_params_file
            }]
        )
    ])
