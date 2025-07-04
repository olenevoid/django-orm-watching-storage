import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь    
    active_passcards_number = Passcard.objects.filter(is_active=True).count()
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    print('Количество активных пропусков:', active_passcards_number)
