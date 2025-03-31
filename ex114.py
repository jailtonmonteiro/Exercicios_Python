def validaURL(url):
    import requests as req
    while True:
        if 'https://' in url:
            try:
                resposta = req.get(url, timeout=5)
                print(f'O site\033[1;32m {url} \033[mestá acessível.')
                break
            except:
                print(f'O site\033[31m {url} \033[mnão está acessível')
                break
        else:
            url = 'https://'+url
            continue


url = str(input('Digite a url: ')).strip().lower()
validaURL(url)