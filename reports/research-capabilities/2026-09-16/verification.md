# Verificación de la ampliación

Fecha: **2026-09-16 UTC**. Base conservada:
`a729cc0d3114aca5f7f14830ca04bc0819aeb38b`. Este informe acompaña la ampliación
del repositorio `valsebaa452-glitch/eeeeng` en `hoplite/heraia-d2a4ba5a`.

**Resultado:** 30 skills verificadas, cinco MCP configurados y **99/99 pruebas
offline aprobadas**. En la ronda funcional del cliente pasaron **cuatro de cinco
servidores**: Firecrawl inicializó y listó herramientas, pero rechazó el acceso
anónimo para la petición. El MCP matemático nuevo también pasó sus cuatro
operaciones por las herramientas **nativas de Hoplite** en este hilo. No se
presenta la instalación como cinco servidores funcionales ni como una prueba de
calidad comercial del modelo.

## Integridad y preservación

- Se añadieron tres skills originales del proyecto: `market-sizing`,
  `business-acquisition-due-diligence` y `public-procurement-screening`.
- Las **27 raíces anteriores conservan sus bytes** y atribuciones. Los hashes
  de las tres nuevas se comprobaron contra `additional-skills.json`.
- Los **cuatro registros MCP anteriores siguen idénticos**; se añadió
  `research-business-math` al final, sin claves, overrides o importación personal.
- Se conservaron sin cambios los siete archivos existentes de dependencias,
  lockfiles y configuración npm verificados. El servidor nuevo reutiliza el SDK
  y entorno fijados; no instala paquetes externos adicionales.
- El verificador portátil reconstruyó **83 archivos** para el kit ampliado. Los
  tests comprueban rutas, carpetas ocultas, reproducibilidad y exclusión de
  secretos, adjuntos, dependencias, historial y reportes de investigación.
- El ZIP recibido y los informes originales de instalación no se reemplazaron.
  README y manifiesto actuales se regeneraron deliberadamente para reflejar la
  ampliación; no se reutilizó el checksum del ZIP inicial.

Preflight reproducible:
[`01-preflight.json`](verification-20260916T094322Z-4a525035/01-preflight.json).

El [control general posterior](verification-20260916T094322Z-4a525035/09-post-setup-protection.json)
conserva un código 1: detectó la ampliación deliberada de `sources.md` realizada
por el agente principal mientras se preparaban los informes, **antes del primer
setup**. Es un informe nuevo fuera del export, no una raíz original ni una
dependencia modificada por el setup. El
[contexto del control](verification-20260916T094322Z-4a525035/09b-protection-context.json)
se conserva por separado; no se reescribió el fallo ni se restauró el registro
para ocultar la diferencia. Las comprobaciones de las raíces, MCP, dependencias
e historial originales siguieron siendo correctas.

## Comandos y resultados locales

| Comprobación | Resultado observado |
| --- | --- |
| `python3 scripts/verify_toolkit.py` | 30 skills: 26 originales y cuatro adicionales; cinco MCP configurados. |
| `python3 scripts/exportar_kit.py verify` | 83 archivos del paquete ampliado verificados. No afirma pruebas MCP live ni importación personal. |
| `bash .hoplite/setup.sh` | Código 0; dependencias fijadas preparadas. |
| `tools/hoplite-research/.venv/bin/python -B -m unittest discover -s tests -v` | **99 tests, 3,994 s, OK; código 0.** |
| Segunda ejecución de `bash .hoplite/setup.sh` | Código 0; comprobación de idempotencia. |
| `research_client.py check --live` | **Código 1, `passed: false`**, por Firecrawl. No se borró ni sustituyó por una comprobación parcial exitosa. |

Logs: [primer setup](verification-20260916T094322Z-4a525035/05-setup-first.log),
[suite completa](verification-20260916T094322Z-4a525035/06-unittest-full.log),
[segundo setup](verification-20260916T094322Z-4a525035/07-setup-idempotence.log) y
[comandos/códigos](verification-20260916T094322Z-4a525035/commands.jsonl).

Las expectativas de inventario pasaron de 27/4 a 30/5 porque cambió el contrato
del paquete. No se retiraron las 70 regresiones previas: se añadieron 19 pruebas
de fórmulas, nueve del MCP y una del cliente local. Incluyen capacidad después
de conversión, moneda/período, decimales, valores no finitos, tipos estrictos,
campos desconocidos, entradas acotadas, retención ponderada, recuperación tras
errores y transporte stdio real. No hay un benchmark de rentabilidad ni del
razonamiento general del agente detrás de ese recuento.

La herramienta de plataforma `sandbox_setup` volvió a fallar antes de ejecutar
el script: `Workspace setup claim ... was blocked`, aun mostrando estado ready.
Se conserva esta limitación ya reportada. La vía alternativa ejecutó **el mismo
script versionado** por shell, no un setup diferente ni un override. Ambos setup
solo emitieron el aviso no bloqueante de npm sobre `store-dir`.

## Estado de los MCP

Ronda del cliente iniciada a las **09:46:02 UTC**:
[`mcp-client.json`](mcp-client.json).

| Servidor | Inicialización y catálogo | Operación del cliente | Evidencia nativa pertinente |
| --- | --- | --- | --- |
| `research-fetch` | Correctos, 1 herramienta | example.com y rechazo de URL privada correctos | La prueba nativa anterior se conserva como histórica; no se repitió para gastar cuota. |
| `research-arxiv` | Correctos, 9 herramientas | Búsqueda limitada encontró Attention Is All You Need | Prueba nativa anterior histórica. |
| `research-context7` | Correctos, 2 herramientas | Resolvió documentación del SDK MCP | Prueba nativa anterior histórica; resolver metadatos no garantiza ejemplos de una versión concreta. |
| `research-firecrawl` | Correctos, 3 herramientas | **Falló:** `Anonymous keyless access is unavailable for this request.` | El éxito nativo anterior no invalida el fallo actual; no se probó otro transporte para eludirlo. |
| `research-business-math` | Correctos, 4 herramientas | Los cuatro cálculos sintéticos coincidieron | **Catálogo completo y cuatro llamadas nativas correctas en este hilo.** |

**Firecrawl queda pendiente de autorización/disponibilidad funcional.** El
proveedor indica que hace falta una API key para esa petición; no se creó una
cuenta, compró un plan, copió una clave ni modificó el registro existente. El
mensaje no acredita el saldo ni permite concluir que se agotó una cuota concreta.
Si se decide autorizarlo, hacerlo mediante la configuración segura de MCP de
Hoplite, nunca pegando secretos en el chat o Git. El cliente portátil conserva
deliberadamente su modo sin credenciales. No hubo reintentos tras el fallo.

La evidencia del nuevo MCP se conserva en
[`native-check.json`](native-check.json): mercado sintético de
1.200.000/240.000/12.000 USD, puente de EBITDA/caja de 75.000/20.000 USD,
economía mensual de 1.000 de facturación y 390 antes de impuestos, y retención
observada ponderada de 9/15 = 0,6. La fila no observada permanece `null`.
Son resultados de **entradas sintéticas**, no ingresos obtenidos o previstos.

**Data360 no se configuró:** su único lookup falló con `isError: true` y 404
interno después de inicializar y listar 15 herramientas. Los dos intentos
técnicos y el fallo local inicial están diferenciados en
[`data360-probe.json`](data360-probe.json). No se consumió más cuota intentando
otros endpoints o herramientas.

## Presupuesto y aceptación pendiente

El descubrimiento quedó en **12 búsquedas y 22 llamadas de lectura sobre 20
URLs**, incluidas continuaciones y dos accesos bloqueados. Firecrawl informó dos
créditos por la única búsqueda de esa fase. Las pruebas técnicas están separadas
en el [registro de consumo](sources.md); no hubo una segunda exploración amplia.
El saldo global y coste total de Hoplite/Exa/proveedores no son observables.

Las tres skills nuevas se cargaron con `load_skill` en este hilo. Sigue pendiente
la **aceptación nativa en un hilo nuevo desde la revisión publicada**: comprobar
la rama/SHA, setup efectivo, 30 raíces y cinco registros, y ejecutar los cálculos
locales. No reintentar Firecrawl mientras siga pendiente su autorización. La
[guía de instalación](../../../docs/installation-verification.md) incluye un
prompt completo; la [guía de uso](../../../docs/business-research-guide.md)
permite empezar una investigación acotada cuando se definan país y restricciones.

No se importó la biblioteca personal ni se alteraron permisos de mantenimiento.
La CI versionada ejecuta setup, pruebas offline, idempotencia y exportación; un
resultado verde de CI **no** demostraría acceso actual a Firecrawl ni aceptación
en otro hilo. Consultar el run de la revisión publicada por separado.
