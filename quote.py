import urllib
import re



def get_quote(symbol):

    base_url = 'http://finance.google.com/finance?q='

    content = urllib.urlopen(base_url + symbol).read()

    m = re.search('id="ref_694653_l".*?>(.*?)<', content)

    if m:

        q = m.group(1)

    else:

        q = 'no quote available for: ' + symbol

    return q
