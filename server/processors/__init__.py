"""Custom frame processors for Tambourine."""

from processors.llm_cleanup import LLMResponseToRTVIConverter, TranscriptionToLLMConverter

__all__ = ["LLMResponseToRTVIConverter", "TranscriptionToLLMConverter"]
