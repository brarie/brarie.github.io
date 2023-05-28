from datetime import datetime
from pytz import timezone

datetime.now(timezone('Asia/Seoul'))

readme = open("README.md", "w")
readme.write("Thank you for visiting my blog!\n")
readme.write("Recent Modified Time: ")
readme.write(datetime.now().strftime('%Y.%m.%d - %H:%M:%S'))
readme.close()
