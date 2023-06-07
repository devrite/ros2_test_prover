import os
import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rcl_interfaces.msg import ParameterDescriptor

def main():

    rclpy.init(args=['--ros-args',
                     '-p', 'ns1.param1:=true',
                     '-p', 'ns1.param2:=true',
                     '-p', 'ns1.param3:=true',
                     '-p', 'ns1.param4:=true',
                     '-p', 'ns1.param5:=true',
                     '-p', 'ns1.param6:=true',
                     '-p', 'ns1.param7:=true',
                     '-p', 'ns1.param8:=true',
                     '-p', 'ns1.param9:=true',
                     '-p', 'ns1.param10:=true'])
    node = Node('paramnode' + str(os.getpid()))
    node.declare_parameters(namespace='ns1', parameters=[
        ('param1', Parameter.Type.BOOL, ParameterDescriptor()),
        ('param2', False, ParameterDescriptor()),
        ('param3', False),
        ('param4', Parameter.Type.BOOL, ParameterDescriptor(type=Parameter.Type.BOOL.value)),
        ('param5', Parameter.Type.BOOL)
    ])

    node.declare_parameters(namespace='', parameters=[
        ('ns1.param6', Parameter.Type.BOOL, ParameterDescriptor()),
        ('ns1.param7', False, ParameterDescriptor()),
        ('param3', False),
        ('ns1.param9', Parameter.Type.BOOL, ParameterDescriptor(type=Parameter.Type.BOOL.value)),
        ('ns1.param10', Parameter.Type.BOOL)
    ])

    ns1_params = node.get_parameters_by_prefix(prefix='ns1')

    ns1_params = dict(map(lambda p:  (p[0], p[1].value), ns1_params.items()))
    print(ns1_params)

if __name__ == '__main__':
    main()