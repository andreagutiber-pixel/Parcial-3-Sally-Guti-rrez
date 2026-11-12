# Lanzamiento v2.0.0 · Cotizador de envíos

La actualización reúne las correcciones del cotizador y separa la aplicación de descuentos del cálculo principal. Si se proporciona un código de cupón desconocido, calc lanza ValueError.

## Actualización de integraciones

Actualice las invocaciones que aún usan `flag`, tanto por posición como por nombre. Si la aplicación muestra la cotización, puede hacerlo con el entero retornado.

```python
# v1.0.0
importe = calc(p, z, c, d, cup, True)

# v2.0.0
importe = calc(p, z, c, d, cup)
```

## Resultado de regresión

La regresión de la Parte 6 registró 42 de 42 pruebas aprobadas y 100 % de cobertura de ramas de envios.py. El detalle de los cambios está en [CHANGELOG.md](CHANGELOG.md).
