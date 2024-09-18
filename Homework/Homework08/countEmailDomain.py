# Sebastian Main

def get_email():
    emails = ["archive-08-05-2030", "archive-02-20-2019", "archive-03-02-2024"]
    email = input("Enter the filename for the email archive: ")
    if email in emails:
        return email
    else:
        print("File " + email + " does not exist. Please try again.")
        return get_email()

def get_domain(email):
    domains = ["uct.ac.za", "berkeley.edu", "iupui.edu", "sakaiproject.org", "umich.edu"]
    domain = input("Enter the domain: ")
    if domain in domains:
        return domain
    else:
        print("Domain " + domain + " does not exist. Please try again.")
        return get_domain(email)

def read_email(email, domain):
    if email == "archive-08-05-2030":
        f = open("archive-08-05-2030.txt")
        counter = 0
        for line in f:
            start_with = line[:5]
            if start_with == "From:":
                rest = line[5:]
                rest = rest.strip()
                if domain in rest:
                    counter += 1
        print("There are " + str(counter) + " emails from " + domain)
        f.close()
        
    elif email == "archive-02-20-2019":
        f = open("archive-02-20-2019.txt")
        counter = 0
        for line in f:
            start_with = line[:5]
            if start_with == "From:":
                rest = line[5:]
                rest = rest.strip()
                if domain in rest:
                    counter += 1
        print("There are " + str(counter) + " emails from " + domain)
        f.close()
        
    elif email == "archive-03-02-2024":
        f = open("archive-02-20-2019.txt")
        counter = 0
        for line in f:
            start_with = line[:5]
            if start_with == "From:":
                rest = line[5:]
                rest = rest.strip()
                if domain in rest:
                    counter += 1
        print("There are " + str(counter) + " emails from " + domain)
        f.close()



def main():
    email = get_email()
    domain = get_domain(email)
    email_from_domain = read_email(email, domain)
    
    
    
main()