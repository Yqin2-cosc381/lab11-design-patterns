from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """initial the string - initial value."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """:return: an initial value."""
        if not not str:
            initial = " ".join([self.get_first_alphanumeric_character(name.upper())+"."
                                for name in text.strip().split()])
            return initial
        return None

    def validate(self, params: Dict = None) -> None:
        """Redact does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize
    
    def get_first_alphanumeric_character(self,name:str):
        if all(not c.isalnum() for c in name): #all none alphanumeric in the name
            return None
        result =""
        for c in name:
            result = result + c
            if c.isalnum():
                break
        return result

