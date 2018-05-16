def send_message_to_slack(text):
    from urllib import request, parse
    import json
    post = {"text": "{0}".format(text)} 
    try:
        json_data = json.dumps(post)
        req = request.Request("https://hooks.slack.com/services/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",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))
 
send_message_to_slack('Dude, this Slack message is coming from my Python program!')