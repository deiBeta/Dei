# Email corporativo: info@almasana.com

Guía paso a paso para poner en marcha `info@almasana.com`.
Los pasos con 💳 son los que **requieren pago**.

## Resumen

| Paso | Qué es | ¿Pago? | Coste aproximado* |
|------|--------|--------|-------------------|
| 1 | Comprobar y registrar el dominio `almasana.com` | 💳 Sí | 10–15 €/año |
| 2 | Contratar un proveedor de correo | 💳 Sí (o gratis con Zoho) | 0–8 €/usuario/mes |
| 3 | Verificar el dominio en el proveedor | No | — |
| 4 | Crear el buzón `info@` | No | — |
| 5 | Configurar DNS (MX, SPF, DKIM, DMARC) | No | — |
| 6 | Probar envío y recepción | No | — |

\* Precios orientativos de 2026; confirma el precio final en la web de cada proveedor antes de pagar.

---

## Paso 1 — Dominio `almasana.com` 💳

1. Comprueba si está libre en un registrador: Cloudflare Registrar (precio de coste),
   Namecheap, Porkbun o, si prefieres uno español, DonDominio / Dinahosting.
2. **Si está libre:** regístralo (≈10–15 €/año). Activa la renovación automática y la
   protección WHOIS (privacidad), que suele ser gratuita.
3. **Si ya está ocupado:** o lo tienes tú ya (busca el registrador en tus emails/facturas),
   o pertenece a otra persona. En ese caso, alternativas: `almasana.es`, `almasana.co`,
   `almasanaoficial.com`, `holaalmasana.com`… (el resto de la guía es igual cambiando el dominio).

> ⚠️ **Aquí hay que pagar.** No tengo acceso para registrar dominios ni introducir datos de pago:
> este paso lo tienes que hacer tú.

## Paso 2 — Proveedor de correo 💳

| Proveedor | Plan recomendado | Precio aprox. | Para quién |
|-----------|------------------|---------------|------------|
| **Google Workspace** | Business Starter | ≈7–8 €/usuario/mes | Si usas Gmail, Drive, Meet. La opción más cómoda. |
| **Microsoft 365** | Business Basic | ≈5–6 €/usuario/mes | Si usas Outlook, Word, Excel, Teams. |
| **Zoho Mail** | Forever Free / Mail Lite | Gratis (hasta 5 usuarios) / ≈1 €/usuario/mes | Presupuesto mínimo. |

**Recomendación:** si solo necesitas `info@`, contrata **1 usuario** y, si más adelante quieres
`hola@`, `pedidos@`, etc., créalos como **alias** (gratis) del mismo buzón en lugar de pagar usuarios extra.

> ⚠️ **Aquí hay que pagar** (salvo con el plan gratuito de Zoho). Alta:
> - Google: https://workspace.google.com/
> - Microsoft: https://www.microsoft.com/microsoft-365/business
> - Zoho: https://www.zoho.com/mail/

## Paso 3 — Verificar el dominio

Durante el alta, el proveedor te pedirá demostrar que el dominio es tuyo añadiendo un registro
**TXT** en el DNS (en el panel de tu registrador). Copia el valor exacto que te dé y añádelo
(ver `dns-records.md`). La verificación tarda de minutos a unas horas.

## Paso 4 — Crear el buzón

- Usuario: `info`
- Nombre visible: `Almasana`
- Dirección resultante: **info@almasana.com**
- Contraseña fuerte + **verificación en dos pasos (2FA) activada** desde el primer día.

## Paso 5 — Registros DNS

Ver [`dns-records.md`](dns-records.md): contiene los registros exactos para cada proveedor.
Sin MX el correo no llega; sin SPF/DKIM/DMARC tus emails acabarán en spam.

## Paso 6 — Comprobaciones

1. Envía un correo desde un Gmail/Hotmail personal a `info@almasana.com` → debe llegar.
2. Responde desde `info@` → debe llegar a la bandeja de entrada (no a spam).
3. Pasa el test de https://www.mail-tester.com/ (objetivo: 9/10 o más).
4. Configura el correo en el móvil (app de Gmail / Outlook / Zoho Mail).

## Extras recomendados

- **Firma corporativa** — plantilla en [`firma.html`](firma.html).
- **Respuesta automática** fuera de horario.
- **Copia de seguridad / reenvío**: no reenvíes todo a un correo personal; mejor da acceso
  delegado a quien lo gestione.
