import random
from datetime import datetime,timedelta
start_date=datetime(2002,12,3)
end_date=datetime(2026,4,27)
random_data=start_date+timedelta(days=random.randint(0,(end_date-start_date).days))
print('random date:',random_data.date())