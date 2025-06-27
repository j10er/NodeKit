"""
Blender Node Attributes Dictionary

This module contains the attributes dictionary for Blender node classes
including Node, NodeSocket, NodeTree, and related interface items.

The structure follows the format: [type, default_value] for each attribute.
"""

SOCKET_TYPES = {}

DEFAULTS = {
    "Element": [
        {},
        {
            "Node": [
                {
                    "bl_idname": ["STRING", ""],
                    "color": [
                        "LIST",
                        [0.6079999804496765, 0.6079999804496765, 0.6079999804496765],
                    ],
                    "height": ["FLOAT", 100],
                    "label": ["STRING", ""],
                    "location": ["LIST", [0, 0]],
                    "mute": ["BOOLEAN", False],
                    "name": ["STRING", ""],
                    "use_custom_color": ["BOOLEAN", False],
                    "warning_propagation": ["STRING", "ALL"],
                    "width": ["FLOAT", 140],
                },
                {
                    "GeometryNodeAccumulateField": [
                        {"data_type": ["STRING", "FLOAT"], "domain": ["STRING", ""]}
                    ],
                    "GeometryNodeAttributeDomainSize": [{"component": ["STRING", ""]}],
                    "GeometryNodeAttributeStatistic": [
                        {"data_type": ["STRING", "FLOAT"], "domain": ["STRING", ""]}
                    ],
                    "GeometryNodeBake": [{}],
                    "GeometryNodeBlurAttribute": [{"data_type": ["STRING", ""]}],
                    "GeometryNodeBoundBox": [{}],
                    "GeometryNodeCaptureAttribute": [
                        {"capture_items": ["NODE_ITEMS", []]}
                    ],
                    "GeometryNodeCollectionInfo": [{"transform_space": ["STRING", ""]}],
                    "GeometryNodeConvexHull": [{}],
                    "GeometryNodeCornersOfEdge": [{}],
                    "GeometryNodeCornersOfFace": [{}],
                    "GeometryNodeCornersOfVertex": [{}],
                    "GeometryNodeCurveArc": [{"mode": ["STRING", ""]}],
                    "GeometryNodeCurveEndpointSelection": [{}],
                    "GeometryNodeCurveHandleTypeSelection": [
                        {"handle_type": ["STRING", ""], "mode": ["STRING", ""]}
                    ],
                    "GeometryNodeCurveLength": [{}],
                    "GeometryNodeCurveOfPoint": [{}],
                    "GeometryNodeCurvePrimitiveBezierSegment": [
                        {"mode": ["STRING", ""]}
                    ],
                    "GeometryNodeCurvePrimitiveCircle": [{"mode": ["STRING", ""]}],
                    "GeometryNodeCurvePrimitiveLine": [{"mode": ["STRING", ""]}],
                    "GeometryNodeCurvePrimitiveQuadrilateral": [{}],
                    "GeometryNodeCurveQuadraticBezier": [{}],
                    "GeometryNodeCurveSetHandles": [
                        {"handle_type": ["STRING", ""], "mode": ["STRING", ""]}
                    ],
                    "GeometryNodeCurveSpiral": [{}],
                    "GeometryNodeCurveSplineType": [{"spline_type": ["STRING", ""]}],
                    "GeometryNodeCurveStar": [{}],
                    "GeometryNodeCurveToMesh": [{}],
                    "GeometryNodeCurveToPoints": [{"mode": ["STRING", ""]}],
                    "GeometryNodeCurvesToGreasePencil": [{}],
                    "GeometryNodeCustomGroup": [{"node_tree": ["NODE_TREE", ""]}],
                    "GeometryNodeDeformCurvesOnSurface": [{}],
                    "GeometryNodeDeleteGeometry": [
                        {"domain": ["STRING", ""], "mode": ["STRING", ""]}
                    ],
                    "GeometryNodeDistributePointsInGrid": [{"mode": ["STRING", ""]}],
                    "GeometryNodeDistributePointsInVolume": [{"mode": ["STRING", ""]}],
                    "GeometryNodeDistributePointsOnFaces": [
                        {"distribute_method": ["STRING", ""]}
                    ],
                    "GeometryNodeDualMesh": [{}],
                    "GeometryNodeDuplicateElements": [{"domain": ["STRING", ""]}],
                    "GeometryNodeEdgePathsToCurves": [{}],
                    "GeometryNodeEdgePathsToSelection": [{}],
                    "GeometryNodeEdgesOfCorner": [{}],
                    "GeometryNodeEdgesOfVertex": [{}],
                    "GeometryNodeEdgesToFaceGroups": [{}],
                    "GeometryNodeExtrudeMesh": [{"mode": ["STRING", ""]}],
                    "GeometryNodeFaceOfCorner": [{}],
                    "GeometryNodeFieldAtIndex": [
                        {"data_type": ["STRING", ""], "domain": ["STRING", ""]}
                    ],
                    "GeometryNodeFieldOnDomain": [
                        {"data_type": ["STRING", ""], "domain": ["STRING", ""]}
                    ],
                    "GeometryNodeFillCurve": [{"mode": ["STRING", ""]}],
                    "GeometryNodeFilletCurve": [{"mode": ["STRING", ""]}],
                    "GeometryNodeFlipFaces": [{}],
                    "GeometryNodeForeachGeometryElementInput": [
                        {"paired_output": ["NODE", ""]}
                    ],
                    "GeometryNodeForeachGeometryElementOutput": [
                        {
                            "domain": ["STRING", ""],
                            "main_items": ["NODE_ITEMS", []],
                            "generation_items": [
                                "NODE_ITEMS",
                                [["Geometry", "GEOMETRY"]],
                            ],
                            "input_items": ["NODE_ITEMS", []],
                        },
                    ],
                    "GeometryNodeGeometryToInstance": [{}],
                    "GeometryNodeGetNamedGrid": [{"data_type": ["STRING", ""]}],
                    "GeometryNodeGizmoDial": [{"color_id": ["STRING", ""]}],
                    "GeometryNodeGizmoLinear": [
                        {"color_id": ["STRING", ""], "draw_style": ["STRING", ""]}
                    ],
                    "GeometryNodeGizmoTransform": [
                        {
                            "use_rotation_x": ["BOOLEAN", False],
                            "use_rotation_y": ["BOOLEAN", False],
                            "use_rotation_z": ["BOOLEAN", False],
                            "use_translation_x": ["BOOLEAN", False],
                            "use_translation_y": ["BOOLEAN", False],
                            "use_translation_z": ["BOOLEAN", False],
                            "use_scale_x": ["BOOLEAN", False],
                            "use_scale_y": ["BOOLEAN", False],
                            "use_scale_z": ["BOOLEAN", False],
                        }
                    ],
                    "GeometryNodeGreasePencilToCurves": [{}],
                    "GeometryNodeGridToMesh": [{}],
                    "GeometryNodeGroup": [{"node_tree": ["NODE_TREE", ""]}],
                    "GeometryNodeImageInfo": [{}],
                    "GeometryNodeImageTexture": [
                        {"extension": ["STRING", ""], "interpolation": ["STRING", ""]}
                    ],
                    "GeometryNodeImportOBJ": [{}],
                    "GeometryNodeImportPLY": [{}],
                    "GeometryNodeImportSTL": [{}],
                    "GeometryNodeIndexOfNearest": [{}],
                    "GeometryNodeIndexSwitch": [
                        {
                            "data_type": ["STRING", ""],
                            "index_switch_items": ["NODE_ITEMS", []],
                        }
                    ],
                    "GeometryNodeInputActiveCamera": [{}],
                    "GeometryNodeInputCollection": [
                        {"collection": ["COLLECTION", None]}
                    ],
                    "GeometryNodeInputCurveHandlePositions": [{}],
                    "GeometryNodeInputCurveTilt": [{}],
                    "GeometryNodeInputEdgeSmooth": [{}],
                    "GeometryNodeInputID": [{}],
                    "GeometryNodeInputImage": [{"image": ["IMAGE", None]}],
                    "GeometryNodeInputIndex": [{}],
                    "GeometryNodeInputInstanceRotation": [{}],
                    "GeometryNodeInputInstanceScale": [{}],
                    "GeometryNodeInputMaterial": [{"material": ["MATERIAL", None]}],
                    "GeometryNodeInputMaterialIndex": [{}],
                    "GeometryNodeInputMeshEdgeAngle": [{}],
                    "GeometryNodeInputMeshEdgeNeighbors": [{}],
                    "GeometryNodeInputMeshEdgeVertices": [{}],
                    "GeometryNodeInputMeshFaceArea": [{}],
                    "GeometryNodeInputMeshFaceIsPlanar": [{}],
                    "GeometryNodeInputMeshFaceNeighbors": [{}],
                    "GeometryNodeInputMeshIsland": [{}],
                    "GeometryNodeInputMeshVertexNeighbors": [{}],
                    "GeometryNodeInputNamedAttribute": [{"data_type": ["STRING", ""]}],
                    "GeometryNodeInputNamedLayerSelection": [{}],
                    "GeometryNodeInputNormal": [{}],
                    "GeometryNodeInputObject": [{"object": ["OBJECT", None]}],
                    "GeometryNodeInputPosition": [{}],
                    "GeometryNodeInputRadius": [{}],
                    "GeometryNodeInputSceneTime": [{}],
                    "GeometryNodeInputShadeSmooth": [{}],
                    "GeometryNodeInputShortestEdgePaths": [{}],
                    "GeometryNodeInputSplineCyclic": [{}],
                    "GeometryNodeInputSplineResolution": [{}],
                    "GeometryNodeInputTangent": [{}],
                    "GeometryNodeInstanceOnPoints": [{}],
                    "GeometryNodeInstanceTransform": [{}],
                    "GeometryNodeInstancesToPoints": [{}],
                    "GeometryNodeInterpolateCurves": [{}],
                    "GeometryNodeIsViewport": [{}],
                    "GeometryNodeJoinGeometry": [{}],
                    "GeometryNodeMaterialSelection": [{}],
                    "GeometryNodeMenuSwitch": [
                        {"data_type": ["STRING", ""], "enum_items": ["NODE_ITEMS", []]}
                    ],
                    "GeometryNodeMergeByDistance": [{"mode": ["STRING", ""]}],
                    "GeometryNodeMergeLayers": [{"mode": ["STRING", ""]}],
                    "GeometryNodeMeshBoolean": [
                        {"operation": ["STRING", ""], "solver": ["STRING", ""]}
                    ],
                    "GeometryNodeMeshCircle": [{"fill_type": ["STRING", ""]}],
                    "GeometryNodeMeshCone": [{"fill_type": ["STRING", ""]}],
                    "GeometryNodeMeshCube": [{}],
                    "GeometryNodeMeshCylinder": [{"fill_type": ["STRING", ""]}],
                    "GeometryNodeMeshFaceSetBoundaries": [{}],
                    "GeometryNodeMeshGrid": [{}],
                    "GeometryNodeMeshIcoSphere": [{}],
                    "GeometryNodeMeshLine": [
                        {"count_mode": ["STRING", ""], "mode": ["STRING", ""]}
                    ],
                    "GeometryNodeMeshToCurve": [{}],
                    "GeometryNodeMeshToDensityGrid": [{}],
                    "GeometryNodeMeshToPoints": [{"mode": ["STRING", ""]}],
                    "GeometryNodeMeshToSDFGrid": [{}],
                    "GeometryNodeMeshToVolume": [{"resolution_mode": ["STRING", ""]}],
                    "GeometryNodeMeshUVSphere": [{}],
                    "GeometryNodeObjectInfo": [{"transform_space": ["STRING", ""]}],
                    "GeometryNodeOffsetCornerInFace": [{}],
                    "GeometryNodeOffsetPointInCurve": [{}],
                    "GeometryNodePoints": [{}],
                    "GeometryNodePointsOfCurve": [{}],
                    "GeometryNodePointsToCurves": [{}],
                    "GeometryNodePointsToSDFGrid": [{}],
                    "GeometryNodePointsToVertices": [{}],
                    "GeometryNodePointsToVolume": [{"resolution_mode": ["STRING", ""]}],
                    "GeometryNodeProximity": [{"target_element": ["STRING", ""]}],
                    "GeometryNodeRaycast": [
                        {"data_type": ["STRING", ""], "mapping": ["STRING", ""]}
                    ],
                    "GeometryNodeRealizeInstances": [{}],
                    "GeometryNodeRemoveAttribute": [{"pattern_mode": ["STRING", ""]}],
                    "GeometryNodeRepeatInput": [{"paired_output": ["NODE", ""]}],
                    "GeometryNodeRepeatOutput": [
                        {
                            "repeat_items": ["NODE_ITEMS", [["Geometry", "GEOMETRY"]]],
                        }
                    ],
                    "GeometryNodeReplaceMaterial": [{}],
                    "GeometryNodeResampleCurve": [{}],
                    "GeometryNodeReverseCurve": [{}],
                    "GeometryNodeRotateInstances": [{}],
                    "GeometryNodeSDFGridBoolean": [{}],
                    "GeometryNodeSampleCurve": [{}],
                    "GeometryNodeSampleGrid": [{}],
                    "GeometryNodeSampleGridIndex": [{}],
                    "GeometryNodeSampleIndex": [{}],
                    "GeometryNodeSampleNearest": [{}],
                    "GeometryNodeSampleNearestSurface": [{}],
                    "GeometryNodeSampleUVSurface": [{}],
                    "GeometryNodeScaleElements": [{}],
                    "GeometryNodeScaleInstances": [{}],
                    "GeometryNodeSelfObject": [{}],
                    "GeometryNodeSeparateComponents": [{}],
                    "GeometryNodeSeparateGeometry": [{}],
                    "GeometryNodeSetCurveHandlePositions": [{}],
                    "GeometryNodeSetCurveNormal": [{}],
                    "GeometryNodeSetCurveRadius": [{}],
                    "GeometryNodeSetCurveTilt": [{}],
                    "GeometryNodeSetGeometryName": [{}],
                    "GeometryNodeSetID": [{}],
                    "GeometryNodeSetInstanceTransform": [{}],
                    "GeometryNodeSetMaterial": [{}],
                    "GeometryNodeSetMaterialIndex": [{}],
                    "GeometryNodeSetPointRadius": [{}],
                    "GeometryNodeSetPosition": [{}],
                    "GeometryNodeSetShadeSmooth": [{}],
                    "GeometryNodeSetSplineCyclic": [{}],
                    "GeometryNodeSetSplineResolution": [{}],
                    "GeometryNodeSimulationInput": [{"paired_output": ["NODE", ""]}],
                    "GeometryNodeSimulationOutput": [
                        {"state_items": ["NODE_ITEMS", []]}
                    ],
                    "GeometryNodeSortElements": [{}],
                    "GeometryNodeSplineLength": [{}],
                    "GeometryNodeSplineParameter": [{}],
                    "GeometryNodeSplitEdges": [{}],
                    "GeometryNodeSplitToInstances": [{}],
                    "GeometryNodeStoreNamedAttribute": [{}],
                    "GeometryNodeStoreNamedGrid": [{}],
                    "GeometryNodeStringJoin": [{}],
                    "GeometryNodeStringToCurves": [{}],
                    "GeometryNodeSubdivideCurve": [{}],
                    "GeometryNodeSubdivideMesh": [{}],
                    "GeometryNodeSubdivisionSurface": [{}],
                    "GeometryNodeSwitch": [{}],
                    "GeometryNodeTool3DCursor": [{}],
                    "GeometryNodeToolActiveElement": [{}],
                    "GeometryNodeToolFaceSet": [{}],
                    "GeometryNodeToolMousePosition": [{}],
                    "GeometryNodeToolSelection": [{}],
                    "GeometryNodeToolSetFaceSet": [{}],
                    "GeometryNodeToolSetSelection": [{}],
                    "GeometryNodeTransform": [{}],
                    "GeometryNodeTranslateInstances": [{}],
                    "GeometryNodeTriangulate": [{}],
                    "GeometryNodeTrimCurve": [{}],
                    "GeometryNodeUVPackIslands": [{}],
                    "GeometryNodeUVUnwrap": [{}],
                    "GeometryNodeVertexOfCorner": [{}],
                    "GeometryNodeViewer": [{}],
                    "GeometryNodeViewportTransform": [{}],
                    "GeometryNodeVolumeCube": [{}],
                    "GeometryNodeVolumeToMesh": [{}],
                    "GeometryNodeWarning": [{}],
                },
            ],
            "NodeSocket": [
                {"type": ["STRING", ""], "name": ["STRING", ""]},
                {
                    "VALUE": [{"default_value": ["FLOAT", 0]}],
                    "INT": [{"default_value": ["INT", 0]}],
                    "BOOLEANEAN": [{"default_value": ["BOOLEAN", False]}],
                    "VECTOR": [{"default_value": ["LIST", [0, 0, 0]]}],
                    "ROTATION": [{"default_value": ["LIST", [0, 0, 0]]}],
                    "MATRIX": [{}],
                    "STRINGING": [{"default_value": ["STRING", ""]}],
                    "RGBA": [{"default_value": ["LIST", [0, 0, 0, 1.0]]}],
                    "SHADER": [{"default_value": ["NONE", None]}],
                    "OBJECT": [{"default_value": ["NONE", None]}],
                    "IMAGE": [{"default_value": ["NONE", None]}],
                    "GEOMETRY": [{}],
                    "COLLECTION": [{"default_value": ["NONE", None]}],
                    "TEXTURE": [{"default_value": ["NONE", None]}],
                    "MATERIAL": [{"default_value": ["NONE", None]}],
                    "MENU": [{"default_value": ["NONE", None]}],
                },
            ],
            "NodeTree": [
                {
                    "name": ["STRING", ""],
                    "color_tag": ["STRING", "NONE"],
                    "default_group_node_width": ["INT", 140],
                    "description": ["STRING", ""],
                    "is_modifier": ["BOOLEAN", False],
                    "is_tool": ["BOOLEAN", False],
                }
            ],
            "NodeTreeInterfaceItem": [
                {
                    "item_type": ["STRING", "SOCKET"],
                    "name": ["STRING", ""],
                    "description": ["STRING", ""],
                },
                {
                    "NodeTreeInterfacePanel": [
                        {
                            "default_closed": ["BOOLEAN", False],
                        }
                    ],
                    "NodeTreeInterfaceSocket": [
                        {
                            "attribute_domain": ["STRING", "POINT"],
                            "default_attribute_name": ["STRING", ""],
                            "description": ["STRING", ""],
                            "force_non_field": ["BOOLEAN", False],
                            "hide_in_modifier": ["BOOLEAN", False],
                            "hide_value": ["BOOLEAN", False],
                            "socket_type": ["STRING", "DEFAULT"],
                            "in_out": ["STRING", "INPUT"],
                        },
                        {
                            "NodeSocketString": [
                                {
                                    "subtype": ["STRING", "NONE"],
                                    "default_value": ["STRING", ""],
                                }
                            ],
                            "NodeSocketBool": [{"default_value": ["BOOLEAN", False]}],
                            "NodeSocketMaterial": [{"default_value": ["NONE", None]}],
                            "NodeSocketVector": [
                                {
                                    "subtype": ["STRING", "NONE"],
                                    "max_value": ["FLOAT", 3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "default_value": ["LIST", [0, 0, 0]],
                                }
                            ],
                            "NodeSocketInt": [
                                {
                                    "subtype": ["STRING", "NONE"],
                                    "max_value": ["INT", 2147483647],
                                    "min_value": ["INT", -2147483648],
                                    "default_value": ["INT", 0],
                                }
                            ],
                            "NodeSocketMenu": [{"default_value": ["NONE", None]}],
                            "NodeSocketCollection": [{"default_value": ["NONE", None]}],
                            "NodeSocketGeometry": [{}],
                            "NodeSocketTexture": [{"default_value": ["NONE", None]}],
                            "NodeSocketFloat": [
                                {
                                    "subtype": ["STRING", "NONE"],
                                    "max_value": ["FLOAT", 3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "default_value": ["FLOAT", 0],
                                }
                            ],
                            "NodeSocketColor": [
                                {"default_value": ["LIST", [0, 0, 0, 1.0]]}
                            ],
                            "NodeSocketObject": [{"default_value": ["NONE", None]}],
                            "NodeSocketRotation": [
                                {"default_value": ["LIST", [0, 0, 0]]}
                            ],
                            "NodeSocketMatrix": [{}],
                            "NodeSocketImage": [{"default_value": ["NONE", None]}],
                        },
                    ],
                },
            ],
        },
    ]
}
