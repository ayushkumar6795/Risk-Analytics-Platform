from auth.auth_service import sign_out

email = "ayushkumar28385@gmail.com"
password = "Test@123"

response, error = sign_out()

if error:
    print("Logout failed:")
    print(error)
else:
    print("Logout request successful!")
    print(response)
    
