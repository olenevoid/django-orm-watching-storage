import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    first = Passcard.objects.first()
    print('owner_name', first)
    for field in first._meta.get_fields():
        if not field.is_relation:
            print(field.verbose_name, getattr(first, field.name))
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
