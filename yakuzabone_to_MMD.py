import bpy
context = bpy.context
obj = context.object

namelist = [
["center_c_n","全ての親"],
["ketu_c_n","下半身"],
["asi1_r_n","右足"],
["asi2_r_n","右ひざ"],
["asi3_r_n","右足首"],
["asi4_r_n","右つま先"],
["asi1_l_n","左足"],
["asi2_l_n","左ひざ"],
["asi3_l_n","左足首"],
["asi4_l_n","左つま先"],
["kosi_c_n","上半身"],
["mune_c_n","上半身2"],
["kubi_c_n","首"],
["face_c_n","頭"],
["_eye_r_n","右目"],
["_eye_l_n","左目"],
["kata_r_n","右肩"],
["ude1_r_n","右腕"],
["ude2_r_n","右ひじ"],
["ude3_r_n","右手首"],
["kou_r_n","small_ring_adjust_r"],
["koyu1_r_n","右小指１"],
["koyu2_r_n","右小指２"],
["koyu3_r_n","右小指３"],
["kusu1_r_n","右薬指１"],
["kusu2_r_n","右薬指２"],
["kusu3_r_n","右薬指３"],
["naka1_r_n","右中指１"],
["naka2_r_n","右中指２"],
["naka3_r_n","右中指３"],
["hito1_r_n","右人指１"],
["hito2_r_n","右人指２"],
["hito3_r_n","右人指３"],
["oya1_r_n","右親指０"],
["oya2_r_n","右親指１"],
["oya3_r_n","右親指２"],
["kata_l_n","左肩"],
["ude1_l_n","左腕"],
["ude2_l_n","左ひじ"],
["ude3_l_n","左手首"],
["kou_l_n","small_ring_adjust_l"],
["koyu1_l_n","左小指１"],
["koyu2_l_n","左小指２"],
["koyu3_l_n","左小指３"],
["kusu1_l_n","左薬指１"],
["kusu2_l_n","左薬指２"],
["kusu3_l_n","左薬指３"],
["naka1_l_n","左中指１"],
["naka2_l_n","左中指２"],
["naka3_l_n","左中指３"],
["hito1_l_n","左人指１"],
["hito2_l_n","左人指２"],
["hito3_l_n","左人指３"],
["oya1_l_n","左親指０"],
["oya2_l_n","左親指１"],
["oya3_l_n","左親指２"],
["",""],
]

for n in namelist:
    pb = obj.pose.bones.get(n[0])
    # continue if no bone of that name
    if pb is None:
        continue
    # rename
    pb.name = n[1]
