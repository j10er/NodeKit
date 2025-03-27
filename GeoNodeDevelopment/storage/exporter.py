import bpy
from pprint import pprint
from .data import Data, NodeTreeData, NodeData, SocketData


def export_groups():
    groups = bpy.data.node_groups
    node = groups[0].nodes[2]
    # print("uuid" in node)
    pprint(groups[0].__dict__)
    nodedata = NodeData(node)
    # pprint(nodedata.__dict__)
