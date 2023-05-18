# find-ip
If you have implemented v2ray protocol for VPN with cloudflare CDN you need clean ips. This project uses [cfscanner](https://github.com/MortezaBashsiz/CFScanner/tree/main/python) to scan clean ips according to your ISP and when it scans the ips it will find the best ip (according to download speed) and place it behind your subdomain that has registered in cloudflare automatically.

# How to run ?
1. You need domain.
2. Register your domain at [cloudflare](https://www.cloudflare.com/).
3. Define a subdomain with `A` type record.
4. Get the API token.

After do the above steps, replace the `email`, `token`, `domain` and `subdomain` with yours and do the followings.:
```
$ git clone https://github.com/SalehBorhani/find-ip.git && cd find-ip
$ pip install -r requirements.txt
$ python3 main.py
```
Star the repository if you like that and also if you have any idea you can contribute =) .
