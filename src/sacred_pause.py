# sacred_pause.py

class SacredPause:
    def __init__(self, severity: int, comment: str = ""):
        if not 1 <= severity <= 10:
            raise ValueError("Severity must be between 1 and 10.")
        self.severity = severity
        self.comment = comment

    def decide(self):
        """
        Returns:
        - '➕' if severity is 1–3: act
        - '⚪' if severity is 4–7: pause
        - '➖' if severity is 8–10: withhold
        """
        if 1 <= self.severity <= 3:
            return "➕", "Action permitted."
        elif 4 <= self.severity <= 7:
            return "⚪", "Pausing for further context."
        else:
            return "➖", "Withholding due to ethical concern."

    def explain(self):
        symbol, message = self.decide()
        return {
            "symbol": symbol,
            "severity": self.severity,
            "comment": self.comment,
            "message": message
        }
