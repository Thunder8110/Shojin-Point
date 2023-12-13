class values:
  def __init__(self) -> None:
    self.user: str | None = None
    self.points: int | None = None
    self.tee: float | None = None
    self.begin_date: int | None = None
    self.end_date: int | None = None
    self.formula: str | None = None
    self.valx: float | None = None
    self.valy: float | None = None
    self.valz: float | None = None

test_data = values()
test_data.user = "KA37RI"
test_data.begin_date = 1701356400
test_data.end_date = 1701961200
test_data.formula = "[tee] * 10"