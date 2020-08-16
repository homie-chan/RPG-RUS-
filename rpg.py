import random
#Переменные:	
moneyplus1=random.randint(4,5)
opplus1=random.randint(8,9)
moneyplus2=random.randint(6,8)
opplus2=random.randint(14,17)

#1lvl
hprat=15
dmgrat=random.randint(1,3) 
hpspider=15
dmgspider=random.randint(1,3) 
hpslime=15
dmgslime=random.randint(1,3)
#2lvl
hpskelet=40
dmgskelet=random.randint(2,5)
hpgoblin=40
dmggoblin=random.randint(2,5)
hpvolk=40
dmgvolk=random.randint(2,5)
hpsnegovik=40
dmgsnegovik=random.randint(2,5)

hp=20
dmg=5
op=0           #Игрок
uroven=1
money=0
potion=0
bpotion=0
hpmax2=hp-hp+30

spisok=('Магазин:\nЗелья:\nМалое лечебное зелье - 10 золота (5 хп) potion\nБольшое лечебное зелье - 20 золота (10 хп) (2 уровень) bpotion\nУрон:\n1)Деревянный меч - 10 золота (10 урон)\n2)Световой меч - 30 золота (15 урон)\nВыход - Enter')

#Код:
print('Early access v.1.0.1\nДобавил 2 уровень\n--------------------')
print('Добро пожаловать! Для конца напишите "Конец", для продолжения, нажмите "Enter".')
while (1==1):
	if(op>=25):
		uroven=2
	hpspider=15
	hpslime=15
	hprat=15
	hpskelet=40
	hpgoblin=40
	hpvolk=40
	hpsnegovik=40
	s=str(input())
	if ((s=='Конец') or (s=='конец') or (hp<=0)):
		break	
	print('Сейчас у вас: '+ str(hp)+' хп '+ str(dmg)+' урона, и '+str(uroven)+(' уровень.'))
	print('Куда отправимся?')
	vybor=input('1 - В магазин 2 - В бой: ')
	print('--------------------')
	if (vybor=='1'):		
		derewo=['1)Деревянный меч - 10 золота (10 урон)']
		laser=['2)Световой меч - 30 золота (15 урон)']
		print('Ваш баланс: ' + str(money) +' золота и ' +str(op)+' опыта\n' +spisok)
		magazin=input()
		if(magazin=='potion'):
			if((money>=10) and (potion<3)):
				print('Вы купили "Малое лечебное зелье".\n--------------------')
				money=money-10
				potion=potion+1
			elif (potion==3):
				print('У вас максимальное кол-во зелий.\n--------------------')
		elif(magazin=='bpotion'):
			if((money>=20)and(uroven>=2)):
				if((bpotion<=1)and(uroven==2)):
					bpotion=1
					money=money-20
					print('Вы купили "Большое лечебное зелье"!\n--------------------')		
			elif((bpotion==1)and(uroven==2)):
					print('У вас максимальное кол-во зелий.\n--------------------')
			elif(uroven==1):
				print('У вас маленький уровень.\n--------------------')
			elif(money<20):
				print('Недостаточно денег.\n--------------------')
		elif(magazin=='1'):
			if ((money>=10) and (dmg<10)):
			    print('Вы купили "Деревянный меч"!\n--------------------')						
			    money=money-10	   
			    dmg=10 
			    for x in derewo:
	 		       spisok=spisok.replace(x,'1)Деревянный меч (Куплено)')
			elif (money<10):
				print('У вас недостаточно золота, сражайтесь, чтобы заработать больше!\n--------------------')
			elif (dmg>10):
				print('У вас есть предмет получше. \n--------------------')
			elif (dmg==10):
				print('Данный предмет уже куплен и экипирован.\n--------------------')
		elif (magazin=='2'):
			if ((money>=30) and (dmg<15)):
			    print('Вы купили "Световой меч"!\n--------------------')						
			    money=money-30	   
			    dmg=15
			    for x in laser:
	 		       spisok=spisok.replace(x,'2)Световой меч (Куплено)')
			elif (money<30):
				print('У вас недостаточно золота, сражайтесь, чтобы заработать больше!\n--------------------')
			elif (dmg>15):
				print('У вас есть предмет получше. \n--------------------')
			elif (dmg==15):
				print('Данный предмет уже кулен и экипирован.\n--------------------')
		elif (magazin==''):
			print('--------------------')
	elif(vybor=='2'):
		if(uroven==1):
			mob1=random.randint(1,3)
			if (mob1==1):
				print('На вас напала крыса: хп - 15, урон - 1-3')
				while(hprat>0):
					bitvavybor1=int(input('1 - Атаковать 2 - Сбежать 3 - Инвентарь'))
					if (bitvavybor1==1):
						hprat=hprat-dmg
						print('Вы атаковали крысу! теперь её хп: ' +str(hprat))	
						if(hprat>0):
							hp=hp-dmgrat
							print('Крыса атаковала вас в ответ, теперь у вас: ' + str(hp)+ ' хп')
							if (hp<=0):
								print('Вы погибли.')
								break
						elif(hprat<=0):
							money=money+moneyplus1
							op=op+opplus1
							print('Вы победили крысу! Ваш баланс: ' + str(money) +' золота\n--------------------')
							if (op>=25):
								hp=hpmax2
								print('Вы повысили уровень до 2-го!')
					elif (bitvavybor1==2):
						hprat=0
						print('Вы сбежали.\nДля продолжения нажмите Enter\n--------------------')					
					elif (bitvavybor1==3):
						print('Инвентарь:\n1)Малые зелья: '+str(potion)+'\n2)Большие зелья: '+str(bpotion))
						invntvybor1=int(input())
						if (invntvybor1==1):
							if ((hp<20)or(hp==15)or(hp==16)or(hp==17)or(hp==18)or(hp==19)and (potion>0)):
								if ((hp==15)or(hp==16)or(hp==17)or(hp==18)or(hp==19)):
									hp=20
									potion=potion-1
									print('Вы восстановили здоровье, у вас: '+str(hp)+' хп')
								else:
									hp=hp+5
									potion=potion-1
									print('Вы восстановили 5 очков здоровья, у вас: '+str(hp)+(' хп'))
							elif(potion==0):
								print('У вас нет зелий.')
							elif(hp==20):
								print('У вас максимальное здоровье.')							
						elif (invntvybor1==2):
							print('У вас нет зелий.')
			elif (mob1==2):
				print('На вас напал паук: хп - 15, урон - 1-3')
				while(hpspider>0):
					bitvavybor1=int(input('1 - Атаковать 2 - Сбежать 3 - Инвентарь'))
					if (bitvavybor1==1):
						hpspider=hpspider-dmg
						print('Вы атаковали паука! теперь его хп: ' +str(hpspider))	
						if(hpspider>0):
							hp=hp-dmgspider
							print('Паук атаковал вас в ответ, теперь у вас: ' + str(hp)+ ' хп')
							if (hp<=0):
								print('Вы погибли.')
								break
						elif(hpspider<=0):
							money=money+moneyplus1
							op=op+opplus1
							print('Вы победили паука! Ваш баланс: ' + str(money)+' золота\n--------------------')			
							if (op>=25):
								hp=hpmax2
								print('Вы повысили уровень до 2-го!')
					elif (bitvavybor1==2):
						hpspider=0
						print('Вы сбежали.\nДля продолжения нажмите Enter\n--------------------')					
					elif (bitvavybor1==3):
						print('Инвентарь:\n1)Малые зелья: '+str(potion)+'\n2)Большие зелья: '+str(bpotion))
						invntvybor1=int(input())
						if (invntvybor1==1):
							if ((hp<20)or(hp==15)or(hp==16)or(hp==17)or(hp==18)or(hp==19)and (potion>0)):
								if ((hp==15)or(hp==16)or(hp==17)or(hp==18)or(hp==19)):
									hp=20
									potion=potion-1
									print('Вы восстановили здоровье, у вас: '+str(hp)+' хп')
								else:
									hp=hp+5
									potion=potion-1
									print('Вы восстановили 5 очков здоровья, у вас: '+str(hp)+(' хп'))
							elif(potion==0):
								print('У вас нет зелий.')
							elif(hp==20):
								print('У вас максимальное здоровье.')							
						elif (invntvybor1==2):
							print('У вас нет зелий.')
			elif (mob1==3):
				print('На вас напал слизень: хп - 15, урон - 1-3')
				while(hpslime>0):
					bitvavybor1=int(input('1 - Атаковать 2 - Сбежать 3 - Инвентарь'))
					if (bitvavybor1==1):
						hpslime=hpslime-dmg
						print('Вы атаковали слизня! теперь его хп: ' +str(hpslime))	
						if(hpslime>0):
							hp=hp-dmgslime
							print('Слизень атаковал вас в ответ, теперь у вас: ' + str(hp)+ ' хп')
							if (hp<=0):
								print('Вы погибли.')
								break
						elif(hpslime<=0):
							money=money+moneyplus1
							op=op+opplus1
							print('Вы победили слизня! Ваш баланс: ' + str(money)+' золота\n--------------------')				
							if (op>=25):
								hp=hpmax2
								print('Вы повысили уровень до 2-го!')
					elif (bitvavybor1==2):
						hpslime=0
						print('Вы сбежали.\nДля продолжения нажмите Enter\n--------------------')
					elif (bitvavybor1==3):
						print('Инвентарь:\n1)Малые зелья: '+str(potion)+'\n2)Большие зелья: '+str(bpotion))
						invntvybor1=int(input())
						if (invntvybor1==1):
							if ((hp<20)or(hp==15)or(hp==16)or(hp==17)or(hp==18)or(hp==19)and (potion>0)):
								if ((hp==15)or(hp==16)or(hp==17)or(hp==18)or(hp==19)):
									hp=20
									potion=potion-1
									print('Вы восстановили здоровье, у вас: '+str(hp)+' хп')
								else:
									hp=hp+5
									potion=potion-1
									print('Вы восстановили 5 очков здоровья, у вас: '+str(hp)+(' хп'))
							elif(potion==0):
								print('У вас нет зелий.')
							elif(hp==20):
								print('У вас максимальное здоровье.')							
						elif (invntvybor1==2):
							print('У вас нет зелий.')
		elif (uroven==2):
			mob2=random.randint(1,4)
			if (mob2==1):
				print('На вас напал скелет: хп - 40, урон - 2-5')
				while(hpskelet>0):
					bitvavybor1=int(input('1 - Атаковать 2 - Сбежать 3 - Инвентарь'))
					if (bitvavybor1==1):
						hpskelet=hpskelet-dmg
						print('Вы атаковали скелета! теперь его хп: ' +str(hpskelet))	
						if(hpskelet>0):
							hp=hp-dmgskelet
							print('Скелет атаковал вас в ответ, теперь у вас: ' + str(hp)+ ' хп')
							if (hp<=0):
								print('Вы погибли.')
								break
						elif(hpskelet<=0):
							money=money+moneyplus2
							op=op+opplus2
							print('Вы победили скелета! Ваш баланс: ' + str(money) +' золота\n--------------------')
					elif (bitvavybor1==2):
						hpskelet=0
						print('Вы сбежали.\nДля продолжения нажмите Enter\n--------------------')					
					elif (bitvavybor1==3):
						print('Инвентарь:\n1)Малые зелья: '+str(potion)+'\n2)Большие зелья: '+str(bpotion))
						invntvybor1=int(input())
						if (invntvybor1==1):
							if ((hp<30)or(hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)and (potion>0)):
								if ((hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)and(potion>0)):
									hp=30
									potion=potion-1
									print('Вы восстановили здоровье, у вас: '+str(hp)+' хп')
								else:
									hp=hp+5
									potion=potion-1
									print('Вы восстановили 5 очков здоровья, у вас: '+str(hp)+(' хп'))
							elif(potion==0):
								print('У вас нет зелий.')
							elif(hp==30):
								print('У вас максимальное здоровье.')							
						elif (invntvybor1==2):
							if ((hp<30)or(hp==20)or(hp==21)or(hp==22)or(hp==23)or(hp==24) or(hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)and (bpotion>0)):
								if ((hp==20)or(hp==21)or(hp==22)or(hp==23)or(hp==24) or(hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)):
									hp=30
									bpotion=bpotion-1
									print('Вы восстановили здоровье, у вас: '+str(hp)+' хп')
								else:
									hp=hp+10
									bpotion=bpotion-1
									print('Вы восстановили 10 очков здоровья, у вас: '+str(hp)+' хп')
							elif(bpotion==0):
								print('У вас нет зелий.')
							elif(hp==30):
								print('У вас максимальное здоровье.')
			elif (mob2==2):
				print('На вас напал гоблин: хп - 40, урон - 2-5')
				while(hpgoblin>0):
					bitvavybor1=int(input('1 - Атаковать 2 - Сбежать 3 - Инвентарь'))
					if (bitvavybor1==1):
						hpgoblin=hpgoblin-dmg
						print('Вы атаковали гоблина! теперь его хп: ' +str(hpgoblin))	
						if(hpgoblin>0):
							hp=hp-dmggoblin
							print('Гоблин атаковал вас в ответ, теперь у вас: ' + str(hp)+ ' хп')
							if (hp<=0):
								print('Вы погибли.')
								break
						elif(hpgoblin<=0):
							money=money+moneyplus2
							op=op+opplus2
							print('Вы победили гоблина! Ваш баланс: ' + str(money) +' золота\n--------------------')
					elif (bitvavybor1==2):
						hpgoblin=0
						print('Вы сбежали.\nДля продолжения нажмите Enter\n--------------------')					
					elif (bitvavybor1==3):
						print('Инвентарь:\n1)Малые зелья: '+str(potion)+'\n2)Большие зелья: '+str(bpotion))
						invntvybor1=int(input())
						if (invntvybor1==1):
							if ((hp<30)or(hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)and (potion>0)):
								if ((hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)and(potion>0)):
									hp=30
									potion=potion-1
									print('Вы восстановили здоровье, у вас: '+str(hp)+' хп')
								else:
									hp=hp+5
									potion=potion-1
									print('Вы восстановили 5 очков здоровья, у вас: '+str(hp)+(' хп'))
							elif(potion==0):
								print('У вас нет зелий.')
							elif(hp==30):
								print('У вас максимальное здоровье.')							
						elif (invntvybor1==2):
							if ((hp<30)or(hp==20)or(hp==21)or(hp==22)or(hp==23)or(hp==24) or(hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)and (bpotion>0)):
								if ((hp==20)or(hp==21)or(hp==22)or(hp==23)or(hp==24) or(hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)):
									hp=30
									bpotion=bpotion-1
									print('Вы восстановили здоровье, у вас: '+str(hp)+' хп')
								else:
									hp=hp+10
									bpotion=bpotion-1
									print('Вы восстановили 10 очков здоровья, у вас: '+str(hp)+' хп')
							elif(bpotion==0):
								print('У вас нет зелий.')
							elif(hp==30):
								print('У вас максимальное здоровье.')
			elif (mob2==3):
				print('На вас напал волк: хп - 40, урон - 2-5')
				while(hpvolk>0):
					bitvavybor1=int(input('1 - Атаковать 2 - Сбежать 3 - Инвентарь'))
					if (bitvavybor1==1):
						hpvolk=hpvolk-dmg
						print('Вы атаковали волка! теперь его хп: ' +str(hpvolk))	
						if(hpvolk>0):
							hp=hp-dmgvolk
							print(' Волк атаковал вас в ответ, теперь у вас: ' + str(hp)+ ' хп')
							if (hp<=0):
								print('Вы погибли.')
								break
						elif(hpvolk<=0):
							money=money+moneyplus2
							op=op+opplus2
							print('Вы победили волка! Ваш баланс: ' + str(money) +' золота\n--------------------')
					elif (bitvavybor1==2):
						hpvolk=0
						print('Вы сбежали.\nДля продолжения нажмите Enter\n--------------------')					
					elif (bitvavybor1==3):
						print('Инвентарь:\n1)Малые зелья: '+str(potion)+'\n2)Большие зелья: '+str(bpotion))
						invntvybor1=int(input())
						if (invntvybor1==1):
							if ((hp<30)or(hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)and (potion>0)):
								if ((hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)and(potion>0)):
									hp=30
									potion=potion-1
									print('Вы восстановили здоровье, у вас: '+str(hp)+' хп')
								else:
									hp=hp+5
									potion=potion-1
									print('Вы восстановили 5 очков здоровья, у вас: '+str(hp)+(' хп'))
							elif(potion==0):
								print('У вас нет зелий.')
							elif(hp==30):
								print('У вас максимальное здоровье.')							
						elif (invntvybor1==2):
							if ((hp<30)or(hp==20)or(hp==21)or(hp==22)or(hp==23)or(hp==24) or(hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)and (bpotion>0)):
								if ((hp==20)or(hp==21)or(hp==22)or(hp==23)or(hp==24) or(hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)):
									hp=30
									bpotion=bpotion-1
									print('Вы восстановили здоровье, у вас: '+str(hp)+' хп')
								else:
									hp=hp+10
									bpotion=bpotion-1
									print('Вы восстановили 10 очков здоровья, у вас: '+str(hp)+' хп')
							elif(bpotion==0):
								print('У вас нет зелий.')
							elif(hp==30):
								print('У вас максимальное здоровье.')
			if (mob2==4):
				print('На вас напал снеговик: хп - 40, урон - 2-5')
				while(hpsnegovik>0):
					bitvavybor1=int(input('1 - Атаковать 2 - Сбежать 3 - Инвентарь'))
					if (bitvavybor1==1):
						hpsnegovik=hpsnegovik-dmg
						print('Вы атаковали снеговика! теперь его хп: ' +str(hpsnegovik))	
						if(hpsnegovik>0):
							hp=hp-dmgsnegovik
							print('Снеговик атаковал вас в ответ, теперь у вас: ' + str(hp)+ ' хп')
							if (hp<=0):
								print('Вы погибли.')
								break
						elif(hpsnegovik<=0):
							money=money+moneyplus2
							op=op+opplus2
							print('Вы победили снеговика! Ваш баланс: ' + str(money) +' золота\n--------------------')
					elif (bitvavybor1==2):
						hpsnegovik=0
						print('Вы сбежали.\nДля продолжения нажмите Enter\n--------------------')					
					elif (bitvavybor1==3):
						print('Инвентарь:\n1)Малые зелья: '+str(potion)+'\n2)Большие зелья: '+str(bpotion))
						invntvybor1=int(input())
						if (invntvybor1==1):
							if ((hp<30)or(hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)and (potion>0)):
								if ((hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)and(potion>0)):
									hp=30
									potion=potion-1
									print('Вы восстановили здоровье, у вас: '+str(hp)+' хп')
								else:
									hp=hp+5
									potion=potion-1
									print('Вы восстановили 5 очков здоровья, у вас: '+str(hp)+(' хп'))
							elif(potion==0):
								print('У вас нет зелий.')
							elif(hp==30):
								print('У вас максимальное здоровье.')							
						elif (invntvybor1==2):
							if ((hp<30)or(hp==20)or(hp==21)or(hp==22)or(hp==23)or(hp==24) or(hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)and (bpotion>0)):
								if ((hp==20)or(hp==21)or(hp==22)or(hp==23)or(hp==24) or(hp==25)
							or(hp==26) or(hp==27)or(hp==28)or(hp==29)):
									hp=30
									bpotion=bpotion-1
									print('Вы восстановили здоровье, у вас: '+str(hp)+' хп')
								else:
									hp=hp+10
									bpotion=bpotion-1
									print('Вы восстановили 10 очков здоровья, у вас: '+str(hp)+' хп')
							elif(bpotion==0):
								print('У вас нет зелий.')
							elif(hp==30):
								print('У вас максимальное здоровье.')