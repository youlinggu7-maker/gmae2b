import bpy
bpy.ops.wm.open_mainfile(filepath='blender/little_dream_demon_lowpoly.blend')
bpy.ops.export_scene.gltf(filepath='blender/little_dream_demon_lowpoly.glb', export_format='GLB', export_animations=True)
