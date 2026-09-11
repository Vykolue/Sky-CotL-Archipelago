# Gameplay
You can play Sky: Children of the Light on any device<br />
This guide is intended to expain the gameplay for version 0.3.0 of the apworld, and may not apply to other versions

Be aware that hard mode includes some incredibly difficult and/or unintuitive skips in the logic

See the [Setup Guide](https://github.com/Vykolue/Sky-CotL-Archipelago/blob/main/README.md) for more information on how to set up the game and prerequisites

## Rules
Don't send checks you didn't earn

Don't use items that haven't been unlocked<br />
See below for a list of locked items

You shouldn't have a friend drag you through a locked Spirit Gate

"Find Children of Light" means that you must be close enough to collect it, but you aren't required to actually collect it<br />
(if you already have it, or prefer not to)

You can lose all your Winged Light before playing<br />
If you start with extra, you won't be allowed to use it until someone unlocks your wedges for you

You can specify in your YAML how many Winged Light you start with, but only count those not included as locations in the game (Orbit, Wing Buffs, Eden, and Shard Memories)<br />
If you start with Winged Light that are meant to be collected as part of the game, the logic will not be able to properly account for them<br />
Your starting Winged Light will show up as "Actual Winged Light" in your starting items, and can be ignored<br />
If you don't know how many you have, it is best to undershoot or default to 1<br />
If you undershoot, locations may be considered out-of-logic when they are actually accessible<br />
If you overshoot, locations may be considered in-logic when they are inaccessible

## Which items are locked?
Always locked without having received the item:
- realms
- the Wandering Carnival area
- wedges
- shortcuts
- the Cave of Prophecies Updrafts

Locked based on YAML settings without having received the item:
- passing through spirit gates `(on by default)`
- cosmetics `(off by default)`
- base emotes `(on by default)`
- seasonal emotes `(off by default)`

Forbidden if used to gain a significant advantage:
- piggy rocket
- chibi fall
- white candle
- tents
- teleport
- warp
- follow or grab hand
- dark dragon repellent or elder masks
- props
- shared spaces/memories/challenges
- friend recharge
- other unintended items, spells, or glitches

Always available to use:
- red candle
- deep call
- starting emotes and cosmetics
- clouds
- creatures of light (recharge or riding)
- light blooms
- other environmental recharge
- boats
- map
- toggle flight mode
- forge candles and dye
- jump
- meditation circles
- dive
- grab/open
- canons
- light falls
- dyed outfits

I intend to add logic for some of these in a future update<br />
If you use any forbidden items or have hard mode off, 
you may to be able to get some things out-of-logic

## How does ___ item/lock work?
Shortcut locks will lock the following areas' shortcuts from being used without the shortcut item:
- The Wind Paths `(locks everything except the Forest Rest connection)`
- The Treehouse `(locks everything except the Forest Rest connection)`
- Harmony Hall `(locks everything except the Village of Dreams connection)`
- Story Space `(locks only the Aviary connection)`

The Cave of Prophecies Updrafts refers to the updraft just outside the Trial of Air<br />
Without the updraft item, more wedges will be required to reach this trial in logic

Cosmetic locks can be done one of two ways:

Method 1 (recommended):
- cosmetics are unlocked along with the spirit you get them from
- turn on cosmetic locks to lock cosmetics not obtained from a regular or seasonal spirit
- using cosmetic locks, all remaining cosmetic items (besides props) will be received by category
- some categories may be left out of the game since they are considered filler items

Method 2:
- use this method if you'd rather not keep track of which spirits provide which cosmetics
- turn on cosmetic locks
- all cosmetics (besides props) are unlocked by category
- some categories may be left out of the game since they are considered filler items

If emote locks are on, you should have the corresponding emote before entering areas that require it, 
even if other players opened the door

"Wedges" are how many wedges you are allowed to use<br />
You are free to use a partial wedge, even if it causes you to use part of a wedge you don't have unlocked

## Traps
Heart Trap: `(on by default)`
- send a heart to a friend

Unskippable Cutscene: `(on by default)`
- make sure 'skip all skippable cutscenes' is off
- sit through the next cutscene

Watch the Incense Burn: `(on by default)`
- visit the Tranquil Garden in Aviary Village
- walk through the arch and sit at the incense
- wait for it to burn out

Home Trap: `(on by default)`
- go home
- do not use the return shrine to get back to where you were

Forgot How to Jump: `(on by default)`
- do not use the jump or fly button for the next 3 minutes

Move Using Emotes: `(on by default)`
- you cannot walk normally or fly for the next 3 minutes
- the movement options you have are emotes that change the way you move (i.e. skipping, tiptoeing, somersault, moping, cartwheel, flight run, slow walk)
- you can used emotes you haven't received for this

## Winning
The win condition is to be reborn<br />
To enter the Gate of Eden, you will need to obtain at least 20 "Winged Light" items<br />
Winged Light items have no other affect on the game, and you are free to use more than what you received in the Eye of Eden

## How does Death Link work?
Death Link is an option you can enable in your YAML `(off by default)`<br />
When enabled, if you or anyone else with Death Link enabled dies in their game, 
every other player with Death Link will also die

You do not have to send a Death Link for every scenerio I listed. 
Do whatever makes the most sense to you

You can send a Death Link when:
- your Sky Kid starts to lose Winged Light, turn dark, or grow crystals 
(except when giving away Winged Light in the Eye of Eden)
- you use more wedges than you've received 
(or are caused to go below that number by rain, Dark Dragons, etc.)
- you die in one of the Trials
- you die in the Eye of Eden

When you receive a Death Link from another player:
- go face the Dark Dragon, or if you prefer, lose some Winged Light (how many is up to you)
- you can enter an area or realm you don't yet have unlocked to do so
- you can use locked or forbidden items (e.g. extra wedges, teleport, warp) to get there faster
- do not send a Death Link if you lose Winged Light for this reason
- if you are in one of the trials, do that trial's equivalent of a death instead

The Death Link button is located in the top right corner of the Manual Client<br />
When not in use, this button will be grey with the text "Death Link: Primed"

When you receive a Death Link, this button will turn red and display "Death Link:" followed by the slot name of the player who died<br />
You will also see a Death Link message in the Archipelago tab<br />
Once you have finished what you need to with Death Link, you can click the button to reset it to "Death Link: Primed"

To send a Death Link, make sure the button says "Death Link: Primed", and click it<br />
It will turn green and say "Death Link: Sent"<br />
You will also see a Death Link message in the Archipelago tab<br />
Click the button again to reset it to "Death Link: Primed"