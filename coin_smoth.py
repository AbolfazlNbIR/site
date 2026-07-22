from bs4 import BeautifulSoup
import requests
import re


def get_price(url):
    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=10
    )

    soup = BeautifulSoup(response.text, "html.parser")

    element = soup.find("span", class_="value")

    if not element:
        return "0"

    text = element.get_text(strip=True)
    text = re.sub(r"[^\d]", "", text)

    if text == "":
        return "0"

    return text


def get_dolar():
    return get_price("https://www.tgju.org/profile/price_dollar_rl")


def get_yuro():
    return get_price("https://www.tgju.org/profile/price_eur")


def get_derham():
    return get_price("https://www.tgju.org/profile/price_aed")


def get_pond():
    return get_price("https://www.tgju.org/profile/price_gbp")


def get_yen_japan():
    return get_price("https://www.tgju.org/profile/price_jpy")


def get_dinar_kuwait():
    return get_price("https://www.tgju.org/profile/price_kwd")


def get_dolar_australia():
    return get_price("https://www.tgju.org/profile/price_aud")


def get_dolar_canada():
    return get_price("https://www.tgju.org/profile/price_cad")


def get_yuan_chin():
    return get_price("https://www.tgju.org/profile/price_cny")


def get_lir_turkey():
    return get_price("https://www.tgju.org/profile/price_try")


def get_rial_saudi():
    return get_price("https://www.tgju.org/profile/price_sar")


def get_franc_swiss():
    return get_price("https://www.tgju.org/profile/bank_chf")


def get_rupee_pakistan():
    return get_price("https://www.tgju.org/profile/price_pkr")


def get_dinar_iraq():
    return get_price("https://www.tgju.org/profile/price_iqd")


def get_lir_syria():
    return get_price("https://www.tgju.org/profile/bank_syp")


def get_kron_sweden():
    return get_price("https://www.tgju.org/profile/price_sek")


def get_rial_qatar():
    return get_price("https://www.tgju.org/profile/price_qar")


def get_rial_oman():
    return get_price("https://www.tgju.org/profile/price_omr")


def get_dinar_bahrain():
    return get_price("https://www.tgju.org/profile/price_bhd")


def get_afghani():
    return get_price("https://www.tgju.org/profile/price_afn")


def get_ringgit_malaysia():
    return get_price("https://www.tgju.org/profile/price_myr")


def get_bat_thailand():
    return get_price("https://www.tgju.org/profile/price_thb")


def get_manat_azerbaijan():
    return get_price("https://www.tgju.org/profile/price_azn")


def get_dram_armenia():
    return get_price("https://www.tgju.org/profile/price_amd")


def get_lari_georgia():
    return get_price("https://www.tgju.org/profile/price_gel")