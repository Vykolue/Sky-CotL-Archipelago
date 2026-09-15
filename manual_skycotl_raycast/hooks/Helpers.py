from typing import Optional, Any
from BaseClasses import MultiWorld


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from ..Items import item_name_groups
    if category_name in item_name_groups["Sheet Music"]:
        # This category is the name of a music sheet
        from ..Helpers import get_option_value
        enabled_music_sheets = get_option_value(multiworld, player, "enabled_music_sheets")
        return category_name in enabled_music_sheets
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    # Remove unwanted music sheets from the item pool
    if "Sheet Music" in item["category"]:
        from ..Helpers import get_option_value
        enabled_music_sheets = get_option_value(multiworld, player, "enabled_music_sheets")
        enabled_sheet_music_sanity = get_option_value(multiworld, player, "sheet_music_sanity")
        return item["name"] in enabled_music_sheets and enabled_sheet_music_sanity  # True if they're in the yaml and sheet music mode is on, false if not
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
