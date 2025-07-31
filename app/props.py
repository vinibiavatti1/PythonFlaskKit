from typing import Any


props: dict[str, Any] = {
    # General
    'app_name': 'Website',
    'lang': 'en',

    # Datetime and region
    'timezone': 'UTC',
    'date_format': '%Y-%m-%d',
    'date_time_format': '%Y-%m-%d %H:%M:%S',

    # Keys
    'salt': '73ef930e2b797a5b5daa73cf3a3025ce853d1bb8',
    'secret_key': '0748b1683e871cb26ce30b4fdf4db088c5f2f97e',

    # E-mail
    'mail_smtp': 'smtp.example.com',
    'mail_port': '465',
    'mail_ssl': True,
    'mail_login': 'contact@company.com',
    'mail_password': 'password',
    'mail_charset': 'UTF-8',
}
