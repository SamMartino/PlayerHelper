#!/usr/bin/python

import subprocess
import pprint
pp = pprint.pprint

player_stats = {}
for stat in ['STR','DEX', 'CON', 'INT', 'WIS', 'CHA']:
  player_stats[stat] = int(subprocess.check_output("cat myPlayer | grep \"^" + stat + ": [+-][0-9]\+$\" |  cut -d'+' -f2", shell=True))
print strength

weapons = []
weapons.append[{'name': 'Unarmed strike', 'type': 'melee', 'properties': [], 'attack bonus': 0, 'damage_bonus': 0}]

attacks=[None]
for weapon in weapons:
  if weapon['type'] == 'melee' :
    relevant_skill = 'STR'
  else
    relevant_skill = 'DEX'
  attacks.append[{
    'weapon': weapon,
    'skill bonus': player_stats[relevant_skill]
  ]}

pp(list(enumerate(attacks))[1:])

chosen_attack=-1
while chosen_attack not in range(len(attacks))[1:]:
  print "Choose the number of the attack you want from the list above"
  chosen_attack = int(input())

