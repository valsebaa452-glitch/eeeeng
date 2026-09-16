# Investigar oportunidades de negocio con este kit

El objetivo es descartar malas oportunidades pronto y encontrar hipótesis que
merezcan una prueba barata. No asegurar ingresos, demostrar que no existe
competencia ni sustituir conocimiento local, ventas o asesoramiento profesional.

## Recorrido recomendado

1. **Definir restricciones.** País y jurisdicción, capital máximo, pérdida
   tolerable, horas, habilidades y acceso a compradores. No deducirlos del idioma
   ni inventarlos. Si faltan, separar escenarios de recomendaciones personales.
2. **Buscar problemas con compradores.** Usar `market-customer-research`,
   `customer-discovery` y `ai-opportunity-validation` para identificar quién paga,
   su alternativa actual, urgencia y compras documentadas. Un precio publicado,
   testimonio, vacante o estadística sectorial no demuestra una venta propia.
3. **Contrastar alternativas.** `competitive-intelligence` y
   `source-fact-checking`: competidores directos, sustitutos, costes de cambiar,
   fuentes originales y contraevidencia. Poca oferta también puede indicar poca
   demanda, regulación o distribución difícil.
4. **Acotar mercado y acceso.** `market-sizing` reconcilia unidades, fechas y
   compradores únicos. `distribution-validation` comprueba cómo llegar a ellos.
   TAM no es facturación prevista; una audiencia no equivale a clientes.
5. **Modelar números completos.** `unit-economics`, `pricing-strategy` y
   `cohort-analysis`: API, entrega, soporte, tiempo humano, adquisición,
   devoluciones, impuestos y capital de trabajo cuando corresponda. Distinguir
   ingreso, beneficio, remuneración del dueño y caja. Mostrar sensibilidad.
6. **Aplicar filtros específicos.** `business-acquisition-due-diligence` para
   negocios existentes; `public-procurement-screening` para compradores públicos.
   Un anuncio de venta no acredita beneficios y una adjudicación ajena no es
   una oportunidad abierta. Elegibilidad desconocida sigue siendo pendiente.
7. **Proponer una prueba.** Entregar criterio de éxito, coste y condición de
   parada. Contactos, ventas, campañas, registros y pagos necesitan autorización
   específica. No ejecutarlos durante la investigación documental.

## Qué aporta cada MCP

| Servidor | Uso y límite |
| --- | --- |
| `research-fetch` | Leer texto público acotado y respetar las restricciones de acceso. No sustituye la comprobación de la fuente. |
| `research-arxiv` | Contrastar capacidades y límites técnicos en publicaciones. Un artículo o sus citas no demuestra demanda comercial. |
| `research-context7` | Comprobar documentación de implementaciones y versiones. Verificar que el resultado corresponda a la versión instalada. |
| `research-firecrawl` | Search/Scrape públicos con límites explícitos. Sin Parse, uploads, headers, acciones o proxies; el transporte nativo no hereda los filtros Python. |
| `research-business-math` | Cuatro cálculos locales sobre datos públicos o sintéticos. No usa APIs externas ni valida la veracidad de las entradas. |

El MCP matemático expone:

- `monthly_economics`: resultado mensual antes de impuestos, horas humanas y
  umbral de equilibrio condicionado. Reutiliza el calculador existente; no
  modela contratos ni convierte un mes rentable en ingreso recurrente.
- `cohort_retention`: retención ponderada por denominadores observados, hasta
  128 filas. `null` significa no observado, no abandono.
- `market_size`: TAM/SAM y SOM de escenario, con capacidad aplicada después de
  la conversión supuesta. No identifica automáticamente solapes entre fuentes.
- `acquisition_cash_bridge`: EBITDA normalizado y caja tras los costes
  enumerados. No es valoración, auditoría ni previsión de financiación.

Las entradas rechazan campos desconocidos, valores no finitos y tamaños fuera
de límites. Las dos herramientas nuevas declaran moneda y período; todos los
importes deben ser comparables. Sus importes monetarios de salida son cadenas
decimales con dos cifras; las herramientas heredadas conservan su formato.

Los ejemplos en [`examples/research-math.json`](../examples/research-math.json)
son **sintéticos**: mercado de 1.200.000, SAM de 240.000 y SOM condicionado de
12.000 USD por 12 meses; EBITDA normalizado de 75.000 y caja de 20.000 USD.
No describen un negocio ni ingresos obtenidos. Para comprobarlos localmente:

```sh
tools/hoplite-research/.venv/bin/python tools/hoplite-research/scripts/research_client.py check --server business-math
```

## Presupuesto y evidencia

Antes de consultar, fijar búsquedas, lecturas, resultados por búsqueda y un
presupuesto separado para pruebas técnicas. Contar también el trabajo delegado.
Reutilizar fuentes ya leídas; no repetir la investigación solo para aumentar el
recuento. Registrar créditos cuando el proveedor los exponga, sin asumir que el
saldo total o el coste del modelo son visibles. El cálculo local evita cuota de
APIs externas, no vuelve gratuito el trabajo del agente.

Ante 401/403/429 o un bloqueo, registrar el fallo y parar ese proveedor. No cambiar
identidad, endpoint ni plan para eludirlo. HTTP 200 con error interno es un fallo.
Usar solo información pública o sintética y no recopilar contactos personales.

Cada afirmación decisiva necesita fecha, URL, contexto y límite. Separar hechos,
inferencias y supuestos. Un registro MCP no certifica seguridad; instalar más
herramientas no prueba mejores resultados.

## Petición lista para adaptar

> Compara hasta tres oportunidades legales para [país], con [capital máximo],
> [horas por semana] y [habilidades/acceso a compradores]. Si faltan esos datos,
> explica qué decisión impiden antes de asumirlos. Presupuesto: hasta seis
> búsquedas y doce lecturas públicas, contando subagentes, sin pruebas externas
> adicionales salvo necesidad justificada dentro del límite. No contactes,
> compres ni crees cuentas. Para cada opción, identifica comprador, problema,
> evidencia de compras y sus límites, competidores y sustitutos, distribución,
> economía unitaria con tiempo humano, riesgos y un dato que la refutaría.
> Verifica aritmética con research-business-math. Entrega una tabla comparativa,
> fuentes fechadas, consumo observado y una prueba pequeña pendiente de mi
> autorización. No confundas baja competencia con demanda ni prometas ingresos.

## Evaluar las instrucciones sin fingir resultados

[`examples/research-evaluation.json`](../examples/research-evaluation.json)
contiene seis casos sintéticos para revisión manual de citas, incertidumbre,
aritmética, elegibilidad, límites de acceso e instrucciones maliciosas. Su
presencia no significa que se haya evaluado al modelo. Comparar con/sin la
ampliación requiere un ensayo separado, mismo corpus y presupuesto, revisión
humana y un denominador explícito; no se ejecuta automáticamente para consumir
cuota ni se convierte una puntuación en garantía de rentabilidad.
