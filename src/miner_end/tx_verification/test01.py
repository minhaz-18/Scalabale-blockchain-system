import time
import datetime

present = time.time()
prs = time.ctime(present)
print("prs: ", type(prs))
print("present: ", present)
r_present = datetime.datetime.strptime(prs, "%a %b %d %H:%M:%S %Y")
return_present = r_present.timestamp()
print("return_present: ", return_present)

future = time.time()
ftr = time.ctime(future)
print("ftr: ", ftr)
print("future: ", future)

# dif = int(ftr) - int(prs)
