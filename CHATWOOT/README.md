# CHATWOOT

## Deploy
- `docker compose run --rm rails bundle exec rails db:chatwoot_prepare`
- `docker compose up -d`

## Cadastrar Caixa de entrada para integração do evolution API
```
curl --request POST \
  --url ${evolution_api_url}/instance/create \
  --header 'Content-Type: application/json' \
  --header 'apiKey: ${evolution_api_api_key}' \
  --data '{
	"instanceName": ${inbox_name},
	"token": "tokensecreto",
	"qrcode": true,
	"chatwoot_account_id": ${chatwoot_account_id},
	"chatwoot_token": ${chatwoot_access_token},
	"chatwoot_url": ${chatwoot_url},
	"chatwoot_sign_msg": true,
	"chatwoot_reopen_conversation": false,
	"chatwoot_conversation_pending": false
}'
```

## TODO
- [ ] Criar os volumes para o evolution API