from acf_utils.fields.getFieldId import getFieldId


def newGroup(title):
    field_id = getFieldId()
    slug = title.replace(" ", "_").lower()
    group = {}
    group['key'] = field_id
    group['label'] = title
    group['name'] = slug
    group['aria-label'] = ""
    group['type'] = "group"
    group['instructions'] = ""
    group['required'] = 0
    group['conditional_logic'] = 0
    group['wrapper'] = {
            "width": "",
            "class": "",
            "id": ""
            }
    group['layout'] = "block"
    group['sub_fields'] = []
    return group
