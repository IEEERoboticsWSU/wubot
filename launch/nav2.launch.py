import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessStart
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node


def generate_launch_description():
    package_name = 'wubot'
    nav2_params = os.path.join(get_package_share_directory(
        package_name), 'config', 'nav2_params.yaml')
    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(
                package_name), 'launch', 'navigation_launch.py'
        )]), launch_arguments={'use_sim_time': 'false', 'params_file': nav2_params}.items()
    )

    return LaunchDescription([
        # Remap cmd_vel to cmd_vel_unstamped
        nav2
    ])
