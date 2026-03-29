"""Controlador de ajustes de usuario (placeholder)."""

from app.models.user_settings import UserSettings


class SettingsController:
    def load(self) -> UserSettings:
        return UserSettings()
