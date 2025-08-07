import bmesh
import bpy
import pytest

from .fixtures import fixture_test_trees, test_tree_names


def _create_single_vertex_object(name: str = "test_object"):
    """Create a mesh object with a single vertex at (0,0,0)."""
    # Create mesh
    mesh = bpy.data.meshes.new(name)

    # Create bmesh and add single vertex
    bm = bmesh.new()
    bm.verts.new((0, 0, 0))
    bm.to_mesh(mesh)
    bm.free()

    # Create object
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)

    return obj


@pytest.mark.parametrize("tree_name", test_tree_names)
def test_modifier_node_groups(fixture_test_trees, tree_name):
    """Test that modifier node groups correctly transform a vertex from (0,0,0) to (0,0,1)."""

    # Create object with single vertex at origin
    obj = _create_single_vertex_object("Point")

    # Set as active object
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    # Add geometry nodes modifier
    modifier = obj.modifiers.new(name="GeometryNodes", type="NODES")
    modifier.node_group = bpy.data.node_groups[tree_name]
    # # Apply modifier
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_apply(modifier="GeometryNodes")

    # Get the mesh data after modifier application
    mesh = obj.data

    # Check that we have at least one vertex
    assert len(mesh.vertices) > 0, f"No vertices found after applying {tree_name}"
    vertex = mesh.vertices[0]
    assert list(vertex.co) == [
        0.0,
        0.0,
        1.0,
    ], f"Vertex position is not (0,0,1) after applying {tree_name}"

    # Clean up
    bpy.data.objects.remove(obj, do_unlink=True)
    bpy.data.meshes.remove(mesh, do_unlink=True)
