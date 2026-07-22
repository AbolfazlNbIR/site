from flask import Flask, render_template
import coin_smoth as cs

app = Flask(__name__)

def safe_int(value):
    try:
        return int(value)
    except:
        return 0

@app.route('/')
def index():
    currencies = [
        ('دلار آمریکا', cs.get_dolar, 'fa-dollar-sign'),
        ('یورو', cs.get_yuro, 'fa-euro-sign'),
        ('درهم امارات', cs.get_derham, 'fa-money-bill-wave'),
        ('پوند انگلیس', cs.get_pond, 'fa-sterling-sign'),
        ('ین ژاپن', cs.get_yen_japan, 'fa-yen-sign'),
        ('دینار کویت', cs.get_dinar_kuwait, 'fa-coins'),
        ('دلار استرالیا', cs.get_dolar_australia, 'fa-dollar-sign'),
        ('دلار کانادا', cs.get_dolar_canada, 'fa-dollar-sign'),
        ('یوان چین', cs.get_yuan_chin, 'fa-yen-sign'),
        ('لیر ترکیه', cs.get_lir_turkey, 'fa-lira-sign'),
        ('ریال عربستان', cs.get_rial_saudi, 'fa-shekel-sign'),
        ('فرانک سوئیس', cs.get_franc_swiss, 'fa-franc-sign'),
        ('روپیه پاکستان', cs.get_rupee_pakistan, 'fa-rupee-sign'),
        ('دینار عراق', cs.get_dinar_iraq, 'fa-dinar'),
        ('لیر سوریه', cs.get_lir_syria, 'fa-lira-sign'),
        ('کرون سوئد', cs.get_kron_sweden, 'fa-krona'),
        ('ریال قطر', cs.get_rial_qatar, 'fa-money-bill'),
        ('ریال عمان', cs.get_rial_oman, 'fa-money-bill'),
        ('دینار بحرین', cs.get_dinar_bahrain, 'fa-coins'),
        ('افغانی', cs.get_afghani, 'fa-afghani'),
        ('رینگیت مالزی', cs.get_ringgit_malaysia, 'fa-ringgit'),
        ('بات تایلند', cs.get_bat_thailand, 'fa-bath'),
        ('منات آذربایجان', cs.get_manat_azerbaijan, 'fa-manat'),
        ('درام ارمنستان', cs.get_dram_armenia, 'fa-dram'),
        ('لاری گرجستان', cs.get_lari_georgia, 'fa-lari'),
    ]

    prices = []
    for name, func, icon in currencies:
        raw = func()
        val = safe_int(raw)
        prices.append({
            'name': name,
            'price': f"{val:,}",
            'icon': icon
        })

    return render_template('index.html', prices=prices)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')