import rules
from django.apps import apps


@rules.predicate
def is_post_author(user, post):
    return user == post.author


@rules.predicate
def is_public_room(post):
    Room = apps.get_model(app_label='house', model_name='Room')
    return post.room.privacy == Room.RoomPrivacyOptions.PUBLIC


@rules.predicate
def is_family_guest_privacy_match(user, post):
    Room = apps.get_model(app_label='house', model_name='Room')
    return post.room.house.family_guests.filter(user=user).exists() \
        and post.room.privacy == Room.RoomPrivacyOptions.FAMILY_GUESTS


@rules.predicate
def is_family_privacy_match(user, post):
    Room = apps.get_model(app_label='house', model_name='Room')
    return post.room.house.family.filter(user=user).exists() \
        and (post.room.privacy == Room.RoomPrivacyOptions.FAMILY_GUESTS
             or post.room.privacy == Room.RoomPrivacyOptions.FAMILY)


@rules.predicate
def is_house_family_member_match(user, post):
    return post.room.house.family.filter(user=user).exists()


can_add_post = rules.is_staff \
               | is_house_family_member_match

can_edit_post = rules.is_staff \
                | is_post_author

can_delete_post = rules.is_staff \
                  | is_post_author

can_view_post = rules.is_staff \
                | is_post_author \
                | is_public_room \
                | is_family_guest_privacy_match \
                | is_family_privacy_match
