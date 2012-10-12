import facebook

graph = facebook.GraphAPI('AAACEdEose0cBAArF5G0ryWaPm5tZCkHMHQgx2JRm4il1CKBagp1FBdX9hiZB2kNOWmqc1a0bTq44X4IIhsvB5EYPqesHYMLPye4yIZCC8xZBHGMXZCDq6')
likes = graph.get_connections('me', 'likes')['data']
friends = [item['uid2'] for item in graph.fql('SELECT uid2 FROM friend WHERE uid1 = me()')['data']]
for item in likes:
    fql = 'SELECT uid FROM page_fan WHERE page_id = %s AND uid IN %s' %(item['id'], tuple(friends))
    d = graph.fql(fql)['data']
    print '%s\t%s\t%s' %(item['name'], item['category'], d)
