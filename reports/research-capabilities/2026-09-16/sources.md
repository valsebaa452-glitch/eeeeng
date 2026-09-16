# Registro de investigación y límites

Consulta: **2026-09-16 UTC**. Este registro distingue lecturas directas,
extractos de buscadores y pruebas del protocolo. Una fuente accesible o un
catálogo no constituyen certificación de calidad ni evidencia de ingresos.

## Presupuesto de descubrimiento utilizado

- **12 búsquedas:** nueve Exa, una Firecrawl, una búsqueda arXiv y una consulta
  Context7. No se solicitaron páginas adicionales de resultados.
- **20 URLs de lectura directa intentadas:** 18 legibles y dos bloqueadas.
  Dos lecturas se continuaron desde el offset anunciado: **22 llamadas de
  lectura**, dentro del límite de 24. El abstract de arXiv se cuenta como una
  lectura, no como lectura del artículo completo.
- Firecrawl informó **2 créditos** por una búsqueda limitada a tres resultados.
  No se ejecutaron más búsquedas Firecrawl, Parse, uploads, acciones o proxies.
- Context7 devolvió extractos, no páginas completas. Las solicitudes internas
  de los proveedores, el saldo y el coste total de Hoplite/Exa no son observables;
  estos límites son de acciones del agente, no una garantía de facturación.
- Las pruebas técnicas MCP se conservan aparte, con sus límites e incidentes.
  No se contrataron planes ni se reutilizaron credenciales de otra cuenta.

## Consultas exactas

| ID | Herramienta | Consulta | Límite |
| --- | --- | --- | --- |
| Q1 | Exa | `site:github.com/anthropics/financial-services-plugins "due-diligence" skills` | 4 resultados |
| Q2 | Exa | `site:github.com/anthropics/skills "skill-creator" "license" evals` | 4 |
| Q3 | Exa | `site:github.com/K-Dense-AI "market-research-reports" "SKILL.md"` | 4 |
| Q4 | Exa | `site:github.com skills "procurement" "SKILL.md" "license"` | 4 |
| Q5 | Exa | `site.ftc.gov business opportunity earnings claims guaranteed income AI scams Business Opportunity Rule` | 4 |
| Q6 | Exa | `site:sba.gov "Market research and competitive analysis" OR "Buy an existing business or franchise"` | 4 |
| Q7 | Exa | `site:sba.gov federal contracting basic requirements SAM eligible small businesses contract opportunities` | 4 |
| Q8 | Exa | `site:openai.com BrowseComp deep research benchmark limitations evaluation cost accuracy` | 4 |
| Q9 | Firecrawl Search | `official MCP server business market research financial datasets World Bank public data pricing open source` | 3 |
| Q10 | Exa | `MCP server World Bank USASpending public data official API financial business research license` | 5 |
| Q11 | arXiv `search_papers` | `ti:"BrowseComp" OR ti:"GAIA" OR ti:"WebWalker"` | 3; abstracts en snippet |
| Q12 | Context7 `query-docs` | `MCP Python SDK v1.30 FastMCP stdio server read-only tool input schemas lifespan httpx client errors and structured outputs; avoid v2-only APIs` | Una llamada; biblioteca `/websites/py_sdk_modelcontextprotocol_io` |

Q1–Q4 se realizaron entre 09:04:56 y 09:05:31 UTC. Para las demás consultas,
la evidencia disponible aquí identifica el día, no una hora individual exacta.
Q5 contiene `site.ftc.gov` tal como se ejecutó; no se presenta como un filtro
`site:` válido. No se gastó otra consulta solo para corregirlo.

## Fuentes leídas o intentadas

Las fechas editoriales no observadas se mantienen como desconocidas. Las ramas
`main`/`dev` siguientes son referencias de investigación mutables: **no se
instaló código desde ellas ni se presentan como versiones fijadas**.

| ID | Fuente primaria | Evidencia pertinente y límite |
| --- | --- | --- |
| A1 | [Anthropic skill-creator](https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md) | Lectura directa, 09:05:31.878 UTC. Evaluación de activación y comparación con/sin skill; presupone scripts y CLI de Claude que no se auditaron ni ejecutaron. |
| A2 | [Licencia específica skill-creator](https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/LICENSE.txt) | Lectura directa, 09:05:48.467 UTC: Apache-2.0, copyright Anthropic 2026. No demuestra compatibilidad de sus automatizaciones. |
| A3 | [K-Dense market-research-reports](https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/skills/market-research-reports/SKILL.md) | Lectura directa, 09:05:48.520 UTC: versión declarada 1.3, reconciliación de mercados. MIT declarada; licencia completa y scripts no auditados. No se copiaron. |
| A4 | [Anthropic financial-services](https://raw.githubusercontent.com/anthropics/financial-services/main/README.md) | Lectura directa, 09:05:48.556 UTC. Catálogo de plugins y conectores; Apache-2.0 declarada por el README, sin verificar todos los NOTICE ni proveedores. |
| A5 | [procurement-optimizer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/business-operations/skills/procurement-optimizer/SKILL.md) | Lectura directa, 09:06:06.692 UTC. Autor/versión declarados: claude-code-skills, 2.8.0; MIT declarada, no completa. Presupone datos internos y tres scripts no revisados. Cifras heurísticas no verificadas. |
| A6 | [Anthropic dd-checklist](https://raw.githubusercontent.com/anthropics/financial-services/main/plugins/vertical-plugins/private-equity/skills/dd-checklist/SKILL.md) | Lectura directa, 09:06:06.802 UTC. Cobertura financiera, contractual y operativa; no se importaron el plugin, documentos privados ni conectores. Sin commit inmutable observado. |
| B1 | [SBA: Plan your business](https://www.sba.gov/counseling/plan-your-business/#market-research) | Lectura directa de planificación, adquisiciones y franquicias. Orientación estadounidense, no prueba de ventas ni respaldo de un negocio. |
| B2 | [SBA: Get started with contracting](https://www.sba.gov/counseling/get-started/#basic-requirements) | Lectura directa de elegibilidad y requisitos. No extrapolar a otra jurisdicción o convocatoria. |
| B3 | [MCP Registry FAQ](https://modelcontextprotocol.io/registry/faq) | Lectura directa: registro de metadatos versionados, no auditoría de ejecución. |
| B4 | [MCP Registry Moderation Policy](https://modelcontextprotocol.io/registry/moderation-policy) | Lectura directa: moderación mínima; estar listado no prueba seguridad, singularidad o calidad. |
| B5 | [FTC: business opportunity sellers](https://www.ftc.gov/business-guidance/blog/2023/08/business-opportunity-sellers-ftc-says-ai-stands-allegedly-inaccurate) | Apertura bloqueada por automatización. **Solo extracto indexado**, fechado 2023-08-22 según el índice; no se afirma una sentencia ni estado procesal actual. No se eludió el bloqueo. |
| B6 | [OpenAI: BrowseComp](https://openai.com/index/browsecomp/) | Apertura bloqueada por desafío Cloudflare. **Solo extracto indexado**, fechado 2025-04-10 según el índice. No se eludió el bloqueo. |
| P1 | [World Bank Data360 MCP](https://worldbank.github.io/data360-mcp/) | Lectura directa completa en dos tramos. Endpoint externo, herramientas, cuotas no cuantificadas, posible autorización y Charts API opcional. Recursos/prompts remotos no se elevan a instrucciones del sistema. |
| P2 | [Página solicitada de términos de datasets](https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets) | Lectura directa en dos tramos. El contenido entregado describió términos generales del sitio y remitió a términos específicos de datasets. **No acredita una licencia comercial universal**; no se asumió CC-BY para todas las series. |
| P3 | [Data360 README](https://raw.githubusercontent.com/worldbank/data360-mcp/dev/README.md) | Lectura directa: instalación documentada 0.1.3, MIT + World Bank IGO Rider, controles de datos y automatizaciones opcionales. No se instalaron paquetes o agentes del repositorio. |
| P4 | [USAspending API documentation](https://api.usaspending.gov/docs/) | Lectura directa del índice oficial. No es una prueba funcional de un MCP comunitario. |
| P5 | [BrowseComp, arXiv 2504.12516](https://arxiv.org/abs/2504.12516) | Abstract obtenido con `get_abstract`, publicado 2025-04-16; se reconoce que respuestas cortas verificables no representan toda la distribución de consultas reales. No se leyó el PDF ni se ejecutó el benchmark. |
| P6 | [USAspending introductory tutorial](https://api.usaspending.gov/docs/intro-tutorial) | Lectura directa de GET/POST, campos y filtros. Adjudicaciones, subvenciones y préstamos son categorías distintas; no equivalen a beneficio del usuario. |
| P7 | [Data360 LICENSE](https://raw.githubusercontent.com/worldbank/data360-mcp/dev/LICENSE) | Lectura directa de MIT y cláusula IGO. Licencia del software, no permiso general para redistribuir datasets. |
| P8 | [Data360 WB-IGO-RIDER.md](https://raw.githubusercontent.com/worldbank/data360-mcp/dev/WB-IGO-RIDER.md) | Lectura directa del rider/resumen incluido; remite a otro texto canónico no abierto. No se redistribuyó software World Bank ni se afirmó relación o respaldo. |

## Extractos, contradicciones y ausencia de corroboración

- Q12 devolvió ejemplos con `MCPServer`/`Client`, no adecuados para asumir el
  contrato del SDK 1.30 instalado. El transporte funcionó, pero **la selección de
  versión fue insuficiente**. Se usará el SDK fijado y pruebas locales, no esos
  ejemplos ni una actualización de dependencia para hacerlos encajar.
- El índice describía K-Dense 1.2; la raíz leída decía 1.3. También aparecieron
  rutas antiguas de Anthropic. No se convirtió un resultado de buscador en un pin.
- Firecrawl y Exa devolvieron la misma documentación Data360: es **una fuente**,
  no corroboración independiente. README, sitio y licencia comparten mantenedor.
- BrowseComp en la página de OpenAI y en arXiv es el mismo trabajo del proveedor.
  El abstract público se obtuvo en el carril académico; no se superó el desafío
  del sitio de OpenAI. No acredita ingresos ni precisión de este kit.
- Los repositorios [asachs01/usaspending-mcp](https://github.com/asachs01/usaspending-mcp),
  [haydentbs/usaspending-mcp-server](https://github.com/haydentbs/usaspending-mcp-server)
  y [thsmale/usa-spending-mcp-server](https://github.com/thsmale/usa-spending-mcp-server)
  se descubrieron mediante extractos. Sus licencias, dependencias, versiones y
  código completo **no** fueron auditados. No se instalaron ni se llamaron.
- Los otros optimizadores de compras y artículos de rankings encontrados no
  sustentan afirmaciones de instalación, seguridad o rendimiento.

La exploración cubrió fuentes primarias seleccionadas de skills, herramientas,
datos y criterios empresariales. No cubrió todos los países, sectores, catálogos,
proveedores o modelos de negocio de internet.

## Pruebas técnicas posteriores al descubrimiento

- **Data360:** dos inicializaciones en total. El primer intento quedó detenido
  por un guard local que rechazaba una cookie recibida; se corrigió descartando
  cookies, sin añadir credenciales ni eludir una limitación del proveedor. El
  segundo completó el catálogo y un único lookup público, que falló con un 404
  interno y `isError: true`. Total observado: cinco POST MCP, incluida una sola
  llamada funcional. Se detuvo sin más reintentos ni endpoints alternativos.
  [Evidencia saneada](data360-probe.json). Versión del servidor alojado observada:
  0.1.0; la release 0.1.3 citada por la documentación no se presume desplegada.
- **MCP matemático:** catálogo nativo y cuatro operaciones sintéticas locales
  comprobadas; cero llamadas a APIs externas para esos cálculos. Las tres skills
  nuevas también se cargaron con `load_skill` en este hilo.
  [Evidencia nativa](native-check.json). No acredita un nuevo sandbox.
- **Regresión de los cuatro MCP existentes:** una ronda acotada del cliente,
  separada del presupuesto de descubrimiento y documentada en el
  [informe técnico](verification.md). No se reabrió la búsqueda amplia.

Las dependencias fijadas se preparan mediante setup; esas descargas técnicas no
son búsquedas comerciales. No se conoce el saldo total de las cuentas ni se
garantiza un importe facturado. No hubo compras ni autorización de planes nuevos.
