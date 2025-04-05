#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim'
        ),
        # Node(
        #     package='turtlesim',
        #     namespace='turtlesim2',
        #     executable='turtlesim_node',
        #     name='sim'
        # ),
        # Node(
        #     package='my_robot_controller',
        #     executable='turtle_controller',
        #     name='mimic',
        #     remappings=[
        #         ('/input/pose', '/turtlesim1/turtle1/pose'),
        #         ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
        #     ]
        # )
        Node(
            package='my_robot_controller',
            executable='draw_circle',
            name='drawing',
            remappings=[
                ('/turtle1/cmd_vel', '/turtlesim1/turtle1/cmd_vel')
            ]
        ),
        Node(
            package='my_robot_controller',
            executable='pose',
            name='position',
            remappings=[
                ('/turtle1/pose', '/turtlesim1/turtle1/pose')
            ]
        )
    ])