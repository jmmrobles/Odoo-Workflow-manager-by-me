"""Funciones auxiliares genéricas (placeholder)."""


def truncate_text(text: str, max_len: int = 80) -> str:
    text = text.strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."
