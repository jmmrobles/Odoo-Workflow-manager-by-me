"""Servicios: I/O, integraciones y lógica sin acoplar a la UI."""

from app.services.excel_service import read_excel_file

__all__ = ["read_excel_file"]
