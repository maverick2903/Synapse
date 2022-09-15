creepy_doll = ['red_light', 'green_light', 'red_light', 'you_got_shot', 'green_light', 'you_got_shot',
'you_got_shot', 'green_light', 'you_ got_shot', 'red_light', 'green_light', 'red_light', 'you_got_shot',
'green_light','red_light', 'red_light', 'green_light', 'you_got_shot','red_light', 'you_got_shot']
"""
next_game = ["","","","","",""]
j=0
for i in range(len(creepy_doll)):
    if(creepy_doll[i]=='green_light'):
        next_game[j] = creepy_doll[i:i+1]
        j+=1
"""
next_game = creepy_doll[1:17:3]

print(next_game)