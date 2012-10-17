import facebook
import pprint

graph = facebook.GraphAPI('AAACEdEose0cBAJoNl0ruByNwBIAHxUNCZB01eKCkAb6jco8WSQJxfkyXWMYGTkDYrg4yIKK75VPqlEXeU7Ywbmk15Fdce1t3oRjSkAiba9o29MxRe')
friends = [item['uid2'] for item in graph.fql('SELECT uid2 FROM friend WHERE uid1 = me()')['data']]
for friend in friends:
    try:
        print friend
        info = graph.get_object(friend)
        likes = graph.get_connections(friend, 'likes')['data']
        print '#'*10
        print info['name']
        pprint.pprint(likes)

    except Exception:
        continue
    #print likes
"""
for item in likes:
    fql = 'SELECT uid FROM page_fan WHERE page_id = %s AND uid IN %s' %(item['id'], tuple(friends))
    d = graph.fql(fql)['data']
    print '%s\t%s\t%s' %(item['name'], item['category'], d)
"""
