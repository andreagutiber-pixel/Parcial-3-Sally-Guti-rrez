"""Pruebas de importes, validación de entradas y salida de diagnóstico."""

import pytest

from envios import calc


IMPORTES = [
    pytest.param((50, 'nacional', 'normal', 5, None), 61500, id='CP-01'),
    pytest.param((3, 'rural', 'normal', 2, None), 7500, id='CP-06'),
    pytest.param((10.75, 'urbana', 'normal', 2, None), 9600, id='CP-07'),
    pytest.param((5, 'nacional', 'vip', 7, None), 13500, id='CP-08'),
    pytest.param((8, 'rural', 'frecuente', 4, 'ENVIO10'), 9600, id='CP-09'),
    pytest.param((1.5, 'urbana', 'vip', 4, 'ENVIO10'), 5000, id='CP-10'),
    pytest.param((6, 'urbana', 'vip', 4, None), 7700, id='CP-11'),
    pytest.param((0.1, 'urbana', 'normal', 5, None), 6000, id='CP-14'),
    pytest.param((2.9, 'rural', 'normal', 2, None), 7500, id='CP-15'),
    pytest.param((3.1, 'rural', 'normal', 2, None), 11300, id='CP-16'),
    pytest.param((9.9, 'urbana', 'normal', 2, None), 9000, id='CP-17'),
    pytest.param((10, 'urbana', 'normal', 2, None), 9000, id='CP-18'),
    pytest.param((10.1, 'urbana', 'normal', 2, None), 9100, id='CP-19'),
    pytest.param((49.9, 'nacional', 'normal', 5, None), 61400, id='CP-20'),
    pytest.param((2, 'urbana', 'normal', 5, None), 6000, id='CP-21'),
    pytest.param((2, 'urbana', 'normal', 5, 'ENVIO10'), 5400, id='CP-22'),
    pytest.param((5, 'nacional', 'vip', 6, None), 13500, id='CP-23'),
    pytest.param((5, 'nacional', 'vip', 5, None), 11500, id='CP-24'),
    pytest.param((2, 'urbana', 'normal', 1, None), 6000, id='CP-26'),
    pytest.param((2, 'urbana', 'normal', 5, None), 6000, id='CF-01'),
    pytest.param((9.9, 'urbana', 'normal', 2, None), 9000, id='CF-04'),
    pytest.param((10.1, 'urbana', 'normal', 2, None), 9100, id='CF-05'),
    pytest.param((2.9, 'rural', 'normal', 2, None), 7500, id='CF-06'),
    pytest.param((50, 'nacional', 'normal', 5, None), 61500, id='CF-07'),
    pytest.param((5, 'nacional', 'vip', 7, None), 13500, id='CF-09'),
    pytest.param((8, 'rural', 'frecuente', 4, None), 10700, id='CF-10'),
    pytest.param((6, 'urbana', 'vip', 4, None), 7700, id='CF-11'),
    pytest.param((2, 'urbana', 'normal', 5, 'ENVIO10'), 5400, id='CF-13'),
    pytest.param((1.5, 'urbana', 'vip', 4, 'ENVIO10'), 5000, id='CF-14'),
]

RECHAZOS = [
    pytest.param((50.1, 'urbana', 'normal', 5, None), 'peso inválido', id='CP-02'),
    pytest.param((2, 'metropolitana', 'normal', 5, None), None, id='CP-03'),
    pytest.param((2, 'urbana', 'normal', 8, None), None, id='CP-04'),
    pytest.param((2, 'urbana', 'normal', 5, 'PROMO20'), None, id='CP-05'),
    pytest.param((-0.1, 'urbana', 'normal', 5, None), 'peso inválido', id='CP-12'),
    pytest.param((0, 'urbana', 'normal', 5, None), 'peso inválido', id='CP-13'),
    pytest.param((2, 'urbana', 'normal', 0, None), None, id='CP-25'),
    pytest.param((50.1, 'nacional', 'normal', 5, None), 'peso inválido', id='CP-27'),
    pytest.param((-0.1, 'urbana', 'normal', 5, None), 'peso inválido', id='CF-02'),
    pytest.param((50.1, 'urbana', 'normal', 5, None), 'peso inválido', id='CF-03'),
    pytest.param((2, 'metropolitana', 'normal', 5, None), None, id='CF-08'),
    pytest.param((2, 'urbana', 'normal', 5, 'PROMO20'), None, id='CF-12'),
]


@pytest.mark.parametrize("datos, total", IMPORTES)
def test_importe_de_la_cotizacion(datos, total):
    assert calc(*datos) == total


@pytest.mark.parametrize("datos, mensaje", RECHAZOS)
def test_rechazo_de_solicitud(datos, mensaje):
    with pytest.raises(ValueError) as error:
        calc(*datos)
    if mensaje is not None:
        assert str(error.value) == mensaje


@pytest.mark.parametrize("datos, total", [
    pytest.param((10, 'urbana', 'normal', 2, None), 9000, id='CF-15'),
])
def test_costo_con_diagnostico(datos, total, capsys):
    assert calc(*datos, flag=True) == total
    assert capsys.readouterr().out.startswith("costo:")
