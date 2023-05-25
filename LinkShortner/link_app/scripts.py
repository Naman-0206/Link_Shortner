from .models import Urls
from datetime import datetime , timedelta

def delete_one_month_old_data():
    cutoff_date = datetime.now().date() - timedelta(days=30)
    Urls.objects.filter(created_at__lte=cutoff_date)
    #print("Data Deleted Succesfully!")