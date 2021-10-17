#26 Tags not including starter/robot
import enum


#SeniorOp =      0b00000000000000000000000001
#TopOp =         0b00000000000000000000000010
#Melee =         0b00000000000000000000000100
#Ranged =        0b00000000000000000000001000
#Guard =         0b00000000000000000000010000
#Medic =         0b00000000000000000000100000
#Vanguard =      0b00000000000000000001000000
#Caster =        0b00000000000000000010000000
#Sniper =        0b00000000000000000100000000
#Defender =      0b00000000000000001000000000
#Supporter =     0b00000000000000010000000000
#Specialist =    0b00000000000000100000000000
#Healing =       0b00000000000001000000000000
#Support =       0b00000000000010000000000000
#DPS =           0b00000000000100000000000000
#AoE =           0b00000000001000000000000000
#Slow =          0b00000000010000000000000000
#Survival =      0b00000000100000000000000000
#Defense =       0b00000001000000000000000000
#Debuff =        0b00000010000000000000000000
#Shift =         0b00000100000000000000000000
#CrowdControl =  0b00001000000000000000000000
#Nuker =         0b00010000000000000000000000
#Summon =        0b00100000000000000000000000
#FastRedeploy =  0b01000000000000000000000000
#DPRecovery =    0b10000000000000000000000000

class OP(enum.Enum):
    SeniorOp = 1
    TopOp = 2
    Melee = 3
    Ranged = 4
    Guard = 5
    Medic = 6
    Vanguard= 7
    Caster= 8
    Sniper = 9
    Defender= 10
    Supporter=11
    Specialist=12
    Healing=13
    Support=14
    DPS=15
    AoE=16
    Slow=17
    Survival=18
    Defense=19
    Debuff=20
    Shift=21
    CrowdControl=22
    Nuker=23
    Summon=24
    FastRedeploy=25
    DPRecovery=26


class Operator:
    Name = ''
    Star = 0
    tags = []

    def __init__(self, Name, Star, tags):
        self.Name = Name
        self.Star = Star
        self.tags = tags


Operators = [
    Operator('Ch\'en',6,[OP.Melee,OP.Guard,OP.DPS,OP.Nuker,OP.TopOp]),
    Operator('Siege',6,[OP.Melee,OP.Vanguard,OP.DPS,OP.DPRecovery,OP.SeniorOp,OP.TopOp]),
    Operator('Shining',6,[OP.Ranged,OP.Medic,OP.Support,OP.Healing,OP.SeniorOp,OP.TopOp]),
    Operator('Nightingale',6,[OP.Ranged,OP.Healing,OP.Support,OP.SeniorOp,OP.TopOp,OP.Medic]),
    Operator('Ifrit',6,[OP.Ranged,OP.AoE,OP.Debuff,OP.SeniorOp,OP.TopOp,OP.Caster]),
    Operator('Exusiai',6,[OP.Ranged,OP.DPS,OP.SeniorOp,OP.TopOp,OP.Sniper]),
    Operator('SilverAsh',6,[OP.Melee,OP.DPS,OP.Support,OP.SeniorOp,OP.TopOp,OP.Guard]),
    Operator('Hoshiguma',6,[OP.Melee,OP.DPS,OP.Defense,OP.SeniorOp,OP.TopOp,OP.Defender]),
    Operator('Saria',6,[OP.Melee,OP.Support,OP.Defense,OP.Healing,OP.SeniorOp,OP.TopOp,OP.Defender]),
    Operator('Skadi',6,[OP.Melee,OP.DPS,OP.Survival,OP.TopOp,OP.Guard]),
    Operator('Schwarz',6,[OP.Ranged,OP.DPS,OP.TopOp,OP.Sniper]),
    Operator('Hellagur',6,[OP.Melee,OP.DPS,OP.Survival,OP.TopOp,OP.Guard]),
    Operator('Texas',5,[OP.CrowdControl,OP.Melee,OP.DPRecovery,OP.SeniorOp,OP.Vanguard]),
    Operator('Zima',5,[OP.Support,OP.Melee,OP.DPRecovery,OP.SeniorOp,OP.Vanguard]),
    Operator('Ptilopsis',5,[OP.Ranged,OP.Healing,OP.Support,OP.SeniorOp,OP.Medic]),
    Operator('Silence',5,[OP.Ranged,OP.Healing,OP.SeniorOp,OP.Medic]),
    Operator('Warfarin',5,[OP.Ranged,OP.Healing,OP.Support,OP.SeniorOp,OP.Medic]),
    Operator('Nightmare',5,[OP.Ranged,OP.DPS,OP.Healing,OP.Slow,OP.SeniorOp,OP.Caster]),
    Operator('Projekt Red',5,[OP.Melee,OP.CrowdControl,OP.FastRedeploy,OP.SeniorOp,OP.Specialist]),
    Operator('Manticore',5,[OP.Survival,OP.Melee,OP.DPS,OP.SeniorOp,OP.Specialist]),
    Operator('Cliffheart',5,[OP.DPS,OP.Melee,OP.Shift,OP.SeniorOp,OP.Specialist]),
    Operator('FEater',5,[OP.Slow,OP.Melee,OP.Shift,OP.SeniorOp,OP.Specialist]),
    Operator('Provence',5,[OP.Ranged,OP.DPS,OP.SeniorOp,OP.Sniper]),
    Operator('Blue Poison',5,[OP.Ranged,OP.DPS,OP.SeniorOp,OP.Sniper]),
    Operator('Firewatch',5,[OP.Ranged,OP.DPS,OP.Nuker,OP.SeniorOp,OP.Sniper]),
    Operator('Meteorite',5,[OP.Ranged,OP.AoE,OP.Debuff,OP.SeniorOp,OP.Sniper]),
    Operator('Platinum',5,[OP.Ranged,OP.DPS,OP.SeniorOp,OP.Sniper]),
    Operator('Pramanix',5,[OP.Ranged,OP.Debuff,OP.SeniorOp,OP.Supporter]),
    Operator('Istina',5,[OP.Ranged,OP.Slow,OP.DPS,OP.SeniorOp,OP.Supporter]),
    Operator('Mayer',5,[OP.Ranged,OP.Summon,OP.CrowdControl,OP.SeniorOp,OP.Supporter]),
    Operator('Specter',5,[OP.Melee,OP.AoE,OP.Survival,OP.SeniorOp,OP.Guard]),
    Operator('Indra',5,[OP.Melee,OP.DPS,OP.Survival,OP.SeniorOp,OP.Guard]),
    Operator('Nearl',5,[OP.Melee,OP.Defense,OP.Healing,OP.SeniorOp,OP.Defender]),
    Operator('Liskarm',5,[OP.Melee,OP.Defense,OP.DPS,OP.SeniorOp,OP.Defender]),
    Operator('Vulcan',5,[OP.Melee,OP.DPS,OP.Defense,OP.Survival,OP.SeniorOp,OP.Defender]),
    Operator('Croissant',5,[OP.Melee,OP.Shift,OP.Defense,OP.SeniorOp,OP.Defender]),
    Operator('Swire',5,[OP.Melee,OP.DPS,OP.Support,OP.SeniorOp,OP.Guard]),
    Operator('Glaucus',5,[OP.Ranged,OP.Slow,OP.CrowdControl,OP.SeniorOp,OP.Supporter]),
    Operator('Astesia',5,[OP.Melee,OP.DPS,OP.Defense,OP.SeniorOp,OP.Guard]),
    Operator('Myrrh',4,[OP.Ranged,OP.Healing,OP.Medic]),
    Operator('Perfumer',4,[OP.Ranged,OP.Healing,OP.Medic]),
    Operator('Sussurro',4,[OP.Ranged,OP.Healing,OP.Medic]),
    Operator('Scavenger',4,[OP.Melee,OP.DPRecovery,OP.DPS,OP.Vanguard]),
    Operator('Vigna',4,[OP.Melee,OP.DPS,OP.DPRecovery,OP.Vanguard]),
    Operator('Myrtle',4,[OP.Melee,OP.DPRecovery,OP.Healing,OP.Vanguard]),
    Operator('Haze',4,[OP.Debuff,OP.Ranged,OP.DPS,OP.Caster]),
    Operator('Gitano',4,[OP.Ranged,OP.AoE,OP.Caster]),
    Operator('Greyy',4,[OP.Slow,OP.AoE,OP.Ranged,OP.Caster]),
    Operator('ShiraYuki',4,[OP.Ranged,OP.AoE,OP.Slow,OP.Sniper]),
    Operator('Meteor',4,[OP.Ranged,OP.DPS,OP.Debuff,OP.Sniper]),
    Operator('Jessica',4,[OP.Ranged,OP.DPS,OP.Survival,OP.Sniper]),
    Operator('Cuora',4,[OP.Melee,OP.Defense,OP.Defender]),
    Operator('Gummy',4,[OP.Melee,OP.Defense,OP.Healing,OP.Defender]),
    Operator('Matterhorn',4,[OP.Melee,OP.Defense,OP.Defender]),
    Operator('Dobermann',4,[OP.Melee,OP.Support,OP.DPS,OP.Guard]),
    Operator('Estelle',4,[OP.Melee,OP.AoE,OP.Survival,OP.Guard]),
    Operator('Beehunter',4,[OP.Melee,OP.DPS,OP.Guard]),
    Operator('Mousse',4,[OP.Melee,OP.DPS,OP.Guard]),
    Operator('Frostleaf',4,[OP.Melee,OP.Slow,OP.DPS,OP.Guard]),
    Operator('Matoimaru',4,[OP.DPS,OP.Melee,OP.Survival,OP.Guard]),
    Operator('Earthspirit',4,[OP.Ranged,OP.Slow,OP.Supporter]),
    Operator('Gravel',4,[OP.Melee,OP.FastRedeploy,OP.Defense,OP.Specialist]),
    Operator('Rope',4,[OP.Melee,OP.Shift,OP.Specialist]),
    Operator('Shaw',4,[OP.Melee,OP.Shift,OP.Specialist]),
    Operator('Hibiscus',3,[OP.Ranged,OP.Healing,OP.Medic]),
    Operator('Ansel',3,[OP.Ranged,OP.Healing,OP.Medic]),
    Operator('Lava',3,[OP.Ranged,OP.AoE,OP.Caster]),
    Operator('Steward',3,[OP.Ranged,OP.DPS,OP.Caster]),
    Operator('Beagle',3,[OP.Melee,OP.Defense,OP.Defender]),
    Operator('Spot',3,[OP.Melee,OP.Healing,OP.Defense,OP.Defender]),
    Operator('Melantha',3,[OP.Melee,OP.DPS,OP.Survival,OP.Guard]),
    Operator('Midnight',3,[OP.Melee,OP.DPS,OP.Guard]),
    Operator('Popukar',3,[OP.Melee,OP.AoE,OP.Survival,OP.Guard]),
    Operator('Fang',3,[OP.Melee,OP.DPRecovery,OP.Vanguard]),
    Operator('Vanilla',3,[OP.Melee,OP.DPRecovery,OP.Vanguard]),
    Operator('Plume',3,[OP.Melee,OP.DPS,OP.DPRecovery,OP.Vanguard]),
    Operator('Kroos',3,[OP.Ranged,OP.DPS,OP.Sniper]),
    Operator('Adnachiel',3,[OP.Ranged,OP.DPS,OP.Sniper]),
    Operator('Catapult',3,[OP.Ranged,OP.AoE,OP.Sniper]),
    Operator('Orchid',3,[OP.Ranged,OP.Slow,OP.Supporter])
]


