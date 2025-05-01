
def accommodate(*guest_groups,**available_rooms):
    accommodations = {}
    unaccommodated_guests = 0


    rooms = sorted(available_rooms.items(), key=lambda r: (r[1], r[0]))

    for guests in guest_groups:
        is_accommodated = False

        for room_key, capacity in rooms:
            if capacity >= guests:
                room_number = room_key.split('_')[1]
                if room_number not in accommodations:
                    accommodations[room_number] = guests

                    rooms.remove((room_key, capacity))
                    is_accommodated = True
                    break
        if not is_accommodated:
            unaccommodated_guests += guests

    if accommodations:
        result = [f"A total of {len(accommodations)} accommodations were completed!"]
        for room_number in sorted(accommodations.keys()):
            result.append(f"<Room {room_number} accommodates {accommodations[room_number]} guests>")
    else:
        result = ["No accommodations were completed!"]

    if unaccommodated_guests > 0:
        result.append(f"Guests with no accommodation: {unaccommodated_guests}")

    if rooms:
        result.append(f"Empty rooms: {len(rooms)}")

    return "\n".join(result).strip()


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))