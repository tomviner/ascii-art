characters = [" ", ".", "-", "&", "#", "*"]

def map_brightness_to_char(brightness):
    n_slots = len(characters)
    slot_width = 1.0/n_slots
    if brightness == 1.0:
        slot = n_slots - 1
    else:
        slot = int(brightness/slot_width)
    return characters[slot]
