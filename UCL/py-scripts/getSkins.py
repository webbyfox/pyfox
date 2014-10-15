#Script (Python) "users_listing.csv"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=path
##ti

request = container.REQUEST
response =  request.response

for item in context.aq_parent.objectValues():
     if item.meta_type == 'Silva Publication':

        try:
           if  str(item.aq_inner.get_metadata_element('silva-layout', 'skin')) == 'UCL Corporate Identity v1.0':
               print item.aq_inner.getId()
        except:
            pass
return printed