#coding:gbk
"""
石头剪刀布史波克蜥蜴大对决
作者：阿水
日期:2019\11\16
"""
import random
def name_to_number(name):
	if name==("石头"):
		number=0
	elif name==("史波克"):
		number=1
	elif name==("纸"):
		number=2
	elif name==("蜥蜴"):
		number=3
	elif name==("剪刀"):
		number=4
	else:
		print("Error: No Correct Name")
	return number

def number_to_name(number):
	if number==(0):
		name="石头"
	elif number==(1):
		name="史波克"
	elif number==(2):
		name="纸"
	elif number==(3):
		name="蜥蜴"
	elif number==(4):
		name="剪刀"
	else:
		print("Error: No Correct Name")
	return name

def rpsls(player_choice):
	com_choice=random.randint(0,4)
	print("机器的选择为%s"%number_to_name(com_choice))
	player_choice_number=name_to_number(player_choice)
	print("你的选择为%s"%player_choice)
	if player_choice_number==com_choice:
		print("你和机器选的一样")
	elif (com_choice==3 or 4) and player_choice_number==0:
		print("你赢了")	
	elif (com_choice==4 or 0) and player_choice_number==1:
		print("你赢了")
	elif (com_choice==0 or 1) and player_choice_number==2:
		print("你赢了")
	elif (com_choice==2 or 1) and player_choice_number==3:
		print("你赢了")
	elif (com_choice==2 or 3) and player_choice_number==4:
		print("你赢了")
	else:
		print("机器赢了")
# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
if choice_name!=["石头","史波克","布","蜥蜴","剪刀"]:
	print("Error: No Correct Name")
else:
	print(rpsls(choice_name))
