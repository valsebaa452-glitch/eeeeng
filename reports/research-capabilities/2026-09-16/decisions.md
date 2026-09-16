# Decisión de ampliación

Revisión del 2026-09-16 sobre la base
`a729cc0d3114aca5f7f14830ca04bc0819aeb38b`. El
[registro de fuentes y consumo](sources.md) delimita lo investigado: no se
afirma haber auditado todo internet ni encontrado ingresos garantizados.

## Componentes incorporados

| Componente | Aporte incremental y decisión |
| --- | --- |
| `market-sizing` | **Incorporada.** TAM/SAM/SOM con compradores únicos, unidades conciliadas y capacidad aplicada después de la conversión. Complementa demanda y economía unitaria. |
| `business-acquisition-due-diligence` | **Incorporada.** Filtra negocios existentes por evidencia, normalización financiera, transferibilidad y pasivos; sin acceder a documentos privados ni recomendar compras. |
| `public-procurement-screening` | **Incorporada.** Separa gasto histórico, avisos vigentes, adjudicaciones y elegibilidad jurisdiccional antes de tratar un registro como oportunidad. |
| `research-business-math` | **Incorporado y habilitado por proyecto.** MCP stdio de autoría local con cuatro cálculos deterministas y acotados: economía mensual, retención, mercado y puente de caja. Sin APIs externas ni nuevas dependencias. |

Las tres skills nuevas son originales del proyecto. La investigación sirvió
para identificar carencias; **no se copiaron las skills candidatas, sus scripts,
plugins ni instaladores**. Sus hashes y referencias se registran en
[`additional-skills.json`](../../../docs/provenance/additional-skills.json).
Las 27 raíces previas conservan sus bytes, licencias y atribuciones.

El MCP reutiliza `business_math.py` para economía y retención, añade
`research_math.py` para los dos cálculos nuevos y usa el SDK **mcp 1.30.0** ya
fijado. Su lanzador conserva el entorno aislado del proyecto, sin heredar
credenciales ni admitir comandos, rutas de archivos o URLs como argumentos.
Los importes deben pertenecer al mismo período y moneda. Ni el código ni el
formato monetario certifican la veracidad de las entradas.

La configuración añade un registro al final; no reemplaza los cuatro MCP
existentes ni crea overrides de Settings. Tampoco importa la biblioteca personal.

## Componentes no activados

| Candidato | Decisión y evidencia pendiente |
| --- | --- |
| World Bank Data360 MCP | **No activado: fallo funcional.** Inicializó y listó 15 herramientas, pero el único lookup devolvió `isError: true` por un 404 interno. No se atribuye el fallo a falta de credenciales; cuota y precio no quedaron cuantificados. Véase [prueba conservada](data360-probe.json). |
| Anthropic `skill-creator` | **No instalado.** Apache-2.0 del componente comprobada, pero sus automatizaciones dependen de scripts/CLI no auditados para Hoplite. Se documentó un protocolo manual sintético, sin importar ni ejecutar el optimizador. |
| K-Dense `market-research-reports` | **No instalado.** La raíz declara MIT y versión 1.3, distinta del extracto indexado; licencia íntegra y scripts no auditados. El alcance general se solapa con skills existentes. |
| Anthropic `dd-checklist` / plugin financiero | **No instalado.** Catálogo útil para identificar el hueco, pero no se auditó cada licencia/NOTICE ni sus conectores; no se incorporó el plugin. |
| `procurement-optimizer` y optimizadores similares | **No instalados.** Presuponen información interna y scripts no auditados; no encajan en una investigación exclusivamente pública/sintética. |
| MCP comunitarios USAspending | **Pendientes de auditoría; no instalados.** Descubiertos en extractos, sin revisión completa de código, licencias, versiones, permisos ni operación. |
| Más generadores genéricos de ideas o copy | **Redundantes para este encargo.** El catálogo inicial ya cubre descubrimiento, competencia, distribución, evaluación y economía unitaria. El recuento no es un criterio de calidad. |

## Qué está y qué no está demostrado

La [verificación técnica](verification.md) separa archivos, pruebas offline,
cliente MCP, herramientas nativas y aceptación en otro hilo. Los cálculos y
límites técnicos sí tienen pruebas reproducibles. Las seis fichas de
[`research-evaluation.json`](../../../examples/research-evaluation.json) son un
protocolo propuesto, **no resultados de un benchmark del modelo**. No se midió
una mejora estadística frente al catálogo anterior, ni se hicieron entrevistas,
ventas, ofertas, compras o campañas.

La selección es una ampliación práctica y acotada, no una certificación de «lo
mejor del mundo» ni de pericia infalible. La siguiente decisión comercial debe
depender de país, capital, tiempo, acceso a compradores y evidencia del problema,
no del número de herramientas instaladas.
