config = {
    # Env
    'env': 'development',
    'version': '1.0.0',

    # General
    'title': 'Website',
    'author': 'Author',
    'company': 'Company',
    'description': '...',
    'lang': 'en',
    'key_words': 'key,words',
    'responsive': True,
    'charset': 'UTF-8',
    'favicon': '/static/medias/favicon-32x32.png',

    # i18n
    'i18n': True,
    'idiom': 'en_US',

    # Datetime and region
    'timezone': 'UTC',
    'date_format': '%Y-%m-%d',
    'date_time_format': '%Y-%m-%d %H:%M:%S',

    # Database
    'db_host': 'localhost',
    'db_port': 3306,
    'db_user': 'root',
    'db_pass': '',
    'db_name': 'database',

    # Hashes
    'salt': '73ef930e2b797a5b5daa73cf3a3025ce853d1bb8',
    'secret_key': '0748b1683e871cb26ce30b4fdf4db088c5f2f97e',

    # E-mail
    'mail_smtp': 'smtp.example.com',
    'mail_port': '465',
    'mail_ssl': True,
    'mail_login': 'contact@company.com',
    'mail_password': 'password',
    'mail_charset': 'UTF-8',

    # ReCaptcha v3
    'recaptcha_enabled': False,
    'recaptcha_site_key': '6LfoMNgdAAAAAFC-FumFY8ga7QGAhBlPaOb0xBdH',
    'recaptcha_secret_key': '6LfoMNgdAAAAAEu51riSXQK5Pkcda8wf3gp5mNRk',
    'recaptcha_threshold': 0.5,
}
