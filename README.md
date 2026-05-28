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
1. Download "Sky Children of the Light.yaml" from the [latest release](https://github.com/Vykolue/Sky-Cotl-Archipelago/releases/latest)
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
Connect to the server that your game is running on
- Type the server name and port next to "Server:"
- If you don't know it, ask your host<br />
Enter your name (and password, if prompted) in the command line

#### If you can't connect
Make sure:
- the game is actively being hosted and the server isn't down
- you are using the correct port
- the name you are using to connect matches your slot name (case sensitive)

### Playing the game
You can play Sky: Children of the Light on any device

To send a check:
1. Connect to the Manual Client
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

### Rules (follow them or don't idc)
Don't send checks you didn't earn

Don't use items that haven't been unlocked<br />
Your locked items will depend on your YAML settings, but may include:
- areas of the game `(always on)`
- passing through spirit gates `(on by default)`
- cosmetics `(off by default)`
- base emotes `(on by default)`
- seasonal emotes `(off by default)`

If emote locks are on, you should have the required emote before entering that area, 
even if other players opened the door<br />
Likewise, you shouldn't have a friend drag you through a locked Spirit Gate

"Find WL" means you can either collect it, or stand on where it normally is

You can lose all your Winged Light before playing,
but I can't guarantee that the game will give you access to 
enough WL for the checks it expects you to get

Additionally, you may run into impossible scenerios if your account has not:
- relived enough Base Spirit Memories to unlock all Spirit Gates and use emotes required to enter certain areas
- unlocked shortcuts for The Wind Paths, The Treehouse, Harmony Hall, and Hall of Stories
- progressed through the first three Cave of Prophecy quests
- progressed through the Vault of Knowledge

If you receive a heart trap, send a heart to a friend `(on by default)`

### Winning
The win condition is to be reborn<br />
All areas of the Eye of Eden as well as three "Eye of Eden Progress" must first be unlocked

The "Path of Eden" (first area) is in a random location in the multiworld<br />
The other areas and Eye of Eden Progress are in the following locations by default:
- Cave of Prophecies Find 1 WL
- Prairie Peaks Find 2 WL
- Forest Cavern Find 2 WL
- Hermit Valley Find 2 WL
- The Graveyard Find 5 WL
- Starlight Desert Find 3 WL

The area a Winged Light is in corresponds to where it appears when looking at your map
except Cave of Prophecies Winged Light, which are all grouped in your checks<br />
(you will still need the corresponding trial key to get to it)

Note: these areas may not match the Sky: Children of the Light wiki exactly<br />
I also use the term Winged Light (WL) to refer to what are technically Children of Light
