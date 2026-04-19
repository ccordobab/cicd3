# app/calculadora.py

"""Funciones básicas de una calculadora."""

AUTOR = "Daniela, Juan Miguel, Camilo y David" 


def sumar(a, b):
    """Suma dos números."""
    return a + b


def restar(a, b):
    """resta dos números."""
    return a - b


def multiplicar(a, b):
    """multiplima dos números."""
    return a * b


def dividir(a, b):
    """divida dos números."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
