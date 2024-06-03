"""
Анализ логов доступа.

Написать функцию analyze_logs которая принимает на себя список строк, 
представляющих логи доступа к веб-сайту. Каждая строка лога содержит 
ip адрес и url к которому был осуществлен доступ. Функция должна возвращать 
словарь, в котором ключами будут ip а значениями количество уникальных url 
к которым был осуществлен доступ с данного ip.

"""
logs = [
    '192.168.0.1 /home',
    '192.168.0.1 /about',
    '192.168.0.2 /home',
    '192.168.0.1 /home',
    '192.168.0.2 /contact',
    '192.168.0.1 /about',
]

def analyze_logs(logs):
    ip_urls = {}

    for log in logs:
        ip, url = log.split()
        if ip in ip_urls:
            ip_urls[ip].add(url)
        else:
            ip_urls[ip] = {url}

    return {ip: len(urls) for ip, urls in ip_urls.items()}

result = analyze_logs(logs)
print(result)

