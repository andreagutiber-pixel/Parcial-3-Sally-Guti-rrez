"""Aceptación de las cotizaciones hacia San Andrés."""

import pytest

from envios import calc


def test_cotizacion_insular_con_peso_excedente():
    # AC-01. (9000 + 0,5 × 800) × 1,70 = 15980; redondeado, 16000.
    assert calc(10.5, "insular", "normal", 2, None) == 16000


def test_descuento_de_cliente_frecuente_en_san_andres():
    # AC-02. 6000 × 1,70 × 0,95 = 9690; redondeado, 9700.
    assert calc(3, "insular", "frecuente", 2) == 9700


@pytest.mark.parametrize(
    "codigo",
    [pytest.param("ENVIO10", id="AC-03"), pytest.param("PROMO20", id="AC-04")],
)
def test_solicitud_insular_con_codigo_promocional_es_invalida(codigo):
    with pytest.raises(ValueError, match="^el destino insular no admite cupones$"):
        calc(5, "insular", "vip", 7, codigo)
