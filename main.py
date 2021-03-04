import requests

si = input("input here: ")
asi = si.split(' ')
aso = []
for word in asi:
    url = "https://en.wiktionary.org/wiki/" + word
    wotmp = requests.get(url)
    ptmp = wotmp.text
    try:
        iLangIndex = ptmp.index('<span class="mw-headline" id="French">')
        iPronIndex = ptmp.index('<span class="IPA">/', iLangIndex) + 19
        iPronTerminal = ptmp.index('/', iPronIndex)
        sPron = ptmp[iPronIndex:iPronTerminal]
    except ValueError as e:
        sPron = "404"
    aso.append(sPron)
so = ' '.join(aso)
print(so)