from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Команда для создания пользователя
    """
    help = 'Создать нового пользователя'

    def add_arguments(self, parser):
        parser.add_argument(
            'email',
            type=str,
            help='Email пользователя'
        )
        parser.add_argument(
            'password',
            type=str,
            help='Пароль пользователя'
        )
        parser.add_argument(
            '--phone',
            type=str,
            help='Телефон пользователя',
            default=None
        )
        parser.add_argument(
            '--city',
            type=str,
            help='Город пользователя',
            default=None
        )
        parser.add_argument(
            '--avatar',
            type=str,
            help='Путь к изображению аватара пользователя',
            default=None
        )
        parser.add_argument(
            '--tg_chat_id',
            type=str,
            help='ID чата пользователя telegram',
            default=None
        )

    def handle(self, *args, **options):
        User = get_user_model()

        email = options['email']
        password = options['password']
        phone = options.get('phone')
        city = options.get('city')
        avatar = options.get('avatar')
        tg_chat_id = options.get('tg_chat_id')

        try:
            User.objects.create_user(
                email=email,
                password=password,
                phone=phone,
                city=city,
                avatar=avatar,
                tg_chat_id=tg_chat_id
            )
            self.stdout.write(
                self.style.SUCCESS(f'Пользователь {email} успешно создан.')
            )
        except ValidationError as e:
            self.stdout.write(
                self.style.ERROR(f'Ошибка создания пользователя: {e}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Неизвестная ошибка: {e}')
            )
