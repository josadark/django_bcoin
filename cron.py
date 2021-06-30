from background_task import background

@background(schedule=5)
def notify():
    print("the croncops on patrol!")


notify()
