from googletrans import Translator
translate = True
def translate_text(text: str, dest: str = 'en', src: str = 'auto') -> str:
    """Переводит text с языка src на dest. Если src='auto' — язык определяется автоматически."""
    translator = Translator()
    result = translator.translate(text, src=src, dest=dest)
    return result.text

def print_language_error(lang_code):
    print(f"Ошибка: язык '{lang_code}' не поддерживается или введён неверно.")
if __name__ == "__main__":
    while True:
        target_lang = input("Введите язык перевода (например, en, ru, fr): ") or "en"
        while True:
            user_text = input("Введите текст для перевода (или 'q' для выхода): ")
            if user_text.strip().lower() == "q":
                print("Выход.")
                exit(0)
            try:
                print("Перевод:", translate_text(user_text, dest=target_lang))
            except Exception as e:
                print_language_error(target_lang)
                break  # Вернуться к выбору языка
            # Опционально: определение языка
            translator = Translator()
            det = translator.detect(user_text)
            print(f"Определённый язык: {det.lang} (уверенность {det.confidence})")