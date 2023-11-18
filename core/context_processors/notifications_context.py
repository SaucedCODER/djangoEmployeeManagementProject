from core.models import Notification

def notifications(request):
    if request.user.is_authenticated:
        user_notifications = Notification.objects.filter(user=request.user, is_read=False)
        notif_count = user_notifications.count()
    else:
        user_notifications = []
        notif_count = 0

    return {'user_notifications': user_notifications ,
            'notification_count': notif_count }