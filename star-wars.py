import requests
import shutil
from tabulate import tabulate

base_url = "https://swapi.dev/api/"
terminal_width = shutil.get_terminal_size().columns
tilde_position = terminal_width


# tilde_position = terminal_width // 2

def verity_connection():
    global response
    try:
        response = requests.get(base_url)
    except requests.RequestException as e:
        print("Error requesting to connect to api {}".format(e))
        exit()

    if response.status_code == requests.codes.ok:
        print(response.status_code)
    else:
        print("Didn't receive a successful status code, exiting")
        exit()

    return response.json()


def query_api(url):
    api_response = requests.get(url)
    choice = []
    if "films" in url:
        key = "title"
    else:
        key = "name"

    print(key)

    for record in api_response.json()['results']:
        choice.append(record[key])

    for c in choice:
        print(c)

    print("\n")
    option = '''please choose from one of the above options: \n'''
    opt = input(option)
    # Remove any leading trailing spaces
    opt = opt.lstrip().rstrip()
    print(" " * (tilde_position - 1) + "**~**")

    for record in api_response.json()['results']:
        if record[key] == opt or record[key] == opt.title():
            for rec_name, rec_value in record.items():
                print(rec_name, rec_value)
        else:
            print("Invalid option")
            exit()

    print(" " * (tilde_position - 1) + "**~**")

    '''
    table = element.values()
    headers = element.keys()
    print(tabulate({"API-Name": table,  "API-URI": headers}, headers="keys"))
    print("\n")
    '''


if __name__ == "__main__":
    apis = verity_connection()
    api_map = {}  
    while True:
        counter = 1
        for name, api in apis.items():
            print("{}) {}: {}".format(counter, name, api))
            api_map[counter] = api
            counter += 1
        print("{}) exit".format(0))

        api_opt = int(input("Choose from a Star Wars API or exit: \n"))
        print(" " * (tilde_position - 1) + "**~**")
        try:
            assert 0 <= api_opt <= 6
        except Exception as main_e:
            print("Incorrect option {}, please choose again:".format(main_e))
            continue

        if api_opt == 0:
            exit()
        else:
            query_api(url=api_map[api_opt])
