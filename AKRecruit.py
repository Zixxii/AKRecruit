from enum import Enum
import itertools
import time
import keyboard
from PIL import Image,ImageGrab,ImageOps
from pytesseract import pytesseract
import OPs
import string
from itertools import permutations
from itertools import combinations


def main():
    TesseractPath = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    
    Rec = ImageGrab.grab(bbox=(600,500,1250,750))
    Rec.save("Recruit.JPG")
    Tags1 = Rec.crop((0,0,175,100))
    Tags1.save("Tags1.JPG")
    Tags2 = Rec.crop((200,0,375,100))
    Tags2.save("Tags2.JPG")
    Tags3 = Rec.crop((420,20,570,100))
    Tags3.save("Tags3.JPG")
    Tags4 = Rec.crop((0,100,175,200))
    Tags4.save("Tags4.JPG")
    Tags5 = Rec.crop((200,100,375,200))
    Tags5.save("Tags5.JPG")

    
    Recruit = Image.open("D:\Python\AKRecruit\Recruit.PNG")
    
    pytesseract.tesseract_cmd = TesseractPath
    Tags = ''
    Tags += pytesseract.image_to_string(Tags1)
    Tags += pytesseract.image_to_string(Tags2)
    Tags += pytesseract.image_to_string(Tags3)
    Tags += pytesseract.image_to_string(Tags4)
    Tags += pytesseract.image_to_string(Tags5)
    
    #print(Tags[:-1])
    Tagl = ParseTags(Tags)
    print(Tagl)
    comb1 = combinations(Tagl,1)
    comb2 = combinations(Tagl,2)
    comb3 = combinations(Tagl,3)
    comb = []
    for i in comb1:
        comb.append(i)
    for i in comb2:
        comb.append(i)
    for i in comb3:
        comb.append(i)
    #print(comb)
    #print(comb[0][0])
    #print(OPs.Operators[0].tags.)

    #Test
    #if OPs.OP.Guard in OPs.Operators[0].tags: #If Guard Enum is in Chen class Needs work
    #    print('Chen is indeed a guard my dude')

    GetOps(comb)

def ParseTags(TagString):
    Tags = str(TagString)
    Tagb = 0b0000000000000000000000000
    Tagl = list()
    if Tags.find("Sniper") != -1:
        #Tagb += OPs.Sniper
        Tagl.append(OPs.OP.Sniper)    
    if Tags.find("Debuff") != -1:
        #Tagb += OPs.Debuff
        Tagl.append(OPs.OP.Debuff)
    if Tags.find("DP-Recovery") != -1:
        #Tagb += OPs.DPRecovery
        Tagl.append(OPs.OP.DPRecovery)
    if Tags.find("Fast-Redeploy") != -1:
        #Tagb += OPs.FastRedeploy
        Tagl.append(OPs.OP.FastRedeploy)
    if Tags.find("Defense") != -1:
        #Tagb += OPs.Defense
        Tagl.append(OPs.OP.Defense)
    if Tags.find("Senior Operator") != -1:
        #Tagb += OPs.SeniorOp
        Tagl.append(OPs.OP.SeniorOp)
    if Tags.find("Top Operator") != -1:
        #Tagb += OPs.TopOp
        Tagl.append(OPs.OP.TopOp)
    if Tags.find("Melee") != -1:
        #Tagb += OPs.Melee
        Tagl.append(OPs.OP.Melee)
    if Tags.find("Ranged") != -1:
        #Tagb += OPs.Ranged
        Tagl.append(OPs.OP.Ranged)
    if Tags.find("Guard") != -1:
        #Tagb += OPs.Guard
        Tagl.append(OPs.OP.Guard)
    if Tags.find("Medic") != -1:
        #Tagb += OPs.Medic
        Tagl.append(OPs.OP.Medic)
    if Tags.find("Vanguard") != -1:
        #Tagb += OPs.Vanguard
        Tagl.append(OPs.OP.Vanguard)
    if Tags.find("Caster") != -1:
        #Tagb += OPs.Caster
        Tagl.append(OPs.OP.Caster)
    if Tags.find("Defender") != -1:
        #Tagb += OPs.Defender
        Tagl.append(OPs.OP.Defender)
    #if Tags.find("Supporter") != -1:
        #Tagb += OPs.Supporter
        #Tagl.append(OPs.OP.Supporter)
    if Tags.find("Specialist") != -1:
        #Tagb += OPs.SpeciaTagl
        Tagl.append(OPs.OP.Specialist)
    if Tags.find("Healing") != -1:
        #Tagb += OPs.Healing
        Tagl.append(OPs.OP.Healing)
    #if Tags.split('ter')[0].find("Support") != -1:
    #if Tags.find("Support") != -1 and Tags[Tags.find("Support") + len("Support")] != 't':
    #if Tags[Tags.find("Support") + len("Support")] != 'e':
        #Tagb += OPs.Support
        #Tagl.append(OPs.OP.Support)
    if Tags.find("Support") != -1:
        if Tags[Tags.find("Support") + len("Support")] == 'e':
            Tagl.append(OPs.OP.Supporter)
            if Tags.find("Support",Tags.find("Support") + 1) != -1:
                Tagl.append(OPs.OP.Support)
        else:
            Tagl.append(OPs.OP.Support)
            if Tags.find("Support",Tags.find("Support") + 1) != -1:
                Tagl.append(OPs.OP.Supporter)
    if Tags.find("DPS") != -1:
        #Tagb += OPs.DPS
        Tagl.append(OPs.OP.DPS)
    if Tags.find("AoE") != -1:
        #Tagb += OPs.AoE
        Tagl.append(OPs.OP.AoE)
    if Tags.find("Slow") != -1:
        #Tagb += OPs.Slow
        Tagl.append(OPs.OP.Slow)
    if Tags.find("Survival") != -1:
        #Tagb += OPs.Survival
        Tagl.append(OPs.OP.Survival)
    if Tags.find("Shift") != -1:
        #Tagb += OPs.Shift
        Tagl.append(OPs.OP.Shift)
    if Tags.find("Crowd Control") != -1:
        #Tagb += OPs.CrowdControl
        Tagl.append(OPs.OP.CrowdControl)
    if Tags.find("Nuker") != -1:
        #Tagb += OPs.Nuker
        Tagl.append(OPs.OP.Nuker)
    if Tags.find("Summon") != -1:
        #Tagb += OPs.Summon
        Tagl.append(OPs.OP.Summon)
     
    return Tagl


def GetOps(Combo):
    #m = Toplevel(root)
    #m.title = 'Obtainable Operators'

    #frame = Frame(m)
    #frame.grid()
    #OPString = ''
    for i in Combo:
        MinStar = 5
        MaxStar = 5
        Obtainable = []
        ObtainableNames = []
        if OPs.OP.SeniorOp in i:
            MinStar = 5
            MaxStar = 5
        if OPs.OP.TopOp in i:
            MinStar = 6
            MaxStar = 6
        for OP in OPs.Operators:
            Skip = False
            for j in i:
                if j not in OP.tags: #If NOT all tags in the combination are in OP.tags
                    #print(OP.Name + ' can be aquired with combo: ' + i)
                    Skip = True
                    break
            if Skip == True:
                continue

            if OP.Star < MinStar:
                MinStar = OP.Star
            if OP.Star <= MaxStar:
                Obtainable.append(OP)
                ObtainableNames.append(OP.Name)
            #print(OP.Name + " can be aquired with combo: " + str(i))
        if MinStar > 3 and len(Obtainable) > 0:
            print("With combo: " + str(i) + " Obtainable operators =")
            Stars6 = ''
            Stars5 = ''
            Stars4 = ''
            for OP in Obtainable:
                if OP.Star == 6:
                    Stars6 += OP.Name + ', '
                if OP.Star == 5:
                    Stars5 += OP.Name + ', '
                if OP.Star == 4:
                    Stars4 += OP.Name + ', '
            if len(Stars6) > 0 and MaxStar > 5:
                print('6*: ' + Stars6[:-2])
            if len(Stars5) > 0:
                print('5*: ' + Stars5[:-2])
            if len(Stars4) > 0:
                print('4*: ' + Stars4[:-2])
            #print((Obtainable[0].Name))
            print('------------------------------')
        
                
        #else:
        #    continue

        #Build string
        #for comboName in i.name:
        #    OPString += comboName + ' + '
        #OPString += ': '
        #for OPName in ObtainableNames:
        #    OPString += OPName + ', '
        #OPString[-1] = ''
    print('------------------------------')
    return

#root = Tk()
#def ShowOps(Combos: list[OPs.OP], Star6, Star5, Star4):
    #m = Toplevel(root)
    #m.title = 'Obtainable Operators'

    #frame = Frame(m)
    #frame.grid()

    #for i in range(Combos):
        #msg1 = Label(frame,text=)

while(True):
    if keyboard.read_key() == "=":
        main()
    if keyboard.read_key() == "-":
        break