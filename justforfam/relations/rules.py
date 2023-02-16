import rules


@rules.predicate
def is_requester(user, relation_request):
    return user == relation_request.requester


@rules.predicate
def is_request_family_member(user, relation_request):
    return relation_request.house.family.filter(id=user.id).exists()


can_add_request = rules.is_authenticated

can_edit_request = rules.is_staff

can_delete_request = rules.is_staff \
                  | is_requester

can_view_request = rules.is_staff \
                | is_requester \
                | is_request_family_member

can_respond_request = rules.is_staff \
                      | is_request_family_member
