#coding:gbk
"""
ʯͷ������ʷ���������Ծ�
���ߣ���ˮ
����:2019\11\16
"""
import random
def name_to_number(name):
	if name==("ʯͷ"):
		number=0
	elif name==("ʷ����"):
		number=1
	elif name==("ֽ"):
		number=2
	elif name==("����"):
		number=3
	elif name==("����"):
		number=4
	else:
		print("Error: No Correct Name")
	return number

def number_to_name(number):
	if number==(0):
		name="ʯͷ"
	elif number==(1):
		name="ʷ����"
	elif number==(2):
		name="ֽ"
	elif number==(3):
		name="����"
	elif number==(4):
		name="����"
	else:
		print("Error: No Correct Name")
	return name

def rpsls(player_choice):
	com_choice=random.randint(0,4)
	print("������ѡ��Ϊ%s"%number_to_name(com_choice))
	player_choice_number=name_to_number(player_choice)
	print("���ѡ��Ϊ%s"%player_choice)
	if player_choice_number==com_choice:
		print("��ͻ���ѡ��һ��")
	elif (com_choice==3 or 4) and player_choice_number==0:
		print("��Ӯ��")	
	elif (com_choice==4 or 0) and player_choice_number==1:
		print("��Ӯ��")
	elif (com_choice==0 or 1) and player_choice_number==2:
		print("��Ӯ��")
	elif (com_choice==2 or 1) and player_choice_number==3:
		print("��Ӯ��")
	elif (com_choice==2 or 3) and player_choice_number==4:
		print("��Ӯ��")
	else:
		print("����Ӯ��")
# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
if choice_name!=["ʯͷ","ʷ����","��","����","����"]:
	print("Error: No Correct Name")
else:
	print(rpsls(choice_name))
