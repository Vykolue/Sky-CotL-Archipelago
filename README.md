# Sky-CotL-Archipelago
A Manual Archipelago for Sky: Children of the Light

This archipelago is a [manual](https://github.com/ManualForArchipelago/Manual), meaning there is no mod and you will need to manually input all checks you get.<br />
You will also be responsible for not using items you don't have unlocked

This is mainly a setup guide. More info on how to play can be found [here](https://github.com/Vykolue/Sky-Cotl-Archipelago/gameplay.md)

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
You can play Sky: Children of the Light on any device

To send a check:
1. Connect to the Manual Client (as described above)
2. Switch to the "Manual" tab
3. Find the check you got under "Remaining Locations"
4. Click it to send it

You can see checks you send and receive in real time under the "Archipelago" tab<br />
Items you receive will also show up under "Items Received" in the "Manual" tab<br />
You can see hints in the "Hints" tab

More information on the gameplay can be found [here](https://github.com/Vykolue/Sky-Cotl-Archipelago/gameplay.md)

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
That is the only situation I know of where I may use AI in this apworld
