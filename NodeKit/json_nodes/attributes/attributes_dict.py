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
                                            "axis": ["ENUM", "X"],
                                            "pivot_axis": ["ENUM", "AUTO"],
                                        }
                                    ],
                                    "FunctionNodeAlignRotationToVector": [
                                        {
                                            "axis": ["ENUM", "X"],
                                            "pivot_axis": ["ENUM", "AUTO"],
                                        }
                                    ],
                                    "FunctionNodeAxesToRotation": [
                                        {
                                            "primary_axis": ["ENUM", "X"],
                                            "secondary_axis": ["ENUM", "X"],
                                        }
                                    ],
                                    "FunctionNodeAxisAngleToRotation": [{}],
                                    "FunctionNodeBitMath": [
                                        {"operation": ["ENUM", "AND"]}
                                    ],
                                    "FunctionNodeBooleanMath": [
                                        {"operation": ["ENUM", "AND"]}
                                    ],
                                    "FunctionNodeCombineColor": [
                                        {"mode": ["ENUM", "RGB"]}
                                    ],
                                    "FunctionNodeCombineMatrix": [{}],
                                    "FunctionNodeCombineTransform": [{}],
                                    "FunctionNodeCompare": [
                                        {
                                            "data_type": ["ENUM", "FLOAT"],
                                            "mode": ["ENUM", "ELEMENT"],
                                            "operation": ["ENUM", "EQUAL"],
                                        }
                                    ],
                                    "FunctionNodeEulerToRotation": [{}],
                                    "FunctionNodeFindInString": [{}],
                                    "FunctionNodeFloatToInt": [
                                        {"rounding_mode": ["ENUM", "ROUND"]}
                                    ],
                                    "FunctionNodeFormatString": [
                                        {
                                            "active_index": ["INT", 0],
                                            "format_items": ["ITEMS", None],
                                        }
                                    ],
                                    "FunctionNodeHashValue": [
                                        {"data_type": ["ENUM", "INT"]}
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
                                        {"operation": ["ENUM", "ADD"]}
                                    ],
                                    "FunctionNodeInvertMatrix": [{}],
                                    "FunctionNodeInvertRotation": [{}],
                                    "FunctionNodeMatchString": [
                                        {"operation": ["ENUM", "STARTS_WITH"]}
                                    ],
                                    "FunctionNodeMatrixDeterminant": [{}],
                                    "FunctionNodeMatrixMultiply": [{}],
                                    "FunctionNodeProjectPoint": [{}],
                                    "FunctionNodeQuaternionToRotation": [{}],
                                    "FunctionNodeRandomValue": [
                                        {"data_type": ["ENUM", "FLOAT"]}
                                    ],
                                    "FunctionNodeReplaceString": [{}],
                                    "FunctionNodeRotateEuler": [
                                        {
                                            "rotation_type": ["ENUM", "EULER"],
                                            "space": ["ENUM", "OBJECT"],
                                        }
                                    ],
                                    "FunctionNodeRotateRotation": [
                                        {"rotation_space": ["ENUM", "GLOBAL"]}
                                    ],
                                    "FunctionNodeRotateVector": [{}],
                                    "FunctionNodeRotationToAxisAngle": [{}],
                                    "FunctionNodeRotationToEuler": [{}],
                                    "FunctionNodeRotationToQuaternion": [{}],
                                    "FunctionNodeSeparateColor": [
                                        {"mode": ["ENUM", "RGB"]}
                                    ],
                                    "FunctionNodeSeparateMatrix": [{}],
                                    "FunctionNodeSeparateTransform": [{}],
                                    "FunctionNodeSliceString": [{}],
                                    "FunctionNodeStringLength": [{}],
                                    "FunctionNodeTransformDirection": [{}],
                                    "FunctionNodeTransformPoint": [{}],
                                    "FunctionNodeTransposeMatrix": [{}],
                                    "FunctionNodeValueToString": [
                                        {"data_type": ["ENUM", "FLOAT"]}
                                    ],
                                },
                            ],
                            "GeometryNode": [
                                {},
                                {
                                    "GeometryNodeAccumulateField": [
                                        {
                                            "data_type": ["ENUM", "FLOAT"],
                                            "domain": ["ENUM", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeAttributeDomainSize": [
                                        {"component": ["ENUM", "MESH"]}
                                    ],
                                    "GeometryNodeAttributeStatistic": [
                                        {
                                            "data_type": ["ENUM", "FLOAT"],
                                            "domain": ["ENUM", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeBake": [
                                        {"bake_items": ["ITEMS", None]}
                                    ],
                                    "GeometryNodeBlurAttribute": [
                                        {"data_type": ["ENUM", "FLOAT"]}
                                    ],
                                    "GeometryNodeBoundBox": [{}],
                                    "GeometryNodeCameraInfo": [{}],
                                    "GeometryNodeCaptureAttribute": [
                                        {
                                            "capture_items": ["ITEMS", None],
                                            "domain": ["ENUM", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeClosureInput": [
                                        {"paired_output": ["NODE", None]}
                                    ],
                                    "GeometryNodeClosureOutput": [
                                        {
                                            "input_items": ["ITEMS", None],
                                            "output_items": ["ITEMS", None],
                                        }
                                    ],
                                    "GeometryNodeCollectionInfo": [
                                        {"transform_space": ["ENUM", "ORIGINAL"]}
                                    ],
                                    "GeometryNodeCombineBundle": [
                                        {"bundle_items": ["ITEMS", None]}
                                    ],
                                    "GeometryNodeConvexHull": [{}],
                                    "GeometryNodeCornersOfEdge": [{}],
                                    "GeometryNodeCornersOfFace": [{}],
                                    "GeometryNodeCornersOfVertex": [{}],
                                    "GeometryNodeCurveArc": [
                                        {"mode": ["ENUM", "RADIUS"]}
                                    ],
                                    "GeometryNodeCurveEndpointSelection": [{}],
                                    "GeometryNodeCurveHandleTypeSelection": [
                                        {
                                            "handle_type": ["ENUM", "FREE"],
                                            "mode": ["ENUM", ""],
                                        }
                                    ],
                                    "GeometryNodeCurveLength": [{}],
                                    "GeometryNodeCurveOfPoint": [{}],
                                    "GeometryNodeCurvePrimitiveBezierSegment": [
                                        {"mode": ["ENUM", "POSITION"]}
                                    ],
                                    "GeometryNodeCurvePrimitiveCircle": [
                                        {"mode": ["ENUM", "RADIUS"]}
                                    ],
                                    "GeometryNodeCurvePrimitiveLine": [
                                        {"mode": ["ENUM", "POINTS"]}
                                    ],
                                    "GeometryNodeCurvePrimitiveQuadrilateral": [
                                        {"mode": ["ENUM", "RECTANGLE"]}
                                    ],
                                    "GeometryNodeCurveQuadraticBezier": [{}],
                                    "GeometryNodeCurveSetHandles": [
                                        {
                                            "handle_type": ["ENUM", "FREE"],
                                            "mode": ["ENUM", ""],
                                        }
                                    ],
                                    "GeometryNodeCurveSpiral": [{}],
                                    "GeometryNodeCurveSplineType": [
                                        {"spline_type": ["ENUM", "POLY"]}
                                    ],
                                    "GeometryNodeCurveStar": [{}],
                                    "GeometryNodeCurveToMesh": [{}],
                                    "GeometryNodeCurveToPoints": [
                                        {"mode": ["ENUM", "COUNT"]}
                                    ],
                                    "GeometryNodeCurvesToGreasePencil": [{}],
                                    "GeometryNodeCustomGroup": [
                                        {"node_tree": ["NODETREE", None]}
                                    ],
                                    "GeometryNodeDeformCurvesOnSurface": [{}],
                                    "GeometryNodeDeleteGeometry": [
                                        {
                                            "domain": ["ENUM", "POINT"],
                                            "mode": ["ENUM", "ALL"],
                                        }
                                    ],
                                    "GeometryNodeDistributePointsInGrid": [
                                        {"mode": ["ENUM", "DENSITY_RANDOM"]}
                                    ],
                                    "GeometryNodeDistributePointsInVolume": [
                                        {"mode": ["ENUM", "DENSITY_RANDOM"]}
                                    ],
                                    "GeometryNodeDistributePointsOnFaces": [
                                        {
                                            "distribute_method": ["ENUM", "RANDOM"],
                                            "use_legacy_normal": ["BOOLEAN", False],
                                        }
                                    ],
                                    "GeometryNodeDualMesh": [{}],
                                    "GeometryNodeDuplicateElements": [
                                        {"domain": ["ENUM", "POINT"]}
                                    ],
                                    "GeometryNodeEdgePathsToCurves": [{}],
                                    "GeometryNodeEdgePathsToSelection": [{}],
                                    "GeometryNodeEdgesOfCorner": [{}],
                                    "GeometryNodeEdgesOfVertex": [{}],
                                    "GeometryNodeEdgesToFaceGroups": [{}],
                                    "GeometryNodeEvaluateClosure": [
                                        {
                                            "input_items": ["ITEMS", None],
                                            "output_items": ["ITEMS", None],
                                        }
                                    ],
                                    "GeometryNodeExtrudeMesh": [
                                        {"mode": ["ENUM", "FACES"]}
                                    ],
                                    "GeometryNodeFaceOfCorner": [{}],
                                    "GeometryNodeFieldAtIndex": [
                                        {
                                            "data_type": ["ENUM", "FLOAT"],
                                            "domain": ["ENUM", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeFieldAverage": [
                                        {
                                            "data_type": ["ENUM", "FLOAT"],
                                            "domain": ["ENUM", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeFieldMinAndMax": [
                                        {
                                            "data_type": ["ENUM", "FLOAT"],
                                            "domain": ["ENUM", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeFieldOnDomain": [
                                        {
                                            "data_type": ["ENUM", "FLOAT"],
                                            "domain": ["ENUM", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeFieldVariance": [
                                        {
                                            "data_type": ["ENUM", "FLOAT"],
                                            "domain": ["ENUM", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeFillCurve": [
                                        {"mode": ["ENUM", "TRIANGLES"]}
                                    ],
                                    "GeometryNodeFilletCurve": [
                                        {"mode": ["ENUM", "BEZIER"]}
                                    ],
                                    "GeometryNodeFlipFaces": [{}],
                                    "GeometryNodeForeachGeometryElementInput": [
                                        {"paired_output": ["NODE", None]}
                                    ],
                                    "GeometryNodeForeachGeometryElementOutput": [
                                        {
                                            "domain": ["ENUM", "POINT"],
                                            "generation_items": ["ITEMS", None],
                                            "input_items": ["ITEMS", None],
                                            "main_items": ["ITEMS", None],
                                        }
                                    ],
                                    "GeometryNodeGeometryToInstance": [{}],
                                    "GeometryNodeGetNamedGrid": [
                                        {"data_type": ["ENUM", "FLOAT"]}
                                    ],
                                    "GeometryNodeGizmoDial": [
                                        {"color_id": ["ENUM", "PRIMARY"]}
                                    ],
                                    "GeometryNodeGizmoLinear": [
                                        {
                                            "color_id": ["ENUM", "PRIMARY"],
                                            "draw_style": ["ENUM", "ARROW"],
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
                                    "GeometryNodeGridInfo": [
                                        {"data_type": ["ENUM", "FLOAT"]}
                                    ],
                                    "GeometryNodeGridToMesh": [{}],
                                    "GeometryNodeGroup": [
                                        {"node_tree": ["NODETREE", None]}
                                    ],
                                    "GeometryNodeImageInfo": [{}],
                                    "GeometryNodeImageTexture": [
                                        {
                                            "extension": ["ENUM", "REPEAT"],
                                            "interpolation": ["ENUM", "Linear"],
                                        }
                                    ],
                                    "GeometryNodeImportCSV": [{}],
                                    "GeometryNodeImportOBJ": [{}],
                                    "GeometryNodeImportPLY": [{}],
                                    "GeometryNodeImportSTL": [{}],
                                    "GeometryNodeImportText": [{}],
                                    "GeometryNodeImportVDB": [{}],
                                    "GeometryNodeIndexOfNearest": [{}],
                                    "GeometryNodeIndexSwitch": [
                                        {"data_type": ["ENUM", "GEOMETRY"]}
                                    ],
                                    "GeometryNodeInputActiveCamera": [{}],
                                    "GeometryNodeInputCollection": [
                                        {"collection": ["COLLECTION", None]}
                                    ],
                                    "GeometryNodeInputCurveHandlePositions": [{}],
                                    "GeometryNodeInputCurveTilt": [{}],
                                    "GeometryNodeInputEdgeSmooth": [{}],
                                    "GeometryNodeInputID": [{}],
                                    "GeometryNodeInputImage": [
                                        {"image": ["IMAGE", None]}
                                    ],
                                    "GeometryNodeInputIndex": [{}],
                                    "GeometryNodeInputInstanceBounds": [{}],
                                    "GeometryNodeInputInstanceRotation": [{}],
                                    "GeometryNodeInputInstanceScale": [{}],
                                    "GeometryNodeInputMaterial": [
                                        {"material": ["MATERIAL", None]}
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
                                        {"data_type": ["ENUM", "FLOAT"]}
                                    ],
                                    "GeometryNodeInputNamedLayerSelection": [{}],
                                    "GeometryNodeInputNormal": [
                                        {"legacy_corner_normals": ["BOOLEAN", False]}
                                    ],
                                    "GeometryNodeInputObject": [
                                        {"object": ["OBJECT", None]}
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
                                            "data_type": ["ENUM", "GEOMETRY"],
                                            "enum_definition": ["NODE", None],
                                            "enum_items": ["ITEMS", None],
                                        }
                                    ],
                                    "GeometryNodeMergeByDistance": [
                                        {"mode": ["ENUM", "ALL"]}
                                    ],
                                    "GeometryNodeMergeLayers": [
                                        {"mode": ["ENUM", "MERGE_BY_NAME"]}
                                    ],
                                    "GeometryNodeMeshBoolean": [
                                        {
                                            "operation": ["ENUM", "INTERSECT"],
                                            "solver": ["ENUM", "FLOAT"],
                                        }
                                    ],
                                    "GeometryNodeMeshCircle": [
                                        {"fill_type": ["ENUM", "NONE"]}
                                    ],
                                    "GeometryNodeMeshCone": [
                                        {"fill_type": ["ENUM", "NGON"]}
                                    ],
                                    "GeometryNodeMeshCube": [{}],
                                    "GeometryNodeMeshCylinder": [
                                        {"fill_type": ["ENUM", "NGON"]}
                                    ],
                                    "GeometryNodeMeshFaceSetBoundaries": [{}],
                                    "GeometryNodeMeshGrid": [{}],
                                    "GeometryNodeMeshIcoSphere": [{}],
                                    "GeometryNodeMeshLine": [
                                        {
                                            "count_mode": ["ENUM", "TOTAL"],
                                            "mode": ["ENUM", "OFFSET"],
                                        }
                                    ],
                                    "GeometryNodeMeshToCurve": [
                                        {"mode": ["ENUM", "EDGES"]}
                                    ],
                                    "GeometryNodeMeshToDensityGrid": [{}],
                                    "GeometryNodeMeshToPoints": [
                                        {"mode": ["ENUM", "VERTICES"]}
                                    ],
                                    "GeometryNodeMeshToSDFGrid": [{}],
                                    "GeometryNodeMeshToVolume": [
                                        {"resolution_mode": ["ENUM", "VOXEL_AMOUNT"]}
                                    ],
                                    "GeometryNodeMeshUVSphere": [{}],
                                    "GeometryNodeObjectInfo": [
                                        {"transform_space": ["ENUM", "ORIGINAL"]}
                                    ],
                                    "GeometryNodeOffsetCornerInFace": [{}],
                                    "GeometryNodeOffsetPointInCurve": [{}],
                                    "GeometryNodePoints": [{}],
                                    "GeometryNodePointsOfCurve": [{}],
                                    "GeometryNodePointsToCurves": [{}],
                                    "GeometryNodePointsToSDFGrid": [{}],
                                    "GeometryNodePointsToVertices": [{}],
                                    "GeometryNodePointsToVolume": [
                                        {"resolution_mode": ["ENUM", "VOXEL_AMOUNT"]}
                                    ],
                                    "GeometryNodeProximity": [
                                        {"target_element": ["ENUM", "FACES"]}
                                    ],
                                    "GeometryNodeRaycast": [
                                        {
                                            "data_type": ["ENUM", "FLOAT"],
                                            "mapping": ["ENUM", "INTERPOLATED"],
                                        }
                                    ],
                                    "GeometryNodeRealizeInstances": [{}],
                                    "GeometryNodeRemoveAttribute": [
                                        {"pattern_mode": ["ENUM", "EXACT"]}
                                    ],
                                    "GeometryNodeRepeatInput": [
                                        {"paired_output": ["NODE", None]}
                                    ],
                                    "GeometryNodeRepeatOutput": [
                                        {"repeat_items": ["ITEMS", None]}
                                    ],
                                    "GeometryNodeReplaceMaterial": [{}],
                                    "GeometryNodeResampleCurve": [
                                        {
                                            "keep_last_segment": ["BOOLEAN", False],
                                            "mode": ["ENUM", "COUNT"],
                                        }
                                    ],
                                    "GeometryNodeReverseCurve": [{}],
                                    "GeometryNodeRotateInstances": [{}],
                                    "GeometryNodeSDFGridBoolean": [
                                        {"operation": ["ENUM", "DIFFERENCE"]}
                                    ],
                                    "GeometryNodeSampleCurve": [
                                        {
                                            "data_type": ["ENUM", "FLOAT"],
                                            "mode": ["ENUM", "FACTOR"],
                                            "use_all_curves": ["BOOLEAN", False],
                                        }
                                    ],
                                    "GeometryNodeSampleGrid": [
                                        {
                                            "data_type": ["ENUM", "FLOAT"],
                                            "interpolation_mode": ["ENUM", "TRILINEAR"],
                                        }
                                    ],
                                    "GeometryNodeSampleGridIndex": [
                                        {"data_type": ["ENUM", "FLOAT"]}
                                    ],
                                    "GeometryNodeSampleIndex": [
                                        {
                                            "clamp": ["BOOLEAN", False],
                                            "data_type": ["ENUM", "FLOAT"],
                                            "domain": ["ENUM", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeSampleNearest": [
                                        {"domain": ["ENUM", "POINT"]}
                                    ],
                                    "GeometryNodeSampleNearestSurface": [
                                        {"data_type": ["ENUM", "FLOAT"]}
                                    ],
                                    "GeometryNodeSampleUVSurface": [
                                        {"data_type": ["ENUM", "FLOAT"]}
                                    ],
                                    "GeometryNodeScaleElements": [
                                        {
                                            "domain": ["ENUM", "FACE"],
                                            "scale_mode": ["ENUM", "UNIFORM"],
                                        }
                                    ],
                                    "GeometryNodeScaleInstances": [{}],
                                    "GeometryNodeSelfObject": [{}],
                                    "GeometryNodeSeparateBundle": [
                                        {"bundle_items": ["ITEMS", None]}
                                    ],
                                    "GeometryNodeSeparateComponents": [{}],
                                    "GeometryNodeSeparateGeometry": [
                                        {"domain": ["ENUM", "POINT"]}
                                    ],
                                    "GeometryNodeSetCurveHandlePositions": [
                                        {"mode": ["ENUM", "LEFT"]}
                                    ],
                                    "GeometryNodeSetCurveNormal": [
                                        {"mode": ["ENUM", "MINIMUM_TWIST"]}
                                    ],
                                    "GeometryNodeSetCurveRadius": [{}],
                                    "GeometryNodeSetCurveTilt": [{}],
                                    "GeometryNodeSetGeometryName": [{}],
                                    "GeometryNodeSetGreasePencilColor": [
                                        {"mode": ["ENUM", "STROKE"]}
                                    ],
                                    "GeometryNodeSetGreasePencilDepth": [
                                        {"depth_order": ["ENUM", "2D"]}
                                    ],
                                    "GeometryNodeSetGreasePencilSoftness": [{}],
                                    "GeometryNodeSetID": [{}],
                                    "GeometryNodeSetInstanceTransform": [{}],
                                    "GeometryNodeSetMaterial": [{}],
                                    "GeometryNodeSetMaterialIndex": [{}],
                                    "GeometryNodeSetMeshNormal": [
                                        {
                                            "domain": ["ENUM", "POINT"],
                                            "mode": ["ENUM", "SHARPNESS"],
                                        }
                                    ],
                                    "GeometryNodeSetPointRadius": [{}],
                                    "GeometryNodeSetPosition": [{}],
                                    "GeometryNodeSetShadeSmooth": [
                                        {"domain": ["ENUM", "EDGE"]}
                                    ],
                                    "GeometryNodeSetSplineCyclic": [{}],
                                    "GeometryNodeSetSplineResolution": [{}],
                                    "GeometryNodeSimulationInput": [
                                        {"paired_output": ["NODE", None]}
                                    ],
                                    "GeometryNodeSimulationOutput": [
                                        {"state_items": ["ITEMS", None]}
                                    ],
                                    "GeometryNodeSortElements": [
                                        {"domain": ["ENUM", "POINT"]}
                                    ],
                                    "GeometryNodeSplineLength": [{}],
                                    "GeometryNodeSplineParameter": [{}],
                                    "GeometryNodeSplitEdges": [{}],
                                    "GeometryNodeSplitToInstances": [
                                        {"domain": ["ENUM", "POINT"]}
                                    ],
                                    "GeometryNodeStoreNamedAttribute": [
                                        {
                                            "data_type": ["ENUM", "FLOAT"],
                                            "domain": ["ENUM", "POINT"],
                                        }
                                    ],
                                    "GeometryNodeStoreNamedGrid": [
                                        {"data_type": ["ENUM", "FLOAT"]}
                                    ],
                                    "GeometryNodeStringJoin": [{}],
                                    "GeometryNodeStringToCurves": [
                                        {
                                            "align_x": ["ENUM", "LEFT"],
                                            "align_y": ["ENUM", "TOP_BASELINE"],
                                            "font": ["NONE", None],
                                            "overflow": ["ENUM", "OVERFLOW"],
                                            "pivot_mode": ["ENUM", "BOTTOM_LEFT"],
                                        }
                                    ],
                                    "GeometryNodeSubdivideCurve": [{}],
                                    "GeometryNodeSubdivideMesh": [{}],
                                    "GeometryNodeSubdivisionSurface": [
                                        {
                                            "boundary_smooth": ["ENUM", "ALL"],
                                            "uv_smooth": [
                                                "ENUM",
                                                "PRESERVE_BOUNDARIES",
                                            ],
                                        }
                                    ],
                                    "GeometryNodeSwitch": [
                                        {"input_type": ["ENUM", "GEOMETRY"]}
                                    ],
                                    "GeometryNodeTool3DCursor": [{}],
                                    "GeometryNodeToolActiveElement": [
                                        {"domain": ["ENUM", "POINT"]}
                                    ],
                                    "GeometryNodeToolFaceSet": [{}],
                                    "GeometryNodeToolMousePosition": [{}],
                                    "GeometryNodeToolSelection": [{}],
                                    "GeometryNodeToolSetFaceSet": [{}],
                                    "GeometryNodeToolSetSelection": [
                                        {
                                            "domain": ["ENUM", "POINT"],
                                            "selection_type": ["ENUM", "BOOLEAN"],
                                        }
                                    ],
                                    "GeometryNodeTransform": [
                                        {"mode": ["ENUM", "COMPONENTS"]}
                                    ],
                                    "GeometryNodeTranslateInstances": [{}],
                                    "GeometryNodeTriangulate": [
                                        {
                                            "ngon_method": ["ENUM", "BEAUTY"],
                                            "quad_method": ["ENUM", "BEAUTY"],
                                        }
                                    ],
                                    "GeometryNodeTrimCurve": [
                                        {"mode": ["ENUM", "FACTOR"]}
                                    ],
                                    "GeometryNodeUVPackIslands": [{}],
                                    "GeometryNodeUVUnwrap": [
                                        {"method": ["ENUM", "ANGLE_BASED"]}
                                    ],
                                    "GeometryNodeVertexOfCorner": [{}],
                                    "GeometryNodeViewer": [
                                        {
                                            "data_type": ["ENUM", "FLOAT"],
                                            "domain": ["ENUM", "POINT"],
                                            "ui_shortcut": ["INT", 0],
                                        }
                                    ],
                                    "GeometryNodeViewportTransform": [{}],
                                    "GeometryNodeVolumeCube": [{}],
                                    "GeometryNodeVolumeToMesh": [
                                        {"resolution_mode": ["ENUM", "GRID"]}
                                    ],
                                    "GeometryNodeWarning": [
                                        {"warning_type": ["ENUM", "ERROR"]}
                                    ],
                                },
                            ],
                            "ShaderNode": [
                                {},
                                {
                                    "ShaderNodeAddShader": [{}],
                                    "ShaderNodeAmbientOcclusion": [
                                        {
                                            "inside": ["BOOLEAN", False],
                                            "only_local": ["BOOLEAN", False],
                                            "samples": ["INT", 0],
                                        }
                                    ],
                                    "ShaderNodeAttribute": [
                                        {
                                            "attribute_name": ["STRING", ""],
                                            "attribute_type": ["ENUM", "GEOMETRY"],
                                        }
                                    ],
                                    "ShaderNodeBackground": [{}],
                                    "ShaderNodeBevel": [{"samples": ["INT", 0]}],
                                    "ShaderNodeBlackbody": [{}],
                                    "ShaderNodeBrightContrast": [{}],
                                    "ShaderNodeBsdfAnisotropic": [
                                        {"distribution": ["ENUM", "BECKMANN"]}
                                    ],
                                    "ShaderNodeBsdfDiffuse": [{}],
                                    "ShaderNodeBsdfGlass": [
                                        {"distribution": ["ENUM", "BECKMANN"]}
                                    ],
                                    "ShaderNodeBsdfHair": [
                                        {"component": ["ENUM", "Reflection"]}
                                    ],
                                    "ShaderNodeBsdfHairPrincipled": [
                                        {
                                            "model": ["ENUM", "HUANG"],
                                            "parametrization": ["ENUM", "COLOR"],
                                        }
                                    ],
                                    "ShaderNodeBsdfMetallic": [
                                        {
                                            "distribution": ["ENUM", "BECKMANN"],
                                            "fresnel_type": [
                                                "ENUM",
                                                "PHYSICAL_CONDUCTOR",
                                            ],
                                        }
                                    ],
                                    "ShaderNodeBsdfPrincipled": [
                                        {
                                            "distribution": ["ENUM", "GGX"],
                                            "subsurface_method": ["ENUM", "BURLEY"],
                                        }
                                    ],
                                    "ShaderNodeBsdfRayPortal": [{}],
                                    "ShaderNodeBsdfRefraction": [
                                        {"distribution": ["ENUM", "BECKMANN"]}
                                    ],
                                    "ShaderNodeBsdfSheen": [
                                        {"distribution": ["ENUM", "ASHIKHMIN"]}
                                    ],
                                    "ShaderNodeBsdfToon": [
                                        {"component": ["ENUM", "DIFFUSE"]}
                                    ],
                                    "ShaderNodeBsdfTranslucent": [{}],
                                    "ShaderNodeBsdfTransparent": [{}],
                                    "ShaderNodeBump": [{"invert": ["BOOLEAN", False]}],
                                    "ShaderNodeCameraData": [{}],
                                    "ShaderNodeClamp": [
                                        {"clamp_type": ["ENUM", "MINMAX"]}
                                    ],
                                    "ShaderNodeCombineColor": [
                                        {"mode": ["ENUM", "RGB"]}
                                    ],
                                    "ShaderNodeCombineHSV": [{}],
                                    "ShaderNodeCombineRGB": [{}],
                                    "ShaderNodeCombineXYZ": [{}],
                                    "ShaderNodeCustomGroup": [
                                        {"node_tree": ["NODETREE", None]}
                                    ],
                                    "ShaderNodeDisplacement": [
                                        {"space": ["ENUM", "OBJECT"]}
                                    ],
                                    "ShaderNodeEeveeSpecular": [{}],
                                    "ShaderNodeEmission": [{}],
                                    "ShaderNodeFloatCurve": [
                                        {"mapping": ["NONE", None]}
                                    ],
                                    "ShaderNodeFresnel": [{}],
                                    "ShaderNodeGamma": [{}],
                                    "ShaderNodeGroup": [
                                        {"node_tree": ["NODETREE", None]}
                                    ],
                                    "ShaderNodeHairInfo": [{}],
                                    "ShaderNodeHoldout": [{}],
                                    "ShaderNodeHueSaturation": [{}],
                                    "ShaderNodeInvert": [{}],
                                    "ShaderNodeLayerWeight": [{}],
                                    "ShaderNodeLightFalloff": [{}],
                                    "ShaderNodeLightPath": [{}],
                                    "ShaderNodeMapRange": [
                                        {
                                            "clamp": ["BOOLEAN", False],
                                            "data_type": ["ENUM", "FLOAT"],
                                            "interpolation_type": ["ENUM", "LINEAR"],
                                        }
                                    ],
                                    "ShaderNodeMapping": [
                                        {"vector_type": ["ENUM", "POINT"]}
                                    ],
                                    "ShaderNodeMath": [
                                        {
                                            "operation": ["ENUM", "ADD"],
                                            "use_clamp": ["BOOLEAN", False],
                                        }
                                    ],
                                    "ShaderNodeMix": [
                                        {
                                            "blend_type": ["ENUM", "MIX"],
                                            "clamp_factor": ["BOOLEAN", False],
                                            "clamp_result": ["BOOLEAN", False],
                                            "data_type": ["ENUM", "FLOAT"],
                                            "factor_mode": ["ENUM", "UNIFORM"],
                                        }
                                    ],
                                    "ShaderNodeMixRGB": [
                                        {
                                            "blend_type": ["ENUM", "MIX"],
                                            "use_alpha": ["BOOLEAN", False],
                                            "use_clamp": ["BOOLEAN", False],
                                        }
                                    ],
                                    "ShaderNodeMixShader": [{}],
                                    "ShaderNodeNewGeometry": [{}],
                                    "ShaderNodeNormal": [{}],
                                    "ShaderNodeNormalMap": [
                                        {
                                            "space": ["ENUM", "TANGENT"],
                                            "uv_map": ["STRING", ""],
                                        }
                                    ],
                                    "ShaderNodeObjectInfo": [{}],
                                    "ShaderNodeOutputAOV": [
                                        {"aov_name": ["STRING", ""]}
                                    ],
                                    "ShaderNodeOutputLight": [
                                        {
                                            "is_active_output": ["BOOLEAN", False],
                                            "target": ["ENUM", "ALL"],
                                        }
                                    ],
                                    "ShaderNodeOutputLineStyle": [
                                        {
                                            "blend_type": ["ENUM", "MIX"],
                                            "is_active_output": ["BOOLEAN", False],
                                            "target": ["ENUM", "ALL"],
                                            "use_alpha": ["BOOLEAN", False],
                                            "use_clamp": ["BOOLEAN", False],
                                        }
                                    ],
                                    "ShaderNodeOutputMaterial": [
                                        {
                                            "is_active_output": ["BOOLEAN", False],
                                            "target": ["ENUM", "ALL"],
                                        }
                                    ],
                                    "ShaderNodeOutputWorld": [
                                        {
                                            "is_active_output": ["BOOLEAN", False],
                                            "target": ["ENUM", "ALL"],
                                        }
                                    ],
                                    "ShaderNodeParticleInfo": [{}],
                                    "ShaderNodePointInfo": [{}],
                                    "ShaderNodeRGB": [{}],
                                    "ShaderNodeRGBCurve": [{"mapping": ["NONE", None]}],
                                    "ShaderNodeRGBToBW": [{}],
                                    "ShaderNodeScript": [
                                        {
                                            "bytecode": ["STRING", ""],
                                            "bytecode_hash": ["STRING", ""],
                                            "filepath": ["STRING", ""],
                                            "mode": ["ENUM", "INTERNAL"],
                                            "script": ["NONE", None],
                                            "use_auto_update": ["BOOLEAN", False],
                                        }
                                    ],
                                    "ShaderNodeSeparateColor": [
                                        {"mode": ["ENUM", "RGB"]}
                                    ],
                                    "ShaderNodeSeparateHSV": [{}],
                                    "ShaderNodeSeparateRGB": [{}],
                                    "ShaderNodeSeparateXYZ": [{}],
                                    "ShaderNodeShaderToRGB": [{}],
                                    "ShaderNodeSqueeze": [{}],
                                    "ShaderNodeSubsurfaceScattering": [
                                        {"falloff": ["ENUM", "BURLEY"]}
                                    ],
                                    "ShaderNodeTangent": [
                                        {
                                            "axis": ["ENUM", "X"],
                                            "direction_type": ["ENUM", "RADIAL"],
                                            "uv_map": ["STRING", ""],
                                        }
                                    ],
                                    "ShaderNodeTexBrick": [
                                        {
                                            "color_mapping": ["NONE", None],
                                            "offset": ["FLOAT", 0.5],
                                            "offset_frequency": ["INT", 2],
                                            "squash": ["FLOAT", 1.0],
                                            "squash_frequency": ["INT", 2],
                                            "texture_mapping": ["NONE", None],
                                        }
                                    ],
                                    "ShaderNodeTexChecker": [
                                        {
                                            "color_mapping": ["NONE", None],
                                            "texture_mapping": ["NONE", None],
                                        }
                                    ],
                                    "ShaderNodeTexCoord": [
                                        {
                                            "from_instancer": ["BOOLEAN", False],
                                            "object": ["OBJECT", None],
                                        }
                                    ],
                                    "ShaderNodeTexEnvironment": [
                                        {
                                            "color_mapping": ["NONE", None],
                                            "image": ["IMAGE", None],
                                            "image_user": ["NONE", None],
                                            "interpolation": ["ENUM", "Linear"],
                                            "projection": ["ENUM", "EQUIRECTANGULAR"],
                                            "texture_mapping": ["NONE", None],
                                        }
                                    ],
                                    "ShaderNodeTexGabor": [
                                        {
                                            "color_mapping": ["NONE", None],
                                            "gabor_type": ["ENUM", "2D"],
                                            "texture_mapping": ["NONE", None],
                                        }
                                    ],
                                    "ShaderNodeTexGradient": [
                                        {
                                            "color_mapping": ["NONE", None],
                                            "gradient_type": ["ENUM", "LINEAR"],
                                            "texture_mapping": ["NONE", None],
                                        }
                                    ],
                                    "ShaderNodeTexIES": [
                                        {
                                            "filepath": ["STRING", ""],
                                            "ies": ["NONE", None],
                                            "mode": ["ENUM", "INTERNAL"],
                                        }
                                    ],
                                    "ShaderNodeTexImage": [
                                        {
                                            "color_mapping": ["NONE", None],
                                            "extension": ["ENUM", "REPEAT"],
                                            "image": ["IMAGE", None],
                                            "image_user": ["NONE", None],
                                            "interpolation": ["ENUM", "Linear"],
                                            "projection": ["ENUM", "FLAT"],
                                            "projection_blend": ["FLOAT", 0.0],
                                            "texture_mapping": ["NONE", None],
                                        }
                                    ],
                                    "ShaderNodeTexMagic": [
                                        {
                                            "color_mapping": ["NONE", None],
                                            "texture_mapping": ["NONE", None],
                                            "turbulence_depth": ["INT", 0],
                                        }
                                    ],
                                    "ShaderNodeTexNoise": [
                                        {
                                            "color_mapping": ["NONE", None],
                                            "noise_dimensions": ["ENUM", "1D"],
                                            "noise_type": ["ENUM", "MULTIFRACTAL"],
                                            "normalize": ["BOOLEAN", False],
                                            "texture_mapping": ["NONE", None],
                                        }
                                    ],
                                    "ShaderNodeTexPointDensity": [
                                        {
                                            "interpolation": ["ENUM", "Linear"],
                                            "object": ["OBJECT", None],
                                            "particle_color_source": [
                                                "ENUM",
                                                "PARTICLE_AGE",
                                            ],
                                            "particle_system": ["NONE", None],
                                            "point_source": ["ENUM", "PARTICLE_SYSTEM"],
                                            "radius": ["FLOAT", 0.0],
                                            "resolution": ["INT", 0],
                                            "space": ["ENUM", "OBJECT"],
                                            "vertex_attribute_name": ["STRING", ""],
                                            "vertex_color_source": [
                                                "ENUM",
                                                "VERTEX_COLOR",
                                            ],
                                        }
                                    ],
                                    "ShaderNodeTexSky": [
                                        {
                                            "air_density": ["FLOAT", 1.0],
                                            "altitude": ["FLOAT", 0.0],
                                            "color_mapping": ["NONE", None],
                                            "dust_density": ["FLOAT", 1.0],
                                            "ground_albedo": ["FLOAT", 0.0],
                                            "ozone_density": ["FLOAT", 1.0],
                                            "sky_type": ["ENUM", "PREETHAM"],
                                            "sun_direction": ["LIST", 0.0],
                                            "sun_disc": ["BOOLEAN", True],
                                            "sun_elevation": [
                                                "FLOAT",
                                                1.5707963705062866,
                                            ],
                                            "sun_intensity": ["FLOAT", 1.0],
                                            "sun_rotation": ["FLOAT", 0.0],
                                            "sun_size": ["FLOAT", 0.009512044489383698],
                                            "texture_mapping": ["NONE", None],
                                            "turbidity": ["FLOAT", 0.0],
                                        }
                                    ],
                                    "ShaderNodeTexVoronoi": [
                                        {
                                            "color_mapping": ["NONE", None],
                                            "distance": ["ENUM", "EUCLIDEAN"],
                                            "feature": ["ENUM", "F1"],
                                            "normalize": ["BOOLEAN", False],
                                            "texture_mapping": ["NONE", None],
                                            "voronoi_dimensions": ["ENUM", "1D"],
                                        }
                                    ],
                                    "ShaderNodeTexWave": [
                                        {
                                            "bands_direction": ["ENUM", "X"],
                                            "color_mapping": ["NONE", None],
                                            "rings_direction": ["ENUM", "X"],
                                            "texture_mapping": ["NONE", None],
                                            "wave_profile": ["ENUM", "SIN"],
                                            "wave_type": ["ENUM", "BANDS"],
                                        }
                                    ],
                                    "ShaderNodeTexWhiteNoise": [
                                        {"noise_dimensions": ["ENUM", "1D"]}
                                    ],
                                    "ShaderNodeUVAlongStroke": [
                                        {"use_tips": ["BOOLEAN", False]}
                                    ],
                                    "ShaderNodeUVMap": [
                                        {
                                            "from_instancer": ["BOOLEAN", False],
                                            "uv_map": ["STRING", ""],
                                        }
                                    ],
                                    "ShaderNodeValToRGB": [
                                        {"color_ramp": ["NONE", None]}
                                    ],
                                    "ShaderNodeValue": [{}],
                                    "ShaderNodeVectorCurve": [
                                        {"mapping": ["NONE", None]}
                                    ],
                                    "ShaderNodeVectorDisplacement": [
                                        {"space": ["ENUM", "TANGENT"]}
                                    ],
                                    "ShaderNodeVectorMath": [
                                        {"operation": ["ENUM", "ADD"]}
                                    ],
                                    "ShaderNodeVectorRotate": [
                                        {
                                            "invert": ["BOOLEAN", False],
                                            "rotation_type": ["ENUM", "AXIS_ANGLE"],
                                        }
                                    ],
                                    "ShaderNodeVectorTransform": [
                                        {
                                            "convert_from": ["ENUM", "WORLD"],
                                            "convert_to": ["ENUM", "WORLD"],
                                            "vector_type": ["ENUM", "VECTOR"],
                                        }
                                    ],
                                    "ShaderNodeVertexColor": [
                                        {"layer_name": ["STRING", ""]}
                                    ],
                                    "ShaderNodeVolumeAbsorption": [{}],
                                    "ShaderNodeVolumeCoefficients": [
                                        {"phase": ["ENUM", "HENYEY_GREENSTEIN"]}
                                    ],
                                    "ShaderNodeVolumeInfo": [{}],
                                    "ShaderNodeVolumePrincipled": [{}],
                                    "ShaderNodeVolumeScatter": [
                                        {"phase": ["ENUM", "HENYEY_GREENSTEIN"]}
                                    ],
                                    "ShaderNodeWavelength": [{}],
                                    "ShaderNodeWireframe": [
                                        {"use_pixel_size": ["BOOLEAN", False]}
                                    ],
                                },
                            ],
                        },
                    ]
                },
            ],
            "NodeSocket": [
                {"bl_idname": ["STRING", ""]},
                {
                    "NodeSocketStandard": [
                        {},
                        {
                            "NodeSocketBool": [{"default_value": ["BOOLEAN", False]}],
                            "NodeSocketBundle": [{}],
                            "NodeSocketClosure": [{}],
                            "NodeSocketCollection": [
                                {"default_value": ["COLLECTION", None]}
                            ],
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
                            "NodeSocketImage": [{"default_value": ["IMAGE", None]}],
                            "NodeSocketInt": [{"default_value": ["INT", 0]}],
                            "NodeSocketIntFactor": [{"default_value": ["INT", 1]}],
                            "NodeSocketIntPercentage": [
                                {"default_value": ["INT", 100]}
                            ],
                            "NodeSocketIntUnsigned": [{"default_value": ["INT", 0]}],
                            "NodeSocketMaterial": [
                                {"default_value": ["MATERIAL", None]}
                            ],
                            "NodeSocketMatrix": [{}],
                            "NodeSocketMenu": [{"default_value": ["ENUM", ""]}],
                            "NodeSocketObject": [{"default_value": ["OBJECT", None]}],
                            "NodeSocketRotation": [{"default_value": ["LIST", 0.0]}],
                            "NodeSocketShader": [{}],
                            "NodeSocketString": [{"default_value": ["STRING", ""]}],
                            "NodeSocketStringFilePath": [
                                {"default_value": ["STRING", ""]}
                            ],
                            "NodeSocketTexture": [{"default_value": ["NONE", None]}],
                            "NodeSocketVector": [{"default_value": ["LIST", 0.0]}],
                            "NodeSocketVector2D": [{"default_value": ["LIST", 0.0]}],
                            "NodeSocketVector4D": [{"default_value": ["LIST", 0.0]}],
                            "NodeSocketVectorAcceleration": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorAcceleration2D": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorAcceleration4D": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorDirection": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorDirection2D": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorDirection4D": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorEuler": [{"default_value": ["LIST", 0.0]}],
                            "NodeSocketVectorEuler2D": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorEuler4D": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorFactor": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorFactor2D": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorFactor4D": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorPercentage": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorPercentage2D": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorPercentage4D": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorTranslation": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorTranslation2D": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorTranslation4D": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorVelocity": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorVelocity2D": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorVelocity4D": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeSocketVectorXYZ": [{"default_value": ["LIST", 0.0]}],
                            "NodeSocketVectorXYZ2D": [{"default_value": ["LIST", 0.0]}],
                            "NodeSocketVectorXYZ4D": [{"default_value": ["LIST", 0.0]}],
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
                            "NodeTreeInterfaceSocketBundle": [{}],
                            "NodeTreeInterfaceSocketClosure": [{}],
                            "NodeTreeInterfaceSocketCollection": [
                                {"default_value": ["COLLECTION", None]}
                            ],
                            "NodeTreeInterfaceSocketColor": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeTreeInterfaceSocketFloat": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatAngle": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatColorTemperature": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatDistance": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatFactor": [
                                {
                                    "default_value": ["FLOAT", 1.0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatFrequency": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatPercentage": [
                                {
                                    "default_value": ["FLOAT", 100.0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatTime": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatTimeAbsolute": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatUnsigned": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketFloatWavelength": [
                                {
                                    "default_value": ["FLOAT", 0.0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketGeometry": [{}],
                            "NodeTreeInterfaceSocketImage": [
                                {"default_value": ["IMAGE", None]}
                            ],
                            "NodeTreeInterfaceSocketInt": [
                                {
                                    "default_value": ["INT", 0],
                                    "max_value": ["INT", 2147483647],
                                    "min_value": ["INT", -2147483648],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketIntFactor": [
                                {
                                    "default_value": ["INT", 0],
                                    "max_value": ["INT", 2147483647],
                                    "min_value": ["INT", -2147483648],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketIntPercentage": [
                                {
                                    "default_value": ["INT", 0],
                                    "max_value": ["INT", 2147483647],
                                    "min_value": ["INT", -2147483648],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketIntUnsigned": [
                                {
                                    "default_value": ["INT", 0],
                                    "max_value": ["INT", 2147483647],
                                    "min_value": ["INT", -2147483648],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketMaterial": [
                                {"default_value": ["MATERIAL", None]}
                            ],
                            "NodeTreeInterfaceSocketMatrix": [{}],
                            "NodeTreeInterfaceSocketMenu": [
                                {"default_value": ["ENUM", ""]}
                            ],
                            "NodeTreeInterfaceSocketObject": [
                                {"default_value": ["OBJECT", None]}
                            ],
                            "NodeTreeInterfaceSocketRotation": [
                                {"default_value": ["LIST", 0.0]}
                            ],
                            "NodeTreeInterfaceSocketShader": [{}],
                            "NodeTreeInterfaceSocketString": [
                                {
                                    "default_value": ["STRING", ""],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketStringFilePath": [
                                {
                                    "default_value": ["STRING", ""],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketTexture": [
                                {"default_value": ["NONE", None]}
                            ],
                            "NodeTreeInterfaceSocketVector": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVector2D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVector4D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorAcceleration": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorAcceleration2D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorAcceleration4D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorDirection": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorDirection2D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorDirection4D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorEuler": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorEuler2D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorEuler4D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorFactor": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorFactor2D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorFactor4D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorPercentage": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorPercentage2D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorPercentage4D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorTranslation": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorTranslation2D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorTranslation4D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorVelocity": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorVelocity2D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorVelocity4D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorXYZ": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorXYZ2D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
                                }
                            ],
                            "NodeTreeInterfaceSocketVectorXYZ4D": [
                                {
                                    "default_value": ["LIST", 0.0],
                                    "dimensions": ["INT", 0],
                                    "max_value": ["FLOAT", -3.4028234663852886e38],
                                    "min_value": ["FLOAT", -3.4028234663852886e38],
                                    "subtype": ["ENUM", "DEFAULT"],
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
    "ENUM",
    "FLOAT",
    "IMAGE",
    "INT",
    "ITEMS",
    "LIST",
    "MATERIAL",
    "NODE",
    "NODETREE",
    "NONE",
    "OBJECT",
    "STRING",
]
