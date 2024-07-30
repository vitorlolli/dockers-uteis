## WP CLI Para Instalação

`wp core install --url=localhost --title=teste --admin_user=teste --admin_password=teste --admin_email=teste@teste.com --locale=pt_BR --skip-email`

`wp plugin install all-in-one-wp-migration --activate`


## Configuração para proxy reverso

Substituir no wp-config.php

```
if (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && strpos($_SERVER['HTTP_X_FORWARDED_PROTO'], 'https') !== false) {
     $_SERVER['HTTPS'] = 'on';
}
```
por
`` $_SERVER['HTTPS'] = 'on'; ``