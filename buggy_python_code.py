import sys
import yaml
import urllib3
import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)


CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}


class Person(object):
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    print(format_string.format(person=person.__init__.__globals__['CONFIG']['API_KEY']))


def fetch_website(urllib_version, url):
    # Import the requested version (2 or 3) of urllib
    exec_string = f"import urllib{'' if urllib_version == 2 else '3'} as urllib"
    exec(exec_string, globals())
    # Fetch and print the requested URL

    try:
        http = urllib3.PoolManager()
        _ = http.request("GET", url)
        print(url)
    except Exception as _:
        print("Exception")


def load_yaml(filename):
    stream = open(filename)
    deserialized_data = yaml.load(stream, Loader=yaml.SafeLoader)  # deserializing data
    return deserialized_data


def authenticate(password):
    # Assert that the password is correct
    if  password != "Iloveyou":
        print("Invalid password!")
        return
    print("Successfully authenticated!")


if __name__ == "__main__":
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("2. Code injection vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")
    choice = input("Select vulnerability: ")
    if choice == "1":
        new_person = Person("Vickie")
        print_nametag(input("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version = input("Choose version of urllib: ")
        if urlib_version != "2" or urlib_version != "3":
            print("wrong version, use either 3 or 2")
            sys.exit(1)
        urlib_version = int(urlib_version)
        fetch_website(urlib_version, url="https://www.google.com")
    elif choice == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)
