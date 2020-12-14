bl_info ={
    "name": "Material Library",
    "author" : "Kayla Man",
    "version" : (1,0),
    "blender" : (2,91,0),
    "location" : "View3D > Add > Mesh > New Object",
    "description" : "Stores some materials",
    "warning": "", 
    "wiki_url": "",
    "category": "MaterialCreation"
}

import bpy
from bpy.props import FloatProperty, PointerProperty

class ShaderMainPanel(bpy.types.Panel):
    
    bl_label = "Shader Library"
    bl_idname = "SHADER_PT_MAINPANEL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Shader Library"
    
    def draw(self, context):
        layout = self.layout
        
        obj = bpy.context.active_object
        matref =obj.active_material
        
        row = layout.row()
        row.label(text= "Select a Shader to be added")
        row=layout.row()
        row.operator('shader.glass_operator')
        row=layout.row()
        row.operator('shader.gold_operator') 
        row=layout.row()
        row.operator('shader.silver_operator')
        row=layout.row()
        row.operator('shader.aluminium_operator')
        row=layout.row()
        row.operator('shader.iron_operator')
        row=layout.row()
        row.operator('shader.copper_operator')
        row=layout.row()
        row.operator('shader.titanium_operator')
        row=layout.row()
        row.operator('shader.brass_operator')
        row=layout.row()
        row.operator('shader.plastic_operator')
        row=layout.row()
        layout.prop(matref, "name")
        row=layout.row()
        row.prop(matref.slot_setting, "rough")  

        
class GLASS_SHADER(bpy.types.Operator):
    
    bl_label = "GLASS"
    bl_idname = "shader.glass_operator"
    
    
    def execute(self,context):
        
       
        activeObject = bpy.context.active_object
          
        mat_glass = bpy.data.materials.new(name="Glass")

        mat_glass.use_nodes = True

        activeObject.data.materials.append(mat_glass)
        
        mat_glass.node_tree.nodes.remove(mat_glass.node_tree.nodes.get('Principled BSDF'))

        mat_output = mat_glass.node_tree.nodes.get("Material Output")

        mat_output.location = (-400,0)

        glass_node = mat_glass.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass_node.location = (-600,0)
        glass_node.inputs[0].default_value=(1,1,1,1)
        glass_node.inputs[1].default_value=0.15
        mat_glass.node_tree.links.new(glass_node.outputs[0],mat_output.inputs[0])
            
        return {'FINISHED'}
    
class GOLD_SHADER(bpy.types.Operator):
    bl_label = "GOLD"
    bl_idname = "shader.gold_operator"
    
    def execute(self,context):
        
        activeObject = bpy.context.active_object        
        
        mat_gold = bpy.data.materials.new(name="Gold")
        
        mat_gold.use_nodes= True
        
        activeObject.data.materials.append(mat_gold)
        
        goldNode = mat_gold.node_tree.nodes.get('Principled BSDF')
        goldNode.inputs[0].default_value = (1.0,0.760508,0.327774,1)
        goldNode.inputs[4].default_value=1.0
        goldNode.inputs[5].default_value =0.0
        goldNode.inputs[7].default_value =0.0
        goldNode.inputs[14].default_value =0.47
        
        return {'FINISHED'}

class SILVER_SHADER(bpy.types.Operator):
    bl_label = "SILVER"
    bl_idname = "shader.silver_operator"
    
    def execute(self,context):
        
        activeObject = bpy.context.active_object
      
        
        mat_silver = bpy.data.materials.new(name="Silver")
        
        mat_silver.use_nodes = True
        
        activeObject.data.materials.append(mat_silver)
        silverNode = mat_silver.node_tree.nodes.get('Principled BSDF')
        silverNode.inputs[0].default_value = (0.973456,0.955983,0.913104,1)
        silverNode.inputs[4].default_value=1.0
        silverNode.inputs[5].default_value =0.0
        silverNode.inputs[7].default_value =0.0
        silverNode.inputs[14].default_value =1.35
        
        return {'FINISHED'}
    
class ALUMINIUM_SHADER(bpy.types.Operator):
    bl_label = "ALUMINIUM"
    bl_idname = "shader.aluminium_operator"
    
    def execute(self,context):
        
        activeObject = bpy.context.active_object
      
        mat_alum = bpy.data.materials.new(name="Aluminium")
        
        mat_alum.use_nodes = True
        
        activeObject.data.materials.append(mat_alum)
        AlumNode = mat_alum.node_tree.nodes.get('Principled BSDF')
        AlumNode.inputs[0].default_value = (0.913118,0.921587,0.921591,1)
        AlumNode.inputs[4].default_value=1.0
        AlumNode.inputs[5].default_value =0.0
        AlumNode.inputs[7].default_value =0.0
        AlumNode.inputs[14].default_value =1.44
        
        return {'FINISHED'}
    
class IRON_SHADER(bpy.types.Operator):
    bl_label = "IRON"
    bl_idname = "shader.iron_operator"
    
    def execute(self,context):
        
        activeObject = bpy.context.active_object
            
        mat_iron = bpy.data.materials.new(name="Iron")
        
        mat_iron.use_nodes = True
        
        activeObject.data.materials.append(mat_iron)
        
        ironNode = mat_iron.node_tree.nodes.get('Principled BSDF')
        ironNode.inputs[0].default_value = (0.552015,0.571113,0.571121,1)
        ironNode.inputs[4].default_value=1.0
        ironNode.inputs[5].default_value =0.0
        ironNode.inputs[7].default_value =0.0
        ironNode.inputs[14].default_value =2.95
        
        return {'FINISHED'}
    
class COPPER_SHADER(bpy.types.Operator):
    bl_label = "COPPER"
    bl_idname = "shader.copper_operator"
    
    def execute(self,context):
        
        activeObject = bpy.context.active_object
           
        mat_copper = bpy.data.materials.new(name="Copper")
        
        mat_copper.use_nodes = True
        
        activeObject.data.materials.append(mat_copper)
        
        copperNode = mat_copper.node_tree.nodes.get('Principled BSDF')
        copperNode.inputs[0].default_value = (0.955969,0.630761,0.527113,1)
        copperNode.inputs[4].default_value=1.0
        copperNode.inputs[5].default_value =0.0
        copperNode.inputs[7].default_value =0.0
        copperNode.inputs[14].default_value =2.43
        
        return {'FINISHED'}
    
class TITANIUM_SHADER(bpy.types.Operator):
    bl_label = "TITANIUM"
    bl_idname = "shader.titanium_operator"
    
    def execute(self,context):
        
        activeObject = bpy.context.active_object
            
        mat_titan = bpy.data.materials.new(name="Titanium")
        
        mat_titan.use_nodes = True
        
        activeObject.data.materials.append(mat_titan)
        
        TitanNode = mat_titan.node_tree.nodes.get('Principled BSDF')
        TitanNode.inputs[0].default_value = (0.319,0.319,0.319,1)
        TitanNode.inputs[4].default_value=1.0
        TitanNode.inputs[5].default_value =0.0
        TitanNode.inputs[7].default_value =0.0
        TitanNode.inputs[14].default_value =2.16
        
        return{'FINISHED'}

class BRASS_SHADER(bpy.types.Operator):
    bl_label = "BRASS"
    bl_idname = "shader.brass_operator"
    
    def execute(self,context):
        activeObject = bpy.context.active_object
        
        mat_brass = bpy.data.materials.new(name="Brass")
        
        mat_brass.use_nodes = True
        
        activeObject.data.materials.append(mat_brass)
        
        BrassNode = mat_brass.node_tree.nodes.get('Principled BSDF')
        BrassNode.inputs[0].default_value = (0.955969,0.838804,0.527112,1)
        BrassNode.inputs[4].default_value=1.0
        BrassNode.inputs[5].default_value =0.0
        BrassNode.inputs[7].default_value =0.0
        BrassNode.inputs[14].default_value =0.46
        
        return{'FINISHED'}

class PLASTIC_SHADER(bpy.types.Operator):
    bl_label = "PLASTIC"
    bl_idname = "shader.plastic_operator"
    
    def execute(self, context):
        
        activeObject = bpy.context.active_object
      
        mat_plastic = bpy.data.materials.new(name="Plastic")
        
        mat_plastic.use_nodes = True
        
        activeObject.data.materials.append(mat_plastic)
        
        PlasticNode = mat_plastic.node_tree.nodes.get('Principled BSDF')
        PlasticNode .inputs[4].default_value =0.0
        PlasticNode .inputs[5].default_value =0.0
        PlasticNode .inputs[7].default_value =0.6
        PlasticNode .inputs[14].default_value =1.46
        
        mat_output = mat_plastic.node_tree.nodes.get("Material Output")
        
        mat_output.location = (400,0)
        
        RGB_node = mat_plastic.node_tree.nodes.new('ShaderNodeRGB')
        RGB_node.location = (-400,0)
        mat_plastic.node_tree.links.new(RGB_node.outputs[0], PlasticNode.inputs[0])
        RGB_node.outputs[0].default_value = (0.011612,0.011612,0.011612,1)
        
        return{'FINISHED'}


def updateRough(self, context):
    
    mat = self.id_data
    node = mat.node_tree.nodes
    nodes = [k for k in node
            if isinstance(k, bpy.types.ShaderNodeBsdfPrincipled)]            
    for k in nodes :
        k.inputs[7].default_value = self.rough
        return k
        
    node_glass = [g for g in node
                    if isinstance(g,bpy.types.ShaderNodeBsdfGlass)]     
    
    for g in node_glass:
        g.inputs[1].default_value=self.rough
        return g
        
class roughSet(bpy.types.PropertyGroup):

    rough: FloatProperty(
            name="Roughness",
            subtype='NONE',
            default=0.0,
            min=0, max=1,
            update = updateRough) 
            
def register():
    bpy.utils.register_class(ShaderMainPanel)
    bpy.utils.register_class(GLASS_SHADER)
    bpy.utils.register_class(GOLD_SHADER)
    bpy.utils.register_class(SILVER_SHADER)
    bpy.utils.register_class(ALUMINIUM_SHADER)
    bpy.utils.register_class(IRON_SHADER)
    bpy.utils.register_class(COPPER_SHADER)
    bpy.utils.register_class(TITANIUM_SHADER)
    bpy.utils.register_class(BRASS_SHADER)
    bpy.utils.register_class(PLASTIC_SHADER)
    bpy.utils.register_class(roughSet)
    bpy.types.Material.slot_setting=PointerProperty(type=roughSet)
    
def unregister():
    bpy.utils.unregister_class(ShaderMainPanel)
    bpy.utils.unregister_class(GLASS_SHADER)
    bpy.utils.unregister_class(GOLD_SHADER)
    bpy.utils.unregister_class(SILVER_SHADER)
    bpy.utils.unregister_class(ALUMINIUM_SHADER)
    bpy.utils.unregister_class(IRON_SHADER)
    bpy.utils.unregister_class(COPPER_SHADER)
    bpy.utils.unregister_class(TITANIUM_SHADER)
    bpy.utils.unregister_class(BRASS_SHADER)
    bpy.utils.unregister_class(PLASTIC_SHADER)
    bpy.utils.unregister_class(roughSet)
    del bpy.types.Material.slot_setting

if __name__ == "__main__":
    register()
    