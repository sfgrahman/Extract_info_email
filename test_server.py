import requests

x = requests.post(
    "http://127.0.0.1:8000/",
    json={
        "from_email":"sfgrahman@hotmail.com",
        "content":""" 
            Dear Sarkar
                    I hope this message finds you well. I'm Moududur from Theta;

                    I'm looking to purchase some company T-shirt for my team, we are a team of 100k people, and we want to get 2 t-shirt per personl

                    Please let me know the price and timeline you can work with;

                    Looking forward

                    Moududur
        """
    }
    
)

print(x.json())