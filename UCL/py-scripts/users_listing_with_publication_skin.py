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

column_name = ['Publication Title','ID','Skin','URL','User Emails','User - Roles', 'Unique User Emails' ]

for field_name in column_name:
  result_string.append(field_name + ',')


result_string.append('\r\n')
unique_users = []
ignore_list = [centre-for-materials-discovery,cpd-shortcourses,dcal,earth-planetary-institute,earth-sciences,
es,icls,ineqcities,ioo,iris-demo,jro,libnet,maps-faculty,pathology,
pathseek,polfree,prospective,prospective-students,proteomics,rid-rti,skip-nmd,staff,surgicalscience,system7,
www.e-pilepsy.eu,www.embalance.eu,www.euroewing.eu,www.evidem.org.uk,www.i-mars.eu,
]

for item in  context.service_catalog(meta_type={'query':'Silva Publication'},
                                                       path={'query' : '/silva/' + path, 'depth' :0}):

  try:
       skin = item.getObject().aq_inner.get_metadata_element('silva-layout', 'skin')
  except:
       skin = None

  if skin == 'UCL Corporate Identity v1.0' and item.id not in ignore_list:
      result_string.append(item.get_title)
      result_string.append(',')
      result_string.append(item.id)
      result_string.append(',')
      result_string.append(skin)
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
