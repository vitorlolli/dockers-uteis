## Configuração para proxy reverso

Substituir no wp-config.php

```
if (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && strpos($_SERVER['HTTP_X_FORWARDED_PROTO'], 'https') !== false) {
     $_SERVER['HTTPS'] = 'on';
}
```
por
`` $_SERVER['HTTPS'] = 'on'; ``