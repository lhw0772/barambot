import telegram
import io
from config import *

test = telegram.Bot(token = TOKEN)
updates = test.getUpdates()
for u in updates:
    print(u.message)
