from .models import Purchase, User, Item, UserAccount

def update_user_balances():

    purchases = Purchase.objects.filter(purchase_date__gte=yesterday)

    for purchase in purchases:
        user = purchase.user
        item = purchase.item
        user_account = UserAccount.objects.get(user=user)
        if item.release_amount > 0:
            user_account.balance += item.release_amount
            # create the released amount to the user profit column
            purchase.profit += item.release_amount
            purchase.save()
            user_account.save()

        print(f"User: {user.username}")
        print(f"User Account Balance: {user_account.balance}")       
        print(f"Item: {item.name}")
        print(f"Item Profit: {item.release_amount}")
        print(f" Total Profit earned: {purchase.profit}")




