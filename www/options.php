<?php
$gfx_options = ['' => 'Default'];
$gfx_info = ['' => ''];
foreach(scandir("LADXR/gfx") as $gfx)
{
    if (substr($gfx, -4) == ".bin")
    {
        $gfx_options[$gfx] = substr($gfx, 0, -4);
        $gfx_info[$gfx] = "by " . trim(file_get_contents("LADXR/gfx/".$gfx.".txt"));
    }
}
$options = [
    'seed' => ['label' => 'Seed', 'type' => 'text', 'placeholder' => 'Leave empty for random seed', 'arg' => '--seed', 'multiworld' => False],
    'heartpiece' => ['label' => 'Randomize heart pieces', 'type' => 'check', 'default' => 'true', 'arg' => '--heartpiece', 'tooltip' => 'Includes heart pieces in the item pool'],
    'seashells' => ['label' => 'Randomize hidden seashells', 'type' => 'check', 'default' => 'true', 'arg' => '--seashells', 'tooltip' => 'Randomizes the secret sea shells hiding in the ground/trees. (chest are always randomized)'],
    'keysanity' => ['label' => 'Keysanity', 'type' => 'check', 'default' => '', 'arg' => '--keysanity', 'tooltip' => 'Dungeon keys, maps and compasses can be found anywhere'],
    'heartcontainers' => ['label' => 'Randomize heart containers', 'type' => 'check', 'default' => '', 'arg' => '--heartcontainers', 'tooltip' => 'Includes boss heart container drops in the item pool'],
    'instruments' => ['label' => 'Randomize instruments', 'type' => 'check', 'default' => '', 'arg' => '--instruments', 'tooltip' => 'Instruments are placed on random locations, dungeon goal will just contain a random item.'],
    'witch' => ['label' => 'Randomize item given by the witch', 'type' => 'check', 'default' => 'true', 'arg' => '--witch', 'tooltip' => 'Adds both the toadstool and the reward for giving the toadstool to the witch to the item pool'],
    'owlstatues' => ['label' => 'Add items on owl statues', 'type' => ['' => 'Never', 'dungeon' => 'In dungeons', 'overworld' => 'On the overworld', 'both' => 'Dungeons and Overworld'], 'arg' => '--owlstatues', 'tooltip' => 'Replaces the hints from owl statues with additional randomized items'],
    'randomstart' => ['label' => 'Random start location', 'type' => 'check', 'default' => '', 'arg' => '--randomstartlocation', 'tooltip' => 'Randomize where your starting house is located'],
    'dungeonshuffle' => ['label' => 'Dungeon shuffle', 'type' => 'check', 'default' => '', 'arg' => '--dungeonshuffle', 'tooltip' => 'Randomizes the dungeon that each dungeon entrance leads to'],
    'boss' => ['label' => 'Boss shuffle', 'type' => ['default' => 'Normal', 'shuffle' => 'Shuffle', 'random' => 'Randomize'], 'arg' => '--boss', 'tooltip' => 'Randomizes the dungeon bosses that each dungeon has'],
    'boomerang' => ['label' => 'Boomerang trade', 'type' => ['default' => 'Normal (require magnifier for boomerang)', 'trade' => 'Trade: Trade is always available, boomerang is shuffled in pool', 'gift' => 'Gift: Boomerang trade guy gives you a gift, boomerang itself is shuffled in the item pool'], 'arg' => '--boomerang'],
    'bowwow' => ['label' => 'Good boy mode', 'type' => ['normal' => 'Disabled', 'always' => 'Enabled', 'swordless' => 'Enabled (swordless)'], 'arg' => '--bowwow', 'tooltip' => 'Allows BowWow to be taken into any area, damage bosses and more enemies'],
    'logic' => ['label' => 'Logic', 'type' => ['' => 'Normal', 'hard' => 'Hard', 'glitched' => 'Glitched'], 'arg' => '--logic', 'tooltip' => 'Affects where items are allowed to be placed.  See the main site linked above for details.'],
    'goal' => ['label' => 'Goal of the game', 'type' => ['8' => '8 instruments', '7' => '7 instruments', '6' => '6 instruments', '5' => '5 instruments', '4' => '4 instruments', '3' => '3 instruments', '2' => '2 instruments', '1' => '1 instrument', '0' => 'No instruments (only Marins song)', '-1' => 'Egg already open', 'random' => 'Random instrument count', 'seashells' => 'Seashell hunt (20)'], 'arg' => '--goal'],
    'accessibility' => ['label' => 'Accessibility', 'type' => ['all' => 'All locations reachable', 'goal' => 'Wake the windfish'], 'arg' => '--accessibility'],
    'overworld' => ['label' => 'Overworld', 'type' => ['normal' => 'Normal', 'dungeondive' => 'Dungeon dive'], 'arg' => '--overworld', 'tooltip' => 'Switching to dungeon dive will create a different overworld where all the dungeons are directly accessible and almost no chests are located in the overworld.'],
    'pool' => ['label' => 'Item pool', 'type' => ['' => 'Normal', 'casual' => 'Casual', 'pain' => 'Path of Pain', 'keyup' => 'More keys'], 'arg' => '--pool', 'tooltip' => 'Effects which items are shuffled. Casual mode puts in more key items so the seed is easier. More keys adds more small keys and extra nightmare keys so dungeons are easier. Path of pain... just find out yourself.'],
    'hpmode' => ['label' => 'Health mode', 'type' => ['default' => 'Normal', 'inverted' => 'Inverted, defeating bosses reduces hearts', '1' => 'Start with 1 heart'], 'arg' => '--hpmode'],
    'hardmode' => ['label' => 'Enable oracle mode:', 'type' => 'check', 'default' => false, 'arg' => '--hard-mode', 'tooltip' => 'Less iframes and heath from drops. Also bombs damage yourself.'],
    'steal' => ['label' => 'Stealing from the shop', 'type' => ['always' => 'Always', 'never' => 'Never', 'default' => 'Normal'], 'arg' => '--steal'],
    'quickswap' => ['label' => 'Quickswap with SELECT key', 'type' => ['none' => 'Disabled', 'a' => 'Swap A button', 'b' => 'Swap B button'], 'arg' => '--quickswap', 'tooltip' => 'Adds a hidden item slot that select swaps with either A or B - think a Tetris hold piece.  The map is not available when quickswap is enabled.', 'aesthetic' => True],
    'textmode' => ['label' => 'Text mode', 'type' => ['fast' => 'Fast', 'default' => 'Normal', 'none' => 'No-text'], 'arg' => '--textmode', 'tooltip' => 'Fast makes text appear twice as fast, none removes all text from the game', 'aesthetic' => True],
    'lowhpbeep' => ['label' => 'Low HP beeps', 'type' => ['slow' => 'Slow', 'default' => 'Normal', 'none' => 'Disabled'], 'arg' => '--lowhpbeep', 'tooltip' => 'Slows or disables the low health beeping sound', 'aesthetic' => True],
    'nag-messages' => ['label' => 'Show nag messages', 'type' => 'check', 'default' => false, 'arg' => '--nag-messages', 'tooltip' => 'Enables the nag messages normally shown when touching stones and crystals', 'aesthetic' => True],
    'gfxmod' => ['label' => 'Graphics', 'type' => $gfx_options, 'arg' => '--gfxmod', 'tooltip' => 'Generally affects at least Link\'s sprite, but can alter any graphics in the game', 'aesthetic' => True],
    'linkspalette' => ['label' => "Link's color", 'type' => ['' => 'Normal (depending on tunic)', '0' => 'Green', '1' => 'Yellow', '2' => 'Red', '3' => 'Blue', '4' => '?? A', '5' => '?? B', '6' => '?? C', '7' => '?? D'], 'arg' => '--linkspalette', 'aesthetic' => True],
    'race' => ['label' => 'Race mode', 'type' => 'check', 'default' => false, 'arg' => '--race', 'tooltip' => 'Spoiler logs can not be generated for ROMs generated with race mode enabled', 'multiworld' => False],
    'spoilerformat' => ['label' => 'Spoiler Format', 'type' => ['none' => 'None', 'text' => 'Text', 'json' => 'JSON'], 'arg' => '--spoilerformat', 'multiworld' => False],
];
?>
