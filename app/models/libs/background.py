from models.modules.core import app, sched, BackgroundScheduler

def run_function_in_background(function_name, time):
    sched.add_job(function_name, 'interval', seconds=10)
    sched.start()

def end_all_backgrounds():
    sched.shutdown()