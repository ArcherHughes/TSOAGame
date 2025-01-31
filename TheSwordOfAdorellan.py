import time
import random
import sys

def slow_print(text, speed=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
from time import sleep
# # end = "/n/n"
print("                       ~~~~~ The Sword of Adorellan ~~~~~     ")
print('-' * 75)
slow_print("Born the son of an elven scholar and a human merchant, Roman Shadow has always been drawn to history and the mysteries of magic.")
print(" \n\n")
slow_print("Hailing from the once-prosperous city of Tranate, a place now shrouded in fear and despair under the rule of the tyrannical demon lord, Azruloth, who forced his way in to power over a decade ago, not only slaughtering Romans parents, but the city's defenders and enslaving the people. ")
print(" \n\n")
slow_print("Years Roman has been a shadow in the streets, collecting rare and powerful magical artifacts, with the hope that one would bring him closer to overthrowing Azruloth's reign.")
print(" \n\n")
slow_print("Through his travels Roman has discovered many powerful relics from past kingdoms, lost civilizations, and even a few dangerous magical experiments, that could turn the tide in the battle for Tranate, and the Crown of Tyris.")
print(" \n\n")
slow_print("Romans ultimate goal… to acquire the Crown of Tyris, an artifact of legend, said to bestow kingship over not just the realm of man, but all realms. ")
print(" \n\n")
slow_print("The crown, to this day, remains hidden away in an ancient vault, no man or bGo Right has yet reached, but Roman believes he has the map, to find the key to toppling Azruloth, and claiming the throne of Tranate as his own. ")
print(" \n\n")
slow_print("Join Roman on his quest for The Sword of Adorellan, and help him free his people.")
print(" \n\n")
# slow_print('-' * 75)

def zoti_grotto():
    slow_print (f"You are walking along the {current_room ['name']}.")
    slow_print ("You see a figure ahead, and stop as you recognise the outline of an ogre.")
    slow_print ("'Come closer, little one.' he says menacingly, as you stand there wondering what to do.")
    slow_print ("You decide to proceed, but you have only taken two steps when two vanishingly deep trenches open across the corridor, cutting you off in both directions.")
    slow_print ("'Riddle me this, you puny creature.', he spits. 'The bigger I get the less of me there is.'")
    slow_print ("What am I? ")
    lreply: list [str] = input().strip(" .").lower().split()
    if 'hole' not in lreply:
        slow_print ("After a brief moment you see the ogre hurl a large rock at you. It hits you squarely in the chest and you fall, helplessly, backwards into the trench.")
        sleep (1)
        slow_print("You see the trench close over you.")
        sleep (1)
        slow_print ("You are dead.")
        sleep (2)
        slow_print ("'Another fool on a fool's errand. Why do they keep trying?' laughs the ogre, cheerfully.")
        print(grave_art)
        main_game()

    slow_print ("The ogre is not pleased, and responds sourly, 'So, a clever one eh! Well let's see how you cope with this.'")
    slow_print ("Suddenly the air is filled with orange, flickering light and sounds of crackling, as hungry flames fill the trench ahead of you.")
    slow_print ("The ogre speaks again, cruelly, 'You can't \"clever\" your way out of this one. So here you'll die.'")
    slow_print ("Terrified, you feel beads of sweat running down your back, even though you don't feel the heat.")

    reply = input ("What do you want to do? ").strip(" .").lower()
    if reply != "move on":
        if reply == "flee":
            slow_print ("You don't fancy the flaming trench ahead of you, so you decide to take your chances and try to negotiate the trench behind you. Unfortunately for you it's every bit as impassable as it looks. You slip and fall into the trench.")
        else:
            slow_print ("You don't know what to do. Both directions seem equally deadly. While you're pondering your situation the flames move nearer to you, and suddenly the heat hits you, forcing you to back away. As you reach the lip of the trench behind you you struggle to keep your balance, but with nowhere left to go you can't, and you fall into the trench.")

        sleep (1)
        slow_print("You see the trench close over you.")
        sleep (1)
        slow_print ("You are dead.")
        sleep (2)
        slow_print (f"Another fool on a fool's errand. Why do they keep trying?' laughs the ogre, cheerfully.")
        print(grave_art)
        main_game()

def temple():
    global riddle_solved
    if riddle_solved:
        print("you've return to the temple.")
    else:
        print("You enter a dimly lit chamber where two massive golems stand before you.")
        print("One is named Zuun, and the other is Eivid.")
        print("They each pose a riddle you must solve to proceed.")

        print("Roman is left with a choice, does he answers Zunn or Eivids riddle. ")

        choice = input("Choose a golem to answer: Zuun or Eivid: ").strip().lower()

        if choice == "zuun":
                print("\nZuun: My riddle is this:")
                print("The more of it you have, the more still the world becomes. What is it?")
                
                answer1 = input("Your answer: ").strip().lower()
                if answer1 == "silence":
                    print("Zuun nods solemnly. 'You have answered correctly.'")
                    print(f"However, it still means death.{grave_art}")
                    main_game()
                else:
                    print(f"Zuun shakes his head. 'That is incorrect. Beware the consequences.{grave_art}") 
                    main_game()
                
        elif choice == "eivid":
                print("\nEivid: My riddle is this:")
                print("I can fly without feathers and breathe without lungs. From my mouth, I spit what you'd certainly want to shun. What am I?")
                
                answer2 = input("Your answer: ").strip().lower()
                if answer2 == "dragon":
                    print("Eivid lets out a rumbling laugh. 'You are wise indeed.'")
                else:
                    print("Eivid's eyes flare with light. 'That is incorrect. Face the consequences!'")
                    print(f"It still means death. {grave_art}")
                    main_game()
    riddle_solved = True
        

def game_sum():
    print("\n     ~~~~~~  The Labyrinth of Lyre  ~~~~~~")
    print('-' * 38)
    slow_print("Welcome Brave Adventurer to The Labyrinth of Lyre. ")
    print("\n")
    slow_print("Venture forth if you dare. To survive this Labyrinth you will need great directions, Go Forwards, Go Backwards, Go Left, Go Right and don't forget to search.")
    print("\n")
    slow_print("Fare thee well and Good luck.\n")
    print(' ' * 38)

slow_print("As Roman stepped into what appears to be the labyrinth's entrance, the towering hedges opened to reveal an otherworldly garden, where myths and legends seemed to converge. The air was rich with the scent of damp earth and wildflowers, a sharp contrast to the haunting silence that enveloped the maze. Ancient stone archways, carved with intricate knotwork and depictions of dragons and knights, framed the entrance to the garden, their moss-covered surfaces glowing faintly under the filtered light of an overcast sky. Roman noticed above the archways some etchings that looked like ancient writing. From what he could decipher, this room was called \"The Garden of Grie\".")

print("\n\n")

slow_print("The garden itself was a place where nature and art met in delicate harmony. Weathered statues of long-forgotten heroes stood guard among clusters of vibrant, untamed greenery. Vines wove themselves around their arms, almost as if nature sought to reclaim the glories of old. A cobblestone path wound its way through the space, its edges softened by patches of wild thyme and creeping ivy.")

print("\n\n")

slow_print("At the center of the garden stood an ancient fountain, its basin cracked and spilling water that shimmered like liquid silver. The fountain's centerpiece was a sculpture of Yggdrasil, the Norse World Tree, its branches entwined with Celtic knots that seemed to twist and move in the shifting light. Around its base, small pools of water reflected the sky, broken occasionally by ripples as unseen forces disturbed their surface.")

print("\n\n")

slow_print("Beyond the garden, the hedges loomed tall and impenetrable, their tops spiraling into designs reminiscent of a knight's crest or the hammer of Thor. A sense of deep magic lingered here, as if the labyrinth itself were alive, watching, waiting to test any who dared venture further. The Garden of Grie was both a sanctuary and a warning—a place of quiet beauty before the trials of the maze.")
game_sum()

#instructions()#

dragon_art = r"""
                                         _
                       /                            )
                      (                             |\
                     /|                              \\
                    //                                \\
                   ///                                 \|
                  /( \                                  )\
                  \\  \_                               //)
                   \\  :\__                           ///
                    \\     )                         // \
                     \\:  /                         // |/
                      \\ / \                       //  \
                       /)   \     ___..-'         ((  \_|
                      //     /  .'  _.'           \ \  \
                     /|       \(  _\_____          \ | /
                    (| _ _  __/          '-.       ) /.'
                     \\ .  '-.__ \          \_    / / \
                      \\_'.     > '-._   '.   \  / / /
                       \ \      \     \    \   .' /.'
                        \ \  '._ /     \  /   / .' |
                         \ \_     \_   |    .'_/ __/
                          \  \      \_ |   / /  _/ \_
                           \  \       / _.' /  /     \
                           \   |     /.'   / .'       '-,_
                            \   \  .'   _.'_/             \
               /\    /\      ) ___(    /_.'           \    |
              | _\__// \    (.'      _/               |    |
              \/_  __  /--'`    ,                   __/    /
              (_ ) /b)  \  '.   :            \___.-:_/ \__/
              /:/:  ,     ) :        (      /_.'_/-' |_ _ /
             /:/: __/\ >  __,_.----.__\    /        (/(/(/
            (_(,_/V .'/--'    _/  __/ |   /
             VvvV  //`    _.-' _.'     \   \
               n_n//     (((/->/        |   /
               '--'         ~='          \  |
                                          | |_,,,
                                          \  \  /
                                           '.__)
                        Prepare To Fight
"""

grave_art = r"""
      ,-=-.       
     /  +  \       .You Died.
     | ~~~ |    ~~ GAME OVER! ~~
     |R.I.P|       Play Again?
  \vV|_____|Vv/     
"""

# BOSS BATTLE#
player_name ="Roman Shadow"
orientations: list [str] = ['north', 'west', 'south', 'east']
directions: list [str] = ['forwards', 'left', 'backwards', 'right']

class Character:
    name: str
    orientation: str
    health: int
    attack_power: int
    
    def __init__(self, name, health, attack_power):
        self.name = name
        self.orientation = 'north'
        self.health = health
        self.attack_power = attack_power

    def set_orientation (self, new_orientation: str) -> None:
        if new_orientation in orientations:
            self.orientation = new_orientation

    def get_orientation (self) -> str:
        return self.orientation

    # takes 'forwards', 'left', 'backwards', or 'right',
    # updates the orientation, and returns the new orientation.
    rotations: dict [str, dict [str, str]] = {
        'north': {'forwards': 'north',
                  'left': 'west',
                  'backwards': 'south',
                  'right': 'east'},
        'west': {'forwards': 'west',
                  'left': 'south',
                  'backwards': 'east',
                  'right': 'north'},
        'south': {'forwards': 'south',
                  'left': 'east',
                  'backwards': 'north',
                  'right': 'west'},
        'east': {'forwards': 'east',
                  'left': 'north',
                  'backwards': 'west',
                  'right': 'south'}
    }
    def turn (self, direction: str) -> str:
        if direction in directions:
            self.orientation = self.rotations [self.orientation][direction]
        return self.orientation

    def attack(self, other) -> None:
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage!")

    def heal(self) -> None:
        heal_amount = random.randint(1, 10)
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount} health!")

    def is_alive(self) -> bool:
        return self.health > 0
    


def play_game():
    player = Character("Roman Shadow", 100, 20)
    boss = Character("Jormunsmog", 150, 15)
    reduced_damage: bool = False
    print("The heavy oak doors groaned as they swung open, the sound echoing through the vast chamber. Roman Shadow stepped cautiously into the hall, his boots striking the cold stone floor with a deliberate rhythm. The air was heavy with the scent of smoke and ancient wood, the faint flicker of torchlight barely illuminating the towering wooden beams overhead, intricately carved with knotwork and depictions of battles long past.In the center of the room, bathed in the dim glow of a solitary brazier, lay the dragon. Its massive form sprawled on the ground like a shadow given monstrous life. Scales glistened like molten iron, each one reflecting a hint of the modest light, creating an almost hypnotic ripple as the beast shifted. The dragon's eyes, fiery orbs of orange and gold, tracked Roman's every step, narrowing slightly as the intruder dared to enter its domain.The walls of the hall seemed to close in as Roman approached, their engravings of warriors clashing with dragons telling tales of triumph and loss. Above, the vaulted ceiling vanished into darkness, a yawning void that pressed down on the room with a suffocating weight.With a low, guttural growl, the dragon unfurled its wings, the motion stirring the air into a chilling draft that extinguished the nearest torches. Shadows danced wildly across the room, making the beast seem even larger, more menacing. Roman tightened his grip on his weapon, the cold steel reassuring against his hand as he squared his shoulders.This was no mere room. This was a throne of battle, and the dragon its sovereign.")
    while player.is_alive() and boss.is_alive():
        print(f"\n{player.name} Health: {player.health}")
        print(f"{boss.name} Health: {boss.health}\n")

        action = input("Choose your action (attack/heal/defend): ").strip(' .').lower()
        if action == "attack":
            player.attack(boss)
        elif action == "heal":
            player.heal()
        elif action == "defend":
            print(f"{player.name} is defending and will take reduced damage from the next attack!")
            reduced_damage = True
        else:
            print("Invalid action. Please choose 'attack', 'heal', or 'defend'.")
            reduced_damage = False

        if boss.is_alive():
            if action == "defend" and reduced_damage:
                damage = random.randint(1, boss.attack_power) // 2
                print(f"{boss.name} attacks, but {player.name} defends! Damage reduced to {damage}.")
                player.health -= damage
            else:
                boss.attack(player)

        # Reset reduced damage before the next round
        reduced_damage = False

    if player.is_alive():
        print("\nCongratulations! You have defeated the boss! Roman sees the sword in the stone when the body disappears. He walks over and grips hold of the blade handle.\nWith a single pull, the stone is freed from the stone.")
        print("With sword in hand, Roman leaves the labyrinth and continues on his quest, having now collected the last artifact needed to defeat the overlord and claim back the kingdom.")
    else:
        print(f"\nYou have been defeated by the boss. Better luck next time!{grave_art}")
        main_game()

def boss_battle() -> None:
   
    play_game()
    restart = input("Would you like to play again? (yes/no): ").strip().lower()
    if restart == "yes":
        print("Game restarting")
        main_game()
    else:
        print("Thank you for playing! Goodbye.")
        sys.exit()
        
# data setup
rooms: dict [str, dict] = {
    'Garden of Grie':
       {'name': 'Garden of Grie',
        'item': [],
        'right': 'Clinker\'s Cache',
        # 'forwards': 'Turmatir\'s Tunnel',
        'left': 'Bunco\'s Concourse',
        'location': 'You are in the Garden of Grie.'},

    'Bunco\'s Concourse':
       {'name': 'Bunco\'s Concourse',
        'item': ['Fire Sword'],
        'backwards': 'Garden of Grie',
        'right': 'Haven Shield',
        'left': 'Abbadon\'s Shelter',
        'location': 'You are on Bunco\'s Concourse.'},

    'Haven Shield':
       {'name': 'Haven Shield',
        'item': ['Magic Ring'],
        'backwards': 'Bunco\'s Concourse',
        'forwards': 'The Temple of Garuch',
        'right': 'Pali Room',
        'location': 'You are in the Haven Shield.'},

    # 'Turmatir\'s Tunnel':
    #    {'name': 'Turmatir\'s Tunnel',
    #     'item': ['Healing Potion'],
    #     'forwards': 'Jurmunsmog\'s Lair',
    #     'backwards': 'Garden of Grie',
    #     'location': 'You are in Turmatir\'s Tunnel.'},

    'Clinker\'s Cache':
       {'name': 'Clinker\'s Cache',
        'item': ['Sandwich'],
        'backwards': 'Garden of Grie',
        'left': 'Pali Room',
        'location': 'You are in Clinker\'s Cache.'},

    'The Temple of Garuch':
       {'name': 'The Temple of Garuch',
        'item': ['Shield'],
        'left': 'Jurmunsmog\'s Lair',
        'backwards': 'Haven Shield',
        'location': 'You are in The Temple of Garuch.'},

    'Zoti\'s Grotto':
       {'name': 'Zoti\'s Grotto',
        'item': ['Shield'],
        'backwards': 'Pali Room',
        'location': 'You are in Zoti\'s Grotto.'},

    'Pali Room':
       {'name': 'Pali Room',
        'item': [],
        'left': 'Haven Shield',
        'backwards': 'Clinker\'s Cache',
        'forwards': 'Zoti\'s Grotto',
        'location': 'You are in the Pali Room.'},

    # insta death
    'Abbadon\'s Shelter':
       {'name': 'Abbadon\'s Shelter',
        'location': 'You are in Abbadon\'s Shelter. How unlucky you are.'},

    # Dragon
    'Jurmunsmog\'s Lair':
       {'name': 'Jurmunsmog\'s Lair',
        'item': ['Magic Key'],
        # 'right': 'Turmatir\'s Tunnel',
        # 'forward': 'Winner\'s Square',
        'backwards':'The Temple of Garuch',
        'location': 'You are in Jurmunsmog\'s Lair.'}
    }
current_room: dict = rooms ['Garden of Grie']
inventory: list [str] = ['Battle Axe', '2 gold coins', 'Sandwich', 'hairpin' ]
riddle_solved = False
verbs: list [str] = ['go', 'search', 'battle', 'attack', 'defend', 'heal', 'quit', 'take', 'use', 'drop', 'look', 'turn']

command: str            # as typed in by the player, then stripped and lowered
scommand: list [str]    # as split into words
verb: str               # the verb extracted from 'scommand', if present
cmdtail: list [str]     # the rest of the words in the command, if any


# get a player command
def get_user_command (prompt: str = "Enter Move: ") -> tuple [str, list [str]]:
    # get user input
    verb: str = ""
    cmdtail: list [str] = []

    command = input (prompt).strip (' .').lower()
    scommand = command.split()
    if len (scommand) == 0:
        verb = ''
        cmdtail = []
    else:
        verb = scommand [0]
        if len (scommand) == 1:
            cmdtail = []
        else:
            cmdtail = scommand[1::]

#    # DEBUG
#    print (f"Verb: '{verb}', command tail: '{cmdtail}'")

    return (verb, cmdtail)

def match_abbr_str (abbr: str, str_list: list [str]) -> str:

    if abbr == "":
        return ""

    s: str
    for s in str_list:
        if s.startswith (abbr):
            return s

    return ""


# game loop
def main_game():
    global current_room, inventory, verbs, command, verb, cmdtail
    #directions: list [str] = ['forwards', 'backwards', 'right', 'left']
    current_room = rooms ['Garden of Grie']
    inventory = ['Battle Axe', '2 gold coins', 'Sandwich', 'hairpin' ]

    verbs = ['go', 'search', 'battle', 'attack', 'defend', 'heal', 'quit', 'take', 'use', 'drop', 'look', 'turn']

    # command: str            # as typed in by the player, then stripped and lowered
    # scommand: list [str]    # as split into words
    # verb: str               # the verb extracted from 'scommand', if present
    # cmdtail: list [str]     # the rest of the words in the command, if any
    while True:

        if current_room['name'] == 'Jurmunsmog\'s Lair':
            print('You have reached Jurmunsmog\'s Lair.')
            print(dragon_art)
            print('Are you prepared to battle, or will you go back?')
    #        command = input ('Enter Move: ').strip (' .').lower()
            (command, cmdtail) = get_user_command()
            verb = match_abbr_str (command, verbs)
            if command == 'battle':
                boss_battle()
        
        elif current_room['name'] == 'Abbadon\'s Shelter':
            slow_print('You have been bitten by Tal-Tal. \n Your vision blurs, as you turn to retreat, your steps falter, you hit the floor with a hard thump. \n You have died by Taipan venom.')
            print(grave_art)
            main_game()
        elif current_room['name']== 'The Temple of Garuch':
            slow_print("The passage opened into a circular chamber, its walls lined with towering runic inscriptions, that shimmered faintly in hues of blue and gold. The ceiling, high and vaulted, seemed to disappear into an endless void, and the air carried an oppressive weight, as though the room itself were alive and judging every breath.\n\nAt the far end of the room stood two massive golems, each carved from stone but distinct in their design.\n\nThe golem on the left was lighter grey than the surrounding stone wall, and looked rather rough around the edges, its left arm covered in sharp spikes and its shoulders supporting two large stalagmites. Its body looked aged and weathered with moss and cracks decorating its stone structure. Across its chest, the word “Truth” was etched in glowing runes.\\nnThe golem on the right was a stark contrast. A jagged, uneven construct of dark stone and marble, its surface cracked and veined with fiery orange light that pulsed like a heartbeat. Its face twisted into a cruel grin, and its gaze seemed to pierce into the soul with mocking intent.\n\nThis one differs as its right arm was covered in spikes, moss grew around the mid-section only and the legs were more spear shaped with pointed ends for feet. Across its chest, the word “False” burned bright, the letters shifting and flickering as if refusing to stay still.\n\nBetween the two stood a pedestal carved from black granite, its surface engraved with an intricate labyrinth design that seemed to shift under Roman’s gaze. On it rested an ancient horn, gilded with gold and adorned with runes that promised wisdom to those who dared to blow it. As Roman stepped further into the room, the golems stirred, their heavy stone limbs grinding against one another as they turned to face him.\n\nThe chamber seemed to grow colder, and an ancient voice echoed from the walls, deep and resonant, shaking the air. “One speaks only truth, and the other only lies. Ask wisely, for the path ahead depends on your wit.” The golems moved no further but stood ready, their glowing eyes fixed on Roman, silently daring him to choose his questions carefully.")
            temple()
    
        elif current_room['name']== 'Zoti\'s Grotto':
            print("How unlucky you are.")
            zoti_grotto()
            return current_room['name'] == 'Haven Shield'
        
        elif current_room['name']== 'Clinker\'s Cache':
            slow_print("You step into a vast chamber carved deep into the heart of the fortress, the air thick with the tang of iron and leather. The walls shimmer faintly in the modest torchlight, etched with runes of protection and old battle hymns. Along the walls, racks of weapons and armor stand in disorderly rows. Swords, of every kind, forged by Arthurian smiths. Axes with crescent blades and thick hafts sit beside massive war hammers, their heads shaped like snarling beasts.\n\nAt the center of the room is a grand table, its surface scarred by decades of use. Upon it rests an array of round wooden shields, adorned with Norse knotwork, larger kite shields embossed with crests of dragons, stags, and lions.\n\nBehind the table, a hulking suit of plate armor looms, its polished steel shimmering like moonlight. A forge blazes in a corner, tended by a shadowy figure, perhaps the smith or guardian of the armory. The steady rhythm of the hammer echoes through the chamber, accompanied by the hiss of water as fresh-forged steel cools in its depths.")
        
        elif current_room['name']== 'Haven Shield':
            slow_print("Roman enters cautiously, pushing open the weathered wooden door, its iron hinges groaning. Inside, the air feels different... lighter, quieter, as though the very walls hum with an ancient magic warding off evil. This is a sanctuary, a rare reprieve amidst the labyrinth's dangers.\n\nThe room is modest in size, its stone walls marked with faint carvings of protective sigils, their meaning lost to time.\n\nIn the far corner, a small hearth burns faintly with a bluish flame, offering warmth but no smoke. The light dances off scattered belongings strewn across the room, a grim reminder of those who came before you.\n\nYou see several adventurer bags abandoned, their leather cracked and buckles rusted. One bag spills its contents: a broken flask, a few tarnished coins, and a map with edges worn by handling.\n\nNearby, a wooden box sits ajar, revealing shards of vials that once contained healing elixirs.\n\nClay vases line the walls, their lids slightly askew. Some appear empty, while others seem to contain supplies left by those with better fortune: dried rations, old bandages, and a single glowing crystal.\n\nAmidst the clutter, you notice a battered longsword leaning against the wall and a dented helmet beside it, both left behind by an adventurer who likely never returned to claim them. The room is silent but for the faint crackle of the flame, and for now, it feels as though the world outside cannot touch you.")

        # display current location and inventory
    #    print (f"\nYou are in {current_room ['name']}.")
        print (f"\n{current_room ['location']}")

        # point out the fire exits
        exits = []
        for x in directions:
            if x in current_room:
                exits.append (x)
        l = len (exits)
        if l == 0:
            print ("There are no exits from this place.")
        elif l == 1:
            print (f"there is 1 exit from here, {exits [0]} from you.")
        else:
            print (f"There are {l} exits from here", end = '')
            for x in exits:
                print (f", {x}", end = '')
            print (" from you.")

        print (f'Your current inventory: {inventory}\n')

        # get user input
    #    command = input('Enter Move: ').strip (' .').lower()
    #    scommand = command.split();
    #    if len (scommand) == 0:
    #        verb = ''
    #        cmdtail = []
    #    else:
    #        verb = match_abbr_str (scommand [0], verbs)
    #        if len (scommand) == 1:
    #            cmdtail = []
    #        else:
    #            cmdtail = scommand[1::]
        (command, cmdtail) = get_user_command()
        verb = match_abbr_str (command, verbs)

    #    # DEBUG
    #    print (f"Verb: '{verb}', command tail: '{cmdtail}'")

        # movement?
        if verb == "go":
            # if direction missing
            if len (cmdtail) == 0:
                print ("\nMissing direction\n")
                continue

            direction = match_abbr_str (cmdtail [0], directions)

            # if direction missing
            if direction == "":
                print ("\nInvalid direction.\n")
                continue
            # if exit in direction in current_room:
            if direction in current_room:
                # go to next room in 'direction'
                current_room = rooms[current_room[direction]]
            else:
                # bad direction command
                print('\nYou cannot go that way.\n')
                continue

        # quit game?
        elif verb == 'quit':
            print('\nThanks for playing!\n')
            break

        # search for useful items?
        elif verb == 'search':
            # is the item list of the room populated?
            if len (current_room['item']) != 0:
                inventory.extend (current_room['item'])
                print(f"\nYou acquired : {current_room['item']}.\n")
                current_room ['item'].clear()
    #            print(inventory)
    #        elif len (current_room['item']) == 0:
            else:
                print("\nNo items to collect in this room.\n")
        elif verb == 'attack':
            pass
        elif verb == 'heal':
            pass
        elif verb == 'defend':
            pass
        elif verb == 'take':
            pass
        elif verb == 'use':
            pass
        elif verb == 'drop':
            pass
        elif verb == 'look':
            pass
        elif verb == 'turn':
            pass
        else:
            print ("That is not a valid verb. Please try again.")


    #if __name__ == "__main__":
    #
    #    buddy: Character = (Character ('Buddy', 100, 20))
    #
    #    orientation: str
    #    new_orientation: str
    #    direction: str
    #
    #    # test all combinations of starting orientation, and direction turned
    #    for orientation in orientations:
    #        for direction in directions:
    #            buddy.set_orientation (orientation)
    #            buddy.turn (direction)
    #
    #            print (f"Starting at '{orientation}', turning '{direction}', and arriving at '{buddy.get_orientation()}'.")
    #        print()   
main_game()