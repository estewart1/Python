from slackclient import SlackClient
 
slack_client = SlackClient("xoxb-341116102976-364383804128-NMmByITSfTwGIt5v7mx0d6Nf")
 
api_call = slack_client.api_call("users.list")
if api_call.get('ok'):
    users = api_call.get('members')
    for user in users:
        print user.get('name')
