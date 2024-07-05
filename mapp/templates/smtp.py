import base64, time ,json

current_time=str(time.time() +3600.0)

encoded_email= current_time+"_"+"sdfghj"
encoded_email = base64.b32encode(encoded_email.encode()).decode()
print(encoded_email)
decoded_email = base64.b32decode(encoded_email)
decoded_email= decoded_email.decode()
print(decoded_email)

