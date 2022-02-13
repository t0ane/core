"""Helpers for Roku."""
from __future__ import annotations

import mimetypes

import yarl

MIME_TO_STREAM_FORMAT = {
    "application/dash+xml": "dash",
    "audio/mpeg": "mp3",
    "audio/x-ms-wma": "wma",
    "video/mp4": "mp4",
    "video/quicktime": "mp4",
    "video/x-matroska": "mkv",
}


def format_channel_name(channel_number: str, channel_name: str | None = None) -> str:
    """Format a Roku Channel name."""
    if channel_name is not None and channel_name != "":
        return f"{channel_name} ({channel_number})"

    return channel_number


def guess_stream_format(url: str, mime_type: str | None = None) -> str | None:
    """Guess the Roku stream format for a given URL."""
    if mime_type is None:
        mime_type, _ = mimetypes.guess_type(url)

    parsed = yarl.URL(url)

    if mime_type == "audio/mpeg" and parsed.path.endswith(".m4a"):
        return "m4a"

    if mime_type == "video/x-matroska":
        if parsed.path.endswith(".mka"):
            return "mka"

        if parsed.path.endswith(".mks"):
            return "mks"

    if parsed.path.endswith(".ism"):
        return "ism"

    if mime_type not in MIME_TO_STREAM_FORMAT:
        return None

    return MIME_TO_STREAM_FORMAT[mime_type]
