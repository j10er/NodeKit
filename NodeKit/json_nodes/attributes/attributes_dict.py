DEFAULTS = {
    "Node": {
        "attributes": {
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
            "parent": ["NODE", None],
            "use_custom_color": ["BOOLEAN", False],
            "warning_propagation": ["STRING", "ALL"],
            "width": ["FLOAT", 140],
        },
        "subtypes": {
            "NodeInternal": {
                "attributes": {
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
                    "parent": ["NODE", None],
                    "use_custom_color": ["BOOLEAN", False],
                    "warning_propagation": ["STRING", "ALL"],
                    "width": ["FLOAT", 140],
                },
                "subtypes": {
                    "CompositorNode": {
                        "attributes": {},
                        "subtypes": {
                            "CompositorNodeAlphaOver": {
                                "attributes": {
                                    "premul": ["FLOAT", 0.0],
                                    "use_premultiply": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeAntiAliasing": {
                                "attributes": {
                                    "contrast_limit": ["FLOAT", 0.0],
                                    "corner_rounding": ["FLOAT", 0.0],
                                    "threshold": ["FLOAT", 0.0],
                                }
                            },
                            "CompositorNodeBilateralblur": {
                                "attributes": {
                                    "iterations": ["INT", 0],
                                    "sigma_color": ["FLOAT", 0.0],
                                    "sigma_space": ["FLOAT", 0.0],
                                }
                            },
                            "CompositorNodeBlur": {
                                "attributes": {
                                    "aspect_correction": ["ENUM", "NONE"],
                                    "factor": ["FLOAT", 0.0],
                                    "factor_x": ["FLOAT", 0.0],
                                    "factor_y": ["FLOAT", 0.0],
                                    "filter_type": ["ENUM", "FLAT"],
                                    "size_x": ["INT", 0],
                                    "size_y": ["INT", 0],
                                    "use_bokeh": ["BOOLEAN", False],
                                    "use_extended_bounds": ["BOOLEAN", False],
                                    "use_gamma_correction": ["BOOLEAN", False],
                                    "use_relative": ["BOOLEAN", False],
                                    "use_variable_size": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeBokehBlur": {
                                "attributes": {
                                    "blur_max": ["FLOAT", 0.0],
                                    "use_extended_bounds": ["BOOLEAN", False],
                                    "use_variable_size": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeBokehImage": {
                                "attributes": {
                                    "angle": ["FLOAT", 0.0],
                                    "catadioptric": ["FLOAT", 0.0],
                                    "flaps": ["INT", 5],
                                    "rounding": ["FLOAT", 0.0],
                                    "shift": ["FLOAT", 0.0],
                                }
                            },
                            "CompositorNodeBoxMask": {
                                "attributes": {
                                    "mask_height": ["FLOAT", 0.20000000298023224],
                                    "mask_type": ["ENUM", "ADD"],
                                    "mask_width": ["FLOAT", 0.30000001192092896],
                                    "rotation": ["FLOAT", 0.0],
                                    "x": ["FLOAT", 0.5],
                                    "y": ["FLOAT", 0.5],
                                }
                            },
                            "CompositorNodeBrightContrast": {
                                "attributes": {"use_premultiply": ["BOOLEAN", False]}
                            },
                            "CompositorNodeChannelMatte": {
                                "attributes": {
                                    "color_space": ["ENUM", "RGB"],
                                    "limit_channel": ["ENUM", "R"],
                                    "limit_max": ["FLOAT", 0.0],
                                    "limit_method": ["ENUM", "SINGLE"],
                                    "limit_min": ["FLOAT", 0.0],
                                    "matte_channel": ["ENUM", "R"],
                                }
                            },
                            "CompositorNodeChromaMatte": {
                                "attributes": {
                                    "gain": ["FLOAT", 0.0],
                                    "lift": ["FLOAT", 0.0],
                                    "shadow_adjust": ["FLOAT", 0.0],
                                    "threshold": ["FLOAT", 0.0],
                                    "tolerance": ["FLOAT", 0.0],
                                }
                            },
                            "CompositorNodeColorBalance": {
                                "attributes": {
                                    "correction_method": ["ENUM", "LIFT_GAMMA_GAIN"],
                                    "gain": ["LIST", 0.0],
                                    "gamma": ["LIST", 0.0],
                                    "input_temperature": ["FLOAT", 6500.0],
                                    "input_tint": ["FLOAT", 10.0],
                                    "input_whitepoint": ["LIST", 0.0],
                                    "lift": ["LIST", 0.0],
                                    "offset": ["LIST", 0.0],
                                    "offset_basis": ["FLOAT", 0.0],
                                    "output_temperature": ["FLOAT", 6500.0],
                                    "output_tint": ["FLOAT", 10.0],
                                    "output_whitepoint": ["LIST", 0.0],
                                    "power": ["LIST", 0.0],
                                    "slope": ["LIST", 0.0],
                                }
                            },
                            "CompositorNodeColorCorrection": {
                                "attributes": {
                                    "blue": ["BOOLEAN", True],
                                    "green": ["BOOLEAN", True],
                                    "highlights_contrast": ["FLOAT", 1.0],
                                    "highlights_gain": ["FLOAT", 1.0],
                                    "highlights_gamma": ["FLOAT", 1.0],
                                    "highlights_lift": ["FLOAT", 0.0],
                                    "highlights_saturation": ["FLOAT", 1.0],
                                    "master_contrast": ["FLOAT", 1.0],
                                    "master_gain": ["FLOAT", 1.0],
                                    "master_gamma": ["FLOAT", 1.0],
                                    "master_lift": ["FLOAT", 0.0],
                                    "master_saturation": ["FLOAT", 1.0],
                                    "midtones_contrast": ["FLOAT", 1.0],
                                    "midtones_end": ["FLOAT", 0.699999988079071],
                                    "midtones_gain": ["FLOAT", 1.0],
                                    "midtones_gamma": ["FLOAT", 1.0],
                                    "midtones_lift": ["FLOAT", 0.0],
                                    "midtones_saturation": ["FLOAT", 1.0],
                                    "midtones_start": ["FLOAT", 0.20000000298023224],
                                    "red": ["BOOLEAN", True],
                                    "shadows_contrast": ["FLOAT", 1.0],
                                    "shadows_gain": ["FLOAT", 1.0],
                                    "shadows_gamma": ["FLOAT", 1.0],
                                    "shadows_lift": ["FLOAT", 0.0],
                                    "shadows_saturation": ["FLOAT", 1.0],
                                }
                            },
                            "CompositorNodeColorMatte": {
                                "attributes": {
                                    "color_hue": ["FLOAT", 0.0],
                                    "color_saturation": ["FLOAT", 0.0],
                                    "color_value": ["FLOAT", 0.0],
                                }
                            },
                            "CompositorNodeColorSpill": {
                                "attributes": {
                                    "channel": ["ENUM", "R"],
                                    "limit_channel": ["ENUM", "R"],
                                    "limit_method": ["ENUM", "SIMPLE"],
                                    "ratio": ["FLOAT", 0.0],
                                    "unspill_blue": ["FLOAT", 0.0],
                                    "unspill_green": ["FLOAT", 0.0],
                                    "unspill_red": ["FLOAT", 0.0],
                                    "use_unspill": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeCombHSVA": {"attributes": {}},
                            "CompositorNodeCombRGBA": {"attributes": {}},
                            "CompositorNodeCombYCCA": {
                                "attributes": {"mode": ["ENUM", "ITUBT601"]}
                            },
                            "CompositorNodeCombYUVA": {"attributes": {}},
                            "CompositorNodeCombineColor": {
                                "attributes": {
                                    "mode": ["ENUM", "RGB"],
                                    "ycc_mode": ["ENUM", "ITUBT601"],
                                }
                            },
                            "CompositorNodeCombineXYZ": {"attributes": {}},
                            "CompositorNodeComposite": {
                                "attributes": {"use_alpha": ["BOOLEAN", False]}
                            },
                            "CompositorNodeConvertColorSpace": {
                                "attributes": {
                                    "from_color_space": ["ENUM", "NONE"],
                                    "to_color_space": ["ENUM", "NONE"],
                                }
                            },
                            "CompositorNodeCornerPin": {
                                "attributes": {"interpolation": ["ENUM", "ANISOTROPIC"]}
                            },
                            "CompositorNodeCrop": {
                                "attributes": {
                                    "max_x": ["INT", 0],
                                    "max_y": ["INT", 0],
                                    "min_x": ["INT", 0],
                                    "min_y": ["INT", 0],
                                    "rel_max_x": ["FLOAT", 0.0],
                                    "rel_max_y": ["FLOAT", 0.0],
                                    "rel_min_x": ["FLOAT", 0.0],
                                    "rel_min_y": ["FLOAT", 0.0],
                                    "relative": ["BOOLEAN", False],
                                    "use_crop_size": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeCryptomatte": {
                                "attributes": {
                                    "add": ["LIST", 0.0],
                                    "matte_id": ["STRING", ""],
                                    "remove": ["LIST", 0.0],
                                }
                            },
                            "CompositorNodeCryptomatteV2": {
                                "attributes": {
                                    "add": ["LIST", 0.0],
                                    "entries": ["ITEMS", None],
                                    "frame_duration": ["INT", 0],
                                    "frame_offset": ["INT", 0],
                                    "frame_start": ["INT", 0],
                                    "has_layers": ["BOOLEAN", False],
                                    "has_views": ["BOOLEAN", False],
                                    "image": ["IMAGE", None],
                                    "layer": ["ENUM", "PLACEHOLDER"],
                                    "layer_name": ["ENUM", "CryptoObject"],
                                    "matte_id": ["STRING", ""],
                                    "remove": ["LIST", 0.0],
                                    "scene": ["NONE", None],
                                    "source": ["ENUM", "RENDER"],
                                    "use_auto_refresh": ["BOOLEAN", False],
                                    "use_cyclic": ["BOOLEAN", False],
                                    "view": ["ENUM", "ALL"],
                                }
                            },
                            "CompositorNodeCurveRGB": {
                                "attributes": {"mapping": ["NONE", None]}
                            },
                            "CompositorNodeCurveVec": {
                                "attributes": {"mapping": ["NONE", None]}
                            },
                            "CompositorNodeCustomGroup": {
                                "attributes": {"node_tree": ["NODETREE", None]}
                            },
                            "CompositorNodeDBlur": {
                                "attributes": {
                                    "angle": ["FLOAT", 0.0],
                                    "center_x": ["FLOAT", 0.0],
                                    "center_y": ["FLOAT", 0.0],
                                    "distance": ["FLOAT", 0.0],
                                    "iterations": ["INT", 0],
                                    "spin": ["FLOAT", 0.0],
                                    "zoom": ["FLOAT", 0.0],
                                }
                            },
                            "CompositorNodeDefocus": {
                                "attributes": {
                                    "angle": ["FLOAT", 0.0],
                                    "blur_max": ["FLOAT", 0.0],
                                    "bokeh": ["ENUM", "CIRCLE"],
                                    "f_stop": ["FLOAT", 0.0],
                                    "scene": ["NONE", None],
                                    "threshold": ["FLOAT", 0.0],
                                    "use_gamma_correction": ["BOOLEAN", False],
                                    "use_preview": ["BOOLEAN", False],
                                    "use_zbuffer": ["BOOLEAN", False],
                                    "z_scale": ["FLOAT", 0.0],
                                }
                            },
                            "CompositorNodeDenoise": {
                                "attributes": {
                                    "prefilter": ["ENUM", "ACCURATE"],
                                    "quality": ["ENUM", "FOLLOW_SCENE"],
                                    "use_hdr": ["BOOLEAN", True],
                                }
                            },
                            "CompositorNodeDespeckle": {
                                "attributes": {
                                    "threshold": ["FLOAT", 0.0],
                                    "threshold_neighbor": ["FLOAT", 0.0],
                                }
                            },
                            "CompositorNodeDiffMatte": {
                                "attributes": {
                                    "falloff": ["FLOAT", 0.0],
                                    "tolerance": ["FLOAT", 0.0],
                                }
                            },
                            "CompositorNodeDilateErode": {
                                "attributes": {
                                    "distance": ["INT", 0],
                                    "edge": ["FLOAT", 0.0],
                                    "falloff": ["ENUM", "SMOOTH"],
                                    "mode": ["ENUM", "STEP"],
                                }
                            },
                            "CompositorNodeDisplace": {"attributes": {}},
                            "CompositorNodeDistanceMatte": {
                                "attributes": {
                                    "channel": ["ENUM", "RGB"],
                                    "falloff": ["FLOAT", 0.0],
                                    "tolerance": ["FLOAT", 0.0],
                                }
                            },
                            "CompositorNodeDoubleEdgeMask": {
                                "attributes": {
                                    "edge_mode": ["ENUM", "BLEED_OUT"],
                                    "inner_mode": ["ENUM", "ALL"],
                                }
                            },
                            "CompositorNodeEllipseMask": {
                                "attributes": {
                                    "mask_height": ["FLOAT", 0.20000000298023224],
                                    "mask_type": ["ENUM", "ADD"],
                                    "mask_width": ["FLOAT", 0.30000001192092896],
                                    "rotation": ["FLOAT", 0.0],
                                    "x": ["FLOAT", 0.5],
                                    "y": ["FLOAT", 0.5],
                                }
                            },
                            "CompositorNodeExposure": {"attributes": {}},
                            "CompositorNodeFilter": {
                                "attributes": {"filter_type": ["ENUM", "SOFTEN"]}
                            },
                            "CompositorNodeFlip": {
                                "attributes": {"axis": ["ENUM", "X"]}
                            },
                            "CompositorNodeGamma": {"attributes": {}},
                            "CompositorNodeGlare": {
                                "attributes": {
                                    "angle_offset": ["FLOAT", 0.0],
                                    "color_modulation": ["FLOAT", 0.0],
                                    "fade": ["FLOAT", 0.0],
                                    "glare_type": ["ENUM", "SIMPLE_STAR"],
                                    "iterations": ["INT", 0],
                                    "mix": ["FLOAT", 0.0],
                                    "quality": ["ENUM", "HIGH"],
                                    "size": ["INT", 0],
                                    "streaks": ["INT", 0],
                                    "threshold": ["FLOAT", 0.0],
                                    "use_rotate_45": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeGroup": {
                                "attributes": {"node_tree": ["NODETREE", None]}
                            },
                            "CompositorNodeHueCorrect": {
                                "attributes": {"mapping": ["NONE", None]}
                            },
                            "CompositorNodeHueSat": {"attributes": {}},
                            "CompositorNodeIDMask": {
                                "attributes": {
                                    "index": ["INT", 0],
                                    "use_antialiasing": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeImage": {
                                "attributes": {
                                    "frame_duration": ["INT", 0],
                                    "frame_offset": ["INT", 0],
                                    "frame_start": ["INT", 0],
                                    "has_layers": ["BOOLEAN", False],
                                    "has_views": ["BOOLEAN", False],
                                    "image": ["IMAGE", None],
                                    "layer": ["ENUM", "PLACEHOLDER"],
                                    "use_auto_refresh": ["BOOLEAN", False],
                                    "use_cyclic": ["BOOLEAN", False],
                                    "use_straight_alpha_output": ["BOOLEAN", False],
                                    "view": ["ENUM", "ALL"],
                                }
                            },
                            "CompositorNodeImageCoordinates": {"attributes": {}},
                            "CompositorNodeImageInfo": {"attributes": {}},
                            "CompositorNodeInpaint": {
                                "attributes": {"distance": ["INT", 0]}
                            },
                            "CompositorNodeInvert": {
                                "attributes": {
                                    "invert_alpha": ["BOOLEAN", False],
                                    "invert_rgb": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeKeying": {
                                "attributes": {
                                    "blur_post": ["INT", 0],
                                    "blur_pre": ["INT", 0],
                                    "clip_black": ["FLOAT", 0.0],
                                    "clip_white": ["FLOAT", 0.0],
                                    "despill_balance": ["FLOAT", 0.0],
                                    "despill_factor": ["FLOAT", 0.0],
                                    "dilate_distance": ["INT", 0],
                                    "edge_kernel_radius": ["INT", 0],
                                    "edge_kernel_tolerance": ["FLOAT", 0.0],
                                    "feather_distance": ["INT", 0],
                                    "feather_falloff": ["ENUM", "SMOOTH"],
                                    "screen_balance": ["FLOAT", 0.0],
                                }
                            },
                            "CompositorNodeKeyingScreen": {
                                "attributes": {
                                    "clip": ["NONE", None],
                                    "smoothness": ["FLOAT", 0.0],
                                    "tracking_object": ["STRING", ""],
                                }
                            },
                            "CompositorNodeKuwahara": {
                                "attributes": {
                                    "eccentricity": ["FLOAT", 0.0],
                                    "sharpness": ["FLOAT", 0.0],
                                    "uniformity": ["INT", 0],
                                    "use_high_precision": ["BOOLEAN", False],
                                    "variation": ["ENUM", "CLASSIC"],
                                }
                            },
                            "CompositorNodeLensdist": {
                                "attributes": {
                                    "distortion_type": ["ENUM", "RADIAL"],
                                    "use_fit": ["BOOLEAN", False],
                                    "use_jitter": ["BOOLEAN", False],
                                    "use_projector": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeLevels": {
                                "attributes": {"channel": ["ENUM", "COMBINED_RGB"]}
                            },
                            "CompositorNodeLumaMatte": {
                                "attributes": {
                                    "limit_max": ["FLOAT", 0.0],
                                    "limit_min": ["FLOAT", 0.0],
                                }
                            },
                            "CompositorNodeMapRange": {
                                "attributes": {"use_clamp": ["BOOLEAN", False]}
                            },
                            "CompositorNodeMapUV": {
                                "attributes": {
                                    "alpha": ["INT", 0],
                                    "filter_type": ["ENUM", "NEAREST"],
                                }
                            },
                            "CompositorNodeMapValue": {
                                "attributes": {
                                    "max": ["LIST", 0.0],
                                    "min": ["LIST", 0.0],
                                    "offset": ["LIST", 0.0],
                                    "size": ["LIST", 0.0],
                                    "use_max": ["BOOLEAN", False],
                                    "use_min": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeMask": {
                                "attributes": {
                                    "mask": ["NONE", None],
                                    "motion_blur_samples": ["INT", 0],
                                    "motion_blur_shutter": ["FLOAT", 0.0],
                                    "size_source": ["ENUM", "SCENE"],
                                    "size_x": ["INT", 0],
                                    "size_y": ["INT", 0],
                                    "use_feather": ["BOOLEAN", False],
                                    "use_motion_blur": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeMath": {
                                "attributes": {
                                    "operation": ["ENUM", "ADD"],
                                    "use_clamp": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeMixRGB": {
                                "attributes": {
                                    "blend_type": ["ENUM", "MIX"],
                                    "use_alpha": ["BOOLEAN", False],
                                    "use_clamp": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeMovieClip": {
                                "attributes": {"clip": ["NONE", None]}
                            },
                            "CompositorNodeMovieDistortion": {
                                "attributes": {
                                    "clip": ["NONE", None],
                                    "distortion_type": ["ENUM", "UNDISTORT"],
                                }
                            },
                            "CompositorNodeNormal": {"attributes": {}},
                            "CompositorNodeNormalize": {"attributes": {}},
                            "CompositorNodeOutputFile": {
                                "attributes": {
                                    "active_input_index": ["INT", 0],
                                    "base_path": ["STRING", ""],
                                    "file_slots": ["ITEMS", None],
                                    "format": ["NONE", None],
                                    "layer_slots": ["ITEMS", None],
                                    "save_as_render": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodePixelate": {
                                "attributes": {"pixel_size": ["INT", 1]}
                            },
                            "CompositorNodePlaneTrackDeform": {
                                "attributes": {
                                    "clip": ["NONE", None],
                                    "motion_blur_samples": ["INT", 0],
                                    "motion_blur_shutter": ["FLOAT", 0.0],
                                    "plane_track_name": ["STRING", ""],
                                    "tracking_object": ["STRING", ""],
                                    "use_motion_blur": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodePosterize": {"attributes": {}},
                            "CompositorNodePremulKey": {
                                "attributes": {
                                    "mapping": ["ENUM", "STRAIGHT_TO_PREMUL"]
                                }
                            },
                            "CompositorNodeRGB": {"attributes": {}},
                            "CompositorNodeRGBToBW": {"attributes": {}},
                            "CompositorNodeRLayers": {
                                "attributes": {
                                    "layer": ["ENUM", "PLACEHOLDER"],
                                    "scene": ["NONE", None],
                                }
                            },
                            "CompositorNodeRelativeToPixel": {
                                "attributes": {
                                    "data_type": ["ENUM", "FLOAT"],
                                    "reference_dimension": ["ENUM", "X"],
                                }
                            },
                            "CompositorNodeRotate": {
                                "attributes": {"filter_type": ["ENUM", "NEAREST"]}
                            },
                            "CompositorNodeScale": {
                                "attributes": {
                                    "frame_method": ["ENUM", "STRETCH"],
                                    "interpolation": ["ENUM", "NEAREST"],
                                    "offset_x": ["FLOAT", 0.0],
                                    "offset_y": ["FLOAT", 0.0],
                                    "space": ["ENUM", "RELATIVE"],
                                }
                            },
                            "CompositorNodeSceneTime": {"attributes": {}},
                            "CompositorNodeSepHSVA": {"attributes": {}},
                            "CompositorNodeSepRGBA": {"attributes": {}},
                            "CompositorNodeSepYCCA": {
                                "attributes": {"mode": ["ENUM", "ITUBT601"]}
                            },
                            "CompositorNodeSepYUVA": {"attributes": {}},
                            "CompositorNodeSeparateColor": {
                                "attributes": {
                                    "mode": ["ENUM", "RGB"],
                                    "ycc_mode": ["ENUM", "ITUBT601"],
                                }
                            },
                            "CompositorNodeSeparateXYZ": {"attributes": {}},
                            "CompositorNodeSetAlpha": {
                                "attributes": {"mode": ["ENUM", "APPLY"]}
                            },
                            "CompositorNodeSplit": {
                                "attributes": {
                                    "axis": ["ENUM", "X"],
                                    "factor": ["INT", 0],
                                }
                            },
                            "CompositorNodeStabilize": {
                                "attributes": {
                                    "clip": ["NONE", None],
                                    "filter_type": ["ENUM", "NEAREST"],
                                    "invert": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeSunBeams": {
                                "attributes": {
                                    "ray_length": ["FLOAT", 0.0],
                                    "source": ["LIST", 0.0],
                                }
                            },
                            "CompositorNodeSwitch": {
                                "attributes": {"check": ["BOOLEAN", False]}
                            },
                            "CompositorNodeSwitchView": {"attributes": {}},
                            "CompositorNodeTexture": {
                                "attributes": {
                                    "node_output": ["INT", 0],
                                    "texture": ["NONE", None],
                                }
                            },
                            "CompositorNodeTime": {
                                "attributes": {
                                    "curve": ["NONE", None],
                                    "frame_end": ["INT", 0],
                                    "frame_start": ["INT", 0],
                                }
                            },
                            "CompositorNodeTonemap": {
                                "attributes": {
                                    "adaptation": ["FLOAT", 0.0],
                                    "contrast": ["FLOAT", 0.0],
                                    "correction": ["FLOAT", 0.0],
                                    "gamma": ["FLOAT", 0.0],
                                    "intensity": ["FLOAT", 0.0],
                                    "key": ["FLOAT", 0.0],
                                    "offset": ["FLOAT", 0.0],
                                    "tonemap_type": ["ENUM", "RH_SIMPLE"],
                                }
                            },
                            "CompositorNodeTrackPos": {
                                "attributes": {
                                    "clip": ["NONE", None],
                                    "frame_relative": ["INT", 0],
                                    "position": ["ENUM", "ABSOLUTE"],
                                    "track_name": ["STRING", ""],
                                    "tracking_object": ["STRING", ""],
                                }
                            },
                            "CompositorNodeTransform": {
                                "attributes": {"filter_type": ["ENUM", "NEAREST"]}
                            },
                            "CompositorNodeTranslate": {
                                "attributes": {
                                    "interpolation": ["ENUM", "NEAREST"],
                                    "use_relative": ["BOOLEAN", False],
                                    "wrap_axis": ["ENUM", "NONE"],
                                }
                            },
                            "CompositorNodeValToRGB": {
                                "attributes": {"color_ramp": ["NONE", None]}
                            },
                            "CompositorNodeValue": {"attributes": {}},
                            "CompositorNodeVecBlur": {
                                "attributes": {
                                    "factor": ["FLOAT", 0.0],
                                    "samples": ["INT", 0],
                                    "speed_max": ["INT", 0],
                                    "speed_min": ["INT", 0],
                                    "use_curved": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeViewer": {
                                "attributes": {
                                    "ui_shortcut": ["INT", 0],
                                    "use_alpha": ["BOOLEAN", False],
                                }
                            },
                            "CompositorNodeZcombine": {
                                "attributes": {
                                    "use_alpha": ["BOOLEAN", False],
                                    "use_antialias_z": ["BOOLEAN", False],
                                }
                            },
                        },
                    },
                    "FunctionNode": {
                        "attributes": {},
                        "subtypes": {
                            "FunctionNodeAlignEulerToVector": {
                                "attributes": {
                                    "axis": ["ENUM", "X"],
                                    "pivot_axis": ["ENUM", "AUTO"],
                                }
                            },
                            "FunctionNodeAlignRotationToVector": {
                                "attributes": {
                                    "axis": ["ENUM", "X"],
                                    "pivot_axis": ["ENUM", "AUTO"],
                                }
                            },
                            "FunctionNodeAxesToRotation": {
                                "attributes": {
                                    "primary_axis": ["ENUM", "X"],
                                    "secondary_axis": ["ENUM", "X"],
                                }
                            },
                            "FunctionNodeAxisAngleToRotation": {"attributes": {}},
                            "FunctionNodeBitMath": {
                                "attributes": {"operation": ["ENUM", "AND"]}
                            },
                            "FunctionNodeBooleanMath": {
                                "attributes": {"operation": ["ENUM", "AND"]}
                            },
                            "FunctionNodeCombineColor": {
                                "attributes": {"mode": ["ENUM", "RGB"]}
                            },
                            "FunctionNodeCombineMatrix": {"attributes": {}},
                            "FunctionNodeCombineTransform": {"attributes": {}},
                            "FunctionNodeCompare": {
                                "attributes": {
                                    "data_type": ["ENUM", "FLOAT"],
                                    "mode": ["ENUM", "ELEMENT"],
                                    "operation": ["ENUM", "GREATER_THAN"],
                                }
                            },
                            "FunctionNodeEulerToRotation": {"attributes": {}},
                            "FunctionNodeFindInString": {"attributes": {}},
                            "FunctionNodeFloatToInt": {
                                "attributes": {"rounding_mode": ["ENUM", "ROUND"]}
                            },
                            "FunctionNodeFormatString": {
                                "attributes": {
                                    "active_index": ["INT", 0],
                                    "format_items": ["ITEMS", None],
                                }
                            },
                            "FunctionNodeHashValue": {
                                "attributes": {"data_type": ["ENUM", "INT"]}
                            },
                            "FunctionNodeInputBool": {
                                "attributes": {"boolean": ["BOOLEAN", False]}
                            },
                            "FunctionNodeInputColor": {
                                "attributes": {"value": ["LIST", 0.0]}
                            },
                            "FunctionNodeInputInt": {
                                "attributes": {"integer": ["INT", 1]}
                            },
                            "FunctionNodeInputRotation": {
                                "attributes": {"rotation_euler": ["LIST", 0.0]}
                            },
                            "FunctionNodeInputSpecialCharacters": {"attributes": {}},
                            "FunctionNodeInputString": {
                                "attributes": {"string": ["STRING", ""]}
                            },
                            "FunctionNodeInputVector": {
                                "attributes": {"vector": ["LIST", 0.0]}
                            },
                            "FunctionNodeIntegerMath": {
                                "attributes": {"operation": ["ENUM", "ADD"]}
                            },
                            "FunctionNodeInvertMatrix": {"attributes": {}},
                            "FunctionNodeInvertRotation": {"attributes": {}},
                            "FunctionNodeMatchString": {
                                "attributes": {"operation": ["ENUM", "STARTS_WITH"]}
                            },
                            "FunctionNodeMatrixDeterminant": {"attributes": {}},
                            "FunctionNodeMatrixMultiply": {"attributes": {}},
                            "FunctionNodeProjectPoint": {"attributes": {}},
                            "FunctionNodeQuaternionToRotation": {"attributes": {}},
                            "FunctionNodeRandomValue": {
                                "attributes": {"data_type": ["ENUM", "FLOAT"]}
                            },
                            "FunctionNodeReplaceString": {"attributes": {}},
                            "FunctionNodeRotateEuler": {
                                "attributes": {
                                    "rotation_type": ["ENUM", "EULER"],
                                    "space": ["ENUM", "OBJECT"],
                                }
                            },
                            "FunctionNodeRotateRotation": {
                                "attributes": {"rotation_space": ["ENUM", "GLOBAL"]}
                            },
                            "FunctionNodeRotateVector": {"attributes": {}},
                            "FunctionNodeRotationToAxisAngle": {"attributes": {}},
                            "FunctionNodeRotationToEuler": {"attributes": {}},
                            "FunctionNodeRotationToQuaternion": {"attributes": {}},
                            "FunctionNodeSeparateColor": {
                                "attributes": {"mode": ["ENUM", "RGB"]}
                            },
                            "FunctionNodeSeparateMatrix": {"attributes": {}},
                            "FunctionNodeSeparateTransform": {"attributes": {}},
                            "FunctionNodeSliceString": {"attributes": {}},
                            "FunctionNodeStringLength": {"attributes": {}},
                            "FunctionNodeTransformDirection": {"attributes": {}},
                            "FunctionNodeTransformPoint": {"attributes": {}},
                            "FunctionNodeTransposeMatrix": {"attributes": {}},
                            "FunctionNodeValueToString": {
                                "attributes": {"data_type": ["ENUM", "FLOAT"]}
                            },
                        },
                    },
                    "GeometryNode": {
                        "attributes": {},
                        "subtypes": {
                            "GeometryNodeAccumulateField": {
                                "attributes": {
                                    "data_type": ["ENUM", "FLOAT"],
                                    "domain": ["ENUM", "POINT"],
                                }
                            },
                            "GeometryNodeAttributeDomainSize": {
                                "attributes": {"component": ["ENUM", "MESH"]}
                            },
                            "GeometryNodeAttributeStatistic": {
                                "attributes": {
                                    "data_type": ["ENUM", "FLOAT"],
                                    "domain": ["ENUM", "POINT"],
                                }
                            },
                            "GeometryNodeBake": {
                                "attributes": {"bake_items": ["ITEMS", None]}
                            },
                            "GeometryNodeBlurAttribute": {
                                "attributes": {"data_type": ["ENUM", "FLOAT"]}
                            },
                            "GeometryNodeBoundBox": {"attributes": {}},
                            "GeometryNodeCameraInfo": {"attributes": {}},
                            "GeometryNodeCaptureAttribute": {
                                "attributes": {
                                    "capture_items": ["ITEMS", None],
                                    "domain": ["ENUM", "POINT"],
                                }
                            },
                            "GeometryNodeClosureInput": {
                                "attributes": {"paired_output": ["NODE", None]}
                            },
                            "GeometryNodeClosureOutput": {
                                "attributes": {
                                    "input_items": ["ITEMS", None],
                                    "output_items": ["ITEMS", None],
                                }
                            },
                            "GeometryNodeCollectionInfo": {
                                "attributes": {"transform_space": ["ENUM", "ORIGINAL"]}
                            },
                            "GeometryNodeCombineBundle": {
                                "attributes": {"bundle_items": ["ITEMS", None]}
                            },
                            "GeometryNodeConvexHull": {"attributes": {}},
                            "GeometryNodeCornersOfEdge": {"attributes": {}},
                            "GeometryNodeCornersOfFace": {"attributes": {}},
                            "GeometryNodeCornersOfVertex": {"attributes": {}},
                            "GeometryNodeCurveArc": {
                                "attributes": {"mode": ["ENUM", "RADIUS"]}
                            },
                            "GeometryNodeCurveEndpointSelection": {"attributes": {}},
                            "GeometryNodeCurveHandleTypeSelection": {
                                "attributes": {
                                    "handle_type": ["ENUM", "FREE"],
                                    "mode": ["ENUM", ""],
                                }
                            },
                            "GeometryNodeCurveLength": {"attributes": {}},
                            "GeometryNodeCurveOfPoint": {"attributes": {}},
                            "GeometryNodeCurvePrimitiveBezierSegment": {
                                "attributes": {"mode": ["ENUM", "POSITION"]}
                            },
                            "GeometryNodeCurvePrimitiveCircle": {
                                "attributes": {"mode": ["ENUM", "RADIUS"]}
                            },
                            "GeometryNodeCurvePrimitiveLine": {
                                "attributes": {"mode": ["ENUM", "POINTS"]}
                            },
                            "GeometryNodeCurvePrimitiveQuadrilateral": {
                                "attributes": {"mode": ["ENUM", "RECTANGLE"]}
                            },
                            "GeometryNodeCurveQuadraticBezier": {"attributes": {}},
                            "GeometryNodeCurveSetHandles": {
                                "attributes": {
                                    "handle_type": ["ENUM", "FREE"],
                                    "mode": ["ENUM", ""],
                                }
                            },
                            "GeometryNodeCurveSpiral": {"attributes": {}},
                            "GeometryNodeCurveSplineType": {
                                "attributes": {"spline_type": ["ENUM", "POLY"]}
                            },
                            "GeometryNodeCurveStar": {"attributes": {}},
                            "GeometryNodeCurveToMesh": {"attributes": {}},
                            "GeometryNodeCurveToPoints": {
                                "attributes": {"mode": ["ENUM", "COUNT"]}
                            },
                            "GeometryNodeCurvesToGreasePencil": {"attributes": {}},
                            "GeometryNodeCustomGroup": {
                                "attributes": {"node_tree": ["NODETREE", None]}
                            },
                            "GeometryNodeDeformCurvesOnSurface": {"attributes": {}},
                            "GeometryNodeDeleteGeometry": {
                                "attributes": {
                                    "domain": ["ENUM", "POINT"],
                                    "mode": ["ENUM", "ALL"],
                                }
                            },
                            "GeometryNodeDistributePointsInGrid": {
                                "attributes": {"mode": ["ENUM", "DENSITY_RANDOM"]}
                            },
                            "GeometryNodeDistributePointsInVolume": {
                                "attributes": {"mode": ["ENUM", "DENSITY_RANDOM"]}
                            },
                            "GeometryNodeDistributePointsOnFaces": {
                                "attributes": {
                                    "distribute_method": ["ENUM", "RANDOM"],
                                    "use_legacy_normal": ["BOOLEAN", False],
                                }
                            },
                            "GeometryNodeDualMesh": {"attributes": {}},
                            "GeometryNodeDuplicateElements": {
                                "attributes": {"domain": ["ENUM", "POINT"]}
                            },
                            "GeometryNodeEdgePathsToCurves": {"attributes": {}},
                            "GeometryNodeEdgePathsToSelection": {"attributes": {}},
                            "GeometryNodeEdgesOfCorner": {"attributes": {}},
                            "GeometryNodeEdgesOfVertex": {"attributes": {}},
                            "GeometryNodeEdgesToFaceGroups": {"attributes": {}},
                            "GeometryNodeEvaluateClosure": {
                                "attributes": {
                                    "input_items": ["ITEMS", None],
                                    "output_items": ["ITEMS", None],
                                }
                            },
                            "GeometryNodeExtrudeMesh": {
                                "attributes": {"mode": ["ENUM", "FACES"]}
                            },
                            "GeometryNodeFaceOfCorner": {"attributes": {}},
                            "GeometryNodeFieldAtIndex": {
                                "attributes": {
                                    "data_type": ["ENUM", "FLOAT"],
                                    "domain": ["ENUM", "POINT"],
                                }
                            },
                            "GeometryNodeFieldAverage": {
                                "attributes": {
                                    "data_type": ["ENUM", "FLOAT"],
                                    "domain": ["ENUM", "POINT"],
                                }
                            },
                            "GeometryNodeFieldMinAndMax": {
                                "attributes": {
                                    "data_type": ["ENUM", "FLOAT"],
                                    "domain": ["ENUM", "POINT"],
                                }
                            },
                            "GeometryNodeFieldOnDomain": {
                                "attributes": {
                                    "data_type": ["ENUM", "FLOAT"],
                                    "domain": ["ENUM", "POINT"],
                                }
                            },
                            "GeometryNodeFieldVariance": {
                                "attributes": {
                                    "data_type": ["ENUM", "FLOAT"],
                                    "domain": ["ENUM", "POINT"],
                                }
                            },
                            "GeometryNodeFillCurve": {
                                "attributes": {"mode": ["ENUM", "TRIANGLES"]}
                            },
                            "GeometryNodeFilletCurve": {
                                "attributes": {"mode": ["ENUM", "BEZIER"]}
                            },
                            "GeometryNodeFlipFaces": {"attributes": {}},
                            "GeometryNodeForeachGeometryElementInput": {
                                "attributes": {"paired_output": ["NODE", None]}
                            },
                            "GeometryNodeForeachGeometryElementOutput": {
                                "attributes": {
                                    "domain": ["ENUM", "POINT"],
                                    "generation_items": ["ITEMS", None],
                                    "input_items": ["ITEMS", None],
                                    "inspection_index": ["INT", 0],
                                    "main_items": ["ITEMS", None],
                                }
                            },
                            "GeometryNodeGeometryToInstance": {"attributes": {}},
                            "GeometryNodeGetNamedGrid": {
                                "attributes": {"data_type": ["ENUM", "FLOAT"]}
                            },
                            "GeometryNodeGizmoDial": {
                                "attributes": {"color_id": ["ENUM", "PRIMARY"]}
                            },
                            "GeometryNodeGizmoLinear": {
                                "attributes": {
                                    "color_id": ["ENUM", "PRIMARY"],
                                    "draw_style": ["ENUM", "ARROW"],
                                }
                            },
                            "GeometryNodeGizmoTransform": {
                                "attributes": {
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
                            },
                            "GeometryNodeGreasePencilToCurves": {"attributes": {}},
                            "GeometryNodeGridInfo": {
                                "attributes": {"data_type": ["ENUM", "FLOAT"]}
                            },
                            "GeometryNodeGridToMesh": {"attributes": {}},
                            "GeometryNodeGroup": {
                                "attributes": {"node_tree": ["NODETREE", None]}
                            },
                            "GeometryNodeImageInfo": {"attributes": {}},
                            "GeometryNodeImageTexture": {
                                "attributes": {
                                    "extension": ["ENUM", "REPEAT"],
                                    "interpolation": ["ENUM", "Linear"],
                                }
                            },
                            "GeometryNodeImportCSV": {"attributes": {}},
                            "GeometryNodeImportOBJ": {"attributes": {}},
                            "GeometryNodeImportPLY": {"attributes": {}},
                            "GeometryNodeImportSTL": {"attributes": {}},
                            "GeometryNodeImportText": {"attributes": {}},
                            "GeometryNodeImportVDB": {"attributes": {}},
                            "GeometryNodeIndexOfNearest": {"attributes": {}},
                            "GeometryNodeIndexSwitch": {
                                "attributes": {
                                    "data_type": ["ENUM", "GEOMETRY"],
                                    "index_switch_items": ["ITEMS", None],
                                }
                            },
                            "GeometryNodeInputActiveCamera": {"attributes": {}},
                            "GeometryNodeInputCollection": {
                                "attributes": {"collection": ["COLLECTION", None]}
                            },
                            "GeometryNodeInputCurveHandlePositions": {"attributes": {}},
                            "GeometryNodeInputCurveTilt": {"attributes": {}},
                            "GeometryNodeInputEdgeSmooth": {"attributes": {}},
                            "GeometryNodeInputID": {"attributes": {}},
                            "GeometryNodeInputImage": {
                                "attributes": {"image": ["IMAGE", None]}
                            },
                            "GeometryNodeInputIndex": {"attributes": {}},
                            "GeometryNodeInputInstanceBounds": {"attributes": {}},
                            "GeometryNodeInputInstanceRotation": {"attributes": {}},
                            "GeometryNodeInputInstanceScale": {"attributes": {}},
                            "GeometryNodeInputMaterial": {
                                "attributes": {"material": ["MATERIAL", None]}
                            },
                            "GeometryNodeInputMaterialIndex": {"attributes": {}},
                            "GeometryNodeInputMeshEdgeAngle": {"attributes": {}},
                            "GeometryNodeInputMeshEdgeNeighbors": {"attributes": {}},
                            "GeometryNodeInputMeshEdgeVertices": {"attributes": {}},
                            "GeometryNodeInputMeshFaceArea": {"attributes": {}},
                            "GeometryNodeInputMeshFaceIsPlanar": {"attributes": {}},
                            "GeometryNodeInputMeshFaceNeighbors": {"attributes": {}},
                            "GeometryNodeInputMeshIsland": {"attributes": {}},
                            "GeometryNodeInputMeshVertexNeighbors": {"attributes": {}},
                            "GeometryNodeInputNamedAttribute": {
                                "attributes": {"data_type": ["ENUM", "FLOAT"]}
                            },
                            "GeometryNodeInputNamedLayerSelection": {"attributes": {}},
                            "GeometryNodeInputNormal": {
                                "attributes": {
                                    "legacy_corner_normals": ["BOOLEAN", False]
                                }
                            },
                            "GeometryNodeInputObject": {
                                "attributes": {"object": ["OBJECT", None]}
                            },
                            "GeometryNodeInputPosition": {"attributes": {}},
                            "GeometryNodeInputRadius": {"attributes": {}},
                            "GeometryNodeInputSceneTime": {"attributes": {}},
                            "GeometryNodeInputShadeSmooth": {"attributes": {}},
                            "GeometryNodeInputShortestEdgePaths": {"attributes": {}},
                            "GeometryNodeInputSplineCyclic": {"attributes": {}},
                            "GeometryNodeInputSplineResolution": {"attributes": {}},
                            "GeometryNodeInputTangent": {"attributes": {}},
                            "GeometryNodeInstanceOnPoints": {"attributes": {}},
                            "GeometryNodeInstanceTransform": {"attributes": {}},
                            "GeometryNodeInstancesToPoints": {"attributes": {}},
                            "GeometryNodeInterpolateCurves": {"attributes": {}},
                            "GeometryNodeIsViewport": {"attributes": {}},
                            "GeometryNodeJoinGeometry": {"attributes": {}},
                            "GeometryNodeMaterialSelection": {"attributes": {}},
                            "GeometryNodeMenuSwitch": {
                                "attributes": {
                                    "data_type": ["ENUM", "GEOMETRY"],
                                    "enum_definition": ["NODE", None],
                                    "enum_items": ["ITEMS", None],
                                }
                            },
                            "GeometryNodeMergeByDistance": {
                                "attributes": {"mode": ["ENUM", "ALL"]}
                            },
                            "GeometryNodeMergeLayers": {
                                "attributes": {"mode": ["ENUM", "MERGE_BY_NAME"]}
                            },
                            "GeometryNodeMeshBoolean": {
                                "attributes": {
                                    "operation": ["ENUM", "DIFFERENCE"],
                                    "solver": ["ENUM", "FLOAT"],
                                }
                            },
                            "GeometryNodeMeshCircle": {
                                "attributes": {"fill_type": ["ENUM", "NONE"]}
                            },
                            "GeometryNodeMeshCone": {
                                "attributes": {"fill_type": ["ENUM", "NGON"]}
                            },
                            "GeometryNodeMeshCube": {"attributes": {}},
                            "GeometryNodeMeshCylinder": {
                                "attributes": {"fill_type": ["ENUM", "NGON"]}
                            },
                            "GeometryNodeMeshFaceSetBoundaries": {"attributes": {}},
                            "GeometryNodeMeshGrid": {"attributes": {}},
                            "GeometryNodeMeshIcoSphere": {"attributes": {}},
                            "GeometryNodeMeshLine": {
                                "attributes": {
                                    "count_mode": ["ENUM", "TOTAL"],
                                    "mode": ["ENUM", "OFFSET"],
                                }
                            },
                            "GeometryNodeMeshToCurve": {
                                "attributes": {"mode": ["ENUM", "EDGES"]}
                            },
                            "GeometryNodeMeshToDensityGrid": {"attributes": {}},
                            "GeometryNodeMeshToPoints": {
                                "attributes": {"mode": ["ENUM", "VERTICES"]}
                            },
                            "GeometryNodeMeshToSDFGrid": {"attributes": {}},
                            "GeometryNodeMeshToVolume": {
                                "attributes": {
                                    "resolution_mode": ["ENUM", "VOXEL_AMOUNT"]
                                }
                            },
                            "GeometryNodeMeshUVSphere": {"attributes": {}},
                            "GeometryNodeObjectInfo": {
                                "attributes": {"transform_space": ["ENUM", "ORIGINAL"]}
                            },
                            "GeometryNodeOffsetCornerInFace": {"attributes": {}},
                            "GeometryNodeOffsetPointInCurve": {"attributes": {}},
                            "GeometryNodePoints": {"attributes": {}},
                            "GeometryNodePointsOfCurve": {"attributes": {}},
                            "GeometryNodePointsToCurves": {"attributes": {}},
                            "GeometryNodePointsToSDFGrid": {"attributes": {}},
                            "GeometryNodePointsToVertices": {"attributes": {}},
                            "GeometryNodePointsToVolume": {
                                "attributes": {
                                    "resolution_mode": ["ENUM", "VOXEL_AMOUNT"]
                                }
                            },
                            "GeometryNodeProximity": {
                                "attributes": {"target_element": ["ENUM", "FACES"]}
                            },
                            "GeometryNodeRaycast": {
                                "attributes": {
                                    "data_type": ["ENUM", "FLOAT"],
                                    "mapping": ["ENUM", "INTERPOLATED"],
                                }
                            },
                            "GeometryNodeRealizeInstances": {"attributes": {}},
                            "GeometryNodeRemoveAttribute": {
                                "attributes": {"pattern_mode": ["ENUM", "EXACT"]}
                            },
                            "GeometryNodeRepeatInput": {
                                "attributes": {"paired_output": ["NODE", None]}
                            },
                            "GeometryNodeRepeatOutput": {
                                "attributes": {
                                    "inspection_index": ["INT", 0],
                                    "repeat_items": ["ITEMS", None],
                                }
                            },
                            "GeometryNodeReplaceMaterial": {"attributes": {}},
                            "GeometryNodeResampleCurve": {
                                "attributes": {
                                    "keep_last_segment": ["BOOLEAN", False],
                                    "mode": ["ENUM", "COUNT"],
                                }
                            },
                            "GeometryNodeReverseCurve": {"attributes": {}},
                            "GeometryNodeRotateInstances": {"attributes": {}},
                            "GeometryNodeSDFGridBoolean": {
                                "attributes": {"operation": ["ENUM", "DIFFERENCE"]}
                            },
                            "GeometryNodeSampleCurve": {
                                "attributes": {
                                    "data_type": ["ENUM", "FLOAT"],
                                    "mode": ["ENUM", "FACTOR"],
                                    "use_all_curves": ["BOOLEAN", False],
                                }
                            },
                            "GeometryNodeSampleGrid": {
                                "attributes": {
                                    "data_type": ["ENUM", "FLOAT"],
                                    "interpolation_mode": ["ENUM", "TRILINEAR"],
                                }
                            },
                            "GeometryNodeSampleGridIndex": {
                                "attributes": {"data_type": ["ENUM", "FLOAT"]}
                            },
                            "GeometryNodeSampleIndex": {
                                "attributes": {
                                    "clamp": ["BOOLEAN", False],
                                    "data_type": ["ENUM", "FLOAT"],
                                    "domain": ["ENUM", "POINT"],
                                }
                            },
                            "GeometryNodeSampleNearest": {
                                "attributes": {"domain": ["ENUM", "POINT"]}
                            },
                            "GeometryNodeSampleNearestSurface": {
                                "attributes": {"data_type": ["ENUM", "FLOAT"]}
                            },
                            "GeometryNodeSampleUVSurface": {
                                "attributes": {"data_type": ["ENUM", "FLOAT"]}
                            },
                            "GeometryNodeScaleElements": {
                                "attributes": {
                                    "domain": ["ENUM", "FACE"],
                                    "scale_mode": ["ENUM", "UNIFORM"],
                                }
                            },
                            "GeometryNodeScaleInstances": {"attributes": {}},
                            "GeometryNodeSelfObject": {"attributes": {}},
                            "GeometryNodeSeparateBundle": {
                                "attributes": {"bundle_items": ["ITEMS", None]}
                            },
                            "GeometryNodeSeparateComponents": {"attributes": {}},
                            "GeometryNodeSeparateGeometry": {
                                "attributes": {"domain": ["ENUM", "POINT"]}
                            },
                            "GeometryNodeSetCurveHandlePositions": {
                                "attributes": {"mode": ["ENUM", "LEFT"]}
                            },
                            "GeometryNodeSetCurveNormal": {
                                "attributes": {"mode": ["ENUM", "MINIMUM_TWIST"]}
                            },
                            "GeometryNodeSetCurveRadius": {"attributes": {}},
                            "GeometryNodeSetCurveTilt": {"attributes": {}},
                            "GeometryNodeSetGeometryName": {"attributes": {}},
                            "GeometryNodeSetGreasePencilColor": {
                                "attributes": {"mode": ["ENUM", "STROKE"]}
                            },
                            "GeometryNodeSetGreasePencilDepth": {
                                "attributes": {"depth_order": ["ENUM", "2D"]}
                            },
                            "GeometryNodeSetGreasePencilSoftness": {"attributes": {}},
                            "GeometryNodeSetID": {"attributes": {}},
                            "GeometryNodeSetInstanceTransform": {"attributes": {}},
                            "GeometryNodeSetMaterial": {"attributes": {}},
                            "GeometryNodeSetMaterialIndex": {"attributes": {}},
                            "GeometryNodeSetMeshNormal": {
                                "attributes": {
                                    "domain": ["ENUM", "POINT"],
                                    "mode": ["ENUM", "SHARPNESS"],
                                }
                            },
                            "GeometryNodeSetPointRadius": {"attributes": {}},
                            "GeometryNodeSetPosition": {"attributes": {}},
                            "GeometryNodeSetShadeSmooth": {
                                "attributes": {"domain": ["ENUM", "EDGE"]}
                            },
                            "GeometryNodeSetSplineCyclic": {"attributes": {}},
                            "GeometryNodeSetSplineResolution": {"attributes": {}},
                            "GeometryNodeSimulationInput": {
                                "attributes": {"paired_output": ["NODE", None]}
                            },
                            "GeometryNodeSimulationOutput": {
                                "attributes": {"state_items": ["ITEMS", None]}
                            },
                            "GeometryNodeSortElements": {
                                "attributes": {"domain": ["ENUM", "POINT"]}
                            },
                            "GeometryNodeSplineLength": {"attributes": {}},
                            "GeometryNodeSplineParameter": {"attributes": {}},
                            "GeometryNodeSplitEdges": {"attributes": {}},
                            "GeometryNodeSplitToInstances": {
                                "attributes": {"domain": ["ENUM", "POINT"]}
                            },
                            "GeometryNodeStoreNamedAttribute": {
                                "attributes": {
                                    "data_type": ["ENUM", "FLOAT"],
                                    "domain": ["ENUM", "POINT"],
                                }
                            },
                            "GeometryNodeStoreNamedGrid": {
                                "attributes": {"data_type": ["ENUM", "FLOAT"]}
                            },
                            "GeometryNodeStringJoin": {"attributes": {}},
                            "GeometryNodeStringToCurves": {
                                "attributes": {
                                    "align_x": ["ENUM", "LEFT"],
                                    "align_y": ["ENUM", "TOP_BASELINE"],
                                    "font": ["NONE", None],
                                    "overflow": ["ENUM", "OVERFLOW"],
                                    "pivot_mode": ["ENUM", "BOTTOM_LEFT"],
                                }
                            },
                            "GeometryNodeSubdivideCurve": {"attributes": {}},
                            "GeometryNodeSubdivideMesh": {"attributes": {}},
                            "GeometryNodeSubdivisionSurface": {
                                "attributes": {
                                    "boundary_smooth": ["ENUM", "ALL"],
                                    "uv_smooth": ["ENUM", "PRESERVE_BOUNDARIES"],
                                }
                            },
                            "GeometryNodeSwitch": {
                                "attributes": {"input_type": ["ENUM", "GEOMETRY"]}
                            },
                            "GeometryNodeTool3DCursor": {"attributes": {}},
                            "GeometryNodeToolActiveElement": {
                                "attributes": {"domain": ["ENUM", "POINT"]}
                            },
                            "GeometryNodeToolFaceSet": {"attributes": {}},
                            "GeometryNodeToolMousePosition": {"attributes": {}},
                            "GeometryNodeToolSelection": {"attributes": {}},
                            "GeometryNodeToolSetFaceSet": {"attributes": {}},
                            "GeometryNodeToolSetSelection": {
                                "attributes": {
                                    "domain": ["ENUM", "POINT"],
                                    "selection_type": ["ENUM", "BOOLEAN"],
                                }
                            },
                            "GeometryNodeTransform": {
                                "attributes": {"mode": ["ENUM", "COMPONENTS"]}
                            },
                            "GeometryNodeTranslateInstances": {"attributes": {}},
                            "GeometryNodeTriangulate": {
                                "attributes": {
                                    "ngon_method": ["ENUM", "BEAUTY"],
                                    "quad_method": ["ENUM", "BEAUTY"],
                                }
                            },
                            "GeometryNodeTrimCurve": {
                                "attributes": {"mode": ["ENUM", "FACTOR"]}
                            },
                            "GeometryNodeUVPackIslands": {"attributes": {}},
                            "GeometryNodeUVUnwrap": {
                                "attributes": {"method": ["ENUM", "ANGLE_BASED"]}
                            },
                            "GeometryNodeVertexOfCorner": {"attributes": {}},
                            "GeometryNodeViewer": {
                                "attributes": {
                                    "data_type": ["ENUM", "FLOAT"],
                                    "domain": ["ENUM", "POINT"],
                                    "ui_shortcut": ["INT", 0],
                                }
                            },
                            "GeometryNodeViewportTransform": {"attributes": {}},
                            "GeometryNodeVolumeCube": {"attributes": {}},
                            "GeometryNodeVolumeToMesh": {
                                "attributes": {"resolution_mode": ["ENUM", "GRID"]}
                            },
                            "GeometryNodeWarning": {
                                "attributes": {"warning_type": ["ENUM", "ERROR"]}
                            },
                        },
                    },
                    "NodeFrame": {
                        "attributes": {
                            "label_size": ["INT", 12],
                            "shrink": ["BOOLEAN", True],
                        }
                    },
                    "NodeGroupInput": {"attributes": {}},
                    "NodeGroupOutput": {"attributes": {}},
                    "NodeReroute": {"attributes": {}},
                    "ShaderNode": {
                        "attributes": {},
                        "subtypes": {
                            "ShaderNodeAddShader": {"attributes": {}},
                            "ShaderNodeAmbientOcclusion": {
                                "attributes": {
                                    "inside": ["BOOLEAN", False],
                                    "only_local": ["BOOLEAN", False],
                                    "samples": ["INT", 0],
                                }
                            },
                            "ShaderNodeAttribute": {
                                "attributes": {
                                    "attribute_name": ["STRING", ""],
                                    "attribute_type": ["ENUM", "GEOMETRY"],
                                }
                            },
                            "ShaderNodeBackground": {"attributes": {}},
                            "ShaderNodeBevel": {"attributes": {"samples": ["INT", 0]}},
                            "ShaderNodeBlackbody": {"attributes": {}},
                            "ShaderNodeBrightContrast": {"attributes": {}},
                            "ShaderNodeBsdfAnisotropic": {
                                "attributes": {"distribution": ["ENUM", "BECKMANN"]}
                            },
                            "ShaderNodeBsdfDiffuse": {"attributes": {}},
                            "ShaderNodeBsdfGlass": {
                                "attributes": {"distribution": ["ENUM", "BECKMANN"]}
                            },
                            "ShaderNodeBsdfHair": {
                                "attributes": {"component": ["ENUM", "Reflection"]}
                            },
                            "ShaderNodeBsdfHairPrincipled": {
                                "attributes": {
                                    "model": ["ENUM", "HUANG"],
                                    "parametrization": ["ENUM", "COLOR"],
                                }
                            },
                            "ShaderNodeBsdfMetallic": {
                                "attributes": {
                                    "distribution": ["ENUM", "BECKMANN"],
                                    "fresnel_type": ["ENUM", "PHYSICAL_CONDUCTOR"],
                                }
                            },
                            "ShaderNodeBsdfPrincipled": {
                                "attributes": {
                                    "distribution": ["ENUM", "GGX"],
                                    "subsurface_method": ["ENUM", "BURLEY"],
                                }
                            },
                            "ShaderNodeBsdfRayPortal": {"attributes": {}},
                            "ShaderNodeBsdfRefraction": {
                                "attributes": {"distribution": ["ENUM", "BECKMANN"]}
                            },
                            "ShaderNodeBsdfSheen": {
                                "attributes": {"distribution": ["ENUM", "ASHIKHMIN"]}
                            },
                            "ShaderNodeBsdfToon": {
                                "attributes": {"component": ["ENUM", "DIFFUSE"]}
                            },
                            "ShaderNodeBsdfTranslucent": {"attributes": {}},
                            "ShaderNodeBsdfTransparent": {"attributes": {}},
                            "ShaderNodeBump": {
                                "attributes": {"invert": ["BOOLEAN", False]}
                            },
                            "ShaderNodeCameraData": {"attributes": {}},
                            "ShaderNodeClamp": {
                                "attributes": {"clamp_type": ["ENUM", "MINMAX"]}
                            },
                            "ShaderNodeCombineColor": {
                                "attributes": {"mode": ["ENUM", "RGB"]}
                            },
                            "ShaderNodeCombineHSV": {"attributes": {}},
                            "ShaderNodeCombineRGB": {"attributes": {}},
                            "ShaderNodeCombineXYZ": {"attributes": {}},
                            "ShaderNodeCustomGroup": {
                                "attributes": {"node_tree": ["NODETREE", None]}
                            },
                            "ShaderNodeDisplacement": {
                                "attributes": {"space": ["ENUM", "OBJECT"]}
                            },
                            "ShaderNodeEeveeSpecular": {"attributes": {}},
                            "ShaderNodeEmission": {"attributes": {}},
                            "ShaderNodeFloatCurve": {
                                "attributes": {"mapping": ["NONE", None]}
                            },
                            "ShaderNodeFresnel": {"attributes": {}},
                            "ShaderNodeGamma": {"attributes": {}},
                            "ShaderNodeGroup": {
                                "attributes": {"node_tree": ["NODETREE", None]}
                            },
                            "ShaderNodeHairInfo": {"attributes": {}},
                            "ShaderNodeHoldout": {"attributes": {}},
                            "ShaderNodeHueSaturation": {"attributes": {}},
                            "ShaderNodeInvert": {"attributes": {}},
                            "ShaderNodeLayerWeight": {"attributes": {}},
                            "ShaderNodeLightFalloff": {"attributes": {}},
                            "ShaderNodeLightPath": {"attributes": {}},
                            "ShaderNodeMapRange": {
                                "attributes": {
                                    "clamp": ["BOOLEAN", False],
                                    "data_type": ["ENUM", "FLOAT"],
                                    "interpolation_type": ["ENUM", "LINEAR"],
                                }
                            },
                            "ShaderNodeMapping": {
                                "attributes": {"vector_type": ["ENUM", "POINT"]}
                            },
                            "ShaderNodeMath": {
                                "attributes": {
                                    "operation": ["ENUM", "ADD"],
                                    "use_clamp": ["BOOLEAN", False],
                                }
                            },
                            "ShaderNodeMix": {
                                "attributes": {
                                    "blend_type": ["ENUM", "MIX"],
                                    "clamp_factor": ["BOOLEAN", False],
                                    "clamp_result": ["BOOLEAN", False],
                                    "data_type": ["ENUM", "FLOAT"],
                                    "factor_mode": ["ENUM", "UNIFORM"],
                                }
                            },
                            "ShaderNodeMixRGB": {
                                "attributes": {
                                    "blend_type": ["ENUM", "MIX"],
                                    "use_alpha": ["BOOLEAN", False],
                                    "use_clamp": ["BOOLEAN", False],
                                }
                            },
                            "ShaderNodeMixShader": {"attributes": {}},
                            "ShaderNodeNewGeometry": {"attributes": {}},
                            "ShaderNodeNormal": {"attributes": {}},
                            "ShaderNodeNormalMap": {
                                "attributes": {
                                    "space": ["ENUM", "TANGENT"],
                                    "uv_map": ["STRING", ""],
                                }
                            },
                            "ShaderNodeObjectInfo": {"attributes": {}},
                            "ShaderNodeOutputAOV": {
                                "attributes": {"aov_name": ["STRING", ""]}
                            },
                            "ShaderNodeOutputLight": {
                                "attributes": {
                                    "is_active_output": ["BOOLEAN", False],
                                    "target": ["ENUM", "ALL"],
                                }
                            },
                            "ShaderNodeOutputLineStyle": {
                                "attributes": {
                                    "blend_type": ["ENUM", "MIX"],
                                    "is_active_output": ["BOOLEAN", False],
                                    "target": ["ENUM", "ALL"],
                                    "use_alpha": ["BOOLEAN", False],
                                    "use_clamp": ["BOOLEAN", False],
                                }
                            },
                            "ShaderNodeOutputMaterial": {
                                "attributes": {
                                    "is_active_output": ["BOOLEAN", False],
                                    "target": ["ENUM", "ALL"],
                                }
                            },
                            "ShaderNodeOutputWorld": {
                                "attributes": {
                                    "is_active_output": ["BOOLEAN", False],
                                    "target": ["ENUM", "ALL"],
                                }
                            },
                            "ShaderNodeParticleInfo": {"attributes": {}},
                            "ShaderNodePointInfo": {"attributes": {}},
                            "ShaderNodeRGB": {"attributes": {}},
                            "ShaderNodeRGBCurve": {
                                "attributes": {"mapping": ["NONE", None]}
                            },
                            "ShaderNodeRGBToBW": {"attributes": {}},
                            "ShaderNodeScript": {
                                "attributes": {
                                    "bytecode": ["STRING", ""],
                                    "bytecode_hash": ["STRING", ""],
                                    "filepath": ["STRING", ""],
                                    "mode": ["ENUM", "INTERNAL"],
                                    "script": ["NONE", None],
                                    "use_auto_update": ["BOOLEAN", False],
                                }
                            },
                            "ShaderNodeSeparateColor": {
                                "attributes": {"mode": ["ENUM", "RGB"]}
                            },
                            "ShaderNodeSeparateHSV": {"attributes": {}},
                            "ShaderNodeSeparateRGB": {"attributes": {}},
                            "ShaderNodeSeparateXYZ": {"attributes": {}},
                            "ShaderNodeShaderToRGB": {"attributes": {}},
                            "ShaderNodeSqueeze": {"attributes": {}},
                            "ShaderNodeSubsurfaceScattering": {
                                "attributes": {"falloff": ["ENUM", "BURLEY"]}
                            },
                            "ShaderNodeTangent": {
                                "attributes": {
                                    "axis": ["ENUM", "X"],
                                    "direction_type": ["ENUM", "RADIAL"],
                                    "uv_map": ["STRING", ""],
                                }
                            },
                            "ShaderNodeTexBrick": {
                                "attributes": {
                                    "color_mapping": ["NONE", None],
                                    "offset": ["FLOAT", 0.5],
                                    "offset_frequency": ["INT", 2],
                                    "squash": ["FLOAT", 1.0],
                                    "squash_frequency": ["INT", 2],
                                    "texture_mapping": ["NONE", None],
                                }
                            },
                            "ShaderNodeTexChecker": {
                                "attributes": {
                                    "color_mapping": ["NONE", None],
                                    "texture_mapping": ["NONE", None],
                                }
                            },
                            "ShaderNodeTexCoord": {
                                "attributes": {
                                    "from_instancer": ["BOOLEAN", False],
                                    "object": ["OBJECT", None],
                                }
                            },
                            "ShaderNodeTexEnvironment": {
                                "attributes": {
                                    "color_mapping": ["NONE", None],
                                    "image": ["IMAGE", None],
                                    "image_user": ["NONE", None],
                                    "interpolation": ["ENUM", "Linear"],
                                    "projection": ["ENUM", "EQUIRECTANGULAR"],
                                    "texture_mapping": ["NONE", None],
                                }
                            },
                            "ShaderNodeTexGabor": {
                                "attributes": {
                                    "color_mapping": ["NONE", None],
                                    "gabor_type": ["ENUM", "2D"],
                                    "texture_mapping": ["NONE", None],
                                }
                            },
                            "ShaderNodeTexGradient": {
                                "attributes": {
                                    "color_mapping": ["NONE", None],
                                    "gradient_type": ["ENUM", "LINEAR"],
                                    "texture_mapping": ["NONE", None],
                                }
                            },
                            "ShaderNodeTexIES": {
                                "attributes": {
                                    "filepath": ["STRING", ""],
                                    "ies": ["NONE", None],
                                    "mode": ["ENUM", "INTERNAL"],
                                }
                            },
                            "ShaderNodeTexImage": {
                                "attributes": {
                                    "color_mapping": ["NONE", None],
                                    "extension": ["ENUM", "REPEAT"],
                                    "image": ["IMAGE", None],
                                    "image_user": ["NONE", None],
                                    "interpolation": ["ENUM", "Linear"],
                                    "projection": ["ENUM", "FLAT"],
                                    "projection_blend": ["FLOAT", 0.0],
                                    "texture_mapping": ["NONE", None],
                                }
                            },
                            "ShaderNodeTexMagic": {
                                "attributes": {
                                    "color_mapping": ["NONE", None],
                                    "texture_mapping": ["NONE", None],
                                    "turbulence_depth": ["INT", 0],
                                }
                            },
                            "ShaderNodeTexNoise": {
                                "attributes": {
                                    "color_mapping": ["NONE", None],
                                    "noise_dimensions": ["ENUM", "1D"],
                                    "noise_type": ["ENUM", "MULTIFRACTAL"],
                                    "normalize": ["BOOLEAN", False],
                                    "texture_mapping": ["NONE", None],
                                }
                            },
                            "ShaderNodeTexPointDensity": {
                                "attributes": {
                                    "interpolation": ["ENUM", "Linear"],
                                    "object": ["OBJECT", None],
                                    "particle_color_source": ["ENUM", "PARTICLE_AGE"],
                                    "particle_system": ["NONE", None],
                                    "point_source": ["ENUM", "PARTICLE_SYSTEM"],
                                    "radius": ["FLOAT", 0.0],
                                    "resolution": ["INT", 0],
                                    "space": ["ENUM", "OBJECT"],
                                    "vertex_attribute_name": ["STRING", ""],
                                    "vertex_color_source": ["ENUM", "VERTEX_COLOR"],
                                }
                            },
                            "ShaderNodeTexSky": {
                                "attributes": {
                                    "air_density": ["FLOAT", 1.0],
                                    "altitude": ["FLOAT", 0.0],
                                    "color_mapping": ["NONE", None],
                                    "dust_density": ["FLOAT", 1.0],
                                    "ground_albedo": ["FLOAT", 0.0],
                                    "ozone_density": ["FLOAT", 1.0],
                                    "sky_type": ["ENUM", "PREETHAM"],
                                    "sun_direction": ["LIST", 0.0],
                                    "sun_disc": ["BOOLEAN", True],
                                    "sun_elevation": ["FLOAT", 1.5707963705062866],
                                    "sun_intensity": ["FLOAT", 1.0],
                                    "sun_rotation": ["FLOAT", 0.0],
                                    "sun_size": ["FLOAT", 0.009512044489383698],
                                    "texture_mapping": ["NONE", None],
                                    "turbidity": ["FLOAT", 0.0],
                                }
                            },
                            "ShaderNodeTexVoronoi": {
                                "attributes": {
                                    "color_mapping": ["NONE", None],
                                    "distance": ["ENUM", "EUCLIDEAN"],
                                    "feature": ["ENUM", "F1"],
                                    "normalize": ["BOOLEAN", False],
                                    "texture_mapping": ["NONE", None],
                                    "voronoi_dimensions": ["ENUM", "1D"],
                                }
                            },
                            "ShaderNodeTexWave": {
                                "attributes": {
                                    "bands_direction": ["ENUM", "X"],
                                    "color_mapping": ["NONE", None],
                                    "rings_direction": ["ENUM", "X"],
                                    "texture_mapping": ["NONE", None],
                                    "wave_profile": ["ENUM", "SIN"],
                                    "wave_type": ["ENUM", "BANDS"],
                                }
                            },
                            "ShaderNodeTexWhiteNoise": {
                                "attributes": {"noise_dimensions": ["ENUM", "1D"]}
                            },
                            "ShaderNodeUVAlongStroke": {
                                "attributes": {"use_tips": ["BOOLEAN", False]}
                            },
                            "ShaderNodeUVMap": {
                                "attributes": {
                                    "from_instancer": ["BOOLEAN", False],
                                    "uv_map": ["STRING", ""],
                                }
                            },
                            "ShaderNodeValToRGB": {
                                "attributes": {"color_ramp": ["NONE", None]}
                            },
                            "ShaderNodeValue": {"attributes": {}},
                            "ShaderNodeVectorCurve": {
                                "attributes": {"mapping": ["NONE", None]}
                            },
                            "ShaderNodeVectorDisplacement": {
                                "attributes": {"space": ["ENUM", "TANGENT"]}
                            },
                            "ShaderNodeVectorMath": {
                                "attributes": {"operation": ["ENUM", "ADD"]}
                            },
                            "ShaderNodeVectorRotate": {
                                "attributes": {
                                    "invert": ["BOOLEAN", False],
                                    "rotation_type": ["ENUM", "AXIS_ANGLE"],
                                }
                            },
                            "ShaderNodeVectorTransform": {
                                "attributes": {
                                    "convert_from": ["ENUM", "WORLD"],
                                    "convert_to": ["ENUM", "WORLD"],
                                    "vector_type": ["ENUM", "VECTOR"],
                                }
                            },
                            "ShaderNodeVertexColor": {
                                "attributes": {"layer_name": ["STRING", ""]}
                            },
                            "ShaderNodeVolumeAbsorption": {"attributes": {}},
                            "ShaderNodeVolumeCoefficients": {
                                "attributes": {"phase": ["ENUM", "HENYEY_GREENSTEIN"]}
                            },
                            "ShaderNodeVolumeInfo": {"attributes": {}},
                            "ShaderNodeVolumePrincipled": {"attributes": {}},
                            "ShaderNodeVolumeScatter": {
                                "attributes": {"phase": ["ENUM", "HENYEY_GREENSTEIN"]}
                            },
                            "ShaderNodeWavelength": {"attributes": {}},
                            "ShaderNodeWireframe": {
                                "attributes": {"use_pixel_size": ["BOOLEAN", False]}
                            },
                        },
                    },
                    "TextureNode": {
                        "attributes": {},
                        "subtypes": {
                            "TextureNodeAt": {"attributes": {}},
                            "TextureNodeBricks": {
                                "attributes": {
                                    "offset": ["FLOAT", 0.0],
                                    "offset_frequency": ["INT", 0],
                                    "squash": ["FLOAT", 0.0],
                                    "squash_frequency": ["INT", 0],
                                }
                            },
                            "TextureNodeChecker": {"attributes": {}},
                            "TextureNodeCombineColor": {
                                "attributes": {"mode": ["ENUM", "RGB"]}
                            },
                            "TextureNodeCompose": {"attributes": {}},
                            "TextureNodeCoordinates": {"attributes": {}},
                            "TextureNodeCurveRGB": {
                                "attributes": {"mapping": ["NONE", None]}
                            },
                            "TextureNodeCurveTime": {
                                "attributes": {
                                    "curve": ["NONE", None],
                                    "frame_end": ["INT", 0],
                                    "frame_start": ["INT", 0],
                                }
                            },
                            "TextureNodeDecompose": {"attributes": {}},
                            "TextureNodeDistance": {"attributes": {}},
                            "TextureNodeGroup": {
                                "attributes": {"node_tree": ["NODETREE", None]}
                            },
                            "TextureNodeHueSaturation": {"attributes": {}},
                            "TextureNodeImage": {
                                "attributes": {
                                    "image": ["IMAGE", None],
                                    "image_user": ["NONE", None],
                                }
                            },
                            "TextureNodeInvert": {"attributes": {}},
                            "TextureNodeMath": {
                                "attributes": {
                                    "operation": ["ENUM", "ADD"],
                                    "use_clamp": ["BOOLEAN", False],
                                }
                            },
                            "TextureNodeMixRGB": {
                                "attributes": {
                                    "blend_type": ["ENUM", "MIX"],
                                    "use_alpha": ["BOOLEAN", False],
                                    "use_clamp": ["BOOLEAN", False],
                                }
                            },
                            "TextureNodeOutput": {
                                "attributes": {"filepath": ["STRING", ""]}
                            },
                            "TextureNodeRGBToBW": {"attributes": {}},
                            "TextureNodeRotate": {"attributes": {}},
                            "TextureNodeScale": {"attributes": {}},
                            "TextureNodeSeparateColor": {
                                "attributes": {"mode": ["ENUM", "RGB"]}
                            },
                            "TextureNodeTexBlend": {"attributes": {}},
                            "TextureNodeTexClouds": {"attributes": {}},
                            "TextureNodeTexDistNoise": {"attributes": {}},
                            "TextureNodeTexMagic": {"attributes": {}},
                            "TextureNodeTexMarble": {"attributes": {}},
                            "TextureNodeTexMusgrave": {"attributes": {}},
                            "TextureNodeTexNoise": {"attributes": {}},
                            "TextureNodeTexStucci": {"attributes": {}},
                            "TextureNodeTexVoronoi": {"attributes": {}},
                            "TextureNodeTexWood": {"attributes": {}},
                            "TextureNodeTexture": {
                                "attributes": {
                                    "node_output": ["INT", 0],
                                    "texture": ["NONE", None],
                                }
                            },
                            "TextureNodeTranslate": {"attributes": {}},
                            "TextureNodeValToNor": {"attributes": {}},
                            "TextureNodeValToRGB": {
                                "attributes": {"color_ramp": ["NONE", None]}
                            },
                            "TextureNodeViewer": {"attributes": {}},
                        },
                    },
                },
            }
        },
    },
    "NodeSocket": {
        "attributes": {"bl_idname": ["STRING", ""]},
        "subtypes": {
            "NodeSocketStandard": {
                "attributes": {},
                "subtypes": {
                    "NodeSocketBool": {
                        "attributes": {"default_value": ["BOOLEAN", False]}
                    },
                    "NodeSocketBundle": {"attributes": {}},
                    "NodeSocketClosure": {"attributes": {}},
                    "NodeSocketCollection": {
                        "attributes": {"default_value": ["COLLECTION", None]}
                    },
                    "NodeSocketColor": {"attributes": {"default_value": ["LIST", 0.0]}},
                    "NodeSocketFloat": {
                        "attributes": {"default_value": ["FLOAT", 0.0]}
                    },
                    "NodeSocketFloatAngle": {
                        "attributes": {"default_value": ["FLOAT", 0.0]}
                    },
                    "NodeSocketFloatColorTemperature": {
                        "attributes": {"default_value": ["FLOAT", 0.0]}
                    },
                    "NodeSocketFloatDistance": {
                        "attributes": {"default_value": ["FLOAT", 0.0]}
                    },
                    "NodeSocketFloatFactor": {
                        "attributes": {"default_value": ["FLOAT", 0.0]}
                    },
                    "NodeSocketFloatFrequency": {
                        "attributes": {"default_value": ["FLOAT", 0.0]}
                    },
                    "NodeSocketFloatPercentage": {
                        "attributes": {"default_value": ["FLOAT", 0.0]}
                    },
                    "NodeSocketFloatTime": {
                        "attributes": {"default_value": ["FLOAT", 0.0]}
                    },
                    "NodeSocketFloatTimeAbsolute": {
                        "attributes": {"default_value": ["FLOAT", 0.0]}
                    },
                    "NodeSocketFloatUnsigned": {
                        "attributes": {"default_value": ["FLOAT", 0.0]}
                    },
                    "NodeSocketFloatWavelength": {
                        "attributes": {"default_value": ["FLOAT", 0.0]}
                    },
                    "NodeSocketGeometry": {"attributes": {}},
                    "NodeSocketImage": {
                        "attributes": {"default_value": ["IMAGE", None]}
                    },
                    "NodeSocketInt": {"attributes": {"default_value": ["INT", 0]}},
                    "NodeSocketIntFactor": {
                        "attributes": {"default_value": ["INT", 1]}
                    },
                    "NodeSocketIntPercentage": {
                        "attributes": {"default_value": ["INT", 100]}
                    },
                    "NodeSocketIntUnsigned": {
                        "attributes": {"default_value": ["INT", 0]}
                    },
                    "NodeSocketMaterial": {
                        "attributes": {"default_value": ["MATERIAL", None]}
                    },
                    "NodeSocketMatrix": {"attributes": {}},
                    "NodeSocketMenu": {"attributes": {"default_value": ["ENUM", ""]}},
                    "NodeSocketObject": {
                        "attributes": {"default_value": ["OBJECT", None]}
                    },
                    "NodeSocketRotation": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketShader": {"attributes": {}},
                    "NodeSocketString": {
                        "attributes": {"default_value": ["STRING", ""]}
                    },
                    "NodeSocketStringFilePath": {
                        "attributes": {"default_value": ["STRING", ""]}
                    },
                    "NodeSocketTexture": {
                        "attributes": {"default_value": ["NONE", None]}
                    },
                    "NodeSocketVector": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVector2D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVector4D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorAcceleration": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorAcceleration2D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorAcceleration4D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorDirection": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorDirection2D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorDirection4D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorEuler": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorEuler2D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorEuler4D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorFactor": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorFactor2D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorFactor4D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorPercentage": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorPercentage2D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorPercentage4D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorTranslation": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorTranslation2D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorTranslation4D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorVelocity": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorVelocity2D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorVelocity4D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorXYZ": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorXYZ2D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVectorXYZ4D": {
                        "attributes": {"default_value": ["LIST", 0.0]}
                    },
                    "NodeSocketVirtual": {"attributes": {}},
                },
            }
        },
    },
    "NodeTree": {
        "attributes": {
            "bl_idname": ["STRING", ""],
            "color_tag": ["STRING", "NONE"],
            "default_group_node_width": ["INT", 140],
            "description": ["STRING", ""],
            "name": ["STRING", ""],
        },
        "subtypes": {
            "GeometryNodeTree": {
                "attributes": {
                    "is_modifier": ["BOOLEAN", False],
                    "is_tool": ["BOOLEAN", False],
                }
            }
        },
    },
    "NodeTreeInterfacePanel": {
        "attributes": {
            "default_closed": ["BOOLEAN", False],
            "description": ["STRING", ""],
            "item_type": ["STRING", "SOCKET"],
            "name": ["STRING", ""],
        }
    },
    "NodeTreeInterfaceSocket": {
        "attributes": {
            "attribute_domain": ["STRING", "POINT"],
            "default_attribute_name": ["STRING", ""],
            "description": ["STRING", ""],
            "force_non_field": ["BOOLEAN", False],
            "hide_in_modifier": ["BOOLEAN", False],
            "hide_value": ["BOOLEAN", False],
            "in_out": ["STRING", "INPUT"],
            "item_type": ["STRING", "SOCKET"],
            "name": ["STRING", ""],
            "socket_type": ["STRING", "DEFAULT"],
        },
        "subtypes": {
            "NodeTreeInterfaceSocketBool": {
                "attributes": {"default_value": ["BOOLEAN", False]}
            },
            "NodeTreeInterfaceSocketBundle": {"attributes": {}},
            "NodeTreeInterfaceSocketClosure": {"attributes": {}},
            "NodeTreeInterfaceSocketCollection": {
                "attributes": {"default_value": ["COLLECTION", None]}
            },
            "NodeTreeInterfaceSocketColor": {
                "attributes": {"default_value": ["LIST", 0.0]}
            },
            "NodeTreeInterfaceSocketFloat": {
                "attributes": {
                    "default_value": ["FLOAT", 0.0],
                    "max_value": ["FLOAT", 3.4028234663852886e38],
                    "min_value": ["FLOAT", -3.4028234663852886e38],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketFloatAngle": {
                "attributes": {
                    "default_value": ["FLOAT", 0.0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketFloatColorTemperature": {
                "attributes": {
                    "default_value": ["FLOAT", 0.0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketFloatDistance": {
                "attributes": {
                    "default_value": ["FLOAT", 0.0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketFloatFactor": {
                "attributes": {
                    "default_value": ["FLOAT", 1.0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketFloatFrequency": {
                "attributes": {
                    "default_value": ["FLOAT", 0.0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketFloatPercentage": {
                "attributes": {
                    "default_value": ["FLOAT", 100.0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketFloatTime": {
                "attributes": {
                    "default_value": ["FLOAT", 0.0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketFloatTimeAbsolute": {
                "attributes": {
                    "default_value": ["FLOAT", 0.0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketFloatUnsigned": {
                "attributes": {
                    "default_value": ["FLOAT", 0.0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketFloatWavelength": {
                "attributes": {
                    "default_value": ["FLOAT", 0.0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketGeometry": {"attributes": {}},
            "NodeTreeInterfaceSocketImage": {
                "attributes": {"default_value": ["IMAGE", None]}
            },
            "NodeTreeInterfaceSocketInt": {
                "attributes": {
                    "default_value": ["INT", 0],
                    "max_value": ["INT", 2147483647],
                    "min_value": ["INT", -2147483648],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketIntFactor": {
                "attributes": {
                    "default_value": ["INT", 0],
                    "max_value": ["INT", 0],
                    "min_value": ["INT", 0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketIntPercentage": {
                "attributes": {
                    "default_value": ["INT", 0],
                    "max_value": ["INT", 0],
                    "min_value": ["INT", 0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketIntUnsigned": {
                "attributes": {
                    "default_value": ["INT", 0],
                    "max_value": ["INT", 0],
                    "min_value": ["INT", 0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketMaterial": {
                "attributes": {"default_value": ["MATERIAL", None]}
            },
            "NodeTreeInterfaceSocketMatrix": {"attributes": {}},
            "NodeTreeInterfaceSocketMenu": {
                "attributes": {"default_value": ["ENUM", ""]}
            },
            "NodeTreeInterfaceSocketObject": {
                "attributes": {"default_value": ["OBJECT", None]}
            },
            "NodeTreeInterfaceSocketRotation": {
                "attributes": {"default_value": ["LIST", 0.0]}
            },
            "NodeTreeInterfaceSocketShader": {"attributes": {}},
            "NodeTreeInterfaceSocketString": {
                "attributes": {
                    "default_value": ["STRING", ""],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketStringFilePath": {
                "attributes": {
                    "default_value": ["STRING", ""],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketTexture": {
                "attributes": {"default_value": ["NONE", None]}
            },
            "NodeTreeInterfaceSocketVector": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVector2D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVector4D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorAcceleration": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorAcceleration2D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorAcceleration4D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorDirection": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorDirection2D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorDirection4D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorEuler": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorEuler2D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorEuler4D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorFactor": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorFactor2D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorFactor4D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorPercentage": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorPercentage2D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorPercentage4D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorTranslation": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorTranslation2D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorTranslation4D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorVelocity": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorVelocity2D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorVelocity4D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorXYZ": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorXYZ2D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
            "NodeTreeInterfaceSocketVectorXYZ4D": {
                "attributes": {
                    "default_value": ["LIST", 0.0],
                    "dimensions": ["INT", 0],
                    "max_value": ["FLOAT", 0.0],
                    "min_value": ["FLOAT", 0.0],
                    "subtype": ["ENUM", "DEFAULT"],
                }
            },
        },
    },
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
