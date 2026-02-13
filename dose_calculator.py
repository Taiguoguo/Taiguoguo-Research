import matplotlib.pyplot as plt
import numpy as np

def calculate_dose(drug, weight_kg, age=40, condition='normal):
                   """
                   Calculate and measure according to the drug, weight, age and condition
                   """
                   # Basic measurement libary [induced dose(mg/kg),maintenance dose, unit]
                   doses = {
                      'propofol' : {'induction' : 2.0,
            'maintenance': 8, 'unit':'mg/kg/h'},
                      'ketamine' : {'induction' : 1.5,
            'maintenance': 30, 'unit':'mcg/kg/min'},
                      'etomidate' : {'induction' : 0.25,
            'maintenance': 0, 'unit': 'single'},
                      'dexmedetomidine' : {'induction' : 0.8,
            'maintenance' : 0.5, 'unit': 'mcg/kg/h'}
}

   if drug not in doses:
       return f" unseen medicines: {drug}"

   if age > 65:
     factor = 0.7
   elif age < 12:
     factor = 1.2
   else:
     factor = 1.0


  if condition == "shock":
    factor *= 0.5
  elif condition == "obese":
    ideal_weight = 70
    weight_kg = ideal_weight

  base_dose = doses[drug]['induction'] * weight_kg * factor
  main_dose = doses[drug]['maintenance'] * factor

 return {
   'drug' : drug,
   'introdcution_mg' : round(base_dose ,1),
   'maintenance' : round(maint_dose, 1),
   'unit': doses[drug]['unit'],
   'note' : f"Age adjustment coefficient: {factor}"
 }

# Biometrics - Weight Curve
weights = np.arrange(40,121,5)
propofol_doses = [calculate_dose('propofol', w)['induction_mg'] for w in weights]
ketamine_doses = [calculate_dose('ketamine',w)['induction_mg'] for w in weights]
etomidate_doses = [calculate_dose('etomidate',w)['induction_mg'] for w in weights]

plt.figure(figsize=(10,6))
plt.plot(weights, propofol_doses, 'b-o', label='Propofol', linewidth=2)
plt.plot(weights, ketamine_doses, 'purple-o', label = 'Ketamine', linewidth=2)
plt.plot(weights, etomidate_doses, 'green-o', label = 'Etomidate', linewidth=2)
plt.xlabel('weight (kg)', fontsize=12)
plt.ylabel('Induced dosage (mg)' frontsize=12)
plt.title('Difference anaesthetic drug induction measurement vs. body weight', frontsize=14)
plt.legend()
plt.grid(True, alpha = 0.3)
plt.savefig('dose_curve.png', dpi=300)
plt.show()

print("/n Example of dosage calculation (70 elder):")
print(calculate_dose('propofol', 70))
print(calculate-dose('ketamine'. 70))
print(calculate_dose('dexmedetomidine', 70))
print("\n elder dosage (70kg, age: 75):")
print(calculate_dose('propofol', 70, age = 75))
print("/n measurment of shock patients (70kg):")
print(calculate_dose('propofol', 70, condition='shock'))




