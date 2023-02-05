def extract(nested_dict, key):
    """
    param: nested dict , dictionary object
    param: key , key to extract
    return: nested dict, value of key
    """

    if '/' not in key:
        return nested_dict.get(key)

    keys = key.split("/")
    for k in keys:
        if type(nested_dict) != dict:
            return None
        nested_dict = nested_dict.get(k)
    return nested_dict

#example:
# nested_dict = {
#     "person": {
#         "name": {
#             "first": "John",
#             "last": "Doe"
#         },
#         "age": 30,
#         "address": {
#             "street": "123 Main St.",
#             "city": "San Francisco",
#             "state": "CA",
#             "zip": "94114"
#         }
#     }
# }

# key = "person/name/first"
# value = extract(nested_dict, key)
# print(value) # Output: John


