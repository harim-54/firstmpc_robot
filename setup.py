from setuptools import setup
import os
from glob import glob

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Launch 파일 설치 경로
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # Params 파일 설치 경로
        (os.path.join('share', package_name, 'params'), glob('params/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    description='RMD-X8 and MD400T Controller',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            # 터미널에서 실행할 이름 = 패키지폴더.파일이름:메인함수
            'can_bridge_node = my_robot_controller.can_bridge_node:main'
        ],
    },
)