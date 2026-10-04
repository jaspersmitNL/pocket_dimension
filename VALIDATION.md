# 26.3 update validation

## Completed

- Confirmed the official Java 26.3 pack formats: data 121.0 and resource 97.1.
- Parsed JSON and metadata files in the current pack and overlays.
- Built separate data and resource ZIP archives and checked their integrity.
- Checked pack function references for missing functions.
- Loaded the rebuilt packs in the Minecraft Java 26.3 PrismLauncher client. The integrated server loaded `pocket_dimension:realm`, loaded 1,869 advancements, and completed `/reload` without registry errors. The pack displayed version 26.3.3.3 and confirmed resource-pack loading.

## Still to test

- Visually inspect the pocket items and displays in the client.
- Test crafting, room creation, placement, entry/exit, leashed mobs, break/refund, compass binding, and reconnect behavior with players.
- Test a copy of a populated 26.2 world to confirm saved rooms survive.
- Test older advertised versions with their overlays if backward compatibility remains a release requirement.

The pack loads in a 26.3 client. Gameplay and older-version compatibility checks remain open.
