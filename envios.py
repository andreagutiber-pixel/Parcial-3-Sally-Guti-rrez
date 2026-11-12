"""Cálculo de cotizaciones con estrategias para los descuentos."""

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from typing import Protocol

PESO_MAXIMO = Decimal("50")
PESO_TRAMO_LIGERO = Decimal("3")
PESO_TRAMO_MEDIO = Decimal("10")
BASE_LIGERA = Decimal("6000")
BASE_MEDIA = Decimal("9000")
PRECIO_POR_KILO_ADICIONAL = Decimal("800")
CARGO_DE_FIN_DE_SEMANA = Decimal("2000")
MINIMO_DE_ENVIO = Decimal("5000")
CENTENA = Decimal("1E2")
DIAS_DE_ENVIO = range(1, 8)
FIN_DE_SEMANA = (6, 7)
CUPON_ENVIO = "ENVIO10"
DESTINO_INSULAR = "insular"
RECARGOS = {
    "urbana": Decimal("0"),
    "rural": Decimal("0.25"),
    "nacional": Decimal("0.50"),
    DESTINO_INSULAR: Decimal("0.70"),
}


class EstrategiaDescuento(Protocol):
    def aplicar(self, importe: Decimal) -> Decimal:
        ...


class SinDescuento:
    def aplicar(self, importe: Decimal) -> Decimal:
        return importe


@dataclass(frozen=True)
class DescuentoPorcentual:
    porcentaje: Decimal

    def aplicar(self, importe: Decimal) -> Decimal:
        return importe * (1 - self.porcentaje)


DESCUENTO_FRECUENTE = Decimal("0.05")
DESCUENTO_VIP = Decimal("0.15")
DESCUENTO_ENVIO10 = Decimal("0.10")
SIN_DESCUENTO = SinDescuento()
DESCUENTOS: dict[str, EstrategiaDescuento] = {
    "frecuente": DescuentoPorcentual(DESCUENTO_FRECUENTE),
    "vip": DescuentoPorcentual(DESCUENTO_VIP),
}
ESTRATEGIA_CUPON = DescuentoPorcentual(DESCUENTO_ENVIO10)


def _peso_valido(peso: float) -> Decimal:
    kilos = Decimal(str(peso))
    if not kilos.is_finite() or not 0 < kilos <= PESO_MAXIMO:
        raise ValueError("peso inválido")
    return kilos


def _recargo_zona(zona: str) -> Decimal:
    if zona not in RECARGOS:
        raise ValueError("zona inválida")
    return RECARGOS[zona]


def _validar_dia(dia: int) -> None:
    if dia not in DIAS_DE_ENVIO:
        raise ValueError("día inválido")


def _estrategia_cupon(cupon: str | None, zona: str) -> EstrategiaDescuento:
    if cupon is None:
        return SIN_DESCUENTO
    if zona == DESTINO_INSULAR:
        raise ValueError("el destino insular no admite cupones")
    if cupon == CUPON_ENVIO:
        return ESTRATEGIA_CUPON
    raise ValueError("cupón inválido")


def _calcular_base(kilos: Decimal) -> Decimal:
    if kilos <= PESO_TRAMO_LIGERO:
        return BASE_LIGERA
    if kilos <= PESO_TRAMO_MEDIO:
        return BASE_MEDIA
    return BASE_MEDIA + (kilos - PESO_TRAMO_MEDIO) * PRECIO_POR_KILO_ADICIONAL


def _cargo_por_dia(dia: int) -> Decimal:
    return CARGO_DE_FIN_DE_SEMANA if dia in FIN_DE_SEMANA else Decimal("0")


def _redondear(total: Decimal) -> int:
    return int(max(MINIMO_DE_ENVIO, total).quantize(CENTENA, ROUND_HALF_UP))


def calc(p, z, c, d, cup=None):
    """Calcula el importe final de un envío, expresado en pesos."""
    kilos = _peso_valido(p)
    recargo = _recargo_zona(z)
    _validar_dia(d)
    promocion = _estrategia_cupon(cup, z)
    con_zona = _calcular_base(kilos) * (1 + recargo)
    cliente = DESCUENTOS.get(c, SIN_DESCUENTO)
    descontado = promocion.aplicar(cliente.aplicar(con_zona))
    return _redondear(descontado + _cargo_por_dia(d))
