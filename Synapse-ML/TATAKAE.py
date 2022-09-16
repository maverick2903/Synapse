class Titandex:
    def __init__(self,tn,h,ts):
        self.titan_name = tn
        self.height = h
        self.titan_strength = ts
        self.win_streak = 0
    
    def TitanvsScout(self):
        scout_name = input("Enter name of the scout: ")
        scout_strength = input("Enter strength of the scout: ")
        if(self.titan_strength > int(scout_strength)):
            self.win_streak += 1
            print(self.titan_name," defeats ",scout_name," and win streak is ",self.win_streak)
        else:
            self.win_streak = 0
            print(scout_name," defeats ",self.titan_name," and win streak is ",self.win_streak)
            print("Now onto the next Titan\n")

    def TitanvsTitan(self):
        while(True):
            print("Name of the first Titan: ",self.titan_name)
            titan2_name = input("Enter name of the second Titan: ")
            titan2_strength = input("Enter strength of the second Titan: ")
            if(self.titan_strength > int(titan2_strength) and titan2_name!=self.titan_name):
                self.win_streak += 1
                print(self.titan_name," defeats ",titan2_name," and win streak is ",self.win_streak)
                break
            elif(self.titan_strength <= int(titan2_strength) and titan2_name!=self.titan_name):
                self.win_streak = 0
                print(titan2_name," defeats ",self.titan_name," and win streak is ",self.win_streak)
                print("Now onto the next Titan\n")
                break
            else:
                print("Can't make a Titan fight against itself\nTry again\n")
        

titans = ["Founding Titan","Attack Titan","Armored Titan","Colossal Titan","War Hammer Titan","Beast Titan","Cart Titan","Female Titan","Jaw Titan"]
t_height = [13,15,15,60,15,17,4,14,5]
t_strength = [350,275,250,300,235,250,175,270,225]
ch = input("1 for Titan vs Scout and 0 for Titan vs Titan ")
if(ch=='1'):
    for i in range(len(titans)):
        fight = Titandex(titans[i],t_height[i],t_strength[i])
        fight.TitanvsScout()
        while fight.win_streak !=0:
            fight.TitanvsScout()
elif(ch=='0'):
    for i in range(len(titans)):
        fight = Titandex(titans[i],t_height[i],t_strength[i])
        fight.TitanvsTitan()
        while fight.win_streak !=0:
            fight.TitanvsTitan()
