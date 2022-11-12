import meower
import datetime

date = datetime.datetime.now()

for i in range(1, 10):
    meower.change_page(i)
    for i in range(0, meower.home_len()):
        print(meower.get_post(meower.find_post(i)))
        f = open(date.strftime("posts/%m-%d-%Y.txt"), "a")
        f.write(f"{meower.get_post(meower.find_post(i))}\n")
        f.close()
