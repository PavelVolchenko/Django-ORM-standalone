import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    [print(f'{passcard.owner_name}\n'
           f'{passcard.passcode}\n'
           f'{passcard.created_at}\n'
           f'{passcard.is_active}\n') for passcard  in Passcard.objects.all()]