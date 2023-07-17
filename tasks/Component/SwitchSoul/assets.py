from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class SwitchSoulAssets: 


	# Click Rule Assets
	# description 
	C_SOU_GROUP_1 = RuleClick(roi_front=(1086,85,158,67), roi_back=(1086,85,158,67), name="sou_group_1")
	# description 
	C_SOU_GROUP_2 = RuleClick(roi_front=(1087,155,162,62), roi_back=(1087,155,162,62), name="sou_group_2")
	# description 
	C_SOU_GROUP_3 = RuleClick(roi_front=(1088,226,154,61), roi_back=(1088,226,154,61), name="sou_group_3")
	# description 
	C_SOU_GROUP_4 = RuleClick(roi_front=(1087,297,157,59), roi_back=(1087,297,157,59), name="sou_group_4")
	# description 
	C_SOU_GROUP_5 = RuleClick(roi_front=(1087,365,154,62), roi_back=(1087,365,154,62), name="sou_group_5")
	# description 
	C_SOU_GROUP_6 = RuleClick(roi_front=(1088,437,156,57), roi_back=(1088,437,156,57), name="sou_group_6")
	# description 
	C_SOU_GROUP_7 = RuleClick(roi_front=(1090,505,156,62), roi_back=(1090,505,156,62), name="sou_group_7")


	# Image Rule Assets
	# 退出式神录 
	I_RECORD_SOUL_BACK = RuleImage(roi_front=(19,9,51,44), roi_back=(19,9,51,44), threshold=0.8, method="Template matching", file="./tasks/Component/SwitchSoul/ss/ss_record_soul_back.png")
	# 预设 
	I_SOUL_PRESET = RuleImage(roi_front=(332,70,90,51), roi_back=(332,70,90,51), threshold=0.8, method="Template matching", file="./tasks/Component/SwitchSoul/ss/ss_soul_preset.png")
	# description 
	I_SOU_SWITCH_1 = RuleImage(roi_front=(971,148,37,35), roi_back=(971,148,37,35), threshold=0.8, method="Template matching", file="./tasks/Component/SwitchSoul/ss/ss_sou_switch_1.png")
	# description 
	I_SOU_SWITCH_2 = RuleImage(roi_front=(978,304,27,29), roi_back=(978,304,27,29), threshold=0.8, method="Template matching", file="./tasks/Component/SwitchSoul/ss/ss_sou_switch_2.png")
	# description 
	I_SOU_SWITCH_3 = RuleImage(roi_front=(973,454,26,26), roi_back=(973,454,26,26), threshold=0.8, method="Template matching", file="./tasks/Component/SwitchSoul/ss/ss_sou_switch_3.png")
	# description 
	I_SOU_SWITCH_4 = RuleImage(roi_front=(971,600,37,26), roi_back=(971,600,37,26), threshold=0.8, method="Template matching", file="./tasks/Component/SwitchSoul/ss/ss_sou_switch_4.png")
	# description 
	I_SOU_SWITCH_SURE = RuleImage(roi_front=(668,401,180,61), roi_back=(668,401,180,61), threshold=0.8, method="Template matching", file="./tasks/Component/SwitchSoul/ss/ss_sou_switch_sure.png")
	# 用于判断是否在式神录里面 
	I_SOU_CHECK_IN = RuleImage(roi_front=(269,69,50,49), roi_back=(269,69,50,49), threshold=0.8, method="Template matching", file="./tasks/Component/SwitchSoul/ss/ss_sou_check_in.png")
	# description 
	I_SOU_CHECK_GROUP_1 = RuleImage(roi_front=(1086,91,22,57), roi_back=(1086,91,22,57), threshold=0.9, method="Template matching", file="./tasks/Component/SwitchSoul/ss/ss_sou_check_group_1.png")
	# description 
	I_SOU_CHECK_GROUP_2 = RuleImage(roi_front=(1086,163,25,57), roi_back=(1086,163,25,57), threshold=0.8, method="Template matching", file="./tasks/Component/SwitchSoul/ss/ss_sou_check_group_2.png")
	# description 
	I_SOU_CHECK_GROUP_3 = RuleImage(roi_front=(1085,234,22,49), roi_back=(1085,234,22,49), threshold=0.8, method="Template matching", file="./tasks/Component/SwitchSoul/ss/ss_sou_check_group_3.png")
	# description 
	I_SOU_CHECK_GROUP_4 = RuleImage(roi_front=(1086,303,21,56), roi_back=(1086,303,21,56), threshold=0.8, method="Template matching", file="./tasks/Component/SwitchSoul/ss/ss_sou_check_group_4.png")
	# description 
	I_SOU_CHECK_GROUP_5 = RuleImage(roi_front=(1088,370,21,53), roi_back=(1088,370,21,53), threshold=0.8, method="Template matching", file="./tasks/Component/SwitchSoul/ss/ss_sou_check_group_5.png")
	# description 
	I_SOU_CHECK_GROUP_6 = RuleImage(roi_front=(1085,443,23,54), roi_back=(1085,443,23,54), threshold=0.8, method="Template matching", file="./tasks/Component/SwitchSoul/ss/ss_sou_check_group_6.png")
	# description 
	I_SOU_CHECK_GROUP_7 = RuleImage(roi_front=(1088,512,21,54), roi_back=(1088,512,21,54), threshold=0.8, method="Template matching", file="./tasks/Component/SwitchSoul/ss/ss_sou_check_group_7.png")


