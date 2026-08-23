# Sky-CotL-Archipelago
A Manual Archipelago for Sky: Children of the Light

This archipelago is a [manual](https://github.com/ManualForArchipelago/Manual), meaning there is no mod and you will need to manually input all checks you get.<br />
You will also be responsible for not using items you don't have unlocked.

## Setup for Hosts
Make sure you have the [Archipelago Launcher](https://github.com/ArchipelagoMW/Archipelago/releases/latest)<br />
(The release is under "Assets" at the bottom of the page)

Download and install "manual_skycotl_raycast.apworld" from the [latest release](https://github.com/Vykolue/Sky-Cotl-Archipelago/releases/latest)<br />
Do NOT rename this file, as it may cause errors

To install manually:
- Locate your archipelago installation
- Place the file in your custom_worlds folder

Get a YAML file from the player (more on this below)<br />
Place it in the Archipelago/Players/ folder

When you have all apworlds and YAMLs needed for your game, run the launcher<br />
(if it is already running, restart it)<br />
Use "Generate" to create your world<br />
The generated world will show up in your Archipelago/output/ folder

Hosting on the Archipelago website:
1. Run the world on the archipelago website by uploading it to https://archipelago.gg/uploads
2. After hosting the world, save the room link you are redirected to for future reference
3. The port will be listed on the room page, but it may change after a period of inactivity
4. If your players have trouble connecting:
    - refresh the room to ensure the server is running
    - ensure they are using the correct server and port number (for example: archipelago.gg:12345)
    - ensure the name they are using to connect matches their slot name listed under the "Name" column (case sensitive)
    - ensure they are using the correct password if you set a password


## Setup for Players
To play this game, you will need the [Archipelago Launcher](https://github.com/ArchipelagoMW/Archipelago/releases/latest)<br />
(The release is under "Assets" at the bottom of the page)

Download and install "manual_skycotl_raycast.apworld" from the [latest release](https://github.com/Vykolue/Sky-Cotl-Archipelago/releases/latest)<br />
Do NOT rename this file, as it may cause errors

To install manually:
- Locate your archipelago installation
- Place the file in your custom_worlds folder

### Getting your YAML
What is a YAML?
- This file allows you to customise certain options for your game
- You still need a YAML, even if you wish to use the default options
- This will tell Archipelago your slot name and what game you are playing

There are a few ways to get your YAML:

Option 1:
1. Download "Manual_SkyCotL_raycast.yaml" from the [latest release](https://github.com/Vykolue/Sky-Cotl-Archipelago/releases/latest)
2. No need to change anything if you want to use the default options
3. Send it to your host

Option 2:
1. Download the same file from Option 1
2. Open it in a text editor
3. Update your name and options following the instructions in the file
4. Send it to your host

Option 3:
1. Run the Archipelago Launcher
2. Open the "Options Creator"
3. Select "Manual_SkyCotL_raycast" from the list
4. Update your options and export
5. Send the file to your host

### Connecting to a game
Run the Archipelago Launcher<br />
Open the "Manual Client"<br />
Connect to the server that your game is running on:
- Type the server name and port next to "Server:"
- If you don't know it, ask your host

Enter your name (and password, if prompted) in the command line

#### If you can't connect
Make sure:
- the game is actively being hosted and the server isn't down
- you are using the correct port
- the name you are using to connect matches your slot name (case sensitive)

## Playing the game
You can play Sky: Children of the Light on any device<br />
This README is intended to expain the gameplay for version 0.2.3 of the apworld, and may not apply to other versions

To send a check:
1. Connect to the Manual Client (as described above)
2. Switch to the "Manual" tab
3. Find the check you got under "Remaining Locations"
4. Click it to send it

You can see checks you send and receive in real time under the "Archipelago" tab<br />
Items you receive will also show up under "Items Received" in the "Manual" tab<br />
You can see hints in the "Hints" tab

### Tips
- You can use "!hint {item_name}" in the command line to find out where the specified item is
- You will need points to afford a hint, which can be earned by sending checks
- Use "/items" to see the names of all items
- Press F1 to change the sort order of items and locations. 
Changing the sort order to "natural" will use the order that I intended
- If using Universal Tracker with accidental button press protection, 
use "/send {location_name}" to send a location out of logic, 
or use the F1 menu to toggle this setting off

The area a Child of Light is in corresponds to where it appears when looking at your map

Note: these areas may not match the Sky: Children of the Light wiki exactly<br />
If you lose all Winged Light before playing (or are reborn and don't collect any new Winged Light), 
you will be able to use your map to track how many Children of Light you have found in each area

### Rules
Don't send checks you didn't earn

Don't use items that haven't been unlocked<br />
Your locked items will depend on your YAML settings, but may include:
- realms `(always on)`
- the Wandering Carnival area `(always on)`
- wedges `(always on)`
- shortcuts `(always on)`
- passing through spirit gates `(on by default)`
- cosmetics `(off by default)`
- props `(on by default)`
- base emotes `(on by default)`
- seasonal emotes `(off by default)`

Shortcut locks will lock the following areas' shortcuts from being used without the shortcut item:
- The Wind Paths `(locks everything except the Forest Rest connection)`
- The Treehouse `(locks everything except the Forest Rest connection)`
- Harmony Hall `(locks everything except the Village of Dreams connection)`
- Story Space `(locks everything except the Vault Rest connection)`

Cosmetic locks can be done one of two ways:<br />
Method 1:
- cosmetics are unlocked along with the spirit you get them from
- turn on cosmetic locks to lock cosmetics not obtained from a regular or seasonal spirit
- using cosmetic locks, all remaining cosmetic items will be received by category
- some categories may be left out of the game since they are considered filler items
Method 2:
- turn on cosmetic locks
- all cosmetics are unlocked by category
- some categories may be left out of the game since they are considered filler items

If emote locks are on, you should have the corresponding emote before entering areas that require it, 
even if other players opened the door<br />
Likewise, you shouldn't have a friend drag you through a locked Spirit Gate

Do not use piggy rocket, chibi fall, white candle, warp, follow, or other items to gain a large advantage<br />
I recommend against using props, shared spaces, shared memory recharge, friend recharge, etc. 
to easily get somewhere that is possible to reach otherwise, or to get somewhere out of logic<br />
If you receive the item, feel free to use it in this way, however, they will not be required to progress<br />
I intend to add logic for them in a future update

"Find Children of Light" means you can either collect it, or stand on where it normally is

"Wedges" are how many wedges you are allowed to use<br />
You are free to use a partial wedge, even if it causes you to use part of a wedge you don't have unlocked

You can lose all your Winged Light before playing<br />
If you start with extra, you won't be able to use it until someone unlocks your wedges for you

You may run into impossible scenerios if your account has not:
- relived enough Base Spirit Memories to unlock all Spirit Gates and use emotes required to enter certain areas
- unlocked shortcuts for The Wind Paths, The Treehouse, and Harmony Hall
- progressed through the first three Cave of Prophecy quests
- progressed through the Vault of Knowledge

You may also be required to:
- complete all Nine-Colored Deer quests
- complete all Season of Moomin quests

Capeless/Wingless gameplay is not currently supported

### Traps
Heart Trap: `(on by default)`
- send a heart to a friend

Unskippable Cutscene: `(on by default)`
- make sure 'skip all skippable cutscenes' is off
- sit through the next cutscene

Watch the Incense Burn: `(on by default)`
- visit the Tranquil Garden in Aviary Village
- walk through the arch and sit at the incense
- wait for it to burn out

### Winning
The win condition is to be reborn<br />
To enter the Gate of Eden, you will need to obtain at least 30 "Winged Light" items<br />
Winged Light items have no other affect on the game, and you are free to use more than what you received in the Eye of Eden

### How does Death Link work?
Death Link is an option you can enable in your YAML `(off by default)`<br />
When enabled, if you or anyone else with Death Link enabled dies in their game, 
every other player with Death Link will also die

You can send a Death Link when:
- your Sky Kid starts to lose Winged Light, turn dark, or grow crystals 
(except when giving away Winged Light in the Eye of Eden)
- you use more wedges than you've received 
(or are caused to go below that number by rain, Dark Dragons, etc.)
- you die in one of the Trials
- you die in the Eye of Eden

When you receive a Death Link from another player:
- go lose some Winged Light (how many is up to you) or face the Dark Dragon
- you can enter an area or realm you don't yet have unlocked to do so
- do not send a Death Link when you lose Winged Light for this reason

The Death Link button is located in the top right corner of the Manual Client<br />
When not in use, this button will be grey with the text "Death Link: Primed"

When you receive a Death Link, this button will turn red and display "Death Link:" followed by the slot name of the player who died<br />
You will also see a Death Link message in the Archipelago tab<br />
Once you have finished what you need to with Death Link, you can click the button to reset it to "Death Link: Primed"

To send a Death Link, make sure the button says "Death Link: Primed", and click it<br />
It will turn green and say "Death Link: Sent"<br />
You will also see a Death Link message in the Archipelago tab<br />
Click the button again to reset it to "Death Link: Primed"

### Using the Universal Tracker
Universal Tracker shows you which checks are in logic<br />
(that is, which checks Archipelago expects you to be able to get)

To use it, you will need to download and install [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases/latest) 
the same way you did with the apworld for this game<br />
Place the same YAML file that you sent to your host in your Archipelago/Players/ folder<br />
If you have other YAMLs in your Players folder, they may cause Universal Tracker to crash<br />
Restart the Archipelago Launcher<br />
Open the Manual Client<br />
You will now see a "Tracker Page" tab<br />
Once you are connected to your slot, you will see a list of in-logic locations in the Tracker Page tab, 
and they will be highlighted green in the Manual tab

## Updating the APWorld
To update, follow the same steps as when you first installed the apworld:
- Download and install "manual_skycotl_raycast.apworld" from the [latest release](https://github.com/Vykolue/Sky-Cotl-Archipelago/releases/latest)
- Do NOT rename this file, as it may cause errors

Make sure that all Sky: CotL players and the host are using the same version of the apworld<br />
It is a good idea to update your YAML at the same time you update the apworld, 
as options may change between versions

## AI Usage Disclosure
If I am searching for how to do something specific and I come across an AI generated response that accomplishes my goal, I will ocassionally use it or adapt it<br />
That is the only situation where I may use AI in this apworld
