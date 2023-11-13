from app.core.settings import Settings


def test_settings_class():
    settings = Settings()

    assert settings.APP_ENV == "DEV"
    assert settings.BOT_PREFIX == "!"
    assert settings.BOT_TOKEN == ""
    assert settings.APP_NAME == "RhenusBot"
