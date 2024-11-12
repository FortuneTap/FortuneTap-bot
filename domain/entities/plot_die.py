from dataclasses import dataclass
from enum import Enum
from typing import Optional
import d20

def roll():
    die_result = d20.roll("1d6").total

    result: PlotDieResult
    if (die_result <= 2):
        result = PlotDieResult(PlotDieResultType.COMPLICATION, die_result*2)
    elif (die_result >= 5):
        result = PlotDieResult(PlotDieResultType.OPPORTUNITY)
    else:
        result = PlotDieResult(PlotDieResultType.NOTHING)

    return result

class PlotDieResultType(Enum):
    OPPORTUNITY = "Opportunity"
    COMPLICATION = "Complication"
    NOTHING = "Nothing"

@dataclass
class PlotDieResult:
    result_type: PlotDieResultType  # Puede ser OPPORTUNITY, COMPLICATION, o NOTHING
    complication_value: Optional[int] = None  # Puede ser None, 2, o 4 en caso de complicación

    def apply_complication(self, roll_value: int) -> int:
        """Si es una complicación, aplica el valor de complicación a la tirada dada."""
        if self.result_type == PlotDieResultType.COMPLICATION and self.complication_value:
            return roll_value + self.complication_value
        return roll_value