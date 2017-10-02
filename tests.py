import items
# check BaseTask
fields = dict(user_='tomek')
params = dict(name_=u'Etap początkowy',state_='pending', type_='start', fields_=fields)
bt = items.Task(params)
print bt.initializeTime

