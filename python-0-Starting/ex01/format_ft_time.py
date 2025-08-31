import time
from datetime import datetime

seconds_epoch = time.time()
print(
    f"Seconds since January 1, 1970: {seconds_epoch:,.4f} or {seconds_epoch:.2e} in scientific notation"
)

current_date = datetime.now()
print(current_date.strftime("%b %d %Y"))
