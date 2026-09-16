# Instalación del kit en este proyecto

Fecha de verificación: **2026-09-16**. Esta evidencia corresponde al repositorio
destino `valsebaa452-glitch/eeeeng`, no a una ejecución de la cuenta de origen.

## Integridad y alcance

- Se leyeron `LEEME-PRIMERO.md`, `PROMPT-PARA-HOPLITE.txt`, `AGENTS.md`, el
  manifiesto, la configuración y los scripts antes de ejecutarlos.
- El ZIP se extrajo en un directorio temporal nuevo, comprobando CRC y rechazando
  rutas absolutas, recorridos `..`, enlaces, archivos especiales y duplicados.
- SHA-256 del ZIP recibido:
  `ff0742b7450e6c299d5cae3d6d9eaf410eeb1529e9b65f3a70b80cc271b7a412`.
  No se adjuntó un checksum externo independiente: esta huella identifica el
  archivo recibido, pero no autentica a su editor.
- **72/72 archivos del paquete verificados**: tamaños y SHA-256 de los 71
  archivos inventariados, más reconstrucción y comprobación del manifiesto.
- Los archivos se instalaron directamente en la raíz, incluidas `.agents`,
  `.hoplite`, `.github` y la `.hoplite` anidada del runtime. No hubo colisiones
  ni sobrescrituras. Se conservaron los bytes del paquete y sus atribuciones.
- No se copiaron credenciales, sesiones, `.git`, dependencias de otra cuenta ni
  material de investigación anterior. Los adjuntos y entornos generados quedan
  excluidos de Git; solo se añadieron los informes públicos seleccionados de
  esta ejecución.
- El setup efectivo es `bash .hoplite/setup.sh`; no había un override y no se
  creó ninguno. La instalación del proyecto no importa la biblioteca personal.

## Inventario de skills: 27/27

Cada raíz existe en `.agents/skills/<nombre>/SKILL.md`, tiene nombre/frontmatter
válidos y coincide con el hash completo del
[`MANIFIESTO-PAQUETE.json`](../MANIFIESTO-PAQUETE.json). La revisión estática no
identificó referencias locales ausentes ni instrucciones maliciosas. Esto
verifica las instrucciones instaladas, no garantiza resultados comerciales ni
sustituye comprobar su carga nativa en un hilo nuevo.

| Skill | SHA-256 verificado |
| --- | --- |
| ab-test-setup | `2c8426cf24debfe84c7242680e5f59945b0507808e6a062b478c7f73a21a43c8` |
| ai-opportunity-validation | `89b08ac0209b7f9e8cd66c80d7260bdd96e7fa25bb73cc0a6dd41f2e50f6d443` |
| ai-service-evaluation | `46406705ca3fd3e3baf99933314d17b818372b192a0f5a4ef7ce0a9f083291ae` |
| analytics-tracking | `02bb5a9de086b69157f582e9a002d08778914d0aab88518a4620ec9358541d36` |
| cohort-analysis | `db4ea78b492610d8c95f793b4bc533cd24da481648e59824fa82aae6d5821d7f` |
| competitive-intelligence | `3b2e0655cb82711f4b7915240c357b8c44c6415d2b7385dcfc164cbaa79d9625` |
| competitor-alternatives | `1ecc8e26a359df8de4e17d45500446e494597190d71637636b9c04735518db18` |
| copywriting | `8cc4247fdd808a467992355ee49b647abc876172ee5401cc47918e9ff11b0370` |
| customer-discovery | `a348c3e0f2efbade550cd4f52762c0046cbd060468f377bcd7e49026ea7e437f` |
| deep-web-research | `8d4ba4494cf4b0f459c3da4018c043ffb8907cb14db68d146e1ebe06937bd44c` |
| distribution-validation | `f6112eee43b24f317f7de9b8f22f1afd62ff7ee64684da18aae2ba2e6686f734` |
| free-tool-strategy | `f3dc1539e65b8cd80b28c74c34baecd4fb99dc729b63c9f73a6878043ed5b093` |
| launch-strategy | `7fba53752a1a060f349b23e3e21a2e39fbe40b3c8741e6880d22f99512eb909b` |
| lead-research-assistant | `f33178ea59a26a6c0401cf615550a8b4f4e49dad9792db1769da35ee17f4c3b5` |
| market-customer-research | `271effe90edd7ff22493782e0b08637aa7db2b71d94db2348654cbf23ed13d82` |
| page-cro | `a77c31525dc0d39cd71cf6ba43309da4608d2782b684815e3fee7bee2820ba07` |
| pricing-strategy | `0606810ac098c53e258811936297f8f3b6415c8808670ed17d6a89c709bcc9e8` |
| product-manager-toolkit | `00908d49be45aaaa7d22eb9298fcad2aa543686905552c4bf42496cb9d1d5982` |
| public-data-analysis | `711992f7511b4719d5b1740cffa954505f6732317760af8f9b1d577d707ebc91` |
| research-team | `217908c6c5d6a7340c2a2f5d0b5b54121cc007ce4c77df0990bcdf7277ecc012` |
| scholarly-metadata | `486fa865259e04e867de05186465814ac3f49cd838a349026f96a6c2218b3fcb` |
| seo-audit | `2c3076c4dd33fae07b5512116cce6d3909eb4975911e89eb1c89ca548f44685a` |
| source-fact-checking | `d38cf39ff5bec2f3a6158502b8e4106ec11a5b4c5b7b69fbc4ed43381a0ea993` |
| tool-due-diligence | `5cc41182ee835fb1fb24e4d04d3b3a5c49f57babbb42099216e1a9c242a3a7cd` |
| trend-analysis | `7387ad2d904ba140c5062d854a322af2ce0c64b806f8694b8711d9d2936a2b0b` |
| unit-economics | `bec8e0fe40cb197e2f7a4124e2b7d99fcbf6fbdd35720ee86c85d824b97fdb89` |
| web-search-strategy | `4eaf4db817de9b6587067d9230f597b121bec1e2789c5b2affd131fdc123c1a5` |

## MCP: 4/4 configurados y funcionales

Los cuatro registros están habilitados en
[`.hoplite/settings.json`](../.hoplite/settings.json), sin secretos. No se
modificaron servidores guardados en Settings ni se afirma alcance global.

El cliente ejecutó una comprobación pública por servidor el
**2026-09-16 a las 06:38 UTC**. Se revisó su JSON completo, no solo el código HTTP:
[`mcp-client.json`](../reports/installation/mcp-client.json).

| MCP | Transporte | Inicialización y catálogo del cliente | Operación del cliente | Catálogo y operación nativos de este hilo |
| --- | --- | --- | --- | --- |
| research-fetch | stdio | Correctos, 1/1 herramienta | example.com extraído; URL privada rechazada | Correctos; texto esperado de example.com |
| research-arxiv | stdio | Correctos, 9/9 herramientas | Encontró Attention Is All You Need | Correctos; búsqueda limitada a 2 resultados, incluido 1706.03762 |
| research-context7 | HTTP | Correctos, 2/2 herramientas | Resolvió MCP Python SDK | Correctos; devolvió identificadores de biblioteca |
| research-firecrawl | HTTP | Correctos, 3/3 herramientas | Scrape de example.com en markdown | Correctos; cuerpo esperado, respuesta cacheada |

Se conserva el fallo nativo inicial de Fetch y arXiv:
`MCP bridge initialization failed: mcp.stdio_server.exited`. Ocurrió antes del
setup; después de preparar las dependencias, una nueva llamada nativa a cada
catálogo y una operación pública real funcionaron. No se cambió la configuración
para ocultarlo. **Estas comprobaciones corresponden al hilo de instalación;
todavía falta la aceptación nativa en un hilo nuevo desde la revisión publicada.**

Context7 resolvió «MCP Python SDK» y devolvió identificadores de biblioteca.
Firecrawl devolvió el cuerpo esperado de `https://example.com`, con
`cacheState: hit` y `creditsUsed: 1`; no se presenta como una captura nueva de la
página ni como una garantía de cuota gratuita. No se usó Parse ni se solicitaron
uploads, headers, acciones o cambios de proxy. Los filtros del cliente Python
no restringen automáticamente el transporte HTTP nativo.

## Entorno y verificación reproducible

Entorno observado: Python **3.12.3**, Node **24.19.0**, npm **11.17.0**, uv
**0.9.28**. Aunque la guía general dice Node ≥22.20, el `jsdom` del lockfile
exige `^22.22.2 || ^24.15.0 || >=26.0.0`. Para reproducir esta instalación,
utilizar Node 24.19.0; no se alteraron las dependencias para aceptar otro runtime.

El arranque administrado `sandbox_setup` fue rechazado antes de ejecutar el
script: `setup operation none`, `setup status ready`, `workspace status ready`.
Se informó a Hoplite; ese resultado no es un fallo del script ni acredita su
ejecución. Como alternativa, se ejecutó exactamente el script versionado mediante
shell, sin cambiar el setup ni los overrides.

```sh
bash .hoplite/setup.sh
python3 scripts/verify_toolkit.py
tools/hoplite-research/.venv/bin/python -m unittest discover -s tests -v
bash .hoplite/setup.sh
tools/hoplite-research/.venv/bin/python tools/hoplite-research/scripts/research_client.py check --live
python3 scripts/exportar_kit.py verify --directory .
```

| Comprobación ejecutada | Resultado |
| --- | --- |
| Setup, 06:37 UTC | Código 0; dependencias preparadas |
| Verificador del toolkit | Código 0; 26 skills originales + 1 adicional, 4 MCP |
| Suite offline | Código 0; **70/70 pruebas**, sin omisiones, 1,308 segundos |
| Segundo setup, 06:38 UTC | Código 0; idempotencia comprobada |
| Cliente MCP `check --live`, una ejecución | Código 0; 4/4 inicializados, catálogos coincidentes y operaciones reales correctas |
| Integridad posterior | Código 0; 72/72 archivos del paquete intactos |

Resultados reproducibles: [`checks.json`](../reports/installation/checks.json)
y [`unittest.txt`](../reports/installation/unittest.txt). Los logs completos
locales se conservan en
`.hoplite/artifacts/installation-verification/run-8xfXUcWA/`.
Se registraron la advertencia npm `Unknown env config "store-dir"` y un error
inicial al crear el directorio de captura; los logs del primer setup se
recuperaron íntegros sin repetirlo. Ninguno se convirtió artificialmente en
éxito: los seis comandos terminaron con código 0 y se comprobaron sus salidas.

El cliente conserva cada comprobación MCP en `.research/checks/`; no se deben
borrar fallos para presentar un resultado posterior como el único observado.
Su campo `native_discovery: not_checked` se mantiene: la evidencia nativa de la
tabla anterior procede de llamadas distintas del agente. Del mismo modo,
`live_mcp_checked: false` en el exportador solo describe su verificación offline.

## Biblioteca personal: autorización separada

El importador y sus dependencias instaladas quedan en `tools/personal-skills/`.
No se ejecutaron `onboard`, `--all`, `--replace` ni una importación autenticada.
Instalar dependencias o probar con un HOME temporal no modifica la biblioteca
personal remota ni acredita autorización de la cuenta de destino.

Se probaron los comandos reales `preparar` y `comprobar` con un **HOME temporal
nuevo y un entorno mínimo sin credenciales**: ambos terminaron con código 0,
con **27/27 skills en el catálogo local y hashes correctos**. Se desactivó la
telemetría; no se ejecutó `importar` ni se intentó autenticar una cuenta. El
resultado y sus límites están en `local_catalog_verification` de
[`checks.json`](../reports/installation/checks.json).

Si se desea esta importación, ejecutar en **la terminal privada del usuario**,
desde el kit completo y con una versión de Node compatible:

```sh
npm ci --prefix tools/personal-skills --ignore-scripts --no-audit --no-fund --engine-strict --registry=https://registry.npmjs.org
node tools/personal-skills/instalar.mjs preparar
node tools/personal-skills/instalar.mjs comprobar
node tools/personal-skills/instalar.mjs importar
```

Antes de autorizar el último paso, comprobar que el CLI corresponde a la cuenta
de destino. La [documentación oficial de autenticación](https://hoplite.sh/docs/cli)
indica una API key creada en **Settings → Workspace → API keys**: gestionarla
solo mediante el flujo oficial en el equipo privado, nunca en este chat o Git.
No reutilizar sesiones de otra cuenta ni usar `onboard` para resolver este paso.
Cancelar la confirmación o encontrar nombres existentes no equivale a importar
27 skills nuevas.

Comprobar después las 27 skills como ese usuario en **otro proyecto sin copias
locales**. Las skills personales no se aplican a automations y una copia del
repositorio con el mismo nombre tiene prioridad.

## Publicación, mantenimiento y comprobación en un hilo nuevo

El repositorio remoto no tenía commits ni ramas al iniciar la instalación. La
rama autorizada del hilo es `hoplite/heraia-d2a4ba5a`. No se debe crear o modificar
la rama base configurada por una vía que el broker no autorice, ni fusionar una
PR sin permiso del usuario.

Después de confirmar la publicación, crear un hilo de este proyecto seleccionando
**la revisión publicada que contiene el kit**, no una rama vacía. Si se desea
usar la rama base habitual, primero debe contener esta instalación mediante el
flujo autorizado. En el hilo nuevo, pedir:

> Verifica esta instalación sin volver a copiar el ZIP ni importar mi biblioteca
> personal. Espera a que termine el setup versionado del nuevo sandbox.
> Comprueba el SHA de la revisión y el setup efectivo; valida los 27 nombres y
> hashes del manifiesto y carga cada skill con `load_skill`. Descubre los cuatro
> MCP con las herramientas nativas de este nuevo run y realiza una operación
> pública acotada por servidor: Fetch sobre example.com; arXiv buscando
> Attention Is All You Need, máximo 2 resultados; Context7 resolviendo MCP Python
> SDK; Firecrawl Scrape de example.com en markdown. No uses Parse ni datos
> privados. Separa instalación, inicialización, catálogo y funcionamiento;
> conserva errores de autenticación, cuota o transporte sin eludirlos. No
> presentes una prueba del cliente Python como prueba de disponibilidad nativa.

Se conservaron `.github/workflows/{verify,maintenance}.yml` y
`.github/dependabot.yml`. El mantenimiento semanal requiere que estén en la
rama predeterminada, Actions/Dependabot habilitados y permiso de Actions para
crear PR (`contents: write`, `pull-requests: write`). No se ampliaron permisos
ni se activó una importación o sincronización personal desatendida. La presencia
de YAML no demuestra que una ejecución programada haya funcionado; revisar los
runs y sus informes en el repositorio destino antes de declararlo operativo.

Documentación oficial contrastada el 2026-09-16:
[skills](https://hoplite.sh/docs/agent/skills),
[MCP](https://hoplite.sh/docs/agent/mcp),
[CLI](https://hoplite.sh/docs/cli).
