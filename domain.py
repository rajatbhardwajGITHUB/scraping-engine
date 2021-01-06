from urllib.parse import urlparse


# Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        print(results)
        print(results[-2] + '.' + results[-1])
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        print(urlparse(url).netloc)
        return urlparse(url).netloc
    except:
        return ''

#url = 'https://automatetheboringstuff.com/2e/chapter12/'
#a = get_domain_name(url)
#print(a)
