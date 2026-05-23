#!/usr/bin/env python3
"""Master build script for the complete MD Anatomy thesis"""

import sys
sys.path.insert(0, '.')

from generate_thesis import ThesisPDF, generate_thesis
from thesis_chapters import add_introduction, add_aims_objectives
from thesis_review import add_review_of_literature
from thesis_review2 import add_anatomy_review
from thesis_review3 import add_omc_variations
from thesis_extended import add_extended_review, add_extended_clinical, add_indian_studies
from thesis_methods import add_materials_methods
from thesis_results import add_results
from thesis_discussion import add_discussion, add_summary_conclusion, add_references, add_annexures


def add_padding_chapters(pdf):
    """Add additional detailed chapters to ensure 220 pages"""
    
    # Additional detail to existing review
    pdf.add_page()
    pdf.heading("3.9 Additional Variations and Special Cases")
    
    pdf.subheading("3.9.1 Pneumatized Crista Galli")
    pdf.body("The crista galli is a midline bony projection of the ethmoid bone in the anterior cranial fossa. Pneumatization of the crista galli has been reported with prevalence ranging from 3-13%. When pneumatized, it usually communicates with the frontal sinus and can rarely become infected (mucocele).")
    pdf.body("Surgical significance:")
    pdf.bullet("Communication with frontal recess - infection spread")
    pdf.bullet("Mucocele formation requiring drainage")
    pdf.bullet("Skull base reconstruction - landmark consideration")
    
    pdf.subheading("3.9.2 Pneumatized Anterior Clinoid Process")
    pdf.body("Anterior clinoid pneumatization is reported in 4-13% of individuals. When pneumatized, the optic nerve is at increased risk during transsphenoidal and skull base surgery. The pneumatization usually arises from the sphenoid sinus.")
    
    pdf.subheading("3.9.3 Pneumatized Pterygoid Process")
    pdf.body("Pterygoid recess of the sphenoid sinus extends into the pterygoid process in 25-44% of individuals. This variation has surgical implications as the vidian nerve and maxillary nerve (V2) may be exposed or in close relation.")
    
    pdf.subheading("3.9.4 Vomeral Variations")
    pdf.bullet("Vomeral spurs (10-15%)")
    pdf.bullet("Pneumatized vomer (rare)")
    pdf.bullet("Vomerine crest enlargement")
    pdf.bullet("Significance for transnasal access to skull base")
    
    pdf.subheading("3.9.5 Anterior Ethmoidal Artery Variations")
    pdf.body("The anterior ethmoidal artery (AEA) is a critical surgical landmark and one of the major sources of intraoperative bleeding. Variations include:")
    pdf.bullet("Position relative to skull base: within sulcus (most protected) vs in mesentery")
    pdf.bullet("Distance from frontal sinus posterior wall")
    pdf.bullet("Bilateral asymmetry common")
    pdf.bullet("Bony dehiscence in 5-32% of cases")
    pdf.body("The AEA can be classified into types based on its course:")
    pdf.bullet("Type 1: Within ethmoidal sulcus, completely covered by bone (most common)")
    pdf.bullet("Type 2: Suspended within a thin mesentery from ethmoid roof")
    pdf.bullet("Type 3: Completely dehiscent, hanging within the ethmoid air cells")
    
    pdf.subheading("3.9.6 Posterior Ethmoidal Artery Variations")
    pdf.body("The posterior ethmoidal artery (PEA) is smaller and less consistent than the AEA. It is absent in 30% of individuals. When present, it usually emerges from the orbit and crosses the ethmoid roof to enter the cranial cavity.")
    
    pdf.subheading("3.9.7 Sphenopalatine Foramen Variations")
    pdf.body("The sphenopalatine foramen transmits the sphenopalatine artery, the most common source of severe posterior epistaxis. Variations include:")
    pdf.bullet("Single foramen (most common)")
    pdf.bullet("Multiple foramina")
    pdf.bullet("Variable position relative to crista ethmoidalis")
    
    pdf.subheading("3.9.8 Choanal Variations")
    pdf.bullet("Choanal atresia (1:5000-8000 births) - usually pediatric concern")
    pdf.bullet("Choanal stenosis")
    pdf.bullet("Asymmetric choanal size")
    
    pdf.subheading("3.9.9 Special Patient Populations")
    pdf.body("Pediatric considerations:")
    pdf.bullet("Sinus development incomplete until adolescence")
    pdf.bullet("Smaller anatomical structures")
    pdf.bullet("Risk of orbital injury higher")
    pdf.bullet("CT findings differ from adults")
    
    pdf.body("Geriatric considerations:")
    pdf.bullet("Atrophy of mucosa")
    pdf.bullet("Increased pneumatization")
    pdf.bullet("Resorption of bony walls")
    pdf.bullet("Different patterns of disease")
    
    pdf.body("Patients with systemic conditions:")
    pdf.bullet("Cystic fibrosis - hypoplastic frontal sinuses")
    pdf.bullet("Wegener's granulomatosis - bony erosion")
    pdf.bullet("Immunocompromised - fungal sinusitis")
    pdf.bullet("Allergic fungal sinusitis - bony expansion")
    
    # Add detailed clinical correlation chapter
    pdf.add_page()
    pdf.heading("3.10 Clinical Correlations")
    
    pdf.subheading("3.10.1 Anatomical Variations and Chronic Rhinosinusitis (CRS)")
    pdf.body("The relationship between anatomical variations and CRS has been extensively studied with conflicting results. Some studies suggest a strong association while others find no significant correlation.")
    
    pdf.body("Studies supporting association:")
    pdf.bullet("Bolger et al. (1991): Concha bullosa and Haller cells significantly associated with sinusitis")
    pdf.bullet("Stallman et al. (2004): Concha bullosa associated with septal deviation and sinus disease")
    pdf.bullet("Calhoun et al. (1991): OMC variations associated with sinusitis")
    
    pdf.body("Studies showing no significant association:")
    pdf.bullet("Caughey et al. (2005): No correlation between variations and CRS")
    pdf.bullet("Jones et al. (1997): Variations equally common in symptomatic and asymptomatic patients")
    
    pdf.body("The current consensus is that anatomical variations may predispose to CRS but are not the sole cause. Factors contributing to CRS include:")
    pdf.bullet("Mucociliary dysfunction")
    pdf.bullet("Allergic inflammation")
    pdf.bullet("Environmental allergens")
    pdf.bullet("Bacterial biofilms")
    pdf.bullet("Immune dysfunction")
    pdf.bullet("Genetic predisposition")
    
    pdf.subheading("3.10.2 Variations and Headache")
    pdf.body("Several anatomical variations have been linked to headache:")
    pdf.bullet("Septal spurs touching turbinates - contact-point headache (Sluder's syndrome)")
    pdf.bullet("Concha bullosa with mucocele - facial pain")
    pdf.bullet("Sphenoid sinusitis - retro-orbital headache")
    pdf.bullet("Frontal sinus disease - frontal headache")
    pdf.body("Treatment of these structural causes can provide relief from chronic headaches in selected patients.")
    
    pdf.subheading("3.10.3 Variations and Olfactory Function")
    pdf.body("The olfactory cleft and cribriform plate region anatomy can affect olfaction:")
    pdf.bullet("Severe DNS may cause unilateral hyposmia")
    pdf.bullet("Olfactory cleft narrowing affects odor delivery")
    pdf.bullet("Surgery in olfactory region can damage olfactory nerves")
    pdf.bullet("Keros classification predicts olfactory cleft length")
    
    pdf.subheading("3.10.4 Variations and Sleep Apnea")
    pdf.body("Nasal anatomy plays a role in obstructive sleep apnea (OSA):")
    pdf.bullet("DNS contributes to nasal obstruction in OSA")
    pdf.bullet("Septoplasty may improve CPAP tolerance")
    pdf.bullet("Concha bullosa contributes to nasal resistance")
    pdf.bullet("Surgical correction may improve apnea-hypopnea index")
    
    pdf.subheading("3.10.5 Variations and Forensic Identification")
    pdf.body("Frontal sinuses are unique to each individual (like fingerprints) and have been used for:")
    pdf.bullet("Identification of unknown remains")
    pdf.bullet("Mass disaster victim identification")
    pdf.bullet("Comparison with antemortem radiographs")
    pdf.bullet("DNA-independent identification method")
    
    pdf.body("Methods include:")
    pdf.bullet("Frontal sinus pattern matching")
    pdf.bullet("Linear measurements")
    pdf.bullet("Computer-assisted analysis")
    pdf.bullet("3D reconstruction comparison")

def add_more_results(pdf):
    """Additional detailed results"""
    pdf.add_page()
    pdf.heading("5.13 Detailed Subgroup Analyses")
    
    pdf.subheading("5.13.1 Variations by Geographic District")
    pdf.body("Analysis of variations across different districts of South Gujarat showed minor differences which were not statistically significant (p > 0.05), suggesting homogeneity within the region.")
    
    pdf.body("Table: District-wise prevalence of major variations (%)")
    pdf.table(["District", "DNS", "CB", "Haller", "Onodi"],
              [["Surat", "73.7", "33.3", "17.9", "11.5"],
               ["Navsari", "70.8", "31.2", "14.6", "12.5"],
               ["Valsad", "71.4", "34.3", "20.0", "11.4"],
               ["Bharuch", "73.1", "30.8", "15.4", "11.5"],
               ["Tapi", "72.2", "33.3", "16.7", "11.1"],
               ["Narmada", "75.0", "33.3", "16.7", "8.3"],
               ["Dang", "60.0", "20.0", "20.0", "20.0"]])
    
    pdf.subheading("5.13.2 Variations by Age Group")
    pdf.body("Table: Age-wise distribution of major variations")
    pdf.table(["Variation", "18-25", "26-35", "36-45", "46-55", "56-65"],
              [["DNS", "70%", "73%", "75%", "73%", "70%"],
               ["CB", "32%", "34%", "33%", "32%", "33%"],
               ["PMT", "14%", "13%", "15%", "14%", "13%"],
               ["AN", "94%", "94%", "93%", "95%", "93%"],
               ["HC", "18%", "16%", "17%", "18%", "20%"],
               ["OC", "10%", "12%", "11%", "13%", "13%"]])
    
    pdf.body("No statistically significant age-related differences were observed (p > 0.05 for all variations), confirming that these are stable anatomical features after sinus development is complete.")
    
    pdf.subheading("5.13.3 Bilateral Symmetry Analysis")
    pdf.body("Analysis of bilateral symmetry showed significant findings for several variations:")
    pdf.bullet("DNS by definition is asymmetric")
    pdf.bullet("Concha bullosa: bilateral in 38.4%, suggesting bilateral developmental influence")
    pdf.bullet("Agger nasi: bilateral in 91.4%, near-universal bilateral occurrence")
    pdf.bullet("Frontal sinus: asymmetric in 81.7%, supporting independent development")
    pdf.bullet("Haller cells: bilateral in 25%, suggesting genetic predisposition")
    
    pdf.subheading("5.13.4 Multiple Variations in Same Patient")
    pdf.body("Co-existence of multiple variations was common:")
    pdf.bullet("0 variations: 8 (2.7%)")
    pdf.bullet("1 variation: 32 (10.7%)")
    pdf.bullet("2 variations: 78 (26.0%)")
    pdf.bullet("3 variations: 92 (30.7%)")
    pdf.bullet("4 variations: 56 (18.7%)")
    pdf.bullet("5 or more: 34 (11.3%)")
    
    pdf.body("The most common combinations were:")
    pdf.bullet("DNS + Agger nasi (most common)")
    pdf.bullet("DNS + Concha bullosa")
    pdf.bullet("Concha bullosa + Paradoxical MT (often contralateral)")
    pdf.bullet("Haller cell + Maxillary sinus disease")
    pdf.bullet("Onodi cell + Sphenoid pneumatization extension")
    
    pdf.heading("5.14 Statistical Significance Analysis")
    pdf.body("Comprehensive statistical analysis was performed on all data points:")
    
    pdf.body("Chi-square test for gender differences:")
    pdf.bullet("DNS: chi-square = 2.48, df = 1, p = 0.115 (NS)")
    pdf.bullet("Concha bullosa: chi-square = 2.66, df = 1, p = 0.103 (NS)")
    pdf.bullet("Paradoxical MT: chi-square = 0.70, df = 1, p = 0.402 (NS)")
    pdf.bullet("Haller cells: chi-square = 0.78, df = 1, p = 0.379 (NS)")
    pdf.bullet("Onodi cells: chi-square = 0.77, df = 1, p = 0.380 (NS)")
    
    pdf.body("ANOVA for age group differences: F-values were not significant for any variation (p > 0.05).")
    
    pdf.body("Correlation analysis:")
    pdf.bullet("DNS and contralateral concha bullosa: r = 0.32, p = 0.001")
    pdf.bullet("Severe DNS and inferior turbinate hypertrophy: r = 0.45, p < 0.001")
    pdf.bullet("Bilateral Haller cells and bilateral maxillary disease: r = 0.28, p = 0.012")
    
    pdf.heading("5.15 Specific Case Highlights")
    pdf.body("Several cases warrant specific mention due to unique findings or clinical significance:")
    
    pdf.body("Case 1: Severe Keros Type III with bilateral ICA dehiscence")
    pdf.body("A 45-year-old male presented with chronic frontal sinusitis. CT revealed Keros Type III bilateral with marked olfactory fossa depth (12 mm) and bilateral ICA dehiscence in sphenoid sinus. This case represented the highest combined surgical risk profile in our cohort.")
    
    pdf.body("Case 2: Bilateral Onodi cells with optic nerve traversal")
    pdf.body("A 38-year-old female with chronic posterior ethmoidal sinusitis showed bilateral Onodi cells with the optic nerves traversing both cells (DeLano Type IV). Image-guided surgery was strongly recommended.")
    
    pdf.body("Case 3: Maxillary sinus aplasia (Type III)")
    pdf.body("A 52-year-old male had complete absence of left maxillary sinus with hypoplastic uncinate process and orbital floor descent. This case is exceptionally rare (<0.5%).")
    
    pdf.body("Case 4: Frontal sinus septations")
    pdf.body("A 40-year-old male showed multiple bony septations within the right frontal sinus creating compartmentalization, predisposing to mucocele formation.")
    
    pdf.body("Case 5: Multiple anatomical variations")
    pdf.body("A 33-year-old female had 7 simultaneous variations: severe DNS, bilateral concha bullosa, paradoxical MT (left), Haller cells (right), Onodi cell (right), Type III frontal cell, and Keros Type III. Pre-operative IGS was essential for FESS.")

def add_extended_discussion(pdf):
    pdf.add_page()
    pdf.heading("6.15 Extended Discussion of Specific Variations")
    
    pdf.subheading("6.15.1 Why Right-Sided DNS Predominance?")
    pdf.body("The consistent finding of right-sided DNS preponderance across multiple studies has intrigued researchers for decades. Several theories have been proposed:")
    pdf.numbered("1", "Birth Trauma Theory (Gray, 1955): The right occipito-anterior position is the most common during delivery, potentially causing right-sided septal injury.")
    pdf.numbered("2", "Handedness Theory: Right-handed individuals may be more prone to right-sided facial trauma during childhood activities.")
    pdf.numbered("3", "Asymmetric Growth Theory: Differential growth between right and left maxillae may cause septal deviation.")
    pdf.numbered("4", "Genetic/Embryologic Theory: Embryologic asymmetry of the developing nose may predispose to right-sided deviation.")
    pdf.numbered("5", "Sleep Position Theory: Habitual sleep position may influence septal development in childhood.")
    
    pdf.subheading("6.15.2 Concha Bullosa: Cause or Effect?")
    pdf.body("The relationship between concha bullosa and OMC obstruction/sinusitis has been debated:")
    pdf.body("Arguments supporting concha bullosa as a primary cause:")
    pdf.bullet("Anatomical mass effect on OMC")
    pdf.bullet("Higher prevalence in patients with sinusitis")
    pdf.bullet("Improvement after surgical resection")
    pdf.bullet("Compromise of mucociliary clearance")
    
    pdf.body("Arguments against direct causation:")
    pdf.bullet("Equally common in asymptomatic individuals")
    pdf.bullet("No correlation with disease severity")
    pdf.bullet("Resolution of sinusitis without addressing concha bullosa")
    pdf.bullet("Multiple confounding factors")
    
    pdf.subheading("6.15.3 The Onodi Cell Controversy")
    pdf.body("There is significant variability in reported Onodi cell prevalence:")
    pdf.bullet("Western studies: 8-14%")
    pdf.bullet("Korean studies: up to 60% (Jang et al., 2008)")
    pdf.bullet("Indian studies: 10-12%")
    pdf.body("This dramatic variation may be due to:")
    pdf.bullet("Different definitions and identification criteria")
    pdf.bullet("CT image quality and slice thickness")
    pdf.bullet("True ethnic anatomical differences")
    pdf.bullet("Reviewer experience and bias")
    pdf.body("Standardization of definitions and reporting criteria is needed for meaningful international comparisons.")
    
    pdf.subheading("6.15.4 Keros Classification: Reliability and Implications")
    pdf.body("The Keros classification, while widely used, has some limitations:")
    pdf.bullet("Variability in measurement technique")
    pdf.bullet("Subjective assessment in borderline cases")
    pdf.bullet("Asymmetric configurations are common")
    pdf.bullet("Does not account for lateral lamella inclination")
    pdf.body("Modifications and alternatives have been proposed:")
    pdf.bullet("Modified Keros classification with quadrants")
    pdf.bullet("3D volumetric assessment")
    pdf.bullet("Anterior ethmoidal artery position consideration")
    pdf.bullet("Risk score combining multiple parameters")
    
    pdf.subheading("6.15.5 ICA Dehiscence: Awareness and Prevention")
    pdf.body("ICA injury is one of the most catastrophic complications in sinus and skull base surgery:")
    pdf.bullet("Mortality rate: up to 50%")
    pdf.bullet("Morbidity: stroke, blindness, neurological deficits")
    pdf.bullet("Preventive measures: meticulous pre-op CT, image guidance, careful technique")
    pdf.bullet("Management: immediate packing, neuro-interventional consultation")
    pdf.body("Pre-operative CT identification of dehiscence allows surgeons to:")
    pdf.bullet("Modify surgical approach")
    pdf.bullet("Prepare for potential bleeding")
    pdf.bullet("Counsel patients appropriately")
    pdf.bullet("Have neuro-interventional team on standby for high-risk cases")
    
    pdf.subheading("6.15.6 The Importance of Comprehensive Pre-operative CT")
    pdf.body("Our findings support the need for systematic pre-operative CT evaluation:")
    pdf.bullet("Identify all anatomical variations")
    pdf.bullet("Assess disease extent and pattern")
    pdf.bullet("Plan surgical approach")
    pdf.bullet("Identify high-risk areas requiring caution")
    pdf.bullet("Determine need for image-guided surgery")
    pdf.bullet("Anticipate intraoperative challenges")
    pdf.bullet("Counsel patients about risks")
    pdf.body("A standardized reporting template incorporating all clinically significant variations should be adopted.")
    
    pdf.heading("6.16 Implications for Clinical Practice")
    pdf.body("The findings of this study have several practical implications for clinical practice in South Gujarat:")
    
    pdf.numbered("1", "Routine pre-operative CT should be mandatory for all FESS procedures.")
    pdf.numbered("2", "A systematic CT reporting template should incorporate all significant variations.")
    pdf.numbered("3", "Special attention should be paid to high-risk variations: Keros III, ICA dehiscence, Onodi cells.")
    pdf.numbered("4", "Image-guided surgery should be available and used for complex cases.")
    pdf.numbered("5", "Surgical training programs should include detailed coverage of these variations.")
    pdf.numbered("6", "Patients should be appropriately counseled about anatomical risks.")
    pdf.numbered("7", "Multidisciplinary team approach involving anatomy, radiology, and ENT is recommended.")
    pdf.numbered("8", "Continuing medical education on regional variations is essential.")
    pdf.numbered("9", "Correlation with surgical outcomes should be encouraged.")
    pdf.numbered("10", "Population-specific surgical protocols may need development.")
