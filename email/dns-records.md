# Registros DNS para almasana.com

Añádelos en el panel DNS de tu registrador (o de Cloudflare si gestionas allí el DNS).
`@` significa el dominio raíz (`almasana.com`). Usa **solo la sección de tu proveedor**.
Borra antes cualquier registro MX antiguo que el registrador haya creado por defecto.

---

## Opción A — Google Workspace

| Tipo | Nombre | Valor | Prioridad |
|------|--------|-------|-----------|
| TXT | @ | `google-site-verification=XXXXXXXX` *(te lo da Google)* | — |
| MX | @ | `smtp.google.com` | 1 |
| TXT | @ | `v=spf1 include:_spf.google.com ~all` | — |
| TXT | google._domainkey | `v=DKIM1; k=rsa; p=XXXXXXXX` *(Admin → Apps → Gmail → Autenticar correo)* | — |
| TXT | _dmarc | `v=DMARC1; p=none; rua=mailto:info@almasana.com` | — |

## Opción B — Microsoft 365

| Tipo | Nombre | Valor | Prioridad |
|------|--------|-------|-----------|
| TXT | @ | `MS=msXXXXXXXX` *(te lo da Microsoft)* | — |
| MX | @ | `almasana-com.mail.protection.outlook.com` *(confírmalo en el asistente)* | 0 |
| TXT | @ | `v=spf1 include:spf.protection.outlook.com -all` | — |
| CNAME | autodiscover | `autodiscover.outlook.com` | — |
| CNAME | selector1._domainkey | *(valor que indica Microsoft Defender → DKIM)* | — |
| CNAME | selector2._domainkey | *(valor que indica Microsoft Defender → DKIM)* | — |
| TXT | _dmarc | `v=DMARC1; p=none; rua=mailto:info@almasana.com` | — |

## Opción C — Zoho Mail (región EU)

| Tipo | Nombre | Valor | Prioridad |
|------|--------|-------|-----------|
| TXT | @ | `zoho-verification=zbXXXXXXXX.zmverify.zoho.eu` *(te lo da Zoho)* | — |
| MX | @ | `mx.zoho.eu` | 10 |
| MX | @ | `mx2.zoho.eu` | 20 |
| MX | @ | `mx3.zoho.eu` | 50 |
| TXT | @ | `v=spf1 include:zoho.eu ~all` | — |
| TXT | zmail._domainkey | `v=DKIM1; k=rsa; p=XXXXXXXX` *(Zoho → Admin → Dominios → DKIM)* | — |
| TXT | _dmarc | `v=DMARC1; p=none; rua=mailto:info@almasana.com` | — |

> Si tu cuenta Zoho es de la región global (zoho.com) en vez de la UE, cambia `zoho.eu` por `zoho.com`.

---

## Notas

- **Solo un registro SPF** por dominio. Si ya existe uno, combina los `include:` en una sola línea.
- **DMARC:** empieza con `p=none` y, tras 2–4 semanas sin problemas, sube a `p=quarantine`.
- Los cambios DNS tardan de minutos a 24–48 h en propagarse.
- Comprobar: https://mxtoolbox.com/SuperTool.aspx?action=mx%3aalmasana.com
