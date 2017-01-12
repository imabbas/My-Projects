# Christine Farinas (caf5ct)

import urllib.request
import re

# tools to use: string manipulation or regular expressions

def find_emails_in_website(url):
    search_text = ""
    email_list = []
    # email_attribute = [" edu", " com", " at ", "@", ".e", ".c", "dot"]
    stream = urllib.request.urlopen(url)
    for line in stream:
        decoded = line.decode("UTF-8").strip()
        search_text += decoded.lower()
        # print(decoded.lower())
    regex = re.compile(r"\w+.\w+[\w]@\w+.\w+.\w+")
    # regex_2 = re.compile(r"")
    results = regex.findall(search_text)
    # results_2 = regex_2.findall(search_text)
    for email in results:
        if email not in email_list:
            email_list.append(email)
    # for email in results_2:
    #     if email not in email_list:
    #         email_list.append(email)
    print(len(email_list))
    return email_list

print(find_emails_in_website("http://cs1110.cs.virginia.edu/emails.html"))