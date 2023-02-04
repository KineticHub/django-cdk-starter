import rules


@rules.predicate
def is_house_family_member(user, room):
    return room.house.family.filter(user=user).exists()


@rules.predicate
def is_family_house_guest_member(user, room):
    return room.house.family_guests.filter(user=user).exists()


@rules.predicate
def is_family_guest_room_member(user, room):
    return room.house.family_guests.filter(user=user).exists() \
        and room.privacy == room.RoomPrivacyOptions.FAMILY_GUESTS


@rules.predicate
def is_public_room(room):
    return room.privacy == room.RoomPrivacyOptions.PUBLIC


# ======================================
# House Rules
# ======================================
can_add_house = rules.is_authenticated

can_edit_house = rules.is_staff \
                 | is_house_family_member

can_delete_house = rules.is_staff

can_view_house = rules.is_staff \
                 | is_house_family_member \
                 | is_family_house_guest_member

# ======================================
# Room Rules
# ======================================
can_add_room = rules.is_staff \
               | is_house_family_member

can_edit_room = rules.is_staff \
               | is_house_family_member

can_delete_room = rules.is_staff \
               | is_house_family_member

can_view_room = rules.is_staff \
                | is_public_room \
                | is_house_family_member \
                | is_family_guest_room_member
