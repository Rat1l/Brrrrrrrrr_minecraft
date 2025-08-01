from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController
app=Ursina()
grass_texture=load_texture("Assets/Textures/Grass_Block.png")
stone_texture=load_texture("Assets/Textures/Stone_Block.png")
brick_texture=load_texture("Assets/Textures/Brick_Block.png")
dirt_texture=load_texture("Assets/Textures/Dirt_Block.png")
wood_texture=load_texture("Assets/Textures/Wood_Block.png")
sky_texture=load_texture("Assets/Textures/Skybox.png")
arm_texture=load_texture("Assets/Textures/Arm_Texture.png")
punch_sound=Audio("Assets/SFX/Punch_Sound.wav",loop=False,autoplay=False)
window.exit_button.visible = True
block_pick = 1
def update():
    global block_pick
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
    if held_keys['1']: block_pick=1
    if held_keys['2']: block_pick=2
    if held_keys['3']: block_pick=3
    if held_keys['4']: block_pick=4
    if held_keys['5']: block_pick=5
    if held_keys['escape']: app.userExit()
class Main(Button):
    def __init__(self,position=(0,0,0),texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model="Assets/Models/Block",
            origin_y =0.5,
            texture=texture,
            color=color.color(0,0,random.uniform(0.9,1)),
            highlight_color=color.light_gray,
            scale=0.5
        )
    def input(self,key):
        if self.hovered:
            if key=="left mouse down":
                punch_sound.play()
                if block_pick==1: main=Main(position=self.position+mouse.normal,texture=grass_texture)
                if block_pick==2: main=Main(position=self.position+mouse.normal,texture=stone_texture)
                if block_pick==3: main=Main(position=self.position+mouse.normal,texture=brick_texture)
                if block_pick==4: main=Main(position=self.position+mouse.normal,texture=dirt_texture)
                if block_pick==5: main=Main(position=self.position+mouse.normal,texture=wood_texture)
            if key=='right mouse down':
                punch_sound.play()
                destroy(self)
