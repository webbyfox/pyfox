#Script (Python) "users_listing.csv"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=path
##ti

csv_out = ''

result_string = []

column_name = ['Publication Title','ID','URL','User Emails','User - Roles', 'Unique User Emails' ]

for field_name in column_name:
  result_string.append(field_name + ',')


result_string.append('\r\n')
unique_users = []    
for item in  context.service_catalog(meta_type={'query':'Silva Publication'},
                                                       path={'query' : '/silva/' + path, 'depth' :0}):
    result_string.append(item.get_title)
    result_string.append(',')
    result_string.append(item.id)
    result_string.append(',')
    result_string.append(item.silva_object_url)
    result_string.append(',')
    item_object = item.getObject()
    users, users_email = [],[]

    for user in item_object.get_local_roles():
           user_email = user[0].strip()+'@ucl.ac.uk'
           users_email.append(user_email)
           users.append(user_email  + ' : ' + str(user[1]))
           if user_email in unique_users:
              continue
           unique_users.append(user_email) 

    result_string.append(str(users_email).replace(',',';').replace('[','').replace(']',''))
    result_string.append(',')
    result_string.append(str(users).replace(',','').replace('(','').replace(')',''))
    result_string.append('\r\n')

result_string.append('\r\n')
result_string.append('\r\n')
result_string.append('Unique User Emails'+ ',' + str(unique_users).replace(',',';').replace('[','').replace(']',''))
 
csv_out = ''.join(result_string)


return csv_out

