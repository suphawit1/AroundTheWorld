from app_user.models import Customer

def custom_context(request):
    user_credit = None

    if request.user.is_authenticated:
        logged_in_user = request.user
        Cus = Customer.objects.get(user=logged_in_user)
        user_credit = Cus.Credits

    return {'user_credit': user_credit}