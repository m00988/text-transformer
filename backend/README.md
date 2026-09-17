# Text Transformer - Backend

Backend پروژه‌ی **Text Transformer** با استفاده از **FastAPI** توسعه داده شده است. این API متن ورودی را دریافت کرده و آن را به حالت‌های مختلف مانند رسمی، خلاصه و ... تبدیل می‌کند.

## پیش‌نیازها

* Python 3.11+
* uv

### نصب uv

**Linux / macOS:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## نصب و اجرا

```bash
uv sync

cd backend

python -m app.main
```

## تنظیم OpenRouter

برای استفاده از API، ابتدا از [OpenRouter](https://openrouter.ai/) یک API Key دریافت کنید.

سپس در پوشه `backend` یک فایل `.env` ایجاد کنید:

```env
OPENROUTER_API_KEY="your_api_key_here"
BASE_URL="https://openrouter.ai/api/v1"
MODEL="nvidia/nemotron-3-ultra-550b-a55b:free"
FALLBACK_MODELS=["nvidia/nemotron-3.5-lightning:free"]
```

`your_api_key_here` را با API Key خودتان جایگزین کنید.

> فایل `.env` را در Git قرار ندهید.

## API

پس از اجرای پروژه:

```text
http://0.0.0.0:8000
```

### API Documentation

```text
http://0.0.0.0:8000/docs
```
