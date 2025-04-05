from setuptools import find_packages, setup
import os
from glob import glob
from setuptools import setup


package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='youhans',
    maintainer_email='youhans@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	"draw_circle = my_robot_controller.draw_circle:main",
        	"test_node = my_robot_controller.my_first_node:main",
        	"pose = my_robot_controller.pose_subscriber:main",
        	"turtle_controller = my_robot_controller.turtle_controller:main",
        ],
    },
)
