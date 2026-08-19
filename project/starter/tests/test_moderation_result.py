from multimodal_moderation.types.moderation_result import (
    ModerationResult,
    TextModerationResult,
    ImageModerationResult,
    VideoModerationResult,
    AudioModerationResult,
)


def test_text_is_flagged_false():
    result = TextModerationResult(
        rationale="Safe text",
        contains_pii=False,
        is_unfriendly=False,
        is_unprofessional=False,
    )

    assert result.is_flagged is False


def test_text_is_flagged_true():
    result = TextModerationResult(
        rationale="Contains PII",
        contains_pii=True,
        is_unfriendly=False,
        is_unprofessional=False,
    )

    assert result.is_flagged is True


def test_image_is_flagged_false():
    result = ImageModerationResult(
        rationale="Safe image",
        contains_pii=False,
        is_disturbing=False,
        is_low_quality=False,
    )

    assert result.is_flagged is False


def test_image_is_flagged_true():
    result = ImageModerationResult(
        rationale="Low quality image",
        contains_pii=False,
        is_disturbing=False,
        is_low_quality=True,
    )

    assert result.is_flagged is True


def test_video_is_flagged_false():
    result = VideoModerationResult(
        rationale="Safe video",
        contains_pii=False,
        is_disturbing=False,
        is_low_quality=False,
    )

    assert result.is_flagged is False


def test_video_is_flagged_true():
    result = VideoModerationResult(
        rationale="Disturbing video",
        contains_pii=False,
        is_disturbing=True,
        is_low_quality=False,
    )

    assert result.is_flagged is True


def test_audio_is_flagged_false():
    result = AudioModerationResult(
        rationale="Safe audio",
        transcription="Hello, how can I help you?",
        contains_pii=False,
        is_unfriendly=False,
        is_unprofessional=False,
    )

    assert result.is_flagged is False


def test_audio_is_flagged_true():
    result = AudioModerationResult(
        rationale="Unprofessional audio",
        transcription="Example transcription",
        contains_pii=False,
        is_unfriendly=False,
        is_unprofessional=True,
    )

    assert result.is_flagged is True