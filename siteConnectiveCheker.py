import urllib.request as urllib

def site_checker(url):
    print("Checking connectivity...")

    response = urllib.urlopen(url)

    print("Connected to ", url, "succesfully")
    print("The response code was:", response.getcode())

print("This is a site connectivity checker program")
input_url = input("Type the url of the site you want to check: ")

site_checker(input_url)