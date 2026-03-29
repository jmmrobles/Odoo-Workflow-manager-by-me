"""Preferencias de usuario persistibles (estructura base)."""

from dataclasses import dataclass


@dataclass
class UserSettings:
    last_excel_path: str | None = None
