import json

def main():
    with open("old_credentials.json", "r") as file:
        credentials_data = json.load(file)

    with open("old_token.json", "r") as file:
        token_data = json.load(file)

    credentials_string = json.dumps(credentials_data)
    token_string = json.dumps(token_data)

    with open("credentials.txt", "w") as file:
        print(credentials_string, file=file)

    with open("token.txt", "w") as file:
        print(token_string, file=file)

    
if __name__ == '__main__':
    main()

