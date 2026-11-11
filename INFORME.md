Nombre: Sally Andrea Gutiérrez Bermúdez

Código: 0182410075

## PARTE 1

### 1.

| A | B | C | D | E | F | PMAX | L1 | L2 | RR | RN | V | S | Cambio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 1 | 0 | 0 | 7 | 5 | 50kg | 3kg | 10kg | 25% | 50% | 15% | 2000 | 0 |

| ID | Regla (con tus valores) |
| --- | --- |
| R1 | El peso debe cumplir 0 < peso ≤ 50 kg. Si no, se lanza el error “peso inválido”. |
| R2 | Si la zona no es una de las tres válidas, o el día no está entre 1 y 7, se lanza un error. |
| R3 | Tarifa base. Tramo 1 (peso ≤ 3 kg): $6.000. Tramo 2 (hasta 10 kg, inclusive): $9.000. Más de 10 kg: $9.000 + $800 por cada kg sobre 10 kg, de forma proporcional. |
| R4 | Recargo por zona. Rural: +25 %. Nacional: +50 %. Urbana: sin recargo. |
| R5 | Fin de semana (sábado y domingo): +$2.000, después de los descuentos. |
| R6 | Descuento de cliente. Frecuente: 5 %. VIP: 15 %. Cupón ENVIO10: 10 %. Si hay los dos, se aplican ambos: primero el del cliente y luego el cupón. |
| R7 | El cupón es opcional. Si se proporciona un cupón desconocido, se devuelve un error. |
| R8 | El costo nunca es menor que $5.000. El resultado se redondea al múltiplo de $100 más cercano; los $50 redondean hacia arriba. |

### 2. Historias de Usuarios

**HU-01.** Detectar datos incorrectos antes de cotizar (R1, R2 y R7). Como operadora de EnvíaYa, quiero que el sistema valide los datos del envío y el cupón para saber qué debo corregir antes de informar un precio. **Dado** un envío nacional de 50 kg, para un cliente normal, el día 5 y sin cupón, **cuando** solicito la cotización, **entonces** el sistema acepta el peso y devuelve $61.500. **Dado** un envío urbano de 2 kg, para un cliente normal, el día 5 y sin cupón, **cuando** intento cotizarlo cambiando solo el peso a 50,1 kg, **entonces** se devuelve el error «peso inválido». Si en ese mismo envío cambio solo la zona a metropolitana o solo el día a 8, el sistema devuelve un error por el dato correspondiente. **Dado** que el envío tiene todos sus datos válidos pero incluye el cupón PROMO20, que no existe, **cuando** solicito el precio, **entonces** el sistema devuelve un error de cupón y la cotización queda sin total.

**HU-02.** Estimar el costo según el destino y el día de despacho (R3, R4 y R5). Como vendedora que prepara sus despachos, quiero cotizar cada paquete según su peso, su zona y el día de envío para estimar cuánto pagaré. **Dado** un paquete rural de exactamente 3 kg, para un cliente normal, el día 2 y sin cupón, **cuando** lo cotizo, **entonces** se aplica la base del primer tramo de $6.000 más el 25 % rural y se devuelve $7.500. **Dado** un envío urbano de 10,75 kg para un cliente normal, el día 2 y sin cupón, **cuando** lo cotizo, **entonces** se suman $600 por los 0,75 kg que exceden el límite de 10 kg y se devuelve $9.600. **Dado** un envío nacional de 5 kg para un cliente VIP, el domingo y sin cupón, cuando se calcula el total, **entonces** la base de $9.000 sube a $13.500 por la zona, baja a $11.475 por el descuento VIP y luego sube a $13.475 al sumar los $2.000 del domingo. El resultado redondeado es $13.500.

**HU-03.** Verificar los descuentos y el importe final (R6 y R8). Como cliente que usa descuentos, quiero que se apliquen mis beneficios en el orden previsto y que el total respete el mínimo y el redondeo establecidos. **Dado** un envío rural de 8 kg, para un cliente frecuente, el día 4 y con ENVIO10, **cuando** se calcula la cotización, **entonces** se aplica primero el 5 % sobre $11.250 y después el 10 % sobre el saldo. Los $9.618,75 resultantes se redondean a $9.600. **Dado** un envío urbano de 1,5 kg, para un cliente VIP, el día 4 y con ENVIO10, **cuando** los descuentos reducen el costo a $4.590, **entonces** se cobra el mínimo de $5.000. **Dado** un envío urbano de 6 kg, para un cliente VIP, el día 4 y sin cupón, **cuando** el descuento deja el costo en $7.650, **entonces** el empate se redondea hacia arriba y se devuelve $7.700.

### 3. Matriz de trazabilidad

Los códigos S-CN identifican los casos de caja negra propuestos a partir de los criterios de aceptación de Sally. Conserva estos códigos al desarrollar su matriz de casos.

| Requisito | Historia | Casos de prueba |
| --- | --- | --- |
| R1 · Peso válido | HU-01 | S-CN-01: 50 kg aceptados. S-CN-02: 50,1 kg rechazados. |
| R2 · Zona y día válidos | HU-01 | S-CN-03: zona «metropolitana» rechazada. S-CN-04: día 8 rechazado. |
| R3 · Tarifa por peso | HU-02 | S-CN-06: 3 kg en el primer tramo. S-CN-08: 5 kg en el segundo. S-CN-07: 10,75 kg con cobro proporcional. |
| R4 · Recargo por zona | HU-02 | S-CN-06: rural +25 %. S-CN-07: urbana sin recargo. S-CN-08: nacional +50 %. |
| R5 · Fin de semana | HU-02 | S-CN-08: el domingo se suman $2.000 después del descuento VIP. |
| R6 · Descuentos | HU-02, HU-03 | S-CN-08: VIP, 15 %. S-CN-09: frecuente, 5 %, y luego ENVIO10, 10 %. |
| R7 · Cupón desconocido | HU-01 | S-CN-05: PROMO20 genera un error y la cotización queda sin total. |
| R8 · Mínimo y redondeo | HU-03 | S-CN-10: $4.590 se ajustan al mínimo de $5.000. S-CN-11: $7.650 suben a $7.700. |

## Parte 2. Plan de pruebas

### 2.1 Objetivo y alcance

Comprobar que cada solicitud de cotización produzca el importe previsto o el error definido en R1–R8. Se priorizarán los límites de peso, la validación de datos y cupones, y la aplicación de los descuentos antes del recargo de sábado y domingo. La primera ejecución se hará sobre `v1.0.0` y servirá de referencia para la regresión.

### 2.2 Niveles de prueba

**Unidad.** Probar comportamientos puntuales de `calc` con entradas controladas. Por ejemplo, verificar que un peso de 50,1 kg se rechace y que un envío urbano de 10,75 kg sin descuentos cueste $9.600.

**Integración.** Verificar que la validación del cupón y el cálculo de la cotización trabajen juntos. Con un envío válido, `ENVIO10` debe reducir el saldo después del descuento del cliente. Un cupón desconocido debe interrumpir el cálculo con un error.

**Sistema.** Ejecutar solicitudes completas mediante la función pública del cotizador. Usar como escenario un envío nacional VIP del domingo y comprobar que la cotización final sea $13.500.

**Aceptación.** Contrastar los resultados con HU-01 a HU-03. Verificar, entre otros criterios, que `PROMO20` genere un error, que un subtotal de $4.590 se ajuste a $5.000 y que $7.650 se redondeen a $7.700.

### 2.3 Estrategia, ambiente y roles

Construir una matriz con al menos 20 casos mediante particiones de equivalencia, valores límite y tabla de decisión. Desarrollar a mano al menos cinco resultados esperados y usar el grafo de `calc` para definir caminos de caja blanca. Ejecutar las pruebas automatizadas contra la versión heredada, registrar las diferencias y repetir la suite después de corregirlas.

**Ambiente.** Windows y PowerShell, Python 3 en un entorno virtual, pytest para ejecutar los casos, pytest-cov para medir cobertura y Git para identificar la versión probada.

**Roles.** Diseño: selecciona entradas y verifica los cálculos manuales. Ejecución: automatiza los casos y adjunta resultados y cobertura. Revisión: relaciona los defectos con los requisitos y comprueba las correcciones mediante regresión.

### 2.4 Riesgos y mitigaciones

Confundir cupón ausente con cupón desconocido. Mantener fijos el peso, la zona, el cliente y el día. Variar solo el cupón entre ausente, `ENVIO10` y `PROMO20`.

Que el mínimo o el redondeo oculten un error de cálculo. Incluir casos con subtotales por debajo del mínimo y casos que produzcan un empate exacto de $50.

Obtener resultados difíciles de reproducir. Registrar el commit, las versiones de herramientas y los comandos de ejecución junto con los resultados.

### 2.5 Criterios de entrada y salida

**Entrada.** Parámetros y reglas revisados, código heredado identificado con `v1.0.0`, entorno operativo y casos vinculados a los requisitos con resultados esperados definidos.

**Salida.** Matriz ejecutada, fallos iniciales documentados con pasos de reproducción y regresión aprobada. Archivar las capturas, la proporción de pruebas aprobadas, los defectos por severidad, la densidad de defectos y la cobertura de sentencias y de ramas. Comparar las coberturas de ambas ejecuciones.
