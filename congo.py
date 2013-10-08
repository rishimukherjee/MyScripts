import json
import requests

TOKEN = ""

def get_posts():
    query = ("SELECT post_id, actor_id, message FROM stream WHERE filter_key = 'others' LIMIT 200")
    payload = {'q': query, 'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    return result['data']

def commentall(posts):
    for post in posts:
        if 'placed' in post['message'].lower()  or 'hired' in post['message'].lower():
            post_comments_payload = {'access_token': TOKEN}
            getcomments = requests.get('https://graph.facebook.com/%s/comments' % post['post_id'], params=post_comments_payload)
            comments = json.loads(getcomments.text)["data"]
            already_congratulated = False
            for comment in comments:
                if "Congratulations! Phode Ho." in comment["message"] or "Jiyo lark" in comment["message"]: #This is hack. :P
                    already_congratulated = True
                    break
            if already_congratulated:
                continue
            print comments
            req = requests.get('https://graph.facebook.com/%s' % post['actor_id'])
            comments_url = 'https://graph.facebook.com/%s/comments' % post['post_id']
            user = json.loads(req.text)
            message = 'Congratulations! Phode Ho. %s :D' % user['first_name']
            payload = {'access_token': TOKEN, 'message': message}
            doComment = requests.post(comments_url, data=payload)

            print "Congratulated %s for (%s)" % (user['first_name'], post['message'])

commentall(get_posts())
