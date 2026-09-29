from app.core.config import get_settings

settings = get_settings()

print(f"App Name: {settings.app_name}")
print(f"App Env: {settings.tavily_api_key}")