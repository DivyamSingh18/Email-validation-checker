# CLASSES FOR ERRORS
class missing_value_error(Exception):
    pass
class invalid_domain_error(Exception):
    pass
class invalid_username_error(Exception):
    pass
class invalid_domain_name_error(Exception):
    pass
                            
#CODE:
print("\n############### The Email Validation Program ###############\n")
while True:
    print("\n            email format => username @ domain-name . domain\n" )
    try:
        mail1 = input("Enter your Email address: ")
        mail =  mail1.lower()
        listOfDomains = ["com","co.in","org","ac.in","net" ]
        userDomain = mail.split(".")[-1] 
        splitmail = mail.split("@")
        count =0
        for i in mail:
                if i =="@":
                    count = count+1
                    splitmail2 = splitmail[1].split(".")            

        if "@" not in mail:
            raise missing_value_error
        elif count>1 :
            raise invalid_username_error     
        elif userDomain not in listOfDomains:
            raise invalid_domain_error
        elif not splitmail[0].isalnum():
            raise invalid_username_error
        elif not splitmail2[0].isalnum():
            raise invalid_domain_name_error    
        else:
            print(mail," is a valid email address." )
            break    
# EXCEPTs 
    except invalid_domain_name_error:
        print("Your email is not containing a valid domain-name")
    except missing_value_error:
        print("Your email is missing the symbol '@'")
    except invalid_domain_error:
        print("Your email is not containing a valid domain")
    except invalid_username_error:
        print("Your email is not containing a valid username")


    