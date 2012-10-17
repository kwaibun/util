import facebook
import facebook
import pprint

graph = facebook.GraphAPI('BAADj6uZBY8NIBAF8zTZCiuAtycvgzh5XRDZBDYNEltgm4TedgfBXgJrekGZC0rzblExsuFZAeZB255l8VHK2j815v3QL069k1vqx1KWWYBtPAJd5rL5puoHMRqLQH0mpIZD')
fql = """
SELECT post_id, filter_key, type, attachment, updated_time, message, description, likes, comments
FROM stream 
WHERE source_id IN 
    (SELECT uid2 FROM friend WHERE uid1 = me())
        AND attachment.fb_object_type in ('photo', 'album') 
            AND created_time >= now()-86400
                ORDER BY likes.count DESC LIMIT 100
"""
data = graph.fql(fql)['data']
print len(data)
for item in data:
    print 'message: ', item['message']
    print 'post_id: ', item['post_id']
    print 'type: ', item['type']
    #d = graph.get_object(item['post_id'])
    #pprint.pprint(d)
    fbid = item['attachment']['media'][0]['photo']['fbid']
    print fbid
    #pprint.pprint(item['attachment'])
    #pprint.pprint(item)
    print '#'*30

