class Report:
    count = 0

    def __init__(self, patient_name, professional_type, professional_name, behavior_description):
        Report.count += 1
        self.report_id = Report.count
        self.patient_name = patient_name
        self.professional_type = professional_type
        self.professional_name = professional_name
        self.behavior_description = behavior_description

    def display_report(self):
        print(f"Report ID: {self.report_id}")
        print(f"Patient: {self.patient_name}")
        print(f"Professional Type: {self.professional_type}")
        print(f"Professional Name: {self.professional_name}")
        print(f"Behavior Description: {self.behavior_description}")
        print("\n")

# Create a report
report1 = Report("Patient1", "Psychiatrist", "Dr. Smith", "The psychiatrist was dismissive and unprofessional during our session.")

# Display the report
report1.display_report()

# More reports can be created and displayed in similar manner
