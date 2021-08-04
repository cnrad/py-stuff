import requests

alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'

def do_request():
    for index in alphabet[2:]:
        for index2 in alphabet:
            for index3 in alphabet:
                r = requests.get(url='https://soundcloud.com/%s%s%s' % (index, index2, index3))
                print('Trying username \"%s%s%s\"' % (index, index2, index3))
                if 'created_at' not in r.text:
                    with open("soundcloudNames.txt","a") as f:
                        f.write('Username \"%s%s%s\" available \n' % (index, index2, index3))
                        f.close()                        
                    print(index + index2 + index3)

do_request()