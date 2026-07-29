# 1.21.10.1.0
## #1 Publishing the Pack!

After months of development, the time has finally come to publish my biggest data pack/ mod so far! I am excited to announce to you:

### "Pocket Dimensions" version 1.21.10 **. 1.0**

You can now take your base with you in your pocket! Read the main page to find out more! :D

# 1.21.10.1.1
## #2 Fixed Bugs

- Vital structures will now be rebuilt every time you enter the pocket, ensuring that the core functionality works.
- To ensure working triggers, trigger advancements will be revoked on reload.

## #3 Updated to 1.21.11

- Updated pack.mcmeta
- No further changes to the datapack
- Updated models to use an item atlas

# 1.21.11.1.3
## #4 Fixed Bug

- When leaving the Pocket Dimension, you could take it with you because there is no one inside, and then rejoin. This was an exploit which has now been fixed.
- When leaving the Pocket Dimension, you will now rejoin at the location you entered.

## #5 Added Entity handling!

- You can now bring your animals into the Pocket Dimension! This means you can carry them over long distances. But be careful — they can also enter the portal and leave with you!
- Please note that this is only possible with friendly mobs that have a small enough hitbox.
- To bring them into the Pocket Dimension, simply put them on a lead.

# 1.21.11.2.0
## #6 Froze older Versions

The pack will still be compatible down to 1.21.9 but **all Minecraft versions up to 1.21.10** will be frozen at **Pack version 1.21.11.1.3**. Major bugs will still be solved in some cases.

## #7 Fixed Bugs

* Beds shouldn't have been working but they did. This has been removed
* Fixed brightness issue with shaders
* Fixed broken pack formats

## #8 Added Version Migration Function

The pack can now better adjust to new versions

## #9 Automatic Pocket leaving

Players now automatically exit pockets upon joining the game. This fix addresses an exploit that allowed players to travel vast distances by logging out inside a pocket and reconnecting after another player had moved. You will now consistently rejoin where you entered before.

# 1.21.11.3.0
## #10 More Languages coming

Translation support has been added. You can now translate the pack! Help me translate it into as many languages as possible! Currently, only English is available, but more will follow.

## #11 Proper Mod packages

Proper mod support has been added. Packaged mods now have a registered item ID for the item. This allows mods like JEI to recognise it properly. It can also now be found in the Creative inventory.

# 3.1 (26.1)
## #12 Migraded to Version 26.1.1

Made minor changes to the dimension type to add compatability with the new version. Changed version numbers to include the newer version.

## #13 Reworked Mod packages (only fabric)

In the last update, I added proper mod packages for Minecraft version 1.21.11. For the new version, however, I had to redo the whole thing for several reasons. The consequence of this is that it no longer relies on the architecture API, but is now fully independent. However, this also forced me to choose an ecosystem, as I had to code everything separately for Fabric and Neoforge.

As there is more demand for the Fabric version, I will discontinue the NeoForge packaging and only create standard packaging similar to past versions. I apologise for this. However, if demand persists, please contact me on GitHub and I will consider it.

# 3.2 (26.2)
## #14 Migraded to Version 26.2

Changed version numbers to include the newer version. Rebuild fabric mod to support the newest Version.

## #15 Added Pocket Locator Compass

There's now a new item to help you locate your placed pocket! Once obtained, simply right-click to bind it to your placed pocket. You can rebind it at any time. You can craft it using this recipe:

![Pocket Locator Compass Recipe](https://cdn.modrinth.com/data/cached_images/eae5ed647bf6b2922a2d01b0eb887dfdf801b058.png)

## #16 Added Error Codes

Error codes will now be displayed when bugs occur to help you solve them by following the instructions in the [Documentation](https://github.com/MavLeague/pocket_dimension/blob/main/SUPPORT.md).

## #17 Added helper function

There's now a new function called ```pocket_dimension:force_pocket_chunkload``` which can help you solve bugs described in the [Documentation](https://github.com/MavLeague/pocket_dimension/blob/main/SUPPORT.md).
