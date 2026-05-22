import pandas as pd


class DiabetesModel:

    def __init__(self):

        # LEER DATASET
        self.df = pd.read_csv(
            "diabetes.csv"
)

    # TOTAL DE PACIENTES
    def total_pacientes(self):

        return len(self.df)

    # PROMEDIO DE GLUCOSA
    def promedio_glucosa(self):

        return round(
            self.df["Glucose"].mean(),
            2
        )

    # PACIENTES CON DIABETES
    def pacientes_diabetes(self):

        return len(
            self.df[self.df["Outcome"] == 1]
        )

    # PROMEDIO DE EMBARAZOS
    def promedio_embarazos_diabetes(self):

        diabetes = self.df[
            self.df["Outcome"] == 1
        ]

        return round(
            diabetes["Pregnancies"].mean(),
            2
        )

    # PACIENTES DE ALTO RIESGO
    def pacientes_riesgo(self):

        riesgo = self.df[
            (self.df["Glucose"] > 150) &
            (self.df["BMI"] > 35)
        ]

        return riesgo.head(30)
    
    def presion_arterial_alta(self):

        return round(
            self.df["BloodPressure"].mean(),
            2
        )
