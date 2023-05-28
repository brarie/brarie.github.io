from datetime import datetime
from pytz import timezone

datetime.now(timezone('Asia/Seoul'))

readme = open("README.md", "w")
readme.write("Thank you for visiting my blog!\n")
readme.write("Recent Modified Time: ")

KST = timezone('Asia/Seoul')

today = datetime.now()
today = today.astimezone(KST).strftime('%Y.%m.%d - %H:%M:%S')

readme.write(today)
readme.close()
