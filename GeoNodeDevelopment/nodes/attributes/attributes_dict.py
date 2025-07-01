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
                    "NodeInternal": [
                        {},
                        {
                            "FunctionNode": [
                                {},
                                {
                                    "FunctionNodeAlignEulerToVector": [
                                        {
                                            "axis": ["STRING", "X"],
                                            "pivot_axis": ["STRING", "AUTO"],
                                        }
                                    ],
                                    "FunctionNodeAlignRotationToVector": [
                                        {
                                            "axis": ["STRING", "X"],
                                            "pivot_axis": ["STRING", "AUTO"],
                                        }
                                    ],
                                    "FunctionNodeAxesToRotation": [
                                        {
                                            "primary_axis": ["STRING", "X"],
                                            "secondary_axis": ["STRING", "X"],
                                        }
                                    ],
                                    "FunctionNodeAxisAngleToRotation": [{}],
                                    "FunctionNodeBooleanMath": [
                                        {"operation": ["STRING", "AND"]}
                                    ],
                                    "FunctionNodeCombineColor": [
                                        {"mode": ["STRING", "RGB"]}
                                    ],
                                    "FunctionNodeCombineMatrix": [{}],
                                    "FunctionNodeCombineTransform": [{}],
                                    "FunctionNodeCompare": [
                                        {
                                            "data_type": ["STRING", "FLOAT"],
                                            "mode": ["STRING", "ELEMENT"],
                                            "operation": ["STRING", "EQUAL"],
                                        }
                                    ],
                                    "FunctionNodeEulerToRotation": [{}],
                                    "FunctionNodeFindInString": [{}],
                                    "FunctionNodeFloatToInt": [
                                        {"rounding_mode": ["STRING", "ROUND"]}
                                    ],
                                    "FunctionNodeHashValue": [
                                        {"data_type": ["STRING", "INT"]}
                                    ],
                                    "FunctionNodeInputBool": [
                                        {"boolean": ["BOOLEAN", False]}
                                    ],
                                    "FunctionNodeInputColor": [
                                        {"value": ["LIST", 0.0]}
                                    ],
                                    "FunctionNodeInputInt": [{"integer": ["INT", 1]}],
                                    "FunctionNodeInputRotation": [
                                        {"rotation_euler": ["LIST", 0.0]}
                                    ],
                                    "FunctionNodeInputSpecialCharacters": [{}],
                                    "FunctionNodeInputString": [
                                        {"string": ["STRING", ""]}
                                    ],
                                    "FunctionNodeInputVector": [
                                        {"vector": ["LIST", 0.0]}
                                    ],
                                    "FunctionNodeIntegerMath": [
                                        {"operation": ["STRING", "ADD"]}
                                    ],
                                    "FunctionNodeInvertMatrix": [{}],
                                    "FunctionNodeInvertRotation": [{}],
                                    "FunctionNodeMatrixDeterminant": [{}],
                                    "FunctionNodeMatrixMultiply": [{}],
                                    "FunctionNodeProjectPoint": [{}],
                                    "FunctionNodeQuaternionToRotation": [{}],
                                    "FunctionNodeRandomValue": [
                                        {"data_type": ["STRING", "FLOAT"]}
                                    ],
                                    "FunctionNodeReplaceString": [{}],
                                    "FunctionNodeRotateEuler": [
                                        {
                                            "rotation_type": ["STRING", "EULER"],
                                            "space": ["STRING", "OBJECT"],
                                        }
                                    ],
                                    "FunctionNodeRotateRotation": [
                                        {"rotation_space": ["STRING", "GLOBAL"]}
                                    ],
                                    "FunctionNodeRotateVector": [{}],
                                    "FunctionNodeRotationToAxisAngle": [{}],
                                    "FunctionNodeRotationToEuler": [{}],
                                    "FunctionNodeRotationToQuaternion": [{}],
                                    "FunctionNodeSeparateColor": [
                                        {"mode": ["STRING", "RGB"]}
                                    ],
                                    "FunctionNodeSeparateMatrix": [{}],
                                    "FunctionNodeSeparateTransform": [{}],
                                    "FunctionNodeSliceString": [{}],
                                    "FunctionNodeStringLength": [{}],
                                    "FunctionNodeTransformDirection": [{}],
                                    "FunctionNodeTransformPoint": [{}],
                                    "FunctionNodeTransposeMatrix": [{}],
                                    "FunctionNodeValueToString": [
                                        {"data_type": ["STRING", "FLOAT"]}
                                    ],
                                },
                            ],
                            "GeometryNode": [
                                {},
                                {
                                    "GeometryNodeAccumulateField": [
                                        {
                                            "data_type": ["STRING", "FLOAT"],
                                            "domain": ["STRING", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeAttributeDomainSize": [
                                        {"component": ["STRING", "MESH"]}
                                    ],
                                    "GeometryNodeAttributeStatistic": [
                                        {
                                            "data_type": ["STRING", "FLOAT"],
                                            "domain": ["STRING", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeBake": [
                                        {
                                            "active_index": ["INT", 0],
                                            "active_item": ["NONE", None],
                                            "bake_items": ["COLLECTION", None],
                                        }
                                    ],
                                    "GeometryNodeBlurAttribute": [
                                        {"data_type": ["STRING", "FLOAT"]}
                                    ],
                                    "GeometryNodeBoundBox": [{}],
                                    "GeometryNodeCaptureAttribute": [
                                        {
                                            "active_index": ["INT", 0],
                                            "active_item": ["NONE", None],
                                            "capture_items": ["COLLECTION", None],
                                            "domain": ["STRING", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeCollectionInfo": [
                                        {"transform_space": ["STRING", "ORIGINAL"]}
                                    ],
                                    "GeometryNodeConvexHull": [{}],
                                    "GeometryNodeCornersOfEdge": [{}],
                                    "GeometryNodeCornersOfFace": [{}],
                                    "GeometryNodeCornersOfVertex": [{}],
                                    "GeometryNodeCurveArc": [
                                        {"mode": ["STRING", "RADIUS"]}
                                    ],
                                    "GeometryNodeCurveEndpointSelection": [{}],
                                    "GeometryNodeCurveHandleTypeSelection": [
                                        {
                                            "handle_type": ["STRING", "FREE"],
                                            "mode": ["STRING", ""],
                                        }
                                    ],
                                    "GeometryNodeCurveLength": [{}],
                                    "GeometryNodeCurveOfPoint": [{}],
                                    "GeometryNodeCurvePrimitiveBezierSegment": [
                                        {"mode": ["STRING", "POSITION"]}
                                    ],
                                    "GeometryNodeCurvePrimitiveCircle": [
                                        {"mode": ["STRING", "RADIUS"]}
                                    ],
                                    "GeometryNodeCurvePrimitiveLine": [
                                        {"mode": ["STRING", "POINTS"]}
                                    ],
                                    "GeometryNodeCurvePrimitiveQuadrilateral": [
                                        {"mode": ["STRING", "RECTANGLE"]}
                                    ],
                                    "GeometryNodeCurveQuadraticBezier": [{}],
                                    "GeometryNodeCurveSetHandles": [
                                        {
                                            "handle_type": ["STRING", "FREE"],
                                            "mode": ["STRING", ""],
                                        }
                                    ],
                                    "GeometryNodeCurveSpiral": [{}],
                                    "GeometryNodeCurveSplineType": [
                                        {"spline_type": ["STRING", "POLY"]}
                                    ],
                                    "GeometryNodeCurveStar": [{}],
                                    "GeometryNodeCurveToMesh": [{}],
                                    "GeometryNodeCurveToPoints": [
                                        {"mode": ["STRING", "COUNT"]}
                                    ],
                                    "GeometryNodeCurvesToGreasePencil": [{}],
                                    "GeometryNodeCustomGroup": [
                                        {"node_tree": ["NODE_TREE", None]}
                                    ],
                                    "GeometryNodeDeformCurvesOnSurface": [{}],
                                    "GeometryNodeDeleteGeometry": [
                                        {
                                            "domain": ["STRING", "POINT"],
                                            "mode": ["STRING", "ALL"],
                                        }
                                    ],
                                    "GeometryNodeDistributePointsInGrid": [
                                        {"mode": ["STRING", "DENSITY_RANDOM"]}
                                    ],
                                    "GeometryNodeDistributePointsInVolume": [
                                        {"mode": ["STRING", "DENSITY_RANDOM"]}
                                    ],
                                    "GeometryNodeDistributePointsOnFaces": [
                                        {
                                            "distribute_method": ["STRING", "RANDOM"],
                                            "use_legacy_normal": ["BOOLEAN", False],
                                        }
                                    ],
                                    "GeometryNodeDualMesh": [{}],
                                    "GeometryNodeDuplicateElements": [
                                        {"domain": ["STRING", "POINT"]}
                                    ],
                                    "GeometryNodeEdgePathsToCurves": [{}],
                                    "GeometryNodeEdgePathsToSelection": [{}],
                                    "GeometryNodeEdgesOfCorner": [{}],
                                    "GeometryNodeEdgesOfVertex": [{}],
                                    "GeometryNodeEdgesToFaceGroups": [{}],
                                    "GeometryNodeExtrudeMesh": [
                                        {"mode": ["STRING", "FACES"]}
                                    ],
                                    "GeometryNodeFaceOfCorner": [{}],
                                    "GeometryNodeFieldAtIndex": [
                                        {
                                            "data_type": ["STRING", "FLOAT"],
                                            "domain": ["STRING", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeFieldOnDomain": [
                                        {
                                            "data_type": ["STRING", "FLOAT"],
                                            "domain": ["STRING", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeFillCurve": [
                                        {"mode": ["STRING", "TRIANGLES"]}
                                    ],
                                    "GeometryNodeFilletCurve": [
                                        {"mode": ["STRING", "BEZIER"]}
                                    ],
                                    "GeometryNodeFlipFaces": [{}],
                                    "GeometryNodeForeachGeometryElementInput": [
                                        {"paired_output": ["NONE", None]}
                                    ],
                                    "GeometryNodeForeachGeometryElementOutput": [
                                        {
                                            "active_generation_index": ["INT", 0],
                                            "active_input_index": ["INT", 0],
                                            "active_main_index": ["INT", 0],
                                            "domain": ["STRING", "POINT"],
                                            "generation_items": ["COLLECTION", None],
                                            "input_items": ["COLLECTION", None],
                                            "inspection_index": ["INT", 0],
                                            "main_items": ["COLLECTION", None],
                                        }
                                    ],
                                    "GeometryNodeGeometryToInstance": [{}],
                                    "GeometryNodeGetNamedGrid": [
                                        {"data_type": ["STRING", "FLOAT"]}
                                    ],
                                    "GeometryNodeGizmoDial": [
                                        {"color_id": ["STRING", "PRIMARY"]}
                                    ],
                                    "GeometryNodeGizmoLinear": [
                                        {
                                            "color_id": ["STRING", "PRIMARY"],
                                            "draw_style": ["STRING", "ARROW"],
                                        }
                                    ],
                                    "GeometryNodeGizmoTransform": [
                                        {
                                            "use_rotation_x": ["BOOLEAN", False],
                                            "use_rotation_y": ["BOOLEAN", False],
                                            "use_rotation_z": ["BOOLEAN", False],
                                            "use_scale_x": ["BOOLEAN", False],
                                            "use_scale_y": ["BOOLEAN", False],
                                            "use_scale_z": ["BOOLEAN", False],
                                            "use_translation_x": ["BOOLEAN", False],
                                            "use_translation_y": ["BOOLEAN", False],
                                            "use_translation_z": ["BOOLEAN", False],
                                        }
                                    ],
                                    "GeometryNodeGreasePencilToCurves": [{}],
                                    "GeometryNodeGridToMesh": [{}],
                                    "GeometryNodeGroup": [
                                        {"node_tree": ["NODE_TREE", None]}
                                    ],
                                    "GeometryNodeImageInfo": [{}],
                                    "GeometryNodeImageTexture": [
                                        {
                                            "extension": ["STRING", "REPEAT"],
                                            "interpolation": ["STRING", "Linear"],
                                        }
                                    ],
                                    "GeometryNodeImportOBJ": [{}],
                                    "GeometryNodeImportPLY": [{}],
                                    "GeometryNodeImportSTL": [{}],
                                    "GeometryNodeIndexOfNearest": [{}],
                                    "GeometryNodeIndexSwitch": [
                                        {
                                            "data_type": ["STRING", "GEOMETRY"],
                                            "index_switch_items": ["COLLECTION", None],
                                        }
                                    ],
                                    "GeometryNodeInputActiveCamera": [{}],
                                    "GeometryNodeInputCollection": [
                                        {"collection": ["NONE", None]}
                                    ],
                                    "GeometryNodeInputCurveHandlePositions": [{}],
                                    "GeometryNodeInputCurveTilt": [{}],
                                    "GeometryNodeInputEdgeSmooth": [{}],
                                    "GeometryNodeInputID": [{}],
                                    "GeometryNodeInputImage": [
                                        {"image": ["NONE", None]}
                                    ],
                                    "GeometryNodeInputIndex": [{}],
                                    "GeometryNodeInputInstanceRotation": [{}],
                                    "GeometryNodeInputInstanceScale": [{}],
                                    "GeometryNodeInputMaterial": [
                                        {"material": ["NONE", None]}
                                    ],
                                    "GeometryNodeInputMaterialIndex": [{}],
                                    "GeometryNodeInputMeshEdgeAngle": [{}],
                                    "GeometryNodeInputMeshEdgeNeighbors": [{}],
                                    "GeometryNodeInputMeshEdgeVertices": [{}],
                                    "GeometryNodeInputMeshFaceArea": [{}],
                                    "GeometryNodeInputMeshFaceIsPlanar": [{}],
                                    "GeometryNodeInputMeshFaceNeighbors": [{}],
                                    "GeometryNodeInputMeshIsland": [{}],
                                    "GeometryNodeInputMeshVertexNeighbors": [{}],
                                    "GeometryNodeInputNamedAttribute": [
                                        {"data_type": ["STRING", "FLOAT"]}
                                    ],
                                    "GeometryNodeInputNamedLayerSelection": [{}],
                                    "GeometryNodeInputNormal": [
                                        {"legacy_corner_normals": ["BOOLEAN", False]}
                                    ],
                                    "GeometryNodeInputObject": [
                                        {"object": ["NONE", None]}
                                    ],
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
                                        {
                                            "active_index": ["INT", 0],
                                            "active_item": ["NONE", None],
                                            "data_type": ["STRING", "GEOMETRY"],
                                            "enum_definition": ["NONE", None],
                                            "enum_items": ["COLLECTION", None],
                                        }
                                    ],
                                    "GeometryNodeMergeByDistance": [
                                        {"mode": ["STRING", "ALL"]}
                                    ],
                                    "GeometryNodeMergeLayers": [
                                        {"mode": ["STRING", "MERGE_BY_NAME"]}
                                    ],
                                    "GeometryNodeMeshBoolean": [
                                        {
                                            "operation": ["STRING", "INTERSECT"],
                                            "solver": ["STRING", "FLOAT"],
                                        }
                                    ],
                                    "GeometryNodeMeshCircle": [
                                        {"fill_type": ["STRING", "NONE"]}
                                    ],
                                    "GeometryNodeMeshCone": [
                                        {"fill_type": ["STRING", "NGON"]}
                                    ],
                                    "GeometryNodeMeshCube": [{}],
                                    "GeometryNodeMeshCylinder": [
                                        {"fill_type": ["STRING", "NGON"]}
                                    ],
                                    "GeometryNodeMeshFaceSetBoundaries": [{}],
                                    "GeometryNodeMeshGrid": [{}],
                                    "GeometryNodeMeshIcoSphere": [{}],
                                    "GeometryNodeMeshLine": [
                                        {
                                            "count_mode": ["STRING", "TOTAL"],
                                            "mode": ["STRING", "OFFSET"],
                                        }
                                    ],
                                    "GeometryNodeMeshToCurve": [{}],
                                    "GeometryNodeMeshToDensityGrid": [{}],
                                    "GeometryNodeMeshToPoints": [
                                        {"mode": ["STRING", "VERTICES"]}
                                    ],
                                    "GeometryNodeMeshToSDFGrid": [{}],
                                    "GeometryNodeMeshToVolume": [
                                        {"resolution_mode": ["STRING", "VOXEL_AMOUNT"]}
                                    ],
                                    "GeometryNodeMeshUVSphere": [{}],
                                    "GeometryNodeObjectInfo": [
                                        {"transform_space": ["STRING", "ORIGINAL"]}
                                    ],
                                    "GeometryNodeOffsetCornerInFace": [{}],
                                    "GeometryNodeOffsetPointInCurve": [{}],
                                    "GeometryNodePoints": [{}],
                                    "GeometryNodePointsOfCurve": [{}],
                                    "GeometryNodePointsToCurves": [{}],
                                    "GeometryNodePointsToSDFGrid": [{}],
                                    "GeometryNodePointsToVertices": [{}],
                                    "GeometryNodePointsToVolume": [
                                        {"resolution_mode": ["STRING", "VOXEL_AMOUNT"]}
                                    ],
                                    "GeometryNodeProximity": [
                                        {"target_element": ["STRING", "FACES"]}
                                    ],
                                    "GeometryNodeRaycast": [
                                        {
                                            "data_type": ["STRING", "FLOAT"],
                                            "mapping": ["STRING", "INTERPOLATED"],
                                        }
                                    ],
                                    "GeometryNodeRealizeInstances": [{}],
                                    "GeometryNodeRemoveAttribute": [
                                        {"pattern_mode": ["STRING", "EXACT"]}
                                    ],
                                    "GeometryNodeRepeatInput": [
                                        {"paired_output": ["NONE", None]}
                                    ],
                                    "GeometryNodeRepeatOutput": [
                                        {
                                            "active_index": ["INT", 0],
                                            "active_item": ["NONE", None],
                                            "inspection_index": ["INT", 0],
                                            "repeat_items": ["COLLECTION", None],
                                        }
                                    ],
                                    "GeometryNodeReplaceMaterial": [{}],
                                    "GeometryNodeResampleCurve": [
                                        {
                                            "keep_last_segment": ["BOOLEAN", False],
                                            "mode": ["STRING", "COUNT"],
                                        }
                                    ],
                                    "GeometryNodeReverseCurve": [{}],
                                    "GeometryNodeRotateInstances": [{}],
                                    "GeometryNodeSDFGridBoolean": [
                                        {"operation": ["STRING", "DIFFERENCE"]}
                                    ],
                                    "GeometryNodeSampleCurve": [
                                        {
                                            "data_type": ["STRING", "FLOAT"],
                                            "mode": ["STRING", "FACTOR"],
                                            "use_all_curves": ["BOOLEAN", False],
                                        }
                                    ],
                                    "GeometryNodeSampleGrid": [
                                        {
                                            "data_type": ["STRING", "FLOAT"],
                                            "interpolation_mode": [
                                                "STRING",
                                                "TRILINEAR",
                                            ],
                                        }
                                    ],
                                    "GeometryNodeSampleGridIndex": [
                                        {"data_type": ["STRING", "FLOAT"]}
                                    ],
                                    "GeometryNodeSampleIndex": [
                                        {
                                            "clamp": ["BOOLEAN", False],
                                            "data_type": ["STRING", "FLOAT"],
                                            "domain": ["STRING", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeSampleNearest": [
                                        {"domain": ["STRING", "POINT"]}
                                    ],
                                    "GeometryNodeSampleNearestSurface": [
                                        {"data_type": ["STRING", "FLOAT"]}
                                    ],
                                    "GeometryNodeSampleUVSurface": [
                                        {"data_type": ["STRING", "FLOAT"]}
                                    ],
                                    "GeometryNodeScaleElements": [
                                        {
                                            "domain": ["STRING", "FACE"],
                                            "scale_mode": ["STRING", "UNIFORM"],
                                        }
                                    ],
                                    "GeometryNodeScaleInstances": [{}],
                                    "GeometryNodeSelfObject": [{}],
                                    "GeometryNodeSeparateComponents": [{}],
                                    "GeometryNodeSeparateGeometry": [
                                        {"domain": ["STRING", "POINT"]}
                                    ],
                                    "GeometryNodeSetCurveHandlePositions": [
                                        {"mode": ["STRING", "LEFT"]}
                                    ],
                                    "GeometryNodeSetCurveNormal": [
                                        {"mode": ["STRING", "MINIMUM_TWIST"]}
                                    ],
                                    "GeometryNodeSetCurveRadius": [{}],
                                    "GeometryNodeSetCurveTilt": [{}],
                                    "GeometryNodeSetGeometryName": [{}],
                                    "GeometryNodeSetID": [{}],
                                    "GeometryNodeSetInstanceTransform": [{}],
                                    "GeometryNodeSetMaterial": [{}],
                                    "GeometryNodeSetMaterialIndex": [{}],
                                    "GeometryNodeSetPointRadius": [{}],
                                    "GeometryNodeSetPosition": [{}],
                                    "GeometryNodeSetShadeSmooth": [
                                        {"domain": ["STRING", "EDGE"]}
                                    ],
                                    "GeometryNodeSetSplineCyclic": [{}],
                                    "GeometryNodeSetSplineResolution": [{}],
                                    "GeometryNodeSimulationInput": [
                                        {"paired_output": ["NONE", None]}
                                    ],
                                    "GeometryNodeSimulationOutput": [
                                        {
                                            "active_index": ["INT", 0],
                                            "active_item": ["NONE", None],
                                            "state_items": ["COLLECTION", None],
                                        }
                                    ],
                                    "GeometryNodeSortElements": [
                                        {"domain": ["STRING", "POINT"]}
                                    ],
                                    "GeometryNodeSplineLength": [{}],
                                    "GeometryNodeSplineParameter": [{}],
                                    "GeometryNodeSplitEdges": [{}],
                                    "GeometryNodeSplitToInstances": [
                                        {"domain": ["STRING", "POINT"]}
                                    ],
                                    "GeometryNodeStoreNamedAttribute": [
                                        {
                                            "data_type": ["STRING", "FLOAT"],
                                            "domain": ["STRING", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeStoreNamedGrid": [
                                        {"data_type": ["STRING", "FLOAT"]}
                                    ],
                                    "GeometryNodeStringJoin": [{}],
                                    "GeometryNodeStringToCurves": [
                                        {
                                            "align_x": ["STRING", "LEFT"],
                                            "align_y": ["STRING", "TOP_BASELINE"],
                                            "font": ["NONE", None],
                                            "overflow": ["STRING", "OVERFLOW"],
                                            "pivot_mode": ["STRING", "BOTTOM_LEFT"],
                                        }
                                    ],
                                    "GeometryNodeSubdivideCurve": [{}],
                                    "GeometryNodeSubdivideMesh": [{}],
                                    "GeometryNodeSubdivisionSurface": [
                                        {
                                            "boundary_smooth": ["STRING", "ALL"],
                                            "uv_smooth": [
                                                "STRING",
                                                "PRESERVE_BOUNDARIES",
                                            ],
                                        }
                                    ],
                                    "GeometryNodeSwitch": [
                                        {"input_type": ["STRING", "GEOMETRY"]}
                                    ],
                                    "GeometryNodeTool3DCursor": [{}],
                                    "GeometryNodeToolActiveElement": [
                                        {"domain": ["STRING", "POINT"]}
                                    ],
                                    "GeometryNodeToolFaceSet": [{}],
                                    "GeometryNodeToolMousePosition": [{}],
                                    "GeometryNodeToolSelection": [{}],
                                    "GeometryNodeToolSetFaceSet": [{}],
                                    "GeometryNodeToolSetSelection": [
                                        {
                                            "domain": ["STRING", "POINT"],
                                            "selection_type": ["STRING", "BOOLEAN"],
                                        }
                                    ],
                                    "GeometryNodeTransform": [
                                        {"mode": ["STRING", "COMPONENTS"]}
                                    ],
                                    "GeometryNodeTranslateInstances": [{}],
                                    "GeometryNodeTriangulate": [
                                        {
                                            "ngon_method": ["STRING", "BEAUTY"],
                                            "quad_method": ["STRING", "BEAUTY"],
                                        }
                                    ],
                                    "GeometryNodeTrimCurve": [
                                        {"mode": ["STRING", "FACTOR"]}
                                    ],
                                    "GeometryNodeUVPackIslands": [{}],
                                    "GeometryNodeUVUnwrap": [
                                        {"method": ["STRING", "ANGLE_BASED"]}
                                    ],
                                    "GeometryNodeVertexOfCorner": [{}],
                                    "GeometryNodeViewer": [
                                        {
                                            "data_type": ["STRING", "FLOAT"],
                                            "domain": ["STRING", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeViewportTransform": [{}],
                                    "GeometryNodeVolumeCube": [{}],
                                    "GeometryNodeVolumeToMesh": [
                                        {"resolution_mode": ["STRING", "GRID"]}
                                    ],
                                    "GeometryNodeWarning": [
                                        {"warning_type": ["STRING", "ERROR"]}
                                    ],
                                },
                            ],
                        },
                    ]
                },
            ],
            "NodeSocket": [
                {
                    "bl_idname": ["STRING", ""],
                    "name": ["STRING", ""],
                    "type": ["STRING", ""],
                },
                {
                    "NodeSocketStandard": [
                        {},
                        {
                            "NodeSocketBool": [{"default_value": ["BOOLEAN", False]}],
                            "NodeSocketCollection": [{"default_value": ["NONE", None]}],
                            "NodeSocketColor": [{"default_value": ["LIST", 0.0]}],
                            "NodeSocketFloat": [{"default_value": ["FLOAT", 0.0]}],
                            "NodeSocketFloatAngle": [{"default_value": ["FLOAT", 0.0]}],
                            "NodeSocketFloatColorTemperature": [
                                {"default_value": ["FLOAT", 0.0]}
                            ],
                            "NodeSocketFloatDistance": [
                                {"default_value": ["FLOAT", 0.0]}
                            ],
                            "NodeSocketFloatFactor": [
                                {"default_value": ["FLOAT", 0.0]}
                            ],
                            "NodeSocketFloatFrequency": [
                                {"default_value": ["FLOAT", 0.0]}
                            ],
                            "NodeSocketFloatPercentage": [
                                {"default_value": ["FLOAT", 0.0]}
                            ],
                            "NodeSocketFloatTime": [{"default_value": ["FLOAT", 0.0]}],
                            "NodeSocketFloatTimeAbsolute": [
                                {"default_value": ["FLOAT", 0.0]}
                            ],
                            "NodeSocketFloatUnsigned": [
                                {"default_value": ["FLOAT", 0.0]}
                            ],
                            "NodeSocketFloatWavelength": [
                                {"default_value": ["FLOAT", 0.0]}
                            ],
                            "NodeSocketGeometry": [{}],
                            "NodeSocketImage": [{"default_value": ["NONE", None]}],
                            "NodeSocketInt": [{"default_value": ["INT", 0]}],
                            "NodeSocketIntFactor": [{"default_value": ["INT", 1]}],
                            "NodeSocketIntPercentage": [
                                {"default_value": ["INT", 100]}
                            ],
                            "NodeSocketIntUnsigned": [{"default_value": ["INT", 0]}],
                            "NodeSocketMaterial": [{"default_value": ["NONE", None]}],
                            "NodeSocketMatrix": [{}],
                            "NodeSocketMenu": [{"default_value": ["STRING", ""]}],
                            "NodeSocketObject": [{"default_value": ["NONE", None]}],
                            "NodeSocketRotation": [{"default_value": ["LIST", 0.0]}],
                            "NodeSocketShader": [{}],
                            "NodeSocketStandard": [{}],
                            "NodeSocketString": [{"default_value": ["STRING", ""]}],
                            "NodeSocketStringFilePath": [
                                {"default_value": ["STRING", ""]}
                            ],
                            "NodeSocketTexture": [{"default_value": ["NONE", None]}],
                            "NodeSocketVector": [{"default_value": ["LIST", 0.0]}],
                            "NodeSocketVectorAcceleration": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorDirection": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorEuler": [{"default_value": ["LIST", 0.0]}],
                            "NodeSocketVectorTranslation": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorVelocity": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorXYZ": [{"default_value": ["LIST", 0.0]}],
                            "NodeSocketVirtual": [{}],
                        },
                    ]
                },
            ],
            "NodeTree": [
                {
                    "bl_idname": ["STRING", ""],
                    "color_tag": ["STRING", "NONE"],
                    "default_group_node_width": ["INT", 140],
                    "description": ["STRING", ""],
                    "name": ["STRING", ""],
                },
                {
                    "GeometryNodeTree": [
                        {
                            "is_modifier": ["BOOLEAN", False],
                            "is_tool": ["BOOLEAN", False],
                        }
                    ]
                },
            ],
            "NodeTreeInterfaceItem": [
                {
                    "description": ["STRING", ""],
                    "item_type": ["STRING", "SOCKET"],
                    "name": ["STRING", ""],
                },
                {
                    "NodeTreeInterfacePanel": [{"default_closed": ["BOOLEAN", False]}],
                    "NodeTreeInterfaceSocket": [
                        {
                            "attribute_domain": ["STRING", "POINT"],
                            "default_attribute_name": ["STRING", ""],
                            "description": ["STRING", ""],
                            "force_non_field": ["BOOLEAN", False],
                            "hide_in_modifier": ["BOOLEAN", False],
                            "hide_value": ["BOOLEAN", False],
                            "in_out": ["STRING", "INPUT"],
                            "socket_type": ["STRING", "DEFAULT"],
                        },
                        {
                            "NodeTreeInterfaceSocketBool": [
                                {"default_value": ["BOOLEAN", False]}
                            ],
                            "NodeTreeInterfaceSocketCollection": [
                                {"default_value": ["NONE", None]}
                            ],
                            "NodeTreeInterfaceSocketColor": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeTreeInterfaceSocketFloat": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatAngle": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatColorTemperature": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatDistance": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatFactor": [
                                {
                                    "default_value": ["FLOAT", 1.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatFrequency": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatPercentage": [
                                {
                                    "default_value": ["FLOAT", 100.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatTime": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatTimeAbsolute": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatUnsigned": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatWavelength": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketGeometry": [{}],
                            "NodeTreeInterfaceSocketImage": [
                                {"default_value": ["NONE", None]}
                            ],
                            "NodeTreeInterfaceSocketInt": [
                                {
                                    "default_value": ["INT", 0],
                                    "max_value": ["INT", 0],
                                    "min_value": ["INT", 0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketIntFactor": [
                                {
                                    "default_value": ["INT", 0],
                                    "max_value": ["INT", 0],
                                    "min_value": ["INT", 0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketIntPercentage": [
                                {
                                    "default_value": ["INT", 0],
                                    "max_value": ["INT", 0],
                                    "min_value": ["INT", 0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketIntUnsigned": [
                                {
                                    "default_value": ["INT", 0],
                                    "max_value": ["INT", 0],
                                    "min_value": ["INT", 0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketMaterial": [
                                {"default_value": ["NONE", None]}
                            ],
                            "NodeTreeInterfaceSocketMatrix": [{}],
                            "NodeTreeInterfaceSocketMenu": [
                                {"default_value": ["STRING", ""]}
                            ],
                            "NodeTreeInterfaceSocketObject": [
                                {"default_value": ["NONE", None]}
                            ],
                            "NodeTreeInterfaceSocketRotation": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeTreeInterfaceSocketShader": [{}],
                            "NodeTreeInterfaceSocketString": [
                                {
                                    "default_value": ["STRING", ""],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketStringFilePath": [
                                {
                                    "default_value": ["STRING", ""],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketTexture": [
                                {"default_value": ["NONE", None]}
                            ],
                            "NodeTreeInterfaceSocketVector": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorAcceleration": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorDirection": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorEuler": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorTranslation": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorVelocity": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorXYZ": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "max_value": ["FLOAT", 0.0],
                                    "min_value": ["FLOAT", 0.0],
                                    "subtype": ["STRING", "DEFAULT"],
                                }
                            ],
                        },
                    ],
                },
            ],
        },
    ]
}

ALL_ATTRIBUTE_TYPES = [
    "BOOLEAN",
    "COLLECTION",
    "FLOAT",
    "INT",
    "LIST",
    "NODE",
    "NODE_TREE",
    "NONE",
    "STRING",
]
