import bpy, math
from mathutils import Vector

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

def mat(name, color, metallic=0.0, roughness=0.65, emission=None):
    m = bpy.data.materials.new(name)
    m.diffuse_color = (*color, 1)
    m.use_nodes = True
    bs = m.node_tree.nodes.get('Principled BSDF')
    bs.inputs['Base Color'].default_value = (*color, 1)
    bs.inputs['Roughness'].default_value = roughness
    bs.inputs['Metallic'].default_value = metallic
    if emission:
        bs.inputs['Emission Color'].default_value = (*emission, 1)
        bs.inputs['Emission Strength'].default_value = 2.5
    return m

def cube(name, loc, scale, material, bevel=0.0):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    o=bpy.context.object; o.name=name; o.scale=scale; bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.data.materials.append(material)
    if bevel:
        mod=o.modifiers.new('Soft bevel','BEVEL'); mod.width=bevel; mod.segments=2
    return o

def ico(name, loc, radius, material, subdivisions=2):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=subdivisions, radius=radius, location=loc)
    o=bpy.context.object; o.name=name; o.data.materials.append(material); return o

def cyl(name, loc, radius, depth, material, vertices=8):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc)
    o=bpy.context.object; o.name=name; o.data.materials.append(material); return o

navy=mat('Dream Navy',(0.035,0.055,0.14),roughness=.9)
wall=mat('Moonlit Wall',(0.10,0.14,0.29),roughness=.82)
violet=mat('Soft Violet',(0.28,0.25,0.55),roughness=.72)
gold=mat('KEY Gold',(0.92,0.69,0.22),metallic=.55,roughness=.28,emission=(.36,.18,.02))
hero_mat=mat('Dream Demon Coat',(0.20,0.30,0.60),roughness=.72)
skin=mat('Warm Face',(0.86,0.56,0.46),roughness=.75)
eye=mat('Star Eyes',(0.88,0.92,1.0),emission=(.55,.68,1.0))
mist=mat('Mist Blue',(0.34,0.48,0.78),roughness=1.0)

cube('RoomFloor',(0,0,0),(7,5,.2),navy,.12)
cube('BackWall',(0,3.8,3.5),(7,.18,3.5),wall,.08)
cube('LeftWall',(-6.8,0,3.5),(.18,3.8,3.5),wall,.08)
cube('RightWall',(6.8,0,3.5),(.18,3.8,3.5),wall,.08)
cube('MoonlitPlatform',(0,-.5,.5),(2.7,1.8,.3),violet,.18)
cube('Shelf',(-3.9,1.8,2.6),(1.5,.28,.16),violet,.08)
for x in (-4.8,-3.9,-3.0): cyl('ShelfPost',(x,1.8,1.4),.08,2.4,violet,6)

window_mat=mat('Window Blue',(0.20,.32,.62),emission=(.18,.30,.65))
cube('WindowGlow',(3.7,3.55,4.4),(1.45,.08,1.7),window_mat,.04)
for x in (2.45,3.7,4.95): cube('WindowMullion',(x,3.42,4.4),(.06,.12,1.75),navy)
for z in (3.0,4.4,5.8): cube('WindowMullion',(3.7,3.42,z),(1.45,.12,.06),navy)

hero=bpy.data.objects.new('LittleDreamDemon',None); bpy.context.collection.objects.link(hero); hero.location=(0,-1.0,1.5)
body=ico('HeroBody',(0,0,0),.75,hero_mat,2); body.parent=hero
hood=cyl('HeroHood',(0,0,.72),.82,1.0,hero_mat,8); hood.rotation_euler[0]=math.radians(180); hood.parent=hero
face=ico('HeroFace',(0,-.53,.18),.45,skin,2); face.scale=(1,.35,1); face.parent=hero
for x in (-.18,.18):
    e=ico('HeroEye',(x,-.72,.30),.075,eye,2); e.parent=hero
for x in (-.28,.28):
    foot=ico('HeroFoot',(x,-.05,-.78),.24,hero_mat,1); foot.scale=(1.2,1.5,.65); foot.parent=hero

key_root=bpy.data.objects.new('KEY_Animated',None); bpy.context.collection.objects.link(key_root); key_root.location=(3.4,-.7,2.6)
ring=cyl('KeyRing',(0,0,.3),.34,.12,gold,12); ring.rotation_euler[0]=math.radians(90); ring.parent=key_root
stem=cyl('KeyStem',(0,0,-.1),.08,.85,gold,8); stem.parent=key_root
for z in (-.42,-.62):
    tooth=cube('KeyTooth',(.16,0,z),(.18,.08,.06),gold,.03); tooth.parent=key_root

for i,(x,y,z,s) in enumerate([(-5,-1,.55,1.0),(5,.3,.7,1.25),(-4,3,.5,.8),(4,1.8,.4,.7)]):
    o=ico('MistStone'+str(i),(x,y,z),s,mist,1); o.scale=(1.5,.8,.7)

bpy.ops.object.light_add(type='AREA', location=(0,-2,7)); moon=bpy.context.object; moon.name='SoftMoon'; moon.data.energy=900; moon.data.shape='DISK'; moon.data.size=6; moon.data.color=(.45,.58,1.0)
bpy.ops.object.light_add(type='AREA', location=(3,-3,2.5)); fill=bpy.context.object; fill.name='WarmKeyLight'; fill.data.energy=420; fill.data.size=3; fill.data.color=(1.0,.65,.28)
bpy.ops.object.camera_add(location=(10,-14,8)); cam=bpy.context.object; cam.name='GameplayCamera'; bpy.context.scene.camera=cam; cam.data.lens=48
cam.rotation_euler=(Vector((0,0,2.1))-cam.location).to_track_quat('-Z','Y').to_euler()

hero.keyframe_insert('location',frame=1,index=2); hero.location.z=1.68; hero.keyframe_insert('location',frame=18,index=2); hero.location.z=1.5; hero.keyframe_insert('location',frame=36,index=2)
key_root.rotation_euler[2]=0; key_root.keyframe_insert('rotation_euler',frame=1,index=2); key_root.rotation_euler[2]=math.tau; key_root.keyframe_insert('rotation_euler',frame=72,index=2)
key_root.keyframe_insert('location',frame=1,index=2); key_root.location.z=2.85; key_root.keyframe_insert('location',frame=36,index=2); key_root.location.z=2.6; key_root.keyframe_insert('location',frame=72,index=2)
scene=bpy.context.scene; scene.frame_start=1; scene.frame_end=72; scene.render.engine='BLENDER_EEVEE'; scene.render.resolution_x=1280; scene.render.resolution_y=720; scene.render.resolution_percentage=50; scene.render.film_transparent=False
scene.world.color=(.015,.02,.07)
scene.render.filepath='blender/lowpoly_preview.png'
bpy.ops.wm.save_as_mainfile(filepath='blender/little_dream_demon_lowpoly.blend')
bpy.ops.render.render(write_still=True)
try:
    bpy.ops.wm.glTF_export(filepath='blender/little_dream_demon_lowpoly.glb', export_animations=True)
except Exception:
    pass
