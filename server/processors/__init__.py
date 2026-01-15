"""Custom frame processors for Tambourine."""

from processors.context_manager import DictationContextManager
from processors.llm import (
    ADVANCED_PROMPT_DEFAULT,
    DICTIONARY_PROMPT_DEFAULT,
    MAIN_PROMPT_DEFAULT,
    combine_prompt_sections,
)

__all__ = [
    "ADVANCED_PROMPT_DEFAULT",
    "DICTIONARY_PROMPT_DEFAULT",
    "MAIN_PROMPT_DEFAULT",
    "DictationContextManager",
    "combine_prompt_sections",
]
