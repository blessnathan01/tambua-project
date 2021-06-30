import requests
url = 'https://tambua-project.herokuapp.com/webhooks/rest/webhook' ##change rasablog with your app name
myobj = {
"message": "habari",
"sender": "user",
}
x = requests.post(url, json = myobj)
print(x.text)
