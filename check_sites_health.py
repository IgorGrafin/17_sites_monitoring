import requests
import whois
import sys


def load_urls4check(path):
    print(path)
    with open(path, mode="r") as file:
        return file.readlines()


def is_server_respond_with_200(url):
    try:
        response = requests.get(url, allow_redirects=True)
    except requests.exceptions.ConnectionError:
        return "Warning! No response!"
    return "Status - OK"


def get_domain_expiration_date(domain_name):
    domain_info = whois.whois(domain_name)
    if domain_info["expiration_date"]:
        return domain_info["expiration_date"][0]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit("Put a file as a parameter")
    sites = load_urls4check(sys.argv[1])
    for site in sites:
        print(site)
        print(is_server_respond_with_200(site))
        print(get_domain_expiration_date(site))
