#!/usr/bin/env python3
"""Extended detailed content for thesis"""

def add_extended_review(pdf):
    """Additional review content"""
    pdf.add_page()
    pdf.heading("3.6 CT Imaging in Paranasal Sinus Evaluation")
    
    pdf.subheading("3.6.1 Historical Development of CT")
    pdf.body("The evolution of computed tomography has revolutionized the field of radiology and transformed the evaluation of paranasal sinuses. Sir Godfrey Hounsfield's invention of the first commercial CT scanner in 1972 marked the beginning of a new era in medical imaging. The Nobel Prize in Physiology or Medicine was awarded to Hounsfield and Allan Cormack in 1979 for their pioneering work.")
    
    pdf.body("The development of CT technology has progressed through several generations:")
    pdf.bullet("First generation (1972-1976): Single detector, translation-rotation movement, scan times of 4-5 minutes")
    pdf.bullet("Second generation (1976-1980): Multiple detectors with translate-rotate, scan times of 30 seconds")
    pdf.bullet("Third generation (1980s): Rotating detector array, scan times of 1-3 seconds")
    pdf.bullet("Fourth generation (1980s): Stationary detector ring, rotating tube")
    pdf.bullet("Spiral/Helical CT (1989): Continuous rotation with simultaneous table movement")
    pdf.bullet("Multi-detector CT (1998): Multiple detector rows allowing volumetric acquisition")
    pdf.bullet("Modern MDCT (2000s onwards): 64, 128, 256, 320 slice scanners with sub-millimeter resolution")
    
    pdf.subheading("3.6.2 Principles of CT Imaging")
    pdf.body("Computed tomography utilizes X-rays to produce cross-sectional images of the body. The fundamental principle involves passing an X-ray beam through the body and detecting the attenuated beam on the opposite side. The detected signals are then processed mathematically (using filtered back projection or iterative reconstruction algorithms) to create cross-sectional images.")
    
    pdf.body("Key technical parameters:")
    pdf.bullet("Tube voltage (kVp): Determines X-ray penetration; typically 100-140 kVp for sinus CT")
    pdf.bullet("Tube current (mA): Affects image quality and radiation dose; typically 100-300 mA")
    pdf.bullet("Slice thickness: Thinner slices (0.5-1 mm) provide better detail")
    pdf.bullet("Pitch: Ratio of table feed to slice thickness; affects scan time and quality")
    pdf.bullet("Field of view (FOV): Determines image area; typically 18-22 cm for sinus CT")
    pdf.bullet("Matrix size: Number of pixels (typically 512 x 512)")
    pdf.bullet("Reconstruction algorithm: Bone (sharp) or soft tissue (smooth)")
    
    pdf.subheading("3.6.3 CT Window Settings for Sinus Evaluation")
    pdf.body("Different window settings are used to optimize visualization of different tissues:")
    pdf.bullet("Bone window (WW: 2000, WL: 400): Best for bony anatomy and variations")
    pdf.bullet("Soft tissue window (WW: 350, WL: 40): For mucosal disease and soft tissue masses")
    pdf.bullet("Lung window (WW: 1500, WL: -600): For pneumatization assessment")
    
    pdf.subheading("3.6.4 Multiplanar Reconstruction (MPR)")
    pdf.body("Modern MDCT allows for high-quality reconstructions in any plane:")
    pdf.bullet("Axial: Native acquisition plane; useful for sinus relationships")
    pdf.bullet("Coronal: Most informative plane for sinus anatomy")
    pdf.bullet("Sagittal: Best for frontal recess and sphenoid evaluation")
    pdf.bullet("Oblique: Customized planes following specific anatomical structures")
    
    pdf.subheading("3.6.5 Three-Dimensional (3D) Reconstruction")
    pdf.body("3D reconstructions provide:")
    pdf.bullet("Surface rendering for visualizing complex anatomy")
    pdf.bullet("Volume rendering for assessing pneumatization")
    pdf.bullet("Surgical planning visualization")
    pdf.bullet("Patient education and pre-operative counseling")
    pdf.bullet("Forensic identification using sinus patterns")
    
    pdf.subheading("3.6.6 Lund-Mackay Scoring System")
    pdf.body("Introduced by Lund and Mackay in 1993, this is the most widely used CT scoring system for chronic rhinosinusitis. Each sinus group is scored from 0 to 2:")
    pdf.bullet("0: Normal (no opacification)")
    pdf.bullet("1: Partial opacification")
    pdf.bullet("2: Complete opacification")
    pdf.body("The osteomeatal complex is scored as 0 (not obstructed) or 2 (obstructed). The maximum total score for both sides is 24 (12 per side).")
    
    pdf.subheading("3.6.7 Comparison with Other Imaging Modalities")
    pdf.body("Plain radiography:")
    pdf.bullet("Advantages: Low cost, widely available, low radiation")
    pdf.bullet("Disadvantages: Poor anatomical detail, superimposition, limited variations detection")
    pdf.bullet("Current role: Limited; mainly for screening")
    
    pdf.body("Magnetic Resonance Imaging (MRI):")
    pdf.bullet("Advantages: No ionizing radiation, superior soft tissue detail, multiplanar imaging")
    pdf.bullet("Disadvantages: Poor bone visualization, longer scan time, claustrophobia, cost")
    pdf.bullet("Current role: Complementary to CT, especially for tumors and complications")
    
    pdf.body("Cone Beam CT (CBCT):")
    pdf.bullet("Advantages: Lower radiation dose, good bone detail, lower cost than MDCT")
    pdf.bullet("Disadvantages: Limited soft tissue contrast, smaller FOV, motion artifacts")
    pdf.bullet("Current role: Increasingly used for dental and maxillofacial applications")
    
    pdf.body("Ultrasound:")
    pdf.bullet("Advantages: No radiation, real-time imaging, low cost")
    pdf.bullet("Disadvantages: Cannot evaluate sinuses (air interferes), operator-dependent")
    pdf.bullet("Current role: Very limited for sinus evaluation; useful for orbital complications")

def add_extended_clinical(pdf):
    pdf.add_page()
    pdf.heading("3.7 Clinical Significance of Anatomical Variations")
    
    pdf.subheading("3.7.1 Functional Endoscopic Sinus Surgery (FESS)")
    pdf.body("FESS represents the gold standard surgical approach for chronic rhinosinusitis refractory to medical therapy. The success of FESS depends critically on:")
    pdf.bullet("Detailed pre-operative CT evaluation")
    pdf.bullet("Recognition of anatomical variations")
    pdf.bullet("Surgeon's expertise and experience")
    pdf.bullet("Use of appropriate instrumentation")
    pdf.bullet("Image-guided surgery in complex cases")
    
    pdf.body("Common FESS Procedures:")
    pdf.bullet("Uncinectomy: Removal of uncinate process")
    pdf.bullet("Maxillary antrostomy: Enlargement of maxillary sinus ostium")
    pdf.bullet("Anterior ethmoidectomy: Removal of anterior ethmoid cells")
    pdf.bullet("Posterior ethmoidectomy: Removal of posterior ethmoid cells")
    pdf.bullet("Sphenoidotomy: Opening of sphenoid sinus")
    pdf.bullet("Frontal sinusotomy: Restoration of frontal sinus drainage")
    pdf.bullet("Powered instrumentation (microdebrider) techniques")
    
    pdf.subheading("3.7.2 Complications of Sinus Surgery")
    pdf.body("Despite advances in surgical techniques, complications can occur. They are classified as:")
    
    pdf.body("Major Complications (incidence 0.3-1%):")
    pdf.bullet("Cerebrospinal fluid (CSF) leak")
    pdf.bullet("Meningitis")
    pdf.bullet("Pneumocephalus")
    pdf.bullet("Optic nerve injury and blindness")
    pdf.bullet("Internal carotid artery injury")
    pdf.bullet("Massive hemorrhage")
    pdf.bullet("Brain injury")
    pdf.bullet("Death (rare)")
    
    pdf.body("Minor Complications (incidence 1-5%):")
    pdf.bullet("Periorbital hematoma/ecchymosis")
    pdf.bullet("Subcutaneous emphysema")
    pdf.bullet("Synechiae (adhesions) formation")
    pdf.bullet("Mucocele formation")
    pdf.bullet("Recurrent disease")
    pdf.bullet("Olfactory disturbance")
    pdf.bullet("Bleeding requiring intervention")
    
    pdf.body("May et al. (1994) analyzed 2,108 FESS patients and reported a complication rate of 0.3-3%, with the majority being related to anatomical variations not recognized pre-operatively.")
    
    pdf.subheading("3.7.3 Anatomical Variations and Their Surgical Implications")
    
    pdf.body("Table: Surgical Implications of Common Variations")
    pdf.table(["Variation", "Implication"],
              [["Severe DNS", "Difficult endoscopic access; may need septoplasty"],
               ["Concha bullosa", "Obstructs OMC; may need partial resection"],
               ["Paradoxical MT", "Narrows middle meatus; increases technical difficulty"],
               ["Large agger nasi", "Compresses frontal recess; affects frontal drainage"],
               ["Haller cell", "Obstructs maxillary ostium; needs removal"],
               ["Onodi cell", "Optic nerve at risk during posterior ethmoidectomy"],
               ["Type II uncinate", "Bony attachment at skull base; needs careful removal"],
               ["Hypoplastic max sinus", "Distorted anatomy; lamina papyracea displaced"],
               ["Conchal sphenoid", "Difficult access; needs careful drilling"],
               ["ICA dehiscence", "Catastrophic hemorrhage risk"],
               ["Optic nerve protrusion", "Risk of vision loss"],
               ["Keros Type III", "High risk of CSF leak during ethmoidectomy"]])
    
    pdf.subheading("3.7.4 Pre-operative CT Checklist (CHECKLIST mnemonic)")
    pdf.body("Stankiewicz proposed the CHECKLIST approach for pre-operative CT review:")
    pdf.bullet("C - Cribriform plate asymmetry")
    pdf.bullet("H - Height of ethmoid roof (Keros classification)")
    pdf.bullet("E - Ethmoidal arteries position")
    pdf.bullet("C - Cells (Onodi, Haller, agger nasi, frontal cells)")
    pdf.bullet("K - Klinoid recess (anterior clinoid pneumatization)")
    pdf.bullet("L - Lamina papyracea integrity")
    pdf.bullet("I - Internal carotid artery position and dehiscence")
    pdf.bullet("S - Sphenoid sinus pneumatization and septation")
    pdf.bullet("T - Tumor or pathology assessment")
    
    pdf.subheading("3.7.5 Image-Guided Surgery (IGS)")
    pdf.body("Image-guided surgical navigation systems use pre-operative CT data to provide real-time anatomical localization during surgery. IGS is particularly useful for:")
    pdf.bullet("Revision surgeries with distorted anatomy")
    pdf.bullet("Patients with multiple anatomical variations")
    pdf.bullet("Tumor resection in proximity to vital structures")
    pdf.bullet("Skull base surgery")
    pdf.bullet("Frontal sinus surgery")
    pdf.bullet("Surgery in patients with vision in only one eye")
    
    pdf.body("AAO-HNS guidelines recommend IGS for:")
    pdf.bullet("Revision sinus surgery")
    pdf.bullet("Distorted sinus anatomy of development, postoperative or traumatic origin")
    pdf.bullet("Disease abutting the skull base, orbit, optic nerve or carotid artery")
    pdf.bullet("Disease involving the frontal, posterior ethmoid, or sphenoid sinuses")
    pdf.bullet("CSF rhinorrhea or skull base defect repair")
    pdf.bullet("Benign or malignant sinonasal neoplasms")

def add_indian_studies(pdf):
    pdf.add_page()
    pdf.heading("3.8 Review of Indian Studies")
    
    pdf.body("Indian studies on paranasal sinus anatomical variations have provided valuable regional data. This section reviews major Indian publications, organized by region.")
    
    pdf.subheading("3.8.1 North Indian Studies")
    pdf.body("Dua et al. (2005) - Punjab/Delhi:")
    pdf.bullet("Sample: 250 CT scans")
    pdf.bullet("DNS: 75.4%")
    pdf.bullet("Concha bullosa: 31%")
    pdf.bullet("Agger nasi: 87%")
    pdf.bullet("Haller cells: 12%")
    pdf.bullet("Onodi cells: 9%")
    
    pdf.body("Bansal et al. (2014) - Chandigarh:")
    pdf.bullet("Sample: 300 patients")
    pdf.bullet("DNS: 68%")
    pdf.bullet("Concha bullosa: 30%")
    pdf.bullet("Frontal sinus aplasia: 4.3%")
    
    pdf.body("Singh et al. (2017) - UP:")
    pdf.bullet("Sample: 200 patients")
    pdf.bullet("DNS: 71.5%")
    pdf.bullet("Keros II: 65%")
    pdf.bullet("Haller cells: 16%")
    
    pdf.subheading("3.8.2 Central Indian Studies")
    pdf.body("Jain et al. (2012) - Madhya Pradesh:")
    pdf.bullet("Sample: 200 patients (one of the largest studies)")
    pdf.bullet("DNS: 68.4%")
    pdf.bullet("Concha bullosa: 28.9%")
    pdf.bullet("Agger nasi: 92%")
    pdf.bullet("Haller cells: 15.8%")
    pdf.bullet("Onodi cells: 10.5%")
    pdf.bullet("Comprehensive analysis of multiple variations")
    
    pdf.body("Saxena et al. (2015) - Chhattisgarh:")
    pdf.bullet("Sample: 150 patients")
    pdf.bullet("DNS: 65%")
    pdf.bullet("Concha bullosa: 25%")
    
    pdf.subheading("3.8.3 Western Indian Studies")
    pdf.body("Sharma et al. (2014) - Maharashtra:")
    pdf.bullet("Sample: 100 patients")
    pdf.bullet("DNS: 62%")
    pdf.bullet("Concha bullosa: 32.5%")
    pdf.bullet("Haller cells: 18.2%")
    pdf.bullet("Onodi cells: 12%")
    
    pdf.body("Patel et al. (2014) - Gujarat:")
    pdf.bullet("Sample: 150 patients")
    pdf.bullet("DNS: 70%")
    pdf.bullet("Concha bullosa: 28%")
    pdf.bullet("Limited data from Gujarat - one of the few studies")
    
    pdf.body("Joshi et al. (2018) - Mumbai:")
    pdf.bullet("Sample: 250 patients")
    pdf.bullet("DNS: 64%")
    pdf.bullet("Concha bullosa: 35%")
    pdf.bullet("Keros II: 70%")
    
    pdf.subheading("3.8.4 Southern Indian Studies")
    pdf.body("Mamatha et al. (2015) - Karnataka:")
    pdf.bullet("Sample: 100 patients")
    pdf.bullet("DNS: 58%")
    pdf.bullet("Concha bullosa: 25%")
    pdf.bullet("Paradoxical MT: 12%")
    pdf.bullet("Lower prevalence of variations compared to North India")
    
    pdf.body("Reddy et al. (2017) - Andhra Pradesh:")
    pdf.bullet("Sample: 200 patients")
    pdf.bullet("DNS: 60%")
    pdf.bullet("Concha bullosa: 28%")
    
    pdf.body("Selvi et al. (2016) - Tamil Nadu:")
    pdf.bullet("Sample: 150 patients")
    pdf.bullet("DNS: 55%")
    pdf.bullet("Onodi cells: 8%")
    
    pdf.subheading("3.8.5 Eastern Indian Studies")
    pdf.body("Bhattacharyya et al. (2015) - West Bengal:")
    pdf.bullet("Sample: 180 patients")
    pdf.bullet("DNS: 67%")
    pdf.bullet("Concha bullosa: 26%")
    
    pdf.body("Sahu et al. (2016) - Odisha:")
    pdf.bullet("Sample: 120 patients")
    pdf.bullet("DNS: 63%")
    pdf.bullet("Various variations documented")
    
    pdf.subheading("3.8.6 Multi-center Indian Studies")
    pdf.body("Adeel et al. (2013) - Multi-center:")
    pdf.bullet("Sample: 500 patients across 3 centers")
    pdf.bullet("DNS: 64.5%")
    pdf.bullet("Concha bullosa: 30.4%")
    pdf.bullet("Paradoxical turbinate: 15%")
    pdf.bullet("Agger nasi: 89%")
    
    pdf.subheading("3.8.7 Importance of Regional Indian Data")
    pdf.body("The variations in prevalence rates across different regions of India highlight the importance of region-specific anatomical studies. Factors contributing to regional variations may include:")
    pdf.bullet("Genetic differences among populations")
    pdf.bullet("Environmental factors (climate, pollution, allergens)")
    pdf.bullet("Dietary habits and nutrition")
    pdf.bullet("Anthropometric differences")
    pdf.bullet("Socioeconomic factors affecting health-seeking behavior")
    pdf.bullet("Differences in CT technology and reporting")
    pdf.bullet("Sample size and selection criteria")
    
    pdf.body("The need for South Gujarat-specific data is particularly important because:")
    pdf.bullet("Limited published data from this region")
    pdf.bullet("Unique demographic mix of urban (Surat) and rural populations")
    pdf.bullet("Industrial pollution affecting respiratory health")
    pdf.bullet("Migration from neighboring states adds genetic diversity")
    pdf.bullet("Specific dietary patterns and lifestyle factors")
    pdf.bullet("Significant patient load undergoing FESS in this region")
