
import urllib.request
import re

# tools to use: string manipulation or regular expressions

def find_emails_in_website(url):
    search_text = ""
    email_list = []
    remove_this = []
    numbers = "0123456789"
    final_email_list = []
    stream = urllib.request.urlopen(url)
    for line in stream:
        decoded = line.decode("UTF-8").strip()
        search_text += decoded.lower()
    search_text = search_text.replace(' at ','@')
    search_text = search_text.replace(' dot ','.')
    search_text = search_text.replace('nospam','')
    search_text = search_text.replace('<br', '')
    search_text = search_text.replace('>br', '')
    # regex = re.compile(r"\w+.\w+[\w]@\w+.\w+.\w+\.\w+")
    regex = re.compile(r"\w+.\w+.\w+.\w+[\w]@\w+.\w+.\w+\.\w+")
    results = regex.findall(search_text)
    for email in results:
        if email not in email_list:
            email_list.append(email)
    for email in email_list:
        if email[-1] in str(numbers) or email[-2] in str(numbers) or email[-3] in str(numbers):
            # print("REMOVE THIS:", email)
            email_list.remove(email)
        if email[-1] == ".":
            email.strip(".")
        elif email[-1] == " ":
            email.strip(" ")
            # for email in email_list:
            # if "nospam" in email:
            #     remove_index = email_list.index(email)
            #     remove_this.append(email_list[remove_index])
            #     index = email.find("nospam")
            #     stripped = email[0: index] + email[index+len("nospam"):]
            #     email_list.append(stripped)
    for email in remove_this:
        email_list.remove(email)
    remove_this.clear()
    for email in email_list:
        if " " in email:
            space_index = email.find(" ")
            at_index = email.find("@")
            if space_index > at_index:
                stripped = email[0: space_index]
                email_list.append(stripped)
                remove_this.append(email)
            else:
                stripped = email[space_index + 1: len(email)]
                email_list.append(stripped)
                remove_this.append(email)
    for email in email_list:
        if email in remove_this:
            email_list.remove(email)
    remove_this.clear()
    for email in email_list:
        dot_index = email.find(".")
        space_index = email.find(" ")
        at_index = email.find("@")
        if "." not in email:
            # email_list.remove(email)
            remove_this.append(email)
        elif len(email) - dot_index < 3:
            # email_list.remove(email)
            remove_this.append(email)
        if " " in email:
            if space_index > at_index:
                stripped = email[0: space_index]
                email_list.append(stripped)
                remove_this.append(email)
            else:
                stripped = email[space_index + 1: len(email)]
                email_list.append(stripped)
                remove_this.append(email)
    for email in email_list:
        if email in remove_this:
            email_list.remove(email)
    regex2= re.compile(r'.@.\.\w+')
    results2 = regex2.findall(search_text)
    for email in email_list:
        space_index = email.find(" ")
        at_index = email.find("@")
        if " " in email:
            if space_index > at_index:
                stripped = email[0: space_index]
                email_list.append(stripped)
                remove_this.append(email)
            else:
                stripped = email[space_index + 1: len(email)]
                email_list.append(stripped)
                remove_this.append(email)
    for email in email_list:
        if email in remove_this:
            email_list.remove(email)
    for email in results2:
        if email not in final_email_list:
            final_email_list.append(email)
    for email in email_list:
        if email not in final_email_list:
            final_email_list.append(email)
    return final_email_list

