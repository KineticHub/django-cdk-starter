from justforfam.house.models import Room, House


class RoomDefinitions:

    @staticmethod
    def get_room_type_definition(room_type: Room.RoomTypeOptions):
        if room_type == Room.RoomTypeOptions.LIVING_ROOM:
            return RoomDefinitions.__living_room()
        if room_type == Room.RoomTypeOptions.FAMILY_DEN:
            return RoomDefinitions.__family_den()
        if room_type == Room.RoomTypeOptions.BEDROOM:
            return RoomDefinitions.__bedroom()

    @staticmethod
    def __living_room():
        return {
            'name': 'Living Room',
            'description': 'Posts in this room are viewable by family members and neighbours.',
            'privacy': Room.RoomPrivacyOptions.FAMILY_GUESTS,
            'type': Room.RoomTypeOptions.LIVING_ROOM
        }

    @staticmethod
    def __family_den():
        return {
            'name': 'Family Den',
            'description': 'Posts in this room are viewable by family members.',
            'privacy': Room.RoomPrivacyOptions.FAMILY,
            'type': Room.RoomTypeOptions.FAMILY_DEN
        }

    @staticmethod
    def __bedroom():
        return {
            'name': 'Bedroom',
            'description': 'Posts in this room are viewable only by you.',
            'privacy': Room.RoomPrivacyOptions.PRIVATE,
            'type': Room.RoomTypeOptions.BEDROOM
        }
