# Plan: update Pocket Dimensions for Minecraft Java 26.3

The official Java release is named **26.3**. This plan treats the requested “1.26.3” as 26.3. Mojang lists data pack format **121.0** and resource pack format **97.1** for that release. The repository initially advertised a maximum data format of 107 and resource format of 88. [26.3 release notes](https://feedback.minecraft.net/hc/en-us/articles/48913133328013-Minecraft-Java-Edition-26-3)

## 1. Establish a safe baseline

- Make a copy of a 26.2 test world containing an unplaced pocket, a placed pocket with blocks inside, a bound compass, and two players with different room IDs. Record current behavior and the server log on 26.2 before upgrading the copy.
- Verify the root pack and matching resource pack load in 26.2. Keep the `1_21_10/` overlay and existing saved room data intact.
- List uses of `/item`, `/execute if items`, loot functions, advancements, dimension type fields, item components, model JSON, and pack metadata. Use release notes as the migration checklist.

## 2. Update pack metadata and packaging

- Update data pack metadata for 121.0 and resource pack metadata for 97.1, using exact minor versions where needed.
- Preserve legacy metadata required for older format ranges. Keep overlay metadata valid across all supported formats and check it in both 26.3 and 1.21.10.
- Keep older schema definitions in an overlay if the 26.3 root files no longer work on older versions. Package data and resource packs separately, each with `pack.mcmeta` at the archive root.

## 3. Adapt commands and data

- Check every `/item modify` and `/item replace` command against 26.3 slot-source syntax and replacement behavior.
- Inspect loot tables, recipes, advancements, predicates, dimension definitions, and the rift structure for schema changes. Change only formats that 26.3 rejects or behaves differently on.
- Confirm pocket entry and exit, respawn rules, and recovery rift behavior without regenerating or moving saved rooms.
- Load the resource pack and inspect held items, room displays, animation, compass tooltip, and translations.

## 4. Fix inspection findings

- Make `place_pocket.mcfunction` verify an anchor matching the item's `pocket_id`, rather than `%step_id`. Test valid older IDs and orphaned items.
- Make reconnect recovery look up the player's exit by UUID rather than relying on shared `enter_success` state. Use a safe world-spawn fallback if no exit record exists.

## 5. Test and preserve world migration

- Start a clean 26.3 test world. Confirm `/reload` reports no invalid files or unknown commands, recipes craft, and models/text appear.
- Test room creation, placement, entry, leashed mobs, exit, breaking/refund, compass binding, and multiple players in survival and creative.
- Upgrade a copy of a populated world and verify room contents, IDs, anchors, display placements, exit records, and compass bindings survive.
- Test older advertised versions with their overlays, or make the compatibility range explicit before release.

## 6. Release criteria and documentation

- Release after 26.3, populated-world migration, and any advertised older versions pass.
- Update README, support notes, changelog, install instructions, and the version stored in `update.mcfunction`.
