catalog = context.service_catalog
ids = ('rizwan-sandbox','acquired_publication')

result_string = []

publications = catalog.searchResults({'meta_type':'Silva Publication','path': '/silva/'})
for publication in publications:
    obj = publication.getObject()
    #print context.service_metadata.getMetadataValue(obj,'silva-layout','skin')
    binding = context.service_metadata.getMetadata(obj)
    #binding.setValues('silva-layout',{'skin':'UCLCorporateIdentityv4.0'},1)
    try:
       if binding.get('silva-layout', 'skin', 0,):
          result_string.append(obj.getId() + ',')
          result_string.append(obj.silva_object_url())
          result_string.append('\r\n')

    except: pass
    #   print publication
    #print context.service_metadata.getMetadataValue(obj,'silva-layout','skin')




csv_out = ''.join(result_string)


return csv_out
