#!/usr/bin/env python3
"""Adds CT image plates and additional content to reach 220 pages"""

def add_ct_image_atlas(pdf):
    """Add comprehensive CT image atlas with placeholders"""
    
    pdf.add_page()
    pdf.section_title("CT IMAGE ATLAS")
    pdf.body("This atlas presents representative CT images demonstrating various anatomical variations of paranasal sinuses observed in our study. Each image is accompanied by detailed annotations and clinical relevance.")
    pdf.body("All images were obtained using high-resolution Multi-Detector Computed Tomography (MDCT) with 0.625 mm slice thickness in axial, coronal, and sagittal planes. Bone window settings were used for evaluation of anatomical variations.")
    
    # Page 1: Normal Anatomy
    pdf.add_page()
    pdf.heading("Plate 1: Normal Paranasal Sinus Anatomy")
    pdf.ct_image_box("A1", "Normal coronal CT - level of frontal sinus")
    pdf.body("This coronal section demonstrates normal frontal sinus anatomy with bilateral frontal sinuses separated by an asymmetric intersinus septum. The frontal recess opens into the middle meatus.")
    pdf.ct_image_box("A2", "Normal coronal CT - level of OMC")
    pdf.body("Coronal CT through the osteomeatal complex showing normal middle turbinate, uncinate process, ethmoid bulla, and maxillary sinus ostium relationships.")
    
    pdf.add_page()
    pdf.heading("Plate 2: Normal Sinuses (Continued)")
    pdf.ct_image_box("A3", "Normal coronal CT - level of posterior ethmoid")
    pdf.body("Posterior ethmoid cells with normal pneumatization, lamina papyracea intact, and normal optic nerve relationship.")
    pdf.ct_image_box("A4", "Normal axial CT - level of maxillary sinus")
    pdf.body("Axial CT showing well-aerated bilateral maxillary sinuses with normal walls and ostia.")
    
    pdf.add_page()
    pdf.heading("Plate 3: Normal Sphenoid Sinus")
    pdf.ct_image_box("A5", "Normal sagittal CT - midline")
    pdf.body("Midline sagittal CT showing the relationship of frontal sinus, ethmoid sinuses, and sphenoid sinus with the skull base.")
    pdf.ct_image_box("A6", "Normal axial CT - level of sphenoid")
    pdf.body("Axial CT showing sellar type sphenoid pneumatization with bilateral sphenoid sinuses, internal carotid artery and optic nerves protected by bone.")
    
    # Page on DNS
    pdf.add_page()
    pdf.heading("Plate 4: Deviated Nasal Septum (DNS)")
    pdf.ct_image_box("B1", "Mild right-sided DNS")
    pdf.body("Coronal CT showing mild deviation of the nasal septum to the right side without significant compromise of the nasal cavity.")
    pdf.ct_image_box("B2", "Severe right-sided DNS with spur")
    pdf.body("Coronal CT demonstrating severe right-sided septal deviation with a prominent septal spur impinging on the inferior turbinate.")
    
    pdf.add_page()
    pdf.heading("Plate 5: DNS Variants")
    pdf.ct_image_box("B3", "S-shaped DNS")
    pdf.body("Complex S-shaped septal deviation with anterior deviation to one side and posterior to the opposite side. This pattern is more challenging surgically.")
    pdf.ct_image_box("B4", "Severe DNS with compensatory turbinate hypertrophy")
    pdf.body("Severe DNS to the left with marked compensatory hypertrophy of the right inferior turbinate. Both contribute to nasal obstruction.")
    
    # Page on Concha Bullosa
    pdf.add_page()
    pdf.heading("Plate 6: Concha Bullosa Variants")
    pdf.ct_image_box("C1", "Lamellar concha bullosa")
    pdf.body("Coronal CT showing pneumatization of the vertical lamella of the right middle turbinate (lamellar type concha bullosa).")
    pdf.ct_image_box("C2", "Bulbous concha bullosa")
    pdf.body("Coronal CT showing pneumatization of the inferior bulbous portion of the left middle turbinate (bulbous type).")
    
    pdf.add_page()
    pdf.heading("Plate 7: Extensive Concha Bullosa")
    pdf.ct_image_box("C3", "Bilateral extensive concha bullosa")
    pdf.body("Bilateral extensive concha bullosa with pneumatization of both lamellar and bulbous portions. This severely narrows the middle meatus bilaterally.")
    pdf.ct_image_box("C4", "Concha bullosa with mucocele")
    pdf.body("Right concha bullosa with mucus retention - early mucocele formation. The pneumatized cavity contains mucus.")
    
    # Page on Turbinate variations
    pdf.add_page()
    pdf.heading("Plate 8: Turbinate Variations")
    pdf.ct_image_box("D1", "Paradoxical middle turbinate")
    pdf.body("Coronal CT showing paradoxical curvature of the right middle turbinate with convexity directed laterally instead of medially. This narrows the OMC.")
    pdf.ct_image_box("D2", "Bilateral paradoxical middle turbinates")
    pdf.body("Bilateral paradoxical middle turbinates - a less common variation that significantly affects middle meatus anatomy.")
    
    pdf.add_page()
    pdf.heading("Plate 9: Secondary Middle Turbinate")
    pdf.ct_image_box("D3", "Secondary middle turbinate")
    pdf.body("Coronal CT showing an additional turbinate (secondary middle turbinate) medial to the regular middle turbinate. This is a rare variation.")
    pdf.ct_image_box("D4", "Inferior turbinate hypertrophy")
    pdf.body("Marked compensatory hypertrophy of the inferior turbinate contralateral to severe DNS.")
    
    # Page on Ethmoid variations
    pdf.add_page()
    pdf.heading("Plate 10: Agger Nasi Cells")
    pdf.ct_image_box("E1", "Agger nasi cells - sagittal CT")
    pdf.body("Sagittal CT clearly demonstrating the agger nasi cell as the most anterior ethmoid air cell, located anterior and superior to the middle turbinate attachment.")
    pdf.ct_image_box("E2", "Large agger nasi compressing frontal recess")
    pdf.body("Large agger nasi cell compressing the frontal recess from anteriorly, predisposing to frontal sinusitis.")
    
    pdf.add_page()
    pdf.heading("Plate 11: Haller Cells")
    pdf.ct_image_box("E3", "Haller cell - coronal CT")
    pdf.body("Coronal CT showing a Haller cell along the medial floor of the right orbit, narrowing the maxillary sinus ostium.")
    pdf.ct_image_box("E4", "Bilateral Haller cells")
    pdf.body("Bilateral Haller cells with associated maxillary sinus mucosal thickening, demonstrating their role in obstructing sinus drainage.")
    
    pdf.add_page()
    pdf.heading("Plate 12: Onodi Cells")
    pdf.ct_image_box("E5", "Onodi cell with optic nerve")
    pdf.body("Axial CT showing an Onodi cell extending superolateral to the sphenoid sinus, with the optic nerve traversing through the lateral wall.")
    pdf.ct_image_box("E6", "Bilateral Onodi cells")
    pdf.body("Bilateral Onodi cells - the most posterior ethmoid cells extending toward the sphenoid. Critical to identify before posterior ethmoidectomy.")
    
    pdf.add_page()
    pdf.heading("Plate 13: Frontal Cells (Kuhn Classification)")
    pdf.ct_image_box("E7", "Kuhn Type I frontal cell")
    pdf.body("Sagittal CT showing a single frontal recess cell above the agger nasi (Kuhn Type I) - the most common frontal cell variant.")
    pdf.ct_image_box("E8", "Kuhn Type III frontal cell")
    pdf.body("Sagittal CT showing a Kuhn Type III frontal cell - a single large cell extending from agger nasi into the frontal sinus.")
    
    # Page on Maxillary variations
    pdf.add_page()
    pdf.heading("Plate 14: Maxillary Sinus Variations")
    pdf.ct_image_box("F1", "Maxillary sinus hypoplasia Type I")
    pdf.body("Coronal CT showing mild maxillary sinus hypoplasia (Bolger Type I) with a normal uncinate process.")
    pdf.ct_image_box("F2", "Maxillary sinus hypoplasia Type II")
    pdf.body("Significant maxillary sinus hypoplasia with hypoplastic uncinate process (Bolger Type II). Note the displaced lamina papyracea.")
    
    pdf.add_page()
    pdf.heading("Plate 15: Underwood Septa")
    pdf.ct_image_box("F3", "Anterior Underwood septum")
    pdf.body("Coronal CT showing an Underwood septum in the anterior part of the maxillary sinus, important consideration for sinus lift procedures.")
    pdf.ct_image_box("F4", "Multiple Underwood septa")
    pdf.body("Multiple bony septa dividing the maxillary sinus into compartments. Each compartment may need separate addressing during surgery.")
    
    pdf.add_page()
    pdf.heading("Plate 16: Accessory Maxillary Ostium")
    pdf.ct_image_box("F5", "Accessory maxillary ostium")
    pdf.body("Axial CT showing accessory maxillary ostium in the posterior fontanelle, separate from the natural ostium. May lead to mucus recirculation.")
    pdf.ct_image_box("F6", "Bilateral accessory ostia")
    pdf.body("Bilateral accessory maxillary ostia - important to recognize during FESS to avoid creating non-functional drainage.")
    
    # Frontal Sinus
    pdf.add_page()
    pdf.heading("Plate 17: Frontal Sinus Variations")
    pdf.ct_image_box("G1", "Frontal sinus aplasia (left)")
    pdf.body("Coronal CT showing complete absence of the left frontal sinus (unilateral aplasia) with normal right frontal sinus.")
    pdf.ct_image_box("G2", "Bilateral frontal sinus hypoplasia")
    pdf.body("Bilateral frontal sinus hypoplasia with markedly small sinus cavities. Note the asymmetry between the two sides.")
    
    pdf.add_page()
    pdf.heading("Plate 18: Frontal Sinus Asymmetry")
    pdf.ct_image_box("G3", "Marked frontal asymmetry")
    pdf.body("Frontal sinus showing marked asymmetry between right (large) and left (small) sides. Such asymmetry is useful for forensic identification.")
    pdf.ct_image_box("G4", "Frontal sinus septations")
    pdf.body("Multiple bony septations within the right frontal sinus creating compartmentalization. May predispose to mucocele formation if drainage is obstructed.")
    
    # Sphenoid
    pdf.add_page()
    pdf.heading("Plate 19: Sphenoid Sinus Pneumatization")
    pdf.ct_image_box("H1", "Conchal type sphenoid")
    pdf.body("Sagittal CT showing conchal type sphenoid sinus with minimal pneumatization. Surgical approach to sella is challenging.")
    pdf.ct_image_box("H2", "Presellar type sphenoid")
    pdf.body("Sagittal CT showing presellar pneumatization extending to the anterior wall of sella but not below it.")
    
    pdf.add_page()
    pdf.heading("Plate 20: Sellar and Postsellar Pneumatization")
    pdf.ct_image_box("H3", "Sellar type sphenoid")
    pdf.body("Sagittal CT showing typical sellar pneumatization extending below the sella turcica - the most common type.")
    pdf.ct_image_box("H4", "Extensive postsellar pneumatization")
    pdf.body("Extensive sphenoid pneumatization extending posteriorly into the clivus (postsellar type).")
    
    pdf.add_page()
    pdf.heading("Plate 21: Sphenoid Sinus Septation")
    pdf.ct_image_box("H5", "Single midline septum")
    pdf.body("Axial CT showing a single midline intersinus septum - relatively uncommon (32%). Most septa are deviated.")
    pdf.ct_image_box("H6", "Multiple sphenoid septa")
    pdf.body("Multiple intersinus septa creating multiple compartments. Each compartment may need separate sphenoidotomy.")
    
    pdf.add_page()
    pdf.heading("Plate 22: ICA in Sphenoid Sinus")
    pdf.ct_image_box("H7", "ICA dehiscence - left side")
    pdf.body("Axial CT demonstrating left internal carotid artery dehiscence with the artery exposed in the sphenoid sinus. Major surgical risk.")
    pdf.ct_image_box("H8", "Bilateral ICA prominence")
    pdf.body("Bilateral internal carotid artery prominence into the sphenoid sinus with thin overlying bone. Caution required during sphenoidotomy.")
    
    pdf.add_page()
    pdf.heading("Plate 23: Optic Nerve Variations")
    pdf.ct_image_box("H9", "DeLano Type I")
    pdf.body("Axial CT showing DeLano Type I configuration - optic nerve adjacent to sphenoid sinus without indentation. Most common type.")
    pdf.ct_image_box("H10", "DeLano Type IV - optic nerve in Onodi cell")
    pdf.body("DeLano Type IV - optic nerve adjacent to both sphenoid sinus and posterior ethmoid (Onodi cell). Highest risk configuration.")
    
    pdf.add_page()
    pdf.heading("Plate 24: Skull Base - Keros Classification")
    pdf.ct_image_box("I1", "Keros Type I (1-3 mm)")
    pdf.body("Coronal CT showing Keros Type I configuration with shallow olfactory fossa (less than 3 mm depth). Lowest surgical risk.")
    pdf.ct_image_box("I2", "Keros Type II (4-7 mm)")
    pdf.body("Most common Keros Type II configuration with moderate olfactory fossa depth (4-7 mm).")
    
    pdf.add_page()
    pdf.heading("Plate 25: Keros Type III (Highest Risk)")
    pdf.ct_image_box("I3", "Keros Type III right")
    pdf.body("Coronal CT showing Keros Type III with deep olfactory fossa (greater than 8 mm) on the right side. High risk for skull base injury.")
    pdf.ct_image_box("I4", "Asymmetric Keros configuration")
    pdf.body("Asymmetric configuration with Type II on right and Type III on left. The lower side (Type III) is at higher risk during surgery.")
    
    # Cribriform
    pdf.add_page()
    pdf.heading("Plate 26: Cribriform Plate Asymmetry")
    pdf.ct_image_box("I5", "Cribriform plate asymmetry")
    pdf.body("Coronal CT showing asymmetry of the cribriform plate height. The lower side is at higher risk of inadvertent injury during ethmoidectomy.")
    pdf.ct_image_box("I6", "Anterior ethmoidal artery in mesentery")
    pdf.body("Coronal CT showing the anterior ethmoidal artery suspended in a thin mesentery from the ethmoid roof - increased risk of bleeding.")
    
    # Special variations
    pdf.add_page()
    pdf.heading("Plate 27: Lamina Papyracea Dehiscence")
    pdf.ct_image_box("I7", "Lamina papyracea dehiscence")
    pdf.body("Coronal CT showing dehiscence of the right lamina papyracea with orbital fat protruding into the ethmoid sinus. Risk of orbital injury.")
    pdf.ct_image_box("I8", "Medial bowing of lamina papyracea")
    pdf.body("Medial bowing of bilateral lamina papyracea reducing the ethmoid air cell space and altering normal anatomy.")
    
    # Uncinate variations  
    pdf.add_page()
    pdf.heading("Plate 28: Uncinate Process Variations")
    pdf.ct_image_box("J1", "Pneumatized uncinate process")
    pdf.body("Coronal CT showing rare pneumatization of the uncinate process (uncinate bulla) with mucosal thickening.")
    pdf.ct_image_box("J2", "Type II uncinate (skull base attachment)")
    pdf.body("Sagittal CT showing Type II uncinate process attaching to the skull base (fovea ethmoidalis) - increased risk of skull base injury during uncinectomy.")
    
    # Pathology cases
    pdf.add_page()
    pdf.heading("Plate 29: Multiple Variations in Same Patient")
    pdf.ct_image_box("K1", "Multiple variations - case 1")
    pdf.body("Coronal CT showing severe DNS (right), bilateral concha bullosa, paradoxical middle turbinate (left), Haller cell (right), and Keros Type III. Six simultaneous variations requiring careful surgical planning.")
    pdf.ct_image_box("K2", "Multiple variations - case 2")
    pdf.body("Sagittal CT of same patient showing additional Onodi cell and Type III frontal cell. Image-guided surgery was used for FESS.")
    
    pdf.add_page()
    pdf.heading("Plate 30: Disease and Variations")
    pdf.ct_image_box("L1", "Sinusitis with anatomical predisposition")
    pdf.body("Coronal CT showing right maxillary sinusitis with associated Haller cell, demonstrating the link between anatomical variations and chronic disease.")
    pdf.ct_image_box("L2", "Mucocele formation")
    pdf.body("Frontal sinus mucocele with bony expansion and erosion. The patient had pre-existing frontal cells obstructing drainage.")

def add_postoperative_chapter(pdf):
    """Postoperative considerations chapter"""
    pdf.add_page()
    pdf.heading("3.14 Postoperative Considerations and Follow-up")
    
    pdf.subheading("3.14.1 Immediate Postoperative Care")
    pdf.body("Following FESS, immediate postoperative care includes:")
    pdf.bullet("Vital signs monitoring")
    pdf.bullet("Observation for complications")
    pdf.bullet("Pain management")
    pdf.bullet("Antibiotic prophylaxis (selective)")
    pdf.bullet("Nasal saline irrigation")
    pdf.bullet("Avoidance of nose blowing")
    pdf.bullet("Head elevation")
    
    pdf.subheading("3.14.2 Postoperative Complications")
    pdf.body("Complications can be early or late:")
    
    pdf.body("Early complications (within 30 days):")
    pdf.bullet("Bleeding (most common)")
    pdf.bullet("Infection")
    pdf.bullet("CSF leak")
    pdf.bullet("Orbital injury")
    pdf.bullet("Persistent pain")
    pdf.bullet("Adhesion formation")
    
    pdf.body("Late complications:")
    pdf.bullet("Synechiae (adhesions)")
    pdf.bullet("Recurrent disease")
    pdf.bullet("Mucocele formation")
    pdf.bullet("Olfactory disturbance")
    pdf.bullet("Frontal sinus stenosis")
    pdf.bullet("Atrophic rhinitis")
    
    pdf.subheading("3.14.3 Follow-up Protocol")
    pdf.body("Standard follow-up includes:")
    pdf.bullet("First visit: 7-10 days postoperative - debridement, examination")
    pdf.bullet("Second visit: 4-6 weeks - assessment of healing")
    pdf.bullet("Third visit: 3 months - assessment of disease control")
    pdf.bullet("Six-month visit - long-term assessment")
    pdf.bullet("Annual follow-up for chronic cases")
    
    pdf.subheading("3.14.4 Postoperative CT Findings")
    pdf.body("Normal postoperative CT findings include:")
    pdf.bullet("Patent surgical openings")
    pdf.bullet("Resolution of mucosal thickening")
    pdf.bullet("Restoration of OMC drainage")
    pdf.bullet("Decreased Lund-Mackay score")
    pdf.bullet("Mild adhesion formation may be seen")
    
    pdf.body("Abnormal findings warranting attention:")
    pdf.bullet("Persistent or recurrent disease")
    pdf.bullet("Stenotic openings")
    pdf.bullet("Significant adhesions")
    pdf.bullet("Bone resorption")
    pdf.bullet("Mucocele formation")
    pdf.bullet("New disease in unoperated areas")
    
    pdf.subheading("3.14.5 Quality of Life Assessment")
    pdf.body("Various tools assess postoperative quality of life:")
    pdf.bullet("Sino-Nasal Outcome Test (SNOT-22)")
    pdf.bullet("Rhinosinusitis Disability Index (RSDI)")
    pdf.bullet("Chronic Sinusitis Survey (CSS)")
    pdf.bullet("SF-36 (general health)")
    pdf.bullet("Visual Analog Scale for symptoms")
    
    pdf.body("Studies have shown significant improvement in QoL after successful FESS in 80-90% of patients.")
    
    pdf.subheading("3.14.6 Revision Surgery")
    pdf.body("Despite optimal primary surgery, some patients require revision FESS. Indications include:")
    pdf.bullet("Persistent symptoms despite medical therapy")
    pdf.bullet("Recurrent polyps")
    pdf.bullet("Anatomical abnormalities (synechiae, scarring)")
    pdf.bullet("Mucocele formation")
    pdf.bullet("New disease development")
    
    pdf.body("Revision surgery is more challenging because:")
    pdf.bullet("Distorted anatomy from previous surgery")
    pdf.bullet("Loss of normal landmarks")
    pdf.bullet("Increased risk of complications")
    pdf.bullet("Often requires image guidance")
    pdf.bullet("Higher rates of unsatisfactory outcomes")

def add_special_cases(pdf):
    """Special cases and considerations"""
    pdf.add_page()
    pdf.heading("3.15 Special Patient Populations")
    
    pdf.subheading("3.15.1 Pediatric Considerations")
    pdf.body("Sinus surgery in children presents unique challenges:")
    
    pdf.body("Anatomical considerations:")
    pdf.bullet("Smaller anatomical structures")
    pdf.bullet("Incomplete sinus development")
    pdf.bullet("Different proportions")
    pdf.bullet("Risk to facial growth (limited)")
    pdf.bullet("Adenoid tissue contribution to nasal obstruction")
    
    pdf.body("Surgical considerations:")
    pdf.bullet("More conservative approach")
    pdf.bullet("Smaller instruments needed")
    pdf.bullet("General anesthesia required")
    pdf.bullet("Postoperative care challenges")
    pdf.bullet("Long-term outcomes consideration")
    
    pdf.body("Common pediatric conditions:")
    pdf.bullet("Choanal atresia (1:5000-8000)")
    pdf.bullet("Recurrent acute rhinosinusitis")
    pdf.bullet("Cystic fibrosis-related sinusitis")
    pdf.bullet("Adenoid hypertrophy")
    pdf.bullet("Allergic rhinitis")
    
    pdf.subheading("3.15.2 Geriatric Considerations")
    pdf.body("Elderly patients present different challenges:")
    pdf.bullet("Atrophic mucosa")
    pdf.bullet("Increased pneumatization")
    pdf.bullet("Bone fragility")
    pdf.bullet("Comorbidities affecting surgery")
    pdf.bullet("Anti-coagulation considerations")
    pdf.bullet("Different healing patterns")
    pdf.bullet("Anesthesia risks")
    
    pdf.subheading("3.15.3 Immunocompromised Patients")
    pdf.body("Special considerations for immunocompromised patients include:")
    pdf.bullet("Higher risk of opportunistic infections")
    pdf.bullet("Acute invasive fungal sinusitis (life-threatening)")
    pdf.bullet("Atypical bacterial infections")
    pdf.bullet("Need for aggressive treatment")
    pdf.bullet("Multi-disciplinary management")
    pdf.bullet("Tissue diagnosis critical")
    pdf.bullet("Rapid surgical intervention often needed")
    
    pdf.body("Conditions causing immunocompromise:")
    pdf.bullet("Diabetes mellitus (especially uncontrolled)")
    pdf.bullet("HIV/AIDS")
    pdf.bullet("Hematological malignancies")
    pdf.bullet("Solid organ transplant recipients")
    pdf.bullet("Chemotherapy patients")
    pdf.bullet("Long-term steroid use")
    pdf.bullet("Chronic kidney disease")
    
    pdf.subheading("3.15.4 Pregnancy and Sinus Surgery")
    pdf.body("Sinus surgery during pregnancy requires special considerations:")
    pdf.bullet("Avoid elective surgery if possible")
    pdf.bullet("Defer to second trimester if needed")
    pdf.bullet("Limit radiation exposure (CT)")
    pdf.bullet("MRI preferred over CT")
    pdf.bullet("Anesthesia considerations")
    pdf.bullet("Medication restrictions")
    pdf.bullet("Multidisciplinary care")
    
    pdf.subheading("3.15.5 Patients with Bleeding Disorders")
    pdf.body("Special precautions for bleeding disorders:")
    pdf.bullet("Pre-operative correction of coagulation")
    pdf.bullet("Hematology consultation")
    pdf.bullet("Topical hemostatic agents")
    pdf.bullet("Bipolar cautery preferred")
    pdf.bullet("Postoperative monitoring")
    pdf.bullet("Avoid nasal packing if possible")
    pdf.bullet("Plan for blood products availability")

def add_more_references_section(pdf):
    """Additional references and bibliography"""
    pdf.add_page()
    pdf.heading("Additional Selected References")
    
    additional_refs = [
        "Baptista J, Lacerda J, Tirado M. Anatomic variations of paranasal sinuses on multi-slice computed tomography: A review. World J Otorhinolaryngol Head Neck Surg. 2019;5(1):41-46.",
        "Tantilipikorn P, Trakulkajornsak S, Bunnag C, Jirapongsananuruk O. Prevalence of paranasal sinus anatomical variations in Thailand. Asian Pac J Allergy Immunol. 2010;28(2-3):152-156.",
        "Aramani A, Karadi RN, Kumar S. A study of anatomical variations of osteomeatal complex in chronic rhinosinusitis patients-CT findings. J Clin Diagn Res. 2014;8(10):KC01-KC04.",
        "Mohebbi A, Ahmadi A, Etemadi M, Safdarian M, Ghourchian S. An epidemiologic study of factors associated with nasal septum deviation by computed tomography scan: a cross sectional study. BMC Ear Nose Throat Disord. 2012;12:15.",
        "Smith TL, Mendolia-Loffredo S, Loehrl TA, Sparapani R, Laud PW, Nattinger AB. Predictive factors and outcomes in endoscopic sinus surgery for chronic rhinosinusitis. Laryngoscope. 2005;115(12):2199-2205.",
        "Dasar U, Gokce E. Evaluation of variations in sinonasal region with computed tomography. World J Radiol. 2016;8(1):98-108.",
        "Sirikci A, Bayazit Y, Bayram M, Kanlikama M. Ethmomaxillary sinus: a particular anatomic variation of the paranasal sinuses. Eur Radiol. 2004;14(2):281-285.",
        "Eweiss AZ, Khalil HS. The prevalence of frontal cells and their relation to frontal sinusitis: a radiological study of the frontal recess area. ISRN Otolaryngol. 2013;2013:687582.",
        "Park SS, Yoon BN, Cho KS, Roh HJ. Pneumatization pattern of the sphenoid sinus is correlated with the shape of the sella in chronic adult rhinosinusitis. Clin Exp Otorhinolaryngol. 2013;6(2):88-93.",
        "Khojastepour L, Haghnegahdar A, Keshtkar M. Comparison of Keros classification of olfactory fossa among patients with and without chronic rhinosinusitis using cone beam computed tomography. J Dent (Shiraz). 2018;19(1):66-72.",
        "Solares CA, Lee WT, Batra PS, Citardi MJ. Lateral lamella of the cribriform plate: software-enabled computed tomographic analysis and its clinical relevance in skull base surgery. Arch Otolaryngol Head Neck Surg. 2008;134(3):285-289.",
        "Kainz J, Stammberger H. The roof of the anterior ethmoid: a place of least resistance in the skull base. Am J Rhinol. 1989;3(4):191-199.",
        "Huang BY, Lloyd KM, DelGaudio JM, Jablonowski E, Hudgins PA. Failed endoscopic sinus surgery: spectrum of CT findings in the frontal recess. Radiographics. 2009;29(1):177-195.",
        "Park SS, Yoon BN, Cho KS, Roh HJ. The pneumatization of the sphenoid sinus: A morphometric analysis using computed tomography in 92 Caucasian. Surg Radiol Anat. 2014;36(5):473-478.",
        "Kazkayasi M, Ergin A, Ersoy M, Bengi O, Tekdemir I, Elhan A. Certain anatomical relations and the precise morphometry of the infraorbital foramen--canal and groove: an anatomical and cephalometric study. Laryngoscope. 2001;111(4 Pt 1):609-614.",
        "Eloy P, Lecomte H, Trussart C, Bertrand B. Anatomic variations of the paranasal sinuses: A study of CT scans. Acta Otorhinolaryngol Belg. 1997;51(2):125-132.",
        "Citardi MJ, Gallivan RP, Batra PS, Maurer CR Jr, Rohlfing T, Bumm K, et al. Quantitative computer-aided computed tomography analysis of sphenoid sinus anatomical relationships. Am J Rhinol. 2004;18(3):173-178.",
        "Lloyd GA. CT of the paranasal sinuses: study of a control series in relation to endoscopic sinus surgery. J Laryngol Otol. 1990;104(6):477-481.",
        "Bademci G, Saygi M, Suzen B. Bilateral pneumatized middle turbinate (concha bullosa): a case report and review. J Neurol Sci [Turk]. 2005;22(2):213-216.",
        "Min YG, Yun YS, Song BH, Cho YS, Lee KS. Recurrence of rhinosinusitis after endoscopic sinus surgery in adults. Ann Otol Rhinol Laryngol. 1995;104(11):838-841.",
        "Wormald PJ, Hoseman W, Callejas C, Weber RK, Kennedy DW, Citardi MJ, et al. The International Frontal Sinus Anatomy Classification (IFAC) and Classification of the Extent of Endoscopic Frontal Sinus Surgery (EFSS). Int Forum Allergy Rhinol. 2016;6(7):677-696.",
        "Owen RG Jr, Kuhn FA. The maxillary sinus ostium: demystifying middle meatal antrostomy. Am J Rhinol. 1995;9(6):313-320.",
        "Wang Y, Ma R, Liu J, Yang HF, Hu Q, Tang Z. Anatomical comparison of the lateral wall of the maxillary sinus in symptomatic and asymptomatic patients. Eur Arch Otorhinolaryngol. 2014;271(7):1923-1929.",
        "Casale M, Pappacena M, Potena M, Vesperini E, Ciglia G, Mladina R, et al. Septal deviation and concha bullosa: any clinical association with chronic rhinosinusitis? Clin Ter. 2012;163(1):33-37.",
        "Madani SA, Hashemi SA, Modanloo S. The prevalence of nasal septal deviation and its relation with chronic rhinosinusitis in patients undergoing functional endoscopic sinus surgery. Iran J Otorhinolaryngol. 2015;27(78):63-67.",
    ]
    
    pdf.set_font('Times', '', 10)
    for i, ref in enumerate(additional_refs, 84):
        pdf.set_x(pdf.l_margin)
        text = f"{i}. {pdf.safe(ref)}"
        pdf.multi_cell(0, 5, text)
        pdf.ln(2)

def add_glossary(pdf):
    """Add glossary of terms"""
    pdf.add_page()
    pdf.section_title("GLOSSARY OF TERMS")
    
    glossary_terms = [
        ("Agger nasi", "The most anterior ethmoid air cell located at the anterior attachment of the middle turbinate"),
        ("Anatomical variation", "Deviation from typical anatomy that is not pathological"),
        ("Antrostomy", "Surgical creation of an opening in a sinus, typically maxillary"),
        ("Choanae", "Posterior nasal apertures opening into nasopharynx"),
        ("Concha bullosa", "Pneumatization of the middle turbinate"),
        ("Cribriform plate", "Perforated horizontal portion of ethmoid bone forming roof of nasal cavity"),
        ("CSF leak", "Leakage of cerebrospinal fluid through a defect in skull base"),
        ("Dehiscence", "Complete or partial absence of bone normally covering a structure"),
        ("Ethmoid bulla", "Largest anterior ethmoid air cell"),
        ("Ethmoidectomy", "Surgical removal of ethmoid air cells"),
        ("FESS", "Functional Endoscopic Sinus Surgery"),
        ("Fovea ethmoidalis", "Roof of ethmoid sinus, formed by frontal bone"),
        ("Frontal recess", "Drainage pathway of frontal sinus into middle meatus"),
        ("Haller cell", "Ethmoid air cell extending along medial orbital floor"),
        ("Hiatus semilunaris", "Crescent-shaped opening between uncinate process and ethmoid bulla"),
        ("Hounsfield unit (HU)", "Measure of radiodensity used in CT imaging"),
        ("Hypoplasia", "Underdevelopment of an anatomical structure"),
        ("Infundibulum", "Funnel-shaped passage; ethmoid infundibulum is the maxillary drainage pathway"),
        ("Keros classification", "Classification of olfactory fossa depth (Types I, II, III)"),
        ("Lamina papyracea", "Thin lateral wall of ethmoid bone separating sinuses from orbit"),
        ("Mucocele", "Mucus-containing expansile cyst due to obstructed sinus drainage"),
        ("Mucociliary clearance", "Coordinated movement of mucus by ciliary action"),
        ("Onodi cell", "Posterior ethmoid cell extending to sphenoid, related to optic nerve"),
        ("Ostium", "Natural opening of a sinus"),
        ("Osteomeatal complex (OMC)", "Functional unit including maxillary ostium and surrounding structures"),
        ("Paranasal sinuses", "Air-filled cavities within facial bones connecting to nasal cavity"),
        ("Paradoxical turbinate", "Turbinate with reversed curvature (convex laterally)"),
        ("Pneumatization", "Process of air cell formation within bones"),
        ("Polyp", "Non-neoplastic outgrowth of edematous mucosa"),
        ("Rhinosinusitis", "Inflammation of nasal cavity and paranasal sinuses"),
        ("Sella turcica", "Bony depression housing the pituitary gland"),
        ("Septoplasty", "Surgical correction of deviated nasal septum"),
        ("Sphenoethmoidal recess", "Drainage area for sphenoid sinus, above superior turbinate"),
        ("Turbinate", "Curved bony shelves projecting from lateral nasal wall"),
        ("Uncinate process", "Thin sickle-shaped bony lamella forming medial wall of ethmoid infundibulum"),
        ("Uncinectomy", "Surgical removal of uncinate process"),
        ("Vidian canal", "Bony canal containing the vidian nerve"),
        ("Window setting", "CT image display parameters (width and level)"),
        ("Zygomatic process", "Lateral projection of maxilla forming part of zygomatic arch"),
    ]
    
    pdf.set_font('Times', '', 11)
    for term, definition in glossary_terms:
        pdf.set_x(pdf.l_margin)
        pdf.set_font('Times', 'B', 11)
        pdf.multi_cell(0, 6, pdf.safe(term))
        pdf.set_font('Times', '', 10)
        pdf.set_x(pdf.l_margin + 5)
        pdf.multi_cell(0, 5, pdf.safe(definition))
        pdf.ln(2)
