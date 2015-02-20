

# MONGO_HOST = 'localhost'
# MONGO_PORT = 27017
# MONGO_USERNAME = 'xidpuser'
# MONGO_PASSWORD = 'xidpuser'
# MONGO_DBNAME = 'xidp'


# RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
# ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']


# schema = {
#     'firstname': {
#         'type': 'string',
#         'minlength': 1,
#         'maxlength': 10,
#     },
#     'lastname': {
#         'type': 'string',
#         'minlength': 1,
#         'maxlength': 15,
#         'required': True,
#         # talk about hard constraints! For the purpose of the demo
#         # 'lastname' is an API entry-point, so we need it to be unique.
#         'unique': True,
#     },
#     # 'role' is a list, and can only contain values from 'allowed'.
#     'sex': {
#         'type': 'list',
#         'allowed': ["male", "female", "rather not say"],
#     },
#     # An embedded 'strongly-typed' dictionary.
#     'location': {
#         'type': 'dict',
#         'schema': {
#             'address': {'type': 'string'},
#             'city': {'type': 'string'}
#         },
#     },
#     'born': {
#         'type': 'datetime',
#     },

#     'institutions': {
#         'type': 'text',
#     },
# }




DOMAIN = {
	'people': {}


	}



