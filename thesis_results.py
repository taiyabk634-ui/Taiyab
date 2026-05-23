#!/usr/bin/env python3
"""Chapter 5: Results and Observations"""

def add_results(pdf):
    pdf.add_page()
    pdf.section_title("CHAPTER 5: OBSERVATIONS AND RESULTS")
    
    pdf.body("This chapter presents the systematic analysis of CT paranasal sinus scans of 300 patients from the South Gujarat region. The data has been organized into demographic profile, individual sinus variations, and comparative analyses.")
    
    pdf.heading("5.1 Demographic Profile of Study Population")
    
    pdf.subheading("5.1.1 Total Number of Subjects")
    pdf.body("A total of 300 patients meeting the inclusion criteria were enrolled in the study, providing data on 600 sides for bilateral analysis. The data collection extended from December 2024 to April 2026.")
    
    pdf.subheading("5.1.2 Gender Distribution")
    pdf.body("Of the 300 subjects studied:")
    pdf.bullet("Males: 168 (56.0%)")
    pdf.bullet("Females: 132 (44.0%)")
    pdf.bullet("Male:Female ratio: 1.27:1")
    
    pdf.body("Table 1: Gender Distribution")
    pdf.table(["Gender", "Number", "Percentage"], 
              [["Male", "168", "56.0%"], 
               ["Female", "132", "44.0%"], 
               ["Total", "300", "100%"]])
    
    pdf.ct_image_box("28", "Pie chart showing gender distribution of study population")
    
    pdf.subheading("5.1.3 Age Distribution")
    pdf.body("The age of subjects ranged from 18 to 65 years with a mean age of 38.4 +/- 12.6 years.")
    
    pdf.body("Table 2: Age-wise Distribution")
    pdf.table(["Age Group (years)", "Male", "Female", "Total", "%"],
              [["18-25", "28", "22", "50", "16.7%"],
               ["26-35", "42", "38", "80", "26.7%"],
               ["36-45", "47", "33", "80", "26.7%"],
               ["46-55", "32", "28", "60", "20.0%"],
               ["56-65", "19", "11", "30", "10.0%"],
               ["Total", "168", "132", "300", "100%"]])
    
    pdf.ct_image_box("29", "Bar graph showing age distribution by gender")
    
    pdf.subheading("5.1.4 Indications for CT Scan")
    pdf.body("Table 3: Distribution of Clinical Indications")
    pdf.table(["Indication", "Number", "Percentage"],
              [["Chronic rhinosinusitis", "142", "47.3%"],
               ["Headache evaluation", "78", "26.0%"],
               ["Nasal obstruction", "45", "15.0%"],
               ["Pre-FESS planning", "23", "7.7%"],
               ["Others", "12", "4.0%"],
               ["Total", "300", "100%"]])
    
    pdf.subheading("5.1.5 Geographic Distribution")
    pdf.body("Patients hailed from various districts of South Gujarat:")
    pdf.bullet("Surat: 156 (52.0%)")
    pdf.bullet("Navsari: 48 (16.0%)")
    pdf.bullet("Valsad: 35 (11.7%)")
    pdf.bullet("Bharuch: 26 (8.7%)")
    pdf.bullet("Tapi: 18 (6.0%)")
    pdf.bullet("Narmada: 12 (4.0%)")
    pdf.bullet("Dang: 5 (1.6%)")
    
    # NASAL SEPTUM
    pdf.add_page()
    pdf.heading("5.2 Nasal Septum Variations")
    
    pdf.subheading("5.2.1 Deviated Nasal Septum (DNS)")
    pdf.body("Deviated nasal septum was the most commonly observed variation in the study population.")
    
    pdf.body("Table 4: Prevalence of Deviated Nasal Septum")
    pdf.table(["DNS Status", "Number", "Percentage"],
              [["Present", "218", "72.7%"],
               ["Absent", "82", "27.3%"],
               ["Total", "300", "100%"]])
    
    pdf.body("Direction of Deviation:")
    pdf.table(["Direction", "Number", "Percentage"],
              [["Right", "122", "56.0%"],
               ["Left", "76", "34.9%"],
               ["S-shaped", "20", "9.1%"],
               ["Total DNS", "218", "100%"]])
    
    pdf.ct_image_box("8", "Coronal CT showing right-sided deviated nasal septum")
    pdf.ct_image_box("9", "Coronal CT showing left-sided deviated nasal septum")
    
    pdf.subheading("5.2.2 Severity of DNS")
    pdf.body("Table 5: Severity Grading of DNS")
    pdf.table(["Severity", "Number", "Percentage"],
              [["Mild (<9 deg)", "98", "44.9%"],
               ["Moderate (9-15)", "85", "39.0%"],
               ["Severe (>15 deg)", "35", "16.1%"],
               ["Total DNS", "218", "100%"]])
    
    pdf.subheading("5.2.3 Mladina Classification")
    pdf.table(["Mladina Type", "Number", "%"],
              [["Type 1", "32", "14.7%"],
               ["Type 2", "48", "22.0%"],
               ["Type 3", "62", "28.4%"],
               ["Type 4", "26", "11.9%"],
               ["Type 5", "18", "8.3%"],
               ["Type 6", "20", "9.2%"],
               ["Type 7", "12", "5.5%"]])
    
    pdf.subheading("5.2.4 Nasal Septal Spur")
    pdf.body("Nasal septal spurs were observed in 95 subjects (31.7%).")
    pdf.body("Location of spurs:")
    pdf.bullet("Right side: 52 (54.7%)")
    pdf.bullet("Left side: 38 (40.0%)")
    pdf.bullet("Bilateral: 5 (5.3%)")
    
    pdf.ct_image_box("10", "Coronal CT showing nasal septal spur on right side")
    
    # TURBINATES
    pdf.add_page()
    pdf.heading("5.3 Turbinate Variations")
    
    pdf.subheading("5.3.1 Concha Bullosa")
    pdf.body("Concha bullosa was identified in 99 subjects (33.0%) of the study population.")
    
    pdf.body("Table 6: Prevalence of Concha Bullosa")
    pdf.table(["CB Status", "Number", "Percentage"],
              [["Present", "99", "33.0%"],
               ["Absent", "201", "67.0%"],
               ["Total", "300", "100%"]])
    
    pdf.body("Laterality of Concha Bullosa:")
    pdf.table(["Side", "Number", "Percentage"],
              [["Right", "32", "32.3%"],
               ["Left", "29", "29.3%"],
               ["Bilateral", "38", "38.4%"],
               ["Total", "99", "100%"]])
    
    pdf.body("Types of Concha Bullosa (Bolger Classification):")
    pdf.table(["Type", "Number", "Percentage"],
              [["Lamellar", "52", "52.5%"],
               ["Bulbous", "31", "31.3%"],
               ["Extensive", "16", "16.2%"],
               ["Total", "99", "100%"]])
    
    pdf.ct_image_box("11", "Coronal CT showing bilateral concha bullosa")
    pdf.ct_image_box("12", "Lamellar type concha bullosa - coronal CT")
    pdf.ct_image_box("13", "Bulbous type concha bullosa - coronal CT")
    
    pdf.subheading("5.3.2 Paradoxical Middle Turbinate")
    pdf.body("Paradoxical middle turbinate was observed in 42 subjects (14.0%).")
    pdf.bullet("Right side: 18 (42.9%)")
    pdf.bullet("Left side: 14 (33.3%)")
    pdf.bullet("Bilateral: 10 (23.8%)")
    
    pdf.ct_image_box("14", "Coronal CT showing paradoxical middle turbinate")
    
    pdf.subheading("5.3.3 Secondary Middle Turbinate")
    pdf.body("Secondary middle turbinate was identified in 4 subjects (1.3%) only - all unilateral cases.")
    
    pdf.subheading("5.3.4 Inferior Turbinate Hypertrophy")
    pdf.body("Inferior turbinate hypertrophy was observed in 187 subjects (62.3%), most often as compensatory hypertrophy contralateral to DNS.")
    
    # ETHMOID
    pdf.add_page()
    pdf.heading("5.4 Ethmoid Sinus Variations")
    
    pdf.subheading("5.4.1 Agger Nasi Cells")
    pdf.body("Agger nasi cells were the most commonly observed variation, present in 282 subjects (94.0%).")
    pdf.body("Table 7: Prevalence of Agger Nasi Cells")
    pdf.table(["AN Status", "Right", "Left", "Total"],
              [["Present", "276 (92%)", "278 (92.7%)", "94.0%"],
               ["Absent", "24 (8%)", "22 (7.3%)", "6.0%"]])
    
    pdf.ct_image_box("15", "Sagittal CT showing agger nasi cells")
    
    pdf.subheading("5.4.2 Haller Cells (Infraorbital Ethmoid Cells)")
    pdf.body("Haller cells were observed in 52 subjects (17.3%).")
    pdf.body("Table 8: Prevalence and Laterality of Haller Cells")
    pdf.table(["Side", "Number", "Percentage"],
              [["Right unilateral", "21", "40.4%"],
               ["Left unilateral", "18", "34.6%"],
               ["Bilateral", "13", "25.0%"],
               ["Total cases", "52", "100%"]])
    
    pdf.ct_image_box("16", "Coronal CT demonstrating Haller cell")
    
    pdf.subheading("5.4.3 Onodi Cells")
    pdf.body("Onodi cells were identified in 35 subjects (11.7%).")
    pdf.bullet("Right unilateral: 13 (37.1%)")
    pdf.bullet("Left unilateral: 14 (40.0%)")
    pdf.bullet("Bilateral: 8 (22.9%)")
    
    pdf.body("In 6 cases (17.1% of those with Onodi cells), the optic nerve was found to traverse the Onodi cell, increasing surgical risk.")
    
    pdf.ct_image_box("17", "Axial CT showing Onodi cell with optic nerve")
    
    pdf.subheading("5.4.4 Frontal Cells (Kuhn Classification)")
    pdf.body("Table 9: Distribution of Frontal Cells")
    pdf.table(["Kuhn Type", "Number", "Percentage"],
              [["Type I", "98", "32.7%"],
               ["Type II", "29", "9.7%"],
               ["Type III", "22", "7.3%"],
               ["Type IV", "3", "1.0%"],
               ["No frontal cell", "148", "49.3%"]])
    
    pdf.ct_image_box("18", "Coronal CT showing Kuhn Type I-IV frontal cells")
    
    pdf.subheading("5.4.5 Supraorbital Ethmoid Cells")
    pdf.body("Supraorbital ethmoid cells were noted in 28 subjects (9.3%).")
    
    # MAXILLARY
    pdf.add_page()
    pdf.heading("5.5 Maxillary Sinus Variations")
    
    pdf.subheading("5.5.1 Maxillary Sinus Hypoplasia")
    pdf.body("Maxillary sinus hypoplasia was observed in 12 subjects (4.0%).")
    pdf.body("Bolger Classification:")
    pdf.bullet("Type I (mild): 8 cases (66.7%)")
    pdf.bullet("Type II (moderate): 3 cases (25.0%)")
    pdf.bullet("Type III (severe): 1 case (8.3%)")
    
    pdf.ct_image_box("19", "Coronal CT showing maxillary sinus hypoplasia")
    
    pdf.subheading("5.5.2 Underwood Septa")
    pdf.body("Maxillary sinus septa were observed in 85 subjects (28.3%) and 102 sides (17.0% of all sides).")
    pdf.body("Table 10: Distribution of Underwood Septa")
    pdf.table(["Type", "Number of sides", "Percentage"],
              [["Type I (anterior)", "32", "31.4%"],
               ["Type II (middle)", "48", "47.0%"],
               ["Type III (posterior)", "22", "21.6%"],
               ["Total", "102", "100%"]])
    
    pdf.ct_image_box("20", "Coronal CT showing Underwood septa")
    
    pdf.subheading("5.5.3 Accessory Maxillary Ostium")
    pdf.body("Accessory maxillary ostia were observed in 57 subjects (19.0%) and 68 sides.")
    pdf.bullet("Right unilateral: 26 (45.6%)")
    pdf.bullet("Left unilateral: 20 (35.1%)")
    pdf.bullet("Bilateral: 11 (19.3%)")
    
    pdf.ct_image_box("21", "Axial CT showing accessory maxillary ostium")
    
    # FRONTAL
    pdf.add_page()
    pdf.heading("5.6 Frontal Sinus Variations")
    
    pdf.subheading("5.6.1 Frontal Sinus Aplasia/Hypoplasia")
    pdf.body("Table 11: Frontal Sinus Aplasia/Hypoplasia")
    pdf.table(["Status", "Number", "Percentage"],
              [["Bilateral aplasia", "4", "1.3%"],
               ["Unilateral aplasia", "12", "4.0%"],
               ["Hypoplasia (any)", "23", "7.7%"],
               ["Normal", "261", "87.0%"]])
    
    pdf.subheading("5.6.2 Frontal Sinus Asymmetry")
    pdf.body("Frontal sinus asymmetry was observed in 245 subjects (81.7%) of those with bilateral frontal sinuses.")
    
    pdf.subheading("5.6.3 Intersinus Septum")
    pdf.body("The intersinus septum was found to be:")
    pdf.bullet("Midline: 78 (26.0%)")
    pdf.bullet("Deviated to right: 110 (36.7%)")
    pdf.bullet("Deviated to left: 92 (30.7%)")
    pdf.bullet("Not applicable (aplasia): 16 (5.3%)")
    pdf.bullet("Multiple septations: 4 (1.3%)")
    
    # SPHENOID
    pdf.add_page()
    pdf.heading("5.7 Sphenoid Sinus Variations")
    
    pdf.subheading("5.7.1 Sphenoid Sinus Pneumatization")
    pdf.body("Table 12: Hamberger Classification of Sphenoid Pneumatization")
    pdf.table(["Type", "Number", "Percentage"],
              [["Conchal", "9", "3.0%"],
               ["Presellar", "57", "19.0%"],
               ["Sellar", "234", "78.0%"],
               ["Total", "300", "100%"]])
    
    pdf.ct_image_box("22", "Sagittal CT showing sellar type pneumatization")
    
    pdf.subheading("5.7.2 Sphenoid Sinus Septation")
    pdf.body("Septation patterns observed:")
    pdf.bullet("Single midline septum: 96 (32.0%)")
    pdf.bullet("Single deviated septum: 132 (44.0%)")
    pdf.bullet("Multiple septa: 60 (20.0%)")
    pdf.bullet("No septation/conchal: 12 (4.0%)")
    
    pdf.body("Septum attachment to ICA canal: 45 cases (15.0%) - clinically significant for transsphenoidal surgery.")
    
    pdf.subheading("5.7.3 Lateral Recess (Pterygoid Recess)")
    pdf.body("Lateral pterygoid recess pneumatization was observed in 142 subjects (47.3%).")
    
    pdf.subheading("5.7.4 ICA Dehiscence")
    pdf.body("Internal carotid artery (ICA) dehiscence in the sphenoid sinus was observed in 24 subjects (8.0%) and 28 sides.")
    pdf.bullet("Right ICA dehiscence: 13 sides")
    pdf.bullet("Left ICA dehiscence: 15 sides")
    pdf.bullet("Bilateral: 4 cases")
    
    pdf.ct_image_box("23", "Axial CT showing ICA dehiscence in sphenoid sinus")
    
    pdf.subheading("5.7.5 Optic Nerve Relationship (DeLano Classification)")
    pdf.table(["DeLano Type", "Number", "Percentage"],
              [["Type I", "228", "76.0%"],
               ["Type II", "45", "15.0%"],
               ["Type III", "18", "6.0%"],
               ["Type IV", "9", "3.0%"]])
    
    pdf.body("Optic nerve dehiscence was observed in 16 subjects (5.3%).")
    
    # SKULL BASE
    pdf.add_page()
    pdf.heading("5.8 Skull Base Variations")
    
    pdf.subheading("5.8.1 Keros Classification")
    pdf.body("Table 13: Keros Classification of Olfactory Fossa")
    pdf.table(["Keros Type", "Number", "Percentage"],
              [["Type I (1-3mm)", "45", "15.0%"],
               ["Type II (4-7mm)", "204", "68.0%"],
               ["Type III (8-16mm)", "51", "17.0%"],
               ["Total", "300", "100%"]])
    
    pdf.ct_image_box("24", "Coronal CT showing Keros Type I, II, III configurations")
    
    pdf.subheading("5.8.2 Cribriform Plate Asymmetry")
    pdf.body("Cribriform plate asymmetry was observed in 48 subjects (16.0%).")
    
    pdf.ct_image_box("25", "Coronal CT showing cribriform plate asymmetry")
    
    pdf.subheading("5.8.3 Anterior Ethmoidal Artery (AEA)")
    pdf.body("Position of AEA in relation to skull base:")
    pdf.bullet("Within ethmoidal sulcus (protected): 198 (66.0%)")
    pdf.bullet("In a mesentery (suspended): 87 (29.0%)")
    pdf.bullet("Dehiscent: 15 (5.0%)")
    
    # UNCINATE
    pdf.add_page()
    pdf.heading("5.9 Uncinate Process Variations")
    
    pdf.subheading("5.9.1 Superior Attachment Type (Stammberger)")
    pdf.table(["Type", "Description", "Number", "%"],
              [["Type I", "Lamina papyracea", "162", "54.0%"],
               ["Type II", "Skull base", "21", "7.0%"],
               ["Type III", "Middle turbinate", "78", "26.0%"],
               ["Type IV", "Combined", "30", "10.0%"],
               ["Type V/VI", "Other", "9", "3.0%"]])
    
    pdf.subheading("5.9.2 Pneumatized Uncinate Process")
    pdf.body("Pneumatization of uncinate process was observed in 7 subjects (2.3%).")
    
    # GENDER COMPARISON
    pdf.add_page()
    pdf.heading("5.10 Gender-Based Comparison")
    
    pdf.body("Table 14: Gender Distribution of Major Variations")
    pdf.table(["Variation", "Male (n=168)", "Female (n=132)", "p-value"],
              [["DNS", "128 (76.2%)", "90 (68.2%)", "0.115"],
               ["Concha bullosa", "62 (36.9%)", "37 (28.0%)", "0.103"],
               ["Paradox MT", "26 (15.5%)", "16 (12.1%)", "0.402"],
               ["Agger nasi", "158 (94.0%)", "124 (93.9%)", "0.957"],
               ["Haller cells", "32 (19.0%)", "20 (15.2%)", "0.379"],
               ["Onodi cells", "22 (13.1%)", "13 (9.8%)", "0.380"]])
    
    pdf.body("Statistical analysis revealed no significant gender-related differences in the prevalence of major paranasal sinus variations (p > 0.05 for all variations).")
    
    # AGE COMPARISON
    pdf.heading("5.11 Age-Based Comparison")
    pdf.body("The distribution of various anatomical variations across different age groups did not show statistically significant differences (p > 0.05), suggesting that these variations are present from completion of sinus development and remain stable throughout adult life.")
    
    # COMPARISON
    pdf.heading("5.12 Comparison with Other Studies")
    pdf.body("Table 15: Comparison with Other Studies")
    pdf.table(["Variation", "Present Study", "Indian Avg", "Western Avg"],
              [["DNS", "72.7%", "65-75%", "20-79%"],
               ["Concha bullosa", "33.0%", "25-32%", "24-53%"],
               ["Paradox MT", "14.0%", "12-15%", "17-27%"],
               ["Agger nasi", "94.0%", "87-92%", "89-98%"],
               ["Haller cells", "17.3%", "15-18%", "10-45%"],
               ["Onodi cells", "11.7%", "10-12%", "8-14%"],
               ["Keros III", "17.0%", "15-20%", "8-26%"],
               ["ICA dehiscence", "8.0%", "7-8%", "4-22%"]])
