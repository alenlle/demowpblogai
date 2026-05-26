import schedule
import time
from generators.workflow import run_workflow

schedule.every(6).hours.do(run_workflow)

while True:
    schedule.run_pending()
    time.sleep(60)