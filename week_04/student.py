class Student:
    def __init__(self, sap_id, name, marks):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty.")
        self.sap_id = str(sap_id)
        self.name = name.strip()
        self._marks = []
        self.set_marks(marks)

    def set_marks(self, marks):
        if not marks or len(marks) == 0:
            raise ValueError("Marks list cannot be empty.")
        for m in marks:
            if not 0 <= m <= 100:
                raise ValueError(f"Invalid mark {m}: must be 0-100.")
        self._marks = list(marks)

    def get_marks(self):
        return self._marks.copy()  # copy taake bahar se change na ho

    def calculate_average(self):
        return sum(self._marks) / len(self._marks)

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 85: return "A"
        if avg >= 70: return "B"
        if avg >= 60: return "C"
        if avg >= 50: return "D"
        return "F"

    def format_profile(self):
        return f"SAP ID: {self.sap_id} | Name: {self.name} | Avg: {self.calculate_average():.2f} | Grade: {self.calculate_grade()}"