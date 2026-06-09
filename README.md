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
Use "Generate" to create your world<br />
The generated world will show up in your Archipelago/output/

Hosting on the Archipelago website:
1. Run the world on the archipelago website by uploading it to https://archipelago.gg/uploads
2. After hosting the world, save the link you are redirected to for future reference
3. The port will be listed on that page, but it may change
4. If your players have trouble connecting, refresh the page to ensure the server is running


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
1. Download "Sky_Children_of_the_Light.yaml" from the [latest release](https://github.com/Vykolue/Sky-Cotl-Archipelago/releases/latest)
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

### Playing the game
You can play Sky: Children of the Light on any device

To send a check:
1. Connect to the Manual Client (as described above)
2. Switch to the "Manual" tab
3. Find the check you got under "Remaining Locations"
4. Click it to send it

You can see checks you send and receive in real time under the "Archipelago" tab<br />
Items you receive will also show up under "Items Received" in the "Manual" tab<br />
You can see hints in the "Hints" tab

Tips:
- You can use "!hint {item_name}" in the command line to find out where the specified item is
- You will need points to afford a hint, which can be earned by sending checks
- Use "/items" to see the names of all items

The area a Child of Light is in corresponds to where it appears when looking at your map

Note: these areas may not match the Sky: Children of the Light wiki exactly
If you lose all Winged Light before playing (or are reborn and don't collect any new Winged Light), 
you will be able to use your map to track how many Children of Light you have found in each area

#### Why are there two checks for each Child of Light and Wedge?
The "Find Children of Light" locations are for sending items to other players
whereas the "Collect Winged Light" locations are for Archipelago to keep track of 
how much Winged Light your Sky Kid actually has, so you won't be expected to reach somewhere unreachable

Likewise, the "Wedge Capacity" items are purely there to ensure accessibility, 
while "Wedge" items determine how many wedges you are allowed to use

I hope to eventually get rid of the duplicates

#### How does Death Link work?
Death Link is an option you can enable in your YAML `(off by default)`<br />
When enabled, if you or anyone else with Death Link enabled dies in their game, 
every other player with Death Link will also die

You can send a Death Link when:
- your Sky Kid starts to lose Winged Light, turn dark, or grow crystals 
(except when giving away Winged Light in the Eye of Eden)
- you use more wedges than you've received 
(or are caused to go below that number by rain, Dark Dragons, etc.)
- you die in the Eye of Eden

When you receive a Death Link from another player:
- go lose some Winged Light (how many is up to you)
- do not send a Death Link when you lose Winged Light for this reason

### Rules (follow them or don't idc)
Don't send checks you didn't earn

Don't use items that haven't been unlocked<br />
Your locked items will depend on your YAML settings, but may include:
- realms `(always on)`
- wedges `(always on)`
- passing through spirit gates `(on by default)`
- cosmetics `(off by default)`
- props `(on by default)`
- base emotes `(on by default)`
- friendship emotes `(on by default)`
- other seasonal emotes `(off by default)`

If emote locks are on, you should have the required emote before entering that area, 
even if other players opened the door<br />
Likewise, you shouldn't have a friend drag you through a locked Spirit Gate

I recommend against using props, shared spaces, white candle, piggy rocket, etc. 
to easily get somewhere that is possible to reach otherwise, or to get somewhere out of logic<br />
This is why I have enabled Prop and Friendship Emote Locks by default<br />
If you receive the item, feel free to use it in this way, though

"Find Children of Light" means you can either collect it, or stand on where it normally is<br />
"Collect Winged Light" is when you collect it, and is used by Archipelago to ensure accessibility

"Wedge Capacity" is how many wedges your Sky Kid has, while "Wedges" are how many wedges you are allowed to use<br />
Claim a "Wing Level" item when you level up your wing

Feel free to lose all your Winged Light before playing<br />
If you start with extra, you won't be able to use it until someone unlocks your wedges for you

You may run into impossible scenerios if your account has not:
- relived enough Base Spirit Memories to unlock all Spirit Gates and use emotes required to enter certain areas
- unlocked shortcuts for The Wind Paths and The Treehouse
- progressed through the first three Cave of Prophecy quests
- completed the 5th Nine-Colored Deer Quest
- progressed through the Vault of Knowledge

#### Traps
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
All areas of the Eye of Eden as well as three "Eye of Eden Progress" must first be unlocked

The "Gate of Eden" (first area) is in a random location in the multiworld<br />
The other areas and Eye of Eden Progress are in the following locations by default:
- Cave of Prophecies Find 1 WL
- Prairie Peaks Find 2 WL
- Forest Cavern Find 2 WL
- Hermit Valley Find 2 WL
- The Graveyard Find 5 WL
- Starlight Desert Find 3 WL

If you wish to change the default locations, you can use [Plando](https://archipelago.gg/tutorial/Archipelago/plando_en)<br />
The items to place are:
- Eye of Eden Progress: 3
- Gate of Eden Key `(if you prefer it not be random)`
- Path of Eden Key
- Eye of Eden Key
- The Passage Key
