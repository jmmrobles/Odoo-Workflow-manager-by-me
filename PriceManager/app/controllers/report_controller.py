"""Controlador de informes (placeholder)."""

from app.models.report_config import ReportConfig


class ReportController:
    def get_default_config(self) -> ReportConfig:
        return ReportConfig(name="default")
