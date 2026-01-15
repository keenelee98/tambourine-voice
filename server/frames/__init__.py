"""Custom frames for Tambourine voice pipeline."""

from dataclasses import dataclass

from pipecat.frames.frames import SystemFrame


@dataclass
class NVidiaSTTFinalizeFrame(SystemFrame):
    """Signal to force NVIDIA STT service to finalize pending transcription.

    Sent upstream from TurnController when user manually stops recording.
    Triggers hard reset with audio padding to capture trailing words.

    This is distinct from VADUserStoppedSpeakingFrame which indicates
    natural silence detection and triggers soft reset.
    """

    pass
