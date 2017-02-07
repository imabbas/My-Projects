import urllib.request

def findAll(url):
    search_text = ""
    emails = []
    stream = urllib.request.urlopen(url)
    for line in stream:
        decoded = line.decode("UTF-8").strip()
        search_text += decoded
    regex = re.compile(r"mailto:\w+[a-z]@\w+.\w+")
    results = regex.findall(search_text)
    for email in results:
        email = email.lstrip("mailto:")
        if email not in emails:
            emails.append(email)
    return emails

print(findAll("http://www.sys.virginia.edu/people/faculty.html"))
