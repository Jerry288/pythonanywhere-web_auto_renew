import requests
import json

with open('auth.json', 'r') as f:
    auth = json.loads(f.read())

username = auth['username']
password = auth['password']

#We retrieve csrf token and sessionid by requesting /login
lgnhead = requests.get("https://www.pythonanywhere.com/login/").cookies
csrf = lgnhead.get('csrftoken')
sessionid = lgnhead.get('sessionid')

cookies = {
    'cookie_warning_seen': 'True',
    'ajs_user_id': '1WbqHnqkttfOyIQIX8TF7pbSdN53',
    'ajs_anonymous_id': 'f58dd242-12cb-4529-9ea4-297e85059e63',
    '_ga': 'GA1.1.75392357.1687790904',
    '_gid': 'GA1.1.541137987.1687790904',
    'csrftoken': csrf,
    'sessionid': sessionid
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en,en-US;q=0.9,zh-TW;q=0.8,zh;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.pythonanywhere.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.pythonanywhere.com/login/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

data = f'csrfmiddlewaretoken={csrf}&auth-username={username}&auth-password={password}&login_view-current_step=auth'

response = requests.post('https://www.pythonanywhere.com/login/', headers=headers, data=data, cookies=cookies, allow_redirects=False)
rawcookies = response.cookies
csrf = rawcookies.get('csrftoken')
sessionid = rawcookies.get('sessionid')

cookies = {
    'web_app_tab_type': '%23tab_id_jlin0312_pythonanywhere_com',
    'cookie_warning_seen': 'True',
    'ajs_user_id': '1WbqHnqkttfOyIQIX8TF7pbSdN53',
    'ajs_anonymous_id': 'f58dd242-12cb-4529-9ea4-297e85059e63',
    '_ga': 'GA1.1.75392357.1687790904',
    '_gid': 'GA1.1.541137987.1687790904',
    'csrftoken': csrf,
    'sessionid': sessionid,
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en,en-US;q=0.9,zh-TW;q=0.8,zh;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.pythonanywhere.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.pythonanywhere.com/user/jlin0312/webapps/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

data = f'csrfmiddlewaretoken={csrf}'

response = requests.post('https://www.pythonanywhere.com/user/jlin0312/webapps/jlin0312.pythonanywhere.com/extend', headers=headers, cookies=cookies, data=data)
if response.status_code != 200:
    print(f'error: {str(response.status_code)}')