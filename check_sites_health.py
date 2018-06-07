import requests
import whois
import sys
import datetime


def load_urls4check(path):
    with open(path, mode="r") as file:
        return file.readlines()


def is_server_respond_with_200(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.ConnectionError:
        return "No response!"


def get_domain_expiration_date(domain_name):
    domain_info = whois.whois(domain_name)
    expiration_date = domain_info["expiration_date"]
    if type(expiration_date) == list:
        return expiration_date[0]
    return expiration_date


def get_days_to_expiration(expiration_date):
    now = datetime.datetime.now()
    delta = expiration_date - now
    return str(delta.days)


def print_checking_results(index, site):
    print("{}) {}".format(index, site))
    print("Status code - {}".format(is_server_respond_with_200(site)))
    expiration_date = get_domain_expiration_date(site)
    if expiration_date:
        print("Days to expiration - {}".format(get_days_to_expiration(expiration_date)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit("Put a file path as an argument")
    sites = load_urls4check(sys.argv[1])
    for index, site in enumerate(sites, start=1):
        print_checking_results(index, site.strip())

