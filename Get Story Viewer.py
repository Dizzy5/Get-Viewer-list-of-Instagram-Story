import requests ,time , re , json , uuid

guid = str(uuid.uuid4()) # for get uuid device

####################################### data and headers ######################################
username = input('Enter username : ')
password = input('Enter password : ')
Story_id = input('Enter The Story ID : ')

headers = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi;1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'i.instagram.com'
}
data = {
	'uuid': guid,
	'password': password,
	'username': username,
	'device_id': guid,
	'from_reg': 'false',
	'_csrftoken': 'missing',
	'login_attempt_count': '0'
}
url_login = "https://i.instagram.com/api/v1/accounts/login/"

####################################### Get Story Viewer ######################################

def Get_Story_Viewer(story_id):
    next_max_id = ''
    users = []

    while True:
        if not next_max_id: # if next_max_id empty choose firts value
            params = f'https://i.instagram.com/api/v1/media/{story_id}/list_reel_media_viewer/?include_blacklist_sample=true'
        else:
            params = f'https://i.instagram.com/api/v1/media/{story_id}/list_reel_media_viewer/?include_blacklist_sample=true&max_id={next_max_id}'

        req_story = requests.get(params , headers = headers , cookies = cookies).json() # get response
        informtion = req_story['users'] # here take first element of data
        next_max_id = req_story['next_max_id'] # here take next page value  
        if next_max_id == None: # if next_max_id == None take the last users and break the program
            for x in informtion:
                with open('Story Users.txt' , 'a')as echo:
                    echo.write(x['username'] + '\n')
                users.append(x['username'])
            break
        else:
            for x in informtion:
                with open('Story Users.txt' , 'a')as echo:
                    echo.write(x['username'] + '\n')
                users.append(x['username'])
                print (x['username'])
        time.sleep(4)
    print (len(users))

####################################### Login and Get Cookies ######################################

req = requests.post(url_login , data = data , headers = headers)
cookies = req.cookies.get_dict()
if 200 == req.status_code:
    print ("Sucssful Login")
    Get_Story_Viewer(Story_id)
else :
    print('plaese check the internet connection or username & password !!!')
    exit()