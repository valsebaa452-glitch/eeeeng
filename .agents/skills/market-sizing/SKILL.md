---
name: market-sizing
description: Dimensiona mercados con estimaciones bottom-up, reconciliación de fuentes y límites reales de acceso y capacidad; no confunde TAM con ventas previstas.
---

# Dimensionamiento de mercado verificable

Úsala para comparar el tamaño y la accesibilidad de un mercado de servicios,
productos digitales o negocios presenciales. No sustituye validar compradores ni
estimar márgenes con `unit-economics`.

## Definir antes de calcular

Registra país/jurisdicción, comprador y unidad de compra, segmento, moneda,
período, precio/base de gasto y fecha de cada fuente. Si faltan, utiliza escenarios
explícitos o pide el dato que cambie la decisión; no inventes el perfil del usuario.
Clasifica cada entrada como dato público, supuesto o dato sintético.

1. **TAM:** compradores únicos del segmento × gasto por comprador en el mismo
   período. Una población, una audiencia web o el PIB no equivalen a compradores.
2. **SAM:** restringe a quienes pueden recibir y comprar la oferta: geografía,
   elegibilidad, idioma, canal y requisitos técnicos. Justifica cada exclusión.
3. **SOM de escenario:** `min(compradores alcanzables × conversión supuesta,
   capacidad de atender clientes) × gasto por comprador`. Aplica la capacidad
   después de la conversión; no multipliques una capacidad ya limitada otra vez
   por esa tasa. Compradores alcanzables ≤ atendibles ≤ totales.
4. Construye escenarios bajo/base/alto variando los supuestos inciertos. No
   presentes el escenario central como ingreso esperado, probabilidad de éxito
   ni compromiso de compra.

## Reconciliar, no promediar cifras incompatibles

- Contrasta una estimación bottom-up con otra fuente o método independiente.
  Dos páginas que repiten el mismo informe cuentan como un origen.
- Revisa compradores duplicados, segmentos superpuestos y unidades distintas
  antes de sumar. Tener etiquetas distintas no demuestra exclusión mutua.
- No mezcles stock con flujo, facturación con volumen transado, población con
  empresas, gasto de toda una categoría con gasto en esta oferta, ni cifras
  anuales con mensuales. Explicita inflación, tipo de cambio y año base cuando
  sean pertinentes; si no puedes conciliarlos, informa rangos no comparables.
- Los datos oficiales describen contexto y cobertura, no voluntad de pago.
  Revisa definición, desagregación, última observación, faltantes y licencia de
  cada serie. No redistribuyas datos comercialmente por presumir que son abiertos.
- Busca sustitutos, compras anteriores y razones de escasa oferta. Pocos
  competidores pueden significar demanda insuficiente o barreras, no una ventaja.

## Entrega y siguiente prueba

Entrega una tabla de entradas con valor, unidad, fecha, URL, categoría de evidencia
y límite; los cálculos reproducibles de TAM/SAM/SOM; diferencias entre fuentes;
supuestos que dominan el resultado; y qué dato invalidaría la oportunidad.
Si está disponible, utiliza `market_size` del MCP `research-business-math` para
comprobar la aritmética; si no, reproduce las fórmulas localmente. El cálculo no
certifica que las entradas sean ciertas ni detecta por sí solo todos los solapes.

Cierra con una prueba pequeña de demanda que requiera autorización antes de
contactar, vender, gastar o publicar. No recomiendes construir por el tamaño del
TAM ni afirmes ingresos seguros o novedad mundial.

## Procedencia y alcance

Instrucciones originales de este proyecto, revisadas el 2026-09-16; no incorporan
scripts ni texto de skills de terceros. Referencias públicas: [SBA, investigación
y planificación](https://www.sba.gov/counseling/plan-your-business/#market-research)
y [Data360, definiciones y cobertura](https://worldbank.github.io/data360-mcp/).
Esta raíz es autónoma y no instala ni autoriza herramientas, cuentas o gastos.
