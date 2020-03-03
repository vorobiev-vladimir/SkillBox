from requests import get

urls = [
    {'link' : 'http://www.avito.ru'},
    {'link' : 'https://moskva.mts.ru/personal'},
    {'link' : 'http://golang.com'},
    {'link' : 'https://www.python.org'},
    {'link' : 'https://www.google.ru'}
]

for url in urls:
    for i in range(1, 101):
        code = get(url['link']).status_code

        if url.get(code) == None:
            url[code] = 1
        else:
            url[code] += 1
    print(url)
