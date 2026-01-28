import re
import language_tool_python


class FrenchSpellCorrector:
    def __init__(self):
        print("Initializing French corrector...")

        self.tool = language_tool_python.LanguageTool(
            "fr-FR",
            remote_server="http://localhost:8081"
        )

        # Fix bug interne connu
        self.tool._new_spellings = set()
        self.tool._new_spellings_persist = False

        print("Corrector ready.")

    def categorize_error(self, rule_id: str) -> str:
        if "SPELL" in rule_id or "MORFOLOGIK" in rule_id:
            return "Orthographe"
        elif "GRAMMAR" in rule_id or "AGREEMENT" in rule_id:
            return "Grammaire"
        elif "PUNCTUATION" in rule_id or "COMMA" in rule_id:
            return "Ponctuation"
        return "Autre"

    def correct_text(self, text: str) -> dict:
        matches = self.tool.check(text)

        errors = []
        for i, match in enumerate(matches, 1):
            start = match.offset
            end = start + match.errorLength

            errors.append({
                "id": i,
                "error": text[start:end],
                "message": match.message,
                "category": self.categorize_error(match.ruleId),
                "suggestions": match.replacements
            })

        corrected_text = self.tool.correct(text)
        word_count = len(re.findall(r"\b\w+\b", text))

        return {
            "original_text": text,
            "corrected_text": corrected_text,
            "errors": errors,
            "statistics": {
                "word_count": word_count,
                "error_count": len(errors)
            }
        }

    def close(self):
        self.tool.close()
