from .tasks import update_user_balances
import time

def timer(seconds=10):
    print(f"Timer started for {seconds} seconds.")
    while True:
        print(f"{seconds} seconds remaining.")
        time.sleep(seconds)
        update_user_balances()
    
# if __name__ == "__main__":
#     seconds = int(input("Enter the number of seconds for the timer: "))
#     timer(seconds)

