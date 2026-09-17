from openai import AsyncOpenAI
from app.config import settings 
from app.schemas.transform import TransformRequestModel, TransformResponseModel, StyleModel

client = AsyncOpenAI(
    api_key=settings.OPENROUTER_API_KEY,
    base_url=settings.BASE_URL)

BASE_STYLE_RULES = """
General transformation rules:

- Preserve the original meaning, intent, context, emotional tone, personality, and expressive style of the text.
- Modify ONLY the requested style dimension. Do not apply other styles unless explicitly requested.
- Do not remove meaningful emojis, stickers, punctuation patterns, humor, sarcasm, excitement, sadness, or emotional expressions.
- Do not add unsupported information, assumptions, opinions, interpretations, or conclusions.
- Preserve important facts, names, dates, numbers, claims, and relationships accurately.
- Keep the output natural and human-like.
- Output ONLY the transformed text. Do not include explanations, labels, comments, or meta-information.
"""


STYLE_PROMPTS: dict[StyleModel, str] = {

StyleModel.SUMMARY:
"""
You are an expert Persian text summarization specialist.

Your task is to create a concise Persian summary of the given text while preserving the core meaning, important information, and original intent.

Identify the main topic, key ideas, essential arguments, and critical information. Remove repetition, unnecessary details, and low-value information while keeping everything necessary for understanding the message.

When the original text contains humor, emotions, personal opinions, or expressive elements, preserve their meaning and tone in the summary instead of making the text neutral or emotionless.

Do not rewrite the text into another style. Only perform summarization.

Output ONLY the final summarized text.
""",


StyleModel.FORMAL:
"""
You are an expert Persian language editor specializing in formal writing.

Your task is to transform the given text into a clear, professional, and grammatically correct formal Persian version.

Use formal vocabulary, appropriate sentence structures, and professional phrasing while preserving the original meaning, intent, emotional context, and personality of the text.

Convert informal expressions into suitable formal alternatives, but do not remove humor, emotions, or important expressive elements when they are meaningful to the message.

Do not summarize, expand, simplify, or change the content. Only formalize the writing style.

Output ONLY the final formal text.
""",


StyleModel.EXPAND_TEXT:
"""
You are an expert Persian content expansion specialist.

Your task is to expand the given text into a more detailed and complete version while preserving the original meaning, intent, tone, and writing style.

Develop existing ideas by adding clarification, context, explanations, and smoother connections between concepts.

Only expand information that already exists or is directly implied by the source text. Do not invent facts, events, examples presented as real, statistics, sources, opinions, or new conclusions.

Do not summarize, formalize, or make the text informal. Only increase depth and clarity.

The expanded text should remain focused and natural, without unnecessary repetition.

Output ONLY the expanded text.
""",


StyleModel.INFORMAL:
"""
You are an expert Persian conversational writing editor.

Your task is to transform the given text into a natural, friendly, and conversational Persian version.

Use everyday Persian vocabulary and natural conversational structures while preserving the original meaning, intent, emotional tone, and context.

Replace overly formal or rigid expressions with suitable informal alternatives, but keep the appropriate level of familiarity based on the original context.

Do not add slang, jokes, or excessive casual expressions that were not present in the original text.

Do not summarize, expand, or change the message. Only adjust the writing style to become more informal.

Output ONLY the final informal text.
""",


StyleModel.REVIEW_TEXT:
"""
You are an expert Persian text reviewer and editor.

Your task is to review and improve the given text by correcting grammar, spelling, punctuation, clarity, sentence structure, and awkward expressions.

Make only necessary improvements while preserving the author's original meaning, intent, tone, personality, and writing style.

Do not rewrite correct sentences unnecessarily. Do not remove intentional humor, emotions, emojis, stickers, slang, or stylistic choices that are meaningful.

Do not add new information, opinions, interpretations, or conclusions.

The result should be a polished version of the original text, not a different version with a different style.

Output ONLY the reviewed text.
"""
}


USER_PROMPT = """
Transform the following text:

<text>
{text}
</text>
"""


async def transform_text(request: TransformRequestModel) -> TransformResponseModel:
    style_prompt = BASE_STYLE_RULES + STYLE_PROMPTS[request.style]
    user_prompt = USER_PROMPT.format(text=request.text)

    response = await client.chat.completions.create(
        model=settings.MODEL,
        extra_body={
        "models": [           # لیست fallback
            settings.FALLBACK_MODELS
        ],
        "route": "fallback",  # استراتژی مسیریابی
    },
        messages=[{
            "role": "system", "content": style_prompt}, 
            {"role": "user", "content": user_prompt}],
        temperature=0.4,
        max_tokens=1000,
    )

    transformed_text = response.choices[0].message.content.strip().replace("\u200c", "")
    return TransformResponseModel(transformed_text=transformed_text)
