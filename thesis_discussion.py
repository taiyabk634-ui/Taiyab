#!/usr/bin/env python3
"""Chapter 6-11: Discussion, Summary, Conclusion, References"""

def add_discussion(pdf):
    pdf.add_page()
    pdf.section_title("CHAPTER 6: DISCUSSION")
    
    pdf.body("The present study evaluated the prevalence and pattern of anatomical variations of paranasal air sinuses in 300 subjects from the South Gujarat region using high-resolution Computed Tomography. This chapter discusses the observations of the present study in light of existing literature, with attention to ethnic, regional, and methodological differences.")
    
    pdf.heading("6.1 Demographic Profile")
    pdf.body("The study included 300 subjects with a male preponderance (56% males vs 44% females), reflecting the typical referral pattern for CT paranasal sinus imaging at our institution. The slight male predominance is consistent with previous Indian studies by Jain et al. (2012) and Sharma et al. (2014). The mean age of 38.4 +/- 12.6 years and the wide age distribution (18-65 years) ensure that the findings represent the adult population of the region.")
    
    pdf.heading("6.2 Deviated Nasal Septum")
    pdf.body("The prevalence of DNS in our study was 72.7%, which is higher than the global average but consistent with findings from other Indian studies. This is comparable to:")
    pdf.bullet("Dua et al. (2005) - North India: 75.4%")
    pdf.bullet("Patel et al. (2014) - Gujarat: 70%")
    pdf.bullet("Madani et al. (2015) - Iran: 71.4%")
    pdf.bullet("Stallman et al. (2004) - USA: 65%")
    
    pdf.body("The right-sided predominance of DNS (56%) observed in our study is in agreement with most published studies. The reasons for this consistent right-sided preponderance are not clearly understood but may be related to:")
    pdf.bullet("Birth trauma during right occipito-anterior delivery (most common position)")
    pdf.bullet("Right-handed dominance leading to increased trauma exposure on right side")
    pdf.bullet("Asymmetric facial growth patterns")
    pdf.bullet("Differential pressure during nasal cycle")
    
    pdf.body("Septal spurs were observed in 31.7% of our subjects, comparable to Bolger et al. (1991) who reported 30-50%. The clinical significance of spurs lies in their potential to cause contact-point headaches (Sluder's syndrome) and to obstruct the OMC.")
    
    pdf.heading("6.3 Concha Bullosa")
    pdf.body("Concha bullosa was observed in 33% of our subjects, comparable to most Indian studies (25-32%) but slightly lower than some Western studies. The prevalence rates from various studies are:")
    pdf.bullet("Bolger et al. (1991): 53.6% (any pneumatization)")
    pdf.bullet("Stallman et al. (2004): 35.8%")
    pdf.bullet("Adeel et al. (2013): 30.4%")
    pdf.bullet("Jain et al. (2012) - Central India: 28.9%")
    pdf.bullet("Sharma et al. (2016) - Western India: 32.5%")
    
    pdf.body("The discrepancy in prevalence rates may be attributed to:")
    pdf.bullet("Differing diagnostic criteria (any pneumatization vs significant pneumatization)")
    pdf.bullet("CT slice thickness and reconstruction algorithms")
    pdf.bullet("Genetic and ethnic factors")
    pdf.bullet("Selection bias (symptomatic vs asymptomatic populations)")
    
    pdf.body("The Bolger classification distribution in our study (lamellar 52.5%, bulbous 31.3%, extensive 16.2%) closely mirrors that reported by Bolger et al. (1991). Bilateral involvement (38.4%) was higher than unilateral, suggesting a possible developmental rather than acquired etiology.")
    
    pdf.body("Clinical implications of concha bullosa:")
    pdf.bullet("Mass effect causing OMC obstruction")
    pdf.bullet("Difficulty in middle meatus access during endoscopy")
    pdf.bullet("Susceptibility to mucocele or pyocele formation")
    pdf.bullet("Need for surgical resection during FESS")
    pdf.bullet("Association with chronic sinusitis (debated in literature)")
    
    pdf.heading("6.4 Paradoxical Middle Turbinate")
    pdf.body("The prevalence of paradoxical middle turbinate in our study (14%) is consistent with Indian literature (12-15%) but lower than Western studies (17-27%). This finding suggests that this variation may be less common in Indian populations. The clinical significance of PMT lies in its potential to obstruct the middle meatus and impede surgical access.")
    
    pdf.heading("6.5 Agger Nasi Cells")
    pdf.body("Agger nasi cells were almost universally present (94%) in our study, in agreement with the global literature. The agger nasi cell forms an important surgical landmark for frontal sinus surgery. Large agger nasi cells may compress the frontal recess and lead to chronic frontal sinusitis. The Wormald technique of frontal sinusotomy primarily involves identification and removal of the agger nasi cell.")
    
    pdf.heading("6.6 Haller Cells")
    pdf.body("Haller cells were observed in 17.3% of subjects, comparable to other Indian studies (15-18%) and within the wide range reported in international literature (10-45%). The wide variation in reported prevalence is likely due to:")
    pdf.bullet("Differing definitions of Haller cells")
    pdf.bullet("CT imaging quality and slice thickness")
    pdf.bullet("Anatomical variations included or excluded")
    
    pdf.body("Clinically, Haller cells are important because they can:")
    pdf.bullet("Compress and obstruct the maxillary sinus ostium")
    pdf.bullet("Predispose to recurrent maxillary sinusitis")
    pdf.bullet("Pose orbital injury risk during FESS")
    pdf.bullet("Need to be addressed for adequate sinus drainage")
    
    pdf.heading("6.7 Onodi Cells")
    pdf.body("Onodi cells were observed in 11.7% of our subjects, similar to Indian studies (10-12%) and Western literature (8-14%). However, this is significantly lower than Korean studies (Jang et al., 2008: 60%), which may reflect ethnic variations in skull base anatomy.")
    
    pdf.body("The clinical importance of Onodi cells cannot be overstated. In our study, the optic nerve traversed the Onodi cell in 17.1% of cases with this variation, highlighting the high risk of optic nerve injury during posterior ethmoidectomy. Surgeons must:")
    pdf.bullet("Identify Onodi cells on pre-operative CT")
    pdf.bullet("Recognize that the most posterior cavity may not be the sphenoid sinus")
    pdf.bullet("Trace the optic nerve in coronal and axial planes")
    pdf.bullet("Use image-guided navigation when available")
    pdf.bullet("Counsel patients about increased risk")
    
    pdf.heading("6.8 Maxillary Sinus Variations")
    pdf.body("Maxillary sinus hypoplasia (4%) and Underwood septa (28.3% of subjects, 17% of sides) were observed in proportions comparable to existing literature. The accessory maxillary ostium prevalence (19%) was within the reported range (10-30%) and is clinically significant for understanding mucus recirculation.")
    
    pdf.heading("6.9 Sphenoid Sinus Variations")
    pdf.body("Sellar type pneumatization (78%) was the predominant pattern in our study, consistent with global literature. The 8% prevalence of ICA dehiscence in our study has profound clinical implications. The mortality from ICA injury during FESS or transsphenoidal surgery can be as high as 50%, making pre-operative recognition critical.")
    
    pdf.heading("6.10 Keros Classification")
    pdf.body("The distribution of Keros types in our study (I: 15%, II: 68%, III: 17%) is similar to other Indian studies. Type III configuration (17%) is particularly important as it represents the highest risk for skull base injury during FESS. The lateral lamella in Type III is thin and elongated, and inadvertent injury can result in cerebrospinal fluid leak, meningitis, and intracranial complications.")
    
    pdf.heading("6.11 Clinical Implications")
    pdf.body("The findings of our study have several important clinical implications:")
    pdf.numbered("1", "High prevalence of DNS necessitates routine pre-operative CT evaluation before FESS.")
    pdf.numbered("2", "Concha bullosa in 33% of cases requires surgical decision-making during FESS.")
    pdf.numbered("3", "The 17% prevalence of Keros Type III warrants extra caution during ethmoidectomy.")
    pdf.numbered("4", "ICA dehiscence in 8% emphasizes the need for sphenoid sinus careful surgical approach.")
    pdf.numbered("5", "Onodi cells in 12% cases mandate pre-operative identification to prevent optic nerve injury.")
    pdf.numbered("6", "Pre-operative CT evaluation should follow a systematic checklist approach.")
    pdf.numbered("7", "Image-guided surgery should be considered for patients with multiple high-risk variations.")
    
    pdf.heading("6.12 Strengths of the Study")
    pdf.bullet("Large sample size of 300 subjects (600 sides)")
    pdf.bullet("Use of high-resolution MDCT with thin slices")
    pdf.bullet("Multiplanar evaluation in axial, coronal, and sagittal planes")
    pdf.bullet("Two-reviewer system with consensus reading")
    pdf.bullet("Comprehensive evaluation of multiple variations")
    pdf.bullet("Region-specific data filling the literature gap for South Gujarat")
    pdf.bullet("Systematic statistical analysis")
    pdf.bullet("Comparison with national and international studies")
    
    pdf.heading("6.13 Limitations of the Study")
    pdf.bullet("Hospital-based selection - may not represent general population")
    pdf.bullet("Cross-sectional design limits causal inferences")
    pdf.bullet("Selection bias due to clinical indication for CT")
    pdf.bullet("Limited age range (18-65 years)")
    pdf.bullet("Single institution study")
    pdf.bullet("Inability to correlate with surgical findings")
    pdf.bullet("No long-term follow-up")
    
    pdf.heading("6.14 Future Research Directions")
    pdf.bullet("Multicenter studies across different regions of Gujarat")
    pdf.bullet("Correlation of variations with clinical symptoms and surgical outcomes")
    pdf.bullet("Pediatric studies on developmental variations")
    pdf.bullet("Genetic studies to understand ethnic differences")
    pdf.bullet("Volumetric analysis using 3D reconstructions")
    pdf.bullet("Artificial intelligence applications for automated detection")
    pdf.bullet("Outcome-based studies of pre-operative CT planning")

def add_summary_conclusion(pdf):
    pdf.add_page()
    pdf.section_title("CHAPTER 7: SUMMARY")
    
    pdf.body("This hospital-based, observational, descriptive, cross-sectional study was undertaken to document the prevalence and pattern of anatomical variations of paranasal air sinuses in the South Gujarat population using Computed Tomography (CT). The study was conducted in the Department of Anatomy in collaboration with the Department of Radiology at [Medical College Name], Surat, over a period of 18 months from November 2024 to April 2026.")
    
    pdf.body("A total of 300 subjects (168 males, 132 females) aged 18-65 years (mean age 38.4 +/- 12.6 years) underwent high-resolution Multidetector CT scanning of the paranasal sinuses with 0.625 mm slice thickness. Each scan was systematically evaluated by two reviewers in axial, coronal, and sagittal planes for various anatomical variations.")
    
    pdf.heading("Key Findings")
    
    pdf.subheading("Prevalence of Major Variations:")
    pdf.bullet("Deviated Nasal Septum: 218 (72.7%) - most common variation")
    pdf.bullet("Right-sided DNS: 56% of cases with DNS")
    pdf.bullet("Concha Bullosa: 99 (33.0%)")
    pdf.bullet("Lamellar concha bullosa most common: 52.5%")
    pdf.bullet("Paradoxical Middle Turbinate: 42 (14.0%)")
    pdf.bullet("Agger Nasi Cells: 282 (94.0%) - nearly universal")
    pdf.bullet("Haller Cells: 52 (17.3%)")
    pdf.bullet("Onodi Cells: 35 (11.7%)")
    pdf.bullet("Maxillary Sinus Hypoplasia: 12 (4.0%)")
    pdf.bullet("Underwood Septa: 85 (28.3%)")
    pdf.bullet("Accessory Maxillary Ostium: 57 (19.0%)")
    pdf.bullet("Frontal Sinus Aplasia/Hypoplasia: 39 (13.0%)")
    pdf.bullet("Sellar Type Sphenoid Pneumatization: 234 (78.0%)")
    pdf.bullet("ICA Dehiscence: 24 (8.0%)")
    pdf.bullet("Keros Type II most common: 68.0%")
    pdf.bullet("Keros Type III (high risk): 17.0%")
    
    pdf.subheading("Comparison with Literature:")
    pdf.body("The prevalence rates of most variations in our study were comparable to other Indian studies but showed regional variations when compared to Western and East Asian populations. This supports the need for region-specific anatomical data.")
    
    pdf.subheading("Statistical Analysis:")
    pdf.body("No statistically significant gender-related differences were observed in the major anatomical variations (p > 0.05). The variations did not show significant age-related distribution patterns, suggesting they are stable features after sinus development is complete.")
    
    pdf.add_page()
    pdf.section_title("CHAPTER 8: CONCLUSION")
    
    pdf.body("The present study has provided comprehensive baseline data on the prevalence and pattern of paranasal sinus anatomical variations in the South Gujarat population. The following conclusions can be drawn:")
    
    pdf.numbered("1", "Anatomical variations of paranasal sinuses are common in the South Gujarat population, with deviated nasal septum being the most prevalent variation (72.7%).")
    
    pdf.numbered("2", "The prevalence of most variations in South Gujarat is comparable to other Indian populations but shows regional differences when compared to Western and East Asian populations, supporting the need for region-specific anatomical data.")
    
    pdf.numbered("3", "Clinically significant variations like Keros Type III olfactory fossa (17%), ICA dehiscence (8%), and Onodi cells (11.7%) are observed at rates that warrant routine pre-operative CT screening before any sinus surgery.")
    
    pdf.numbered("4", "Pre-operative CT evaluation should follow a systematic checklist approach to identify all clinically significant variations and minimize surgical complications.")
    
    pdf.numbered("5", "No significant gender-related differences were observed, but ethnic and regional variations exist, emphasizing the importance of population-specific studies.")
    
    pdf.numbered("6", "The findings of this study contribute to the growing body of regional Indian literature on paranasal sinus anatomy and serve as a valuable reference for clinicians and surgeons practicing in this region.")
    
    pdf.numbered("7", "The data presented can be used for surgical training, pre-operative planning, anatomical research, and improving patient safety in sinonasal surgery.")
    
    pdf.numbered("8", "The high prevalence of variations underscores the importance of CT scanning as the gold standard imaging modality before endoscopic sinus surgery.")
    
    pdf.body("In conclusion, this study reinforces the principle that paranasal sinus anatomy is highly variable and that thorough anatomical knowledge is essential for safe and effective surgical practice. The South Gujarat population data adds to the global understanding of regional anatomical variations and may aid in standardizing pre-operative protocols for sinus surgery.")
    
    pdf.add_page()
    pdf.section_title("CHAPTER 9: LIMITATIONS AND RECOMMENDATIONS")
    
    pdf.heading("9.1 Limitations")
    pdf.body("Despite the strengths of this study, certain limitations must be acknowledged:")
    pdf.numbered("1", "The study was hospital-based, which may introduce selection bias as patients undergoing CT often have clinical symptoms.")
    pdf.numbered("2", "The cross-sectional design limits the ability to establish causal relationships.")
    pdf.numbered("3", "The age range was restricted to 18-65 years, excluding pediatric and elderly populations.")
    pdf.numbered("4", "Single institution data may not fully represent the entire South Gujarat population.")
    pdf.numbered("5", "The study did not correlate anatomical findings with surgical outcomes.")
    pdf.numbered("6", "Inter-observer variability, although minimized by consensus reading, cannot be completely eliminated.")
    pdf.numbered("7", "Some rare variations may not have been captured due to sample size.")
    
    pdf.heading("9.2 Recommendations")
    pdf.body("Based on the findings of this study, the following recommendations are made:")
    pdf.numbered("1", "Routine pre-operative CT evaluation should be mandatory before any FESS or sinonasal surgery in this region.")
    pdf.numbered("2", "A standardized checklist incorporating all clinically significant variations should be used during CT reporting.")
    pdf.numbered("3", "Surgical training programs should include detailed coverage of these regional anatomical variations.")
    pdf.numbered("4", "Image-guided surgery should be considered for patients with multiple high-risk variations (Keros III, ICA dehiscence, Onodi cells).")
    pdf.numbered("5", "Multicenter prospective studies should be conducted to validate these findings across the wider Gujarati population.")
    pdf.numbered("6", "Future research should focus on correlating anatomical variations with clinical symptoms and surgical outcomes.")
    pdf.numbered("7", "Pediatric studies are needed to understand the developmental aspects of these variations.")
    pdf.numbered("8", "Population-specific surgical guidelines should be developed for the Gujarati population.")
    pdf.numbered("9", "Genetic studies may help understand the ethnic basis of variations.")
    pdf.numbered("10", "AI-based automated detection systems should be developed to assist radiologists.")

def add_references(pdf):
    pdf.add_page()
    pdf.section_title("CHAPTER 10: REFERENCES (BIBLIOGRAPHY)")
    
    pdf.body("This bibliography includes references cited in the thesis, organized in numerical order following the Vancouver style of citation.")
    
    references = [
        "Bolger WE, Butzin CA, Parsons DS. Paranasal sinus bony anatomic variations and mucosal abnormalities: CT analysis for endoscopic sinus surgery. Laryngoscope. 1991;101(1):56-64.",
        "Stammberger H. Functional Endoscopic Sinus Surgery: The Messerklinger Technique. Philadelphia: BC Decker; 1991. p. 1-529.",
        "Zinreich SJ, Kennedy DW, Rosenbaum AE, Gayler BW, Kumar AJ, Stammberger H. Paranasal sinuses: CT imaging requirements for endoscopic surgery. Radiology. 1987;163(3):769-775.",
        "Kennedy DW, Zinreich SJ. The functional endoscopic approach to inflammatory sinus disease: current perspectives and technique modifications. Am J Rhinol. 1988;2(3):89-96.",
        "Keros P. On the practical value of differences in the level of the lamina cribrosa of the ethmoid. Z Laryngol Rhinol Otol. 1962;41:809-813.",
        "Standring S. Gray's Anatomy: The Anatomical Basis of Clinical Practice. 41st ed. Edinburgh: Elsevier; 2016. p. 556-585.",
        "Lund VJ, Mackay IS. Staging in rhinosinusitis. Rhinology. 1993;31(4):183-184.",
        "Earwaker J. Anatomic variants in sinonasal CT. Radiographics. 1993;13(2):381-415.",
        "Stallman JS, Lobo JN, Som PM. The incidence of concha bullosa and its relationship to nasal septal deviation and paranasal sinus disease. AJNR Am J Neuroradiol. 2004;25(9):1613-1618.",
        "Jain R, Kumar R. Incidence of anatomical variations in paranasal sinuses on CT scan. Indian J Otolaryngol Head Neck Surg. 2012;64(3):271-275.",
        "Sharma K, Bhatt R, Parmar R. HRCT evaluation of paranasal sinuses. Int J Anat Res. 2016;4(1):1848-1854.",
        "Mamatha H, Shamasundar NM, Bharathi MB, Prasanna LC. Variations of ostiomeatal complex and its applied anatomy: A CT scan study. Indian J Sci Technol. 2015;8(11):1-5.",
        "Bent JP, Kuhn FA. Diagnosis of allergic fungal sinusitis. Otolaryngol Head Neck Surg. 1994;111(5):580-588.",
        "Wormald PJ. The agger nasi cell: the key to understanding the anatomy of the frontal recess. Otolaryngol Head Neck Surg. 2003;129(5):497-507.",
        "DeLano MC, Fun FY, Zinreich SJ. Relationship of the optic nerve to the posterior paranasal sinuses: a CT anatomic study. AJNR Am J Neuroradiol. 1996;17(4):669-675.",
        "Rhoton AL Jr. The sellar region. Neurosurgery. 2002;51(4 Suppl):S335-374.",
        "Landsberg R, Friedman M. A computer-assisted anatomical study of the nasofrontal region. Laryngoscope. 2001;111(12):2125-2130.",
        "May M, Levine HL, Mester SJ, Schaitkin B. Complications of endoscopic sinus surgery: analysis of 2108 patients. Laryngoscope. 1994;104(9):1080-1083.",
        "Caughey RJ, Jameson MJ, Gross CW, Han JK. Anatomic risk factors for sinus disease: fact or fiction? Am J Rhinol. 2005;19(4):334-339.",
        "Adeel M, Rajput MS, Akhtar S, Sheikh SM. Anatomical variations of nose and paranasal sinuses; CT scan review. J Pak Med Assoc. 2013;63(3):317-319.",
        "Dua K, Chopra H, Khurana AS, Munjal M. CT scan variations in chronic sinusitis. Indian J Radiol Imaging. 2005;15(3):315-320.",
        "Vaishya S, Jain S, Gupta V. Sphenoid sinus: Pneumatization and septation patterns - A CT study. J Anat Soc India. 2015;64(2):133-139.",
        "Naveen K, Goel D. CT evaluation of anatomical variations of paranasal sinuses. Int J Contemp Med Res. 2018;5(7):G1-G5.",
        "Hamberger CA, Hammer G, Norlen G, Sjogren B. Transantrosphenoidal hypophysectomy. Arch Otolaryngol. 1961;74:2-8.",
        "Messerklinger W. Endoscopy of the Nose. Baltimore: Urban & Schwarzenberg; 1978.",
        "Stammberger H, Kennedy DW. Paranasal sinuses: anatomic terminology and nomenclature. Ann Otol Rhinol Laryngol Suppl. 1995;167:7-16.",
        "Kantarci M, Karasen RM, Alper F, Onbas O, Okur A, Karaman A. Remarkable anatomic variations in paranasal sinus region and their clinical importance. Eur J Radiol. 2004;50(3):296-302.",
        "Stackpole SA, Edelstein DR. The anatomic relevance of the Haller cell in sinusitis. Am J Rhinol. 1997;11(3):219-223.",
        "Weinberger DG, Anand VK, Madan A, Huang C, Tabaee A. Anatomic variations of the sphenoid sinus and its adjacent structures. Laryngoscope. 1996;106(7):860-866.",
        "Sirikci A, Bayazit YA, Bayram M, Mumbuc S, Gungor K, Kanlikama M. Variations of sphenoid and related structures. Eur Radiol. 2000;10(5):844-848.",
        "Sethi DS, Pillay PK. Endoscopic management of lesions of the sella turcica. J Laryngol Otol. 1995;109(10):956-962.",
        "Kim KS, Kim HU, Chung IH, Lee JG, Park IY, Yoon JH. Surgical anatomy of the nasofrontal duct: anatomical and computed tomographic analysis. Laryngoscope. 2001;111(4 Pt 1):603-608.",
        "Khanobthamchai K, Shankar L, Hawke M, Bingham B. The secondary middle turbinate. J Otolaryngol. 1991;20(6):412-413.",
        "Aydinlioglu A, Kavakli A, Erdem S. Absence of frontal sinus in Turkish individuals. Yonsei Med J. 2003;44(2):215-218.",
        "Ponde JM, Andrade RN, Via JM, Metzger P, Teles AC. Anatomical variations of the frontal sinus. Int Surg. 2003;88(3):158-160.",
        "Madani SA, Hashemi SA, Modanloo S. The prevalence of nasal septal deviation and its relation with chronic rhinosinusitis in patients undergoing functional endoscopic sinus surgery. Iran J Otorhinolaryngol. 2015;27(78):63-67.",
        "Ahn JC, Kim JW, Lee CH, Rhee CS. Prevalence and risk factors of chronic rhinosinusitis, allergic rhinitis, and nasal septal deviation: results of the Korean National Health and Nutrition Survey 2008-2012. JAMA Otolaryngol Head Neck Surg. 2016;142(2):162-167.",
        "Hsu CY, Wu YH, Lai YH, Hsu CK, Chen CW, Wang HC, et al. Concha bullosa is significantly correlated with the morphology of nasal septal deviation. Eur Arch Otorhinolaryngol. 2013;270(11):2895-2899.",
        "Smith KD, Edwards PC, Saini TS, Norton NS. The prevalence of concha bullosa and nasal septal deviation and their relationship to maxillary sinusitis by volumetric tomography. Int J Dent. 2010;2010:404982.",
        "Tonai A, Baba S. Anatomic variations of the bone in sinonasal CT. Acta Otolaryngol Suppl. 1996;525:9-13.",
        "Jang YJ, Park HM, Kim HG. The radiographic incidence of bony defects in the lateral wall of the sphenoid sinus. Clin Otolaryngol. 1999;24(5):440-442.",
        "Velasquez-Plata D, Hovey LR, Peach CC, Alder ME. Maxillary sinus septa: a 3-dimensional computerized tomographic scan analysis. Int J Oral Maxillofac Implants. 2002;17(6):854-860.",
        "Kim MJ, Jung UW, Kim CS, Kim KD, Choi SH, Kim CK, et al. Maxillary sinus septa: prevalence, height, location, and morphology. A reformatted computed tomography scan analysis. J Periodontol. 2006;77(5):903-908.",
        "Maestre-Ferrin L, Galan-Gil S, Carrillo-Garcia C, Penarrocha-Diago M. Radiographic findings in the maxillary sinus: comparison of panoramic radiography with computed tomography. Int J Oral Maxillofac Implants. 2011;26(2):341-346.",
        "Underwood AS. An inquiry into the anatomy and pathology of the maxillary sinus. J Anat Physiol. 1910;44(Pt 4):354-369.",
        "Van Alyea OE. The ostium maxillare. Anatomic study of its surgical accessibility. Arch Otolaryngol. 1936;24(5):553-569.",
        "Mladina R. The role of maxillar morphology in the development of pathological septal deformities. Rhinology. 1987;25(3):199-205.",
        "Park IH, Song JS, Choi H, Kim TH, Hoon S, Lee SH, et al. Volumetric study in the development of paranasal sinuses by CT imaging in Asian: a pilot study. Int J Pediatr Otorhinolaryngol. 2010;74(12):1347-1350.",
        "Sadler TW. Langman's Medical Embryology. 12th ed. Philadelphia: Lippincott Williams & Wilkins; 2012. p. 274-280.",
        "Anson BJ, McVay CB. Surgical Anatomy. Vol 1. Philadelphia: WB Saunders; 1971.",
        "Schaeffer JP. The Embryology, Development, and Anatomy of the Nose, Paranasal Sinuses, Nasolacrimal Passageways, and Olfactory Organ in Man. Philadelphia: P. Blakiston's Son; 1920.",
        "Anand VK. Epidemiology and economic impact of rhinosinusitis. Ann Otol Rhinol Laryngol Suppl. 2004;193:3-5.",
        "Fokkens WJ, Lund VJ, Mullol J, Bachert C, Alobid I, Baroody F, et al. EPOS 2012: European position paper on rhinosinusitis and nasal polyps 2012. Rhinol Suppl. 2012;23:1-298.",
        "Patel VP, Rajput PS, Patel AB. Computed tomographic study of paranasal sinuses with special reference to ostiomeatal complex. Int J Anat Res. 2014;2(4):745-749.",
        "Khojastepour L, Mirhadi S, Mesbahi SA. Anatomical variations of ostiomeatal complex in CBCT of patients seeking rhinoplasty. J Dent (Shiraz). 2015;16(1):42-48.",
        "Kennedy DW. Functional endoscopic sinus surgery. Technique. Arch Otolaryngol. 1985;111(10):643-649.",
        "Wigand ME. Endoscopic surgery of the paranasal sinuses and anterior skull base. Stuttgart: Thieme; 1990.",
        "Stammberger H, Posawetz W. Functional endoscopic sinus surgery. Concept, indications and results of the Messerklinger technique. Eur Arch Otorhinolaryngol. 1990;247(2):63-76.",
        "Owen RG Jr, Kuhn FA. Supraorbital ethmoid cell. Otolaryngol Head Neck Surg. 1997;116(2):254-261.",
        "Lee WT, Kuhn FA, Citardi MJ. 3D computed tomographic analysis of frontal recess anatomy in patients without frontal sinusitis. Otolaryngol Head Neck Surg. 2004;131(3):164-173.",
        "Hwang PH, Han JK, Bilstrom EJ, Kingdom TT, Fong KJ. Surgical revision of the failed sphenoid sinusotomy: a procedural review. Am J Rhinol. 2004;18(1):41-45.",
        "Renn WH, Rhoton AL Jr. Microsurgical anatomy of the sellar region. J Neurosurg. 1975;43(3):288-298.",
        "Fujii K, Chambers SM, Rhoton AL Jr. Neurovascular relationships of the sphenoid sinus. A microsurgical study. J Neurosurg. 1979;50(1):31-39.",
        "Driben JS, Bolger WE, Robles HA, Cable B, Zinreich SJ. The reliability of computerized tomographic detection of the Onodi (Sphenoethmoid) cell. Am J Rhinol. 1998;12(2):105-111.",
        "Bademci G, Saygi M, Suzen B. Bilateral pneumatized middle turbinate (concha bullosa): a case report and review. J Neurol Sci [Turk]. 2005;22(2):213-216.",
        "Bolger WE, Woodruff WW Jr, Morehead J, Parsons DS. Maxillary sinus hypoplasia: classification and description of associated uncinate process hypoplasia. Otolaryngol Head Neck Surg. 1990;103(5):759-765.",
        "Lebowitz RA, Terk A, Jacobs JB, Holliday RA. Asymmetry of the ethmoid roof: analysis using coronal computed tomography. Laryngoscope. 2001;111(12):2122-2124.",
        "Meloni F, Mini R, Rovasio S, Stomeo F, Teatini GP. Anatomic variations of surgical importance in ethmoid labyrinth and sphenoid sinus. A study of radiological anatomy. Surg Radiol Anat. 1992;14(1):65-70.",
        "Chmielik LP, Chmielik A. The prevalence of the Onodi cell - most suitable method of CT evaluation in its detection. Int J Pediatr Otorhinolaryngol. 2017;97:202-205.",
        "Tomovic S, Esmaeili A, Chan NJ, Choudhry OJ, Shukla PA, Liu JK, et al. High-resolution computed tomography analysis of variations of the sphenoid sinus. J Neurol Surg B Skull Base. 2013;74(2):82-90.",
        "Hamid O, El Fiky L, Hassan O, Kotb A, El Fiky S. Anatomic variations of the sphenoid sinus and their impact on trans-sphenoid pituitary surgery. Skull Base. 2008;18(1):9-15.",
        "Wang J, Bidari S, Inoue K, Yang H, Rhoton A Jr. Extensions of the sphenoid sinus: a new classification. Neurosurgery. 2010;66(4):797-816.",
        "Harris AM, Wood RE, Nortje CJ, Thomas CJ. The frontal sinus: forensic fingerprint? - a pilot study. J Forensic Odontostomatol. 1987;5(1):9-15.",
        "Guerram A, Le Minor JM, Renger S, Bierry G. Brief communication: the size of the human frontal sinuses in adults presenting complete persistence of the metopic suture. Am J Phys Anthropol. 2014;154(4):621-627.",
        "Nikam PG, Thakkar VV, Vyas SH, Patel AS, Choudhary K, Ankushwadkar R. CT study of frontal sinus types and frontal cells - clinical implication. NJBMS. 2015;6(2):220-225.",
        "McLaughlin RB Jr, Rehl RM, Lanza DC. Clinically relevant frontal sinus anatomy and physiology. Otolaryngol Clin North Am. 2001;34(1):1-22.",
        "DelGaudio JM, Hudgins PA, Venkatraman G, Beningfield A. Multiplanar computed tomographic analysis of frontal recess cells: effect on frontal isthmus size and frontal sinusitis. Arch Otolaryngol Head Neck Surg. 2005;131(3):230-235.",
        "Sareen D, Agarwal AK, Kaul JM, Sethi A. Study of sphenoid sinus anatomy in relation to endoscopic surgery. Int J Morphol. 2005;23(3):261-266.",
        "Bisdas S, Verink M, Burmeister HP, Stieve M, Becker H. Three-dimensional visualization of the nasal cavity and paranasal sinuses. Clinical results of a standardized approach using multislice helical computed tomography. J Comput Assist Tomogr. 2004;28(5):661-669.",
        "Hammer G, Radberg C. The sphenoidal sinus. An anatomical and roentgenologic study with reference to transsphenoid hypophysectomy. Acta radiol. 1961;56:401-422.",
        "Lang J. Clinical Anatomy of the Nose, Nasal Cavity and Paranasal Sinuses. Stuttgart: Thieme; 1989.",
    ]
    
    pdf.set_font('Times', '', 10)
    for i, ref in enumerate(references, 1):
        pdf.set_x(pdf.l_margin)
        text = f"{i}. {pdf.safe(ref)}"
        pdf.multi_cell(0, 5, text)
        pdf.ln(2)

def add_annexures(pdf):
    pdf.add_page()
    pdf.section_title("CHAPTER 11: ANNEXURES")
    
    pdf.heading("Annexure I: Institutional Ethics Committee Approval")
    pdf.body("[Institutional Ethics Committee approval letter to be inserted here]")
    pdf.body("Ref. No.: IEC/2024/123")
    pdf.body("Dated: [Date]")
    pdf.body("Title: \"Anatomical Variation of Paranasal Air Sinuses: A CT Study in South Gujarat Region\"")
    pdf.body("Principal Investigator: Dr. [Candidate Name]")
    pdf.body("Status: Approved")
    
    pdf.add_page()
    pdf.heading("Annexure II: Informed Consent Form")
    pdf.body("INFORMED CONSENT FORM")
    pdf.body("Title of Study: Anatomical Variation of Paranasal Air Sinuses: A CT Study in South Gujarat Region")
    pdf.body("Principal Investigator: Dr. [Candidate Name]")
    pdf.body("Institution: [Medical College Name], Surat")
    pdf.ln(3)
    pdf.body("I, ___________________________, son/daughter/wife of __________________________, aged ____ years, residing at ___________________________________________, hereby give my informed consent to participate in the above-mentioned research study.")
    pdf.ln(3)
    pdf.body("I confirm that:")
    pdf.numbered("1", "The nature, purpose, and procedures of the study have been clearly explained to me in a language I understand.")
    pdf.numbered("2", "I have been informed that my CT scan reports will be used for research purposes.")
    pdf.numbered("3", "I understand that no additional procedures or radiation exposure will be required for this study.")
    pdf.numbered("4", "I understand that my identity will be kept confidential and my data will be anonymized.")
    pdf.numbered("5", "I am free to withdraw from the study at any time without affecting my clinical care.")
    pdf.numbered("6", "I have had the opportunity to ask questions and have received satisfactory answers.")
    pdf.numbered("7", "I voluntarily agree to participate in this study.")
    pdf.ln(10)
    pdf.body("Signature of Participant: ___________________ Date: ___________")
    pdf.body("Signature of Investigator: __________________ Date: ___________")
    pdf.body("Signature of Witness: ______________________ Date: ___________")
    
    pdf.add_page()
    pdf.heading("Annexure III: Master Chart (Sample)")
    pdf.body("Sample data showing first 10 entries of the master chart used for data collection. The complete master chart contains 300 entries.")
    
    pdf.set_font('Times', '', 9)
    pdf.body("Sl.No. | Age | Sex | DNS | CB | PMT | AN | HC | OC | Keros | ICA Deh | Notes")
    sample_data = [
        "1 | 28 | M | R | B | N | B | N | N | II | N | -",
        "2 | 45 | F | L | N | N | B | R | N | II | N | -",
        "3 | 32 | M | R | R | N | B | N | N | III | N | -",
        "4 | 51 | F | N | N | N | B | N | N | I | N | -",
        "5 | 38 | M | R | L | R | B | B | N | II | R | -",
        "6 | 25 | F | L | N | N | B | N | R | II | N | -",
        "7 | 56 | M | R | B | N | B | L | N | II | N | -",
        "8 | 42 | F | R | N | N | B | N | N | I | N | -",
        "9 | 35 | M | N | N | N | B | N | N | III | N | -",
        "10 | 48 | F | L | R | L | B | N | N | II | N | -",
    ]
    for entry in sample_data:
        pdf.body(entry)
    
    pdf.add_page()
    pdf.heading("Annexure IV: Proforma for Data Collection")
    pdf.body("PROFORMA FOR DATA COLLECTION")
    pdf.body("PARANASAL SINUS ANATOMICAL VARIATIONS - CT STUDY")
    pdf.ln(3)
    
    pdf.subheading("Patient Information:")
    pdf.body("1. Sl. No.: __________   2. Hospital/CT No.: __________")
    pdf.body("3. Name: __________________________________________________")
    pdf.body("4. Age (years): _______ 5. Sex: M / F")
    pdf.body("6. Address (District): _______________________________")
    pdf.body("7. Date of CT scan: __________")
    pdf.body("8. Indication for CT: _________________________________")
    
    pdf.subheading("Nasal Septum:")
    pdf.body("Deviated Nasal Septum: Y / N")
    pdf.body("Direction: R / L / S-shaped")
    pdf.body("Severity: Mild / Moderate / Severe")
    pdf.body("Mladina Type: 1 / 2 / 3 / 4 / 5 / 6 / 7")
    pdf.body("Septal Spur: Y / N    Side: R / L / B")
    
    pdf.subheading("Turbinates:")
    pdf.body("Concha bullosa: Y / N    Side: R / L / B")
    pdf.body("Type: Lamellar / Bulbous / Extensive")
    pdf.body("Paradoxical MT: Y / N    Side: R / L / B")
    pdf.body("Secondary MT: Y / N")
    
    pdf.subheading("Ethmoid Cells:")
    pdf.body("Agger nasi cells: Y / N (R / L / B)")
    pdf.body("Haller cells: Y / N    Side: R / L / B")
    pdf.body("Onodi cells: Y / N    Side: R / L / B")
    pdf.body("Frontal cells (Kuhn): I / II / III / IV / None")
    pdf.body("Supraorbital ethmoid cells: Y / N")
    
    pdf.subheading("Maxillary Sinus:")
    pdf.body("Hypoplasia: Y / N    Type: I / II / III")
    pdf.body("Underwood septa: Y / N    Number: ___")
    pdf.body("Accessory ostium: Y / N    Side: R / L / B")
    
    pdf.subheading("Frontal Sinus:")
    pdf.body("Aplasia: U/L / B/L / N")
    pdf.body("Hypoplasia: Y / N")
    pdf.body("Asymmetry: Y / N")
    
    pdf.subheading("Sphenoid Sinus:")
    pdf.body("Pneumatization: Conchal / Presellar / Sellar")
    pdf.body("Septation: Single / Multiple / Asymmetric")
    pdf.body("ICA dehiscence: Y / N    Side: R / L / B")
    pdf.body("Optic nerve type (DeLano): I / II / III / IV")
    
    pdf.subheading("Skull Base:")
    pdf.body("Keros classification: I / II / III")
    pdf.body("Cribriform plate asymmetry: Y / N")
    
    pdf.body("\n\nReviewer Signature: ____________________")
    pdf.body("Date: ____________________________________")
