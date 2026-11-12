# Changelog

Este registro sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y el proyecto usa [versionado semántico](https://semver.org/lang/es/).

## [Unreleased]

## [2.0.0] - 2026-11-11

### Added

- Conjunto de 42 casos automatizados para verificar cotizaciones y rechazos.

### Changed

- El cálculo delega los descuentos al protocolo EstrategiaDescuento, con las variantes SinDescuento y DescuentoPorcentual.

### Fixed

- El cotizador devuelve un error si recibe un cupón desconocido, un destino fuera del catálogo o un día inválido.
- El cargo de fin de semana se activa desde el día seis y se suma sobre el importe descontado.
- El importe final se redondea al múltiplo de cien y el mensaje de peso inválido coincide con el requisito.

### Removed

- Se eliminó `flag` de la interfaz pública y se retiró la salida de diagnóstico de `calc`.

## [1.0.0] - 2026-11-11

### Added

- Cotizador heredado con los parámetros iniciales, usado como referencia para las pruebas.

[Unreleased]: https://github.com/andreagutiber-pixel/Parcial-3-Sally-Guti-rrez/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/andreagutiber-pixel/Parcial-3-Sally-Guti-rrez/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/andreagutiber-pixel/Parcial-3-Sally-Guti-rrez/tree/v1.0.0
