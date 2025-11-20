from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """initial the string - initial value."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """:return: an initial value."""
        initial = " ".join([(name.capitalize()[0]+".") for name in text.strip().split()])
        return initial

    def validate(self, params: Dict = None) -> None:
        """Redact does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize
