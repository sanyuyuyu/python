
#n = int(input("请输出一个整数："))
#sum = 0
#print("1~%d的求和结果为"%(n,sum))

for i in range(1,10):
    for j in range(1,i+1):
            print("%d*%d=%-2d"%(j,i,i*j),end="")
    print("")






import time
import random

while True:
    #counter
    player_victory=0
    enemy_victory=0
    #cycle times also the number of the game
    for i in range(1,4):
        time.sleep(1.5)
        #attribute
        print('第%s局------开始'% i)
        player_HP=random.randint(8,10)
        player_A=random.randint(3,5)
        enemy_HP=random.randint(8,10)
        enemy_A=random.randint(3,5)
        #let the player know the imformations of the game
        print('player \n HP:%s\n attack:%s'% (player_HP,player_A))
        time.sleep(1)
        print('enemy \n HP:%s\n attack:%s'%(enemy_HP,player_A))
        time.sleep(1)
        #coures of battle
        while player_HP>0 and enemy_HP>0:
            player_HP=player_HP-enemy_A
            enemy_HP=enemy_HP-player_A
            print("you are attacking the enemy,and the enemy's HP drop to %d"%enemy_HP)
            time.sleep(1)
            print("you are attacked by the enemy ,and your HP is droping to %d"%player_HP)
            time.sleep(1)
            print('----------------------------------------------------')
            
        if player_HP>0 and enemy_HP<=0:
                print('Victory！')
                player_victory+=1
        elif player_HP<=0 and enemy_HP>0:
                print('Failure...')
                enemy_victory+=1
        else:
                print('what just happened?')
        time.sleep(1)
            
            
        if player_victory>enemy_victory:
            print('Win!')
        elif player_victory<enemy_victory:
            print('Failure...')
        else:
            print('dogfall')
    answer=input('Are you really wanting to continue?')
    if answer!='yes':
       break








