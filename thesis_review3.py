#!/usr/bin/env python3
"""Chapter 3 - Variations & OMC"""

def add_omc_variations(pdf):
    pdf.add_page()
    pdf.heading("3.4 The Osteomeatal Complex (OMC)")
    pdf.body("The osteomeatal complex (OMC) is the functional core of the paranasal sinus drainage system. The term was coined by Naumann in 1965 and later popularized by Stammberger and Kennedy as the cornerstone of FESS. The OMC is not a single anatomical structure but rather a complex region where the maxillary, frontal, and anterior ethmoid sinuses converge and drain.")
    
    pdf.subheading("3.4.1 Components of OMC")
    pdf.bullet("Maxillary sinus ostium")
    pdf.bullet("Ethmoid infundibulum")
    pdf.bullet("Hiatus semilunaris")
    pdf.bullet("Middle turbinate")
    pdf.bullet("Uncinate process")
    pdf.bullet("Ethmoid bulla")
    pdf.bullet("Frontal recess")
    pdf.bullet("Anterior ethmoid air cells")
    
    pdf.subheading("3.4.2 The Uncinate Process")
    pdf.body("The uncinate process is a thin, sickle-shaped bony lamella forming the medial wall of the ethmoid infundibulum. Its anatomy is critical for understanding sinus drainage and FESS.")
    pdf.body("The superior attachment of the uncinate process is highly variable. Stammberger described six types based on its superior insertion:")
    pdf.bullet("Type I: Attaches to lamina papyracea (most common, 52%)")
    pdf.bullet("Type II: Attaches to skull base (fovea ethmoidalis) (6%)")
    pdf.bullet("Type III: Attaches to middle turbinate (26%)")
    pdf.bullet("Type IV: Combined attachments")
    pdf.bullet("Type V: Attaches to roof of maxillary sinus")
    pdf.bullet("Type VI: Free edge or bifurcated")
    
    pdf.body("The pattern of uncinate attachment determines the drainage of the frontal sinus:")
    pdf.bullet("Lamina papyracea attachment: Frontal sinus drains medial to uncinate (into middle meatus directly)")
    pdf.bullet("Skull base/middle turbinate attachment: Frontal sinus drains into ethmoid infundibulum")
    
    pdf.subheading("3.4.3 The Ethmoid Bulla")
    pdf.body("The ethmoid bulla is the largest and most consistent anterior ethmoid air cell, located posterior to the uncinate process. It forms the posterior wall of the hiatus semilunaris. Variations in size and pneumatization of the ethmoid bulla can affect drainage of adjacent sinuses.")
    
    pdf.subheading("3.4.4 The Hiatus Semilunaris")
    pdf.body("The hiatus semilunaris is a crescent-shaped opening between the uncinate process (anteriorly) and the ethmoid bulla (posteriorly). It is the entrance to the ethmoid infundibulum.")
    
    pdf.subheading("3.4.5 Clinical Significance of OMC")
    pdf.body("Obstruction of the OMC, even by minor mucosal swelling, can lead to:")
    pdf.bullet("Reduced ventilation of the maxillary, frontal, and anterior ethmoid sinuses")
    pdf.bullet("Mucus stasis and bacterial colonization")
    pdf.bullet("Chronic rhinosinusitis")
    pdf.bullet("Mucocele formation")
    pdf.body("FESS aims to restore ventilation and drainage by clearing OMC obstruction while preserving normal mucosa.")
    
    pdf.add_page()
    pdf.heading("3.5 Anatomical Variations of Paranasal Sinuses")
    pdf.body("This section provides a detailed account of various anatomical variations of paranasal sinuses, their prevalence in different populations, and their clinical significance.")
    
    pdf.subheading("3.5.1 Nasal Septum Variations")
    pdf.subheading("3.5.1.1 Deviated Nasal Septum (DNS)")
    pdf.body("Deviated nasal septum is the most common anatomical variation affecting the nasal cavity and indirectly the paranasal sinuses. The nasal septum is composed of the perpendicular plate of ethmoid (superiorly), vomer (inferoposteriorly), and quadrangular cartilage (anteriorly).")
    
    pdf.body("Etiology of DNS:")
    pdf.bullet("Congenital: Birth trauma, intrauterine pressure")
    pdf.bullet("Developmental: Asymmetric growth of facial bones")
    pdf.bullet("Acquired: Trauma (most common in adults)")
    pdf.bullet("Idiopathic")
    
    pdf.body("Classification (Mladina, 1987):")
    pdf.bullet("Type 1: Septum has unilateral vertical deviation that does not encroach on the valve area")
    pdf.bullet("Type 2: Septum has unilateral vertical deviation in the valve area")
    pdf.bullet("Type 3: Septum has unilateral deviation at the level of middle/superior turbinate")
    pdf.bullet("Type 4: Severe DNS with S-shape (one side anterior, opposite side posterior)")
    pdf.bullet("Type 5: Bony spur on one side")
    pdf.bullet("Type 6: Spur with deep groove or concavity on opposite side")
    pdf.bullet("Type 7: Combination of above types")
    
    pdf.body("Prevalence in Different Studies:")
    pdf.bullet("Earwaker (1993): 20-79% in CT studies")
    pdf.bullet("Stallman et al. (2004): 65%")
    pdf.bullet("Smith et al. (2010): 41-79%")
    pdf.bullet("Kim et al. (2007 - Korean): 78.9%")
    pdf.bullet("Adeel et al. (2013 - Pakistan): 64.5%")
    pdf.bullet("Dua et al. (2005 - North India): 75.4%")
    pdf.bullet("Mamatha et al. (2015 - South India): 58%")
    pdf.bullet("Patel et al. (2014 - Gujarat): 70%")
    
    pdf.body("Clinical Significance:")
    pdf.bullet("Nasal obstruction (most common symptom)")
    pdf.bullet("Recurrent sinusitis on the obstructed side")
    pdf.bullet("Compensatory hypertrophy of contralateral inferior turbinate")
    pdf.bullet("Snoring and sleep apnea")
    pdf.bullet("Epistaxis from spurs")
    pdf.bullet("Difficulty in nasal endoscopy and FESS")
    pdf.bullet("Paradoxical sinusitis on contralateral side")
    
    pdf.subheading("3.5.1.2 Septal Spurs and Crests")
    pdf.body("Septal spurs are localized angulations or projections of the septum, often at the junction of vomer and ethmoidal plate. Bolger et al. (1991) reported a prevalence of 30-50%. Spurs may impinge on the lateral nasal wall or middle turbinate, causing facial pain (Sluder's neuralgia) or contact-point headaches.")
    
    pdf.subheading("3.5.2 Turbinate Variations")
    
    pdf.subheading("3.5.2.1 Concha Bullosa")
    pdf.body("Concha bullosa refers to the pneumatization of the middle turbinate. It is one of the most common anatomical variations of the lateral nasal wall and has significant implications for sinus drainage and surgical access.")
    
    pdf.body("Bolger Classification (1991):")
    pdf.bullet("Lamellar type: Pneumatization confined to vertical lamella of middle turbinate")
    pdf.bullet("Bulbous type: Pneumatization in the inferior bulbous portion")
    pdf.bullet("Extensive (true) concha bullosa: Pneumatization of both lamellar and bulbous portions")
    
    pdf.body("Prevalence:")
    pdf.bullet("Bolger et al. (1991): 53.6% (any type)")
    pdf.bullet("Zinreich et al. (1988): 34%")
    pdf.bullet("Stallman et al. (2004): 35.8%")
    pdf.bullet("Tonai and Baba (1996 - Japan): 34%")
    pdf.bullet("Stackpole and Edelstein (1997): 24%")
    pdf.bullet("Adeel et al. (2013): 30.4%")
    pdf.bullet("Sharma et al. (2016 - India): 32.5%")
    pdf.bullet("Mamatha et al. (2015 - South India): 25%")
    
    pdf.body("Other Turbinate Pneumatizations:")
    pdf.bullet("Superior concha bullosa (4-15%)")
    pdf.bullet("Inferior turbinate pneumatization (rare, 1-2%)")
    pdf.bullet("Supreme turbinate pneumatization (rare)")
    
    pdf.body("Clinical Significance:")
    pdf.bullet("OMC obstruction leading to sinusitis")
    pdf.bullet("Headaches, facial pressure")
    pdf.bullet("Difficulty in middle meatus visualization during endoscopy")
    pdf.bullet("Need for surgical resection during FESS")
    pdf.bullet("Rarely, pyocele formation if obstructed")
    
    pdf.subheading("3.5.2.2 Paradoxical Middle Turbinate")
    pdf.body("Normally, the middle turbinate has a medial concavity. In paradoxical middle turbinate, the convexity faces medially (i.e., the lateral surface is concave). This variation can narrow the middle meatus and obstruct OMC drainage.")
    
    pdf.body("Prevalence:")
    pdf.bullet("Bolger et al. (1991): 26.1%")
    pdf.bullet("Stallman et al. (2004): 26.9%")
    pdf.bullet("Badia et al. (2005): 17%")
    pdf.bullet("Adeel et al. (2013): 15%")
    pdf.bullet("Indian studies: 12-15%")
    
    pdf.subheading("3.5.2.3 Secondary/Accessory Middle Turbinate")
    pdf.body("Secondary middle turbinate is a rare variation first described by Khanobthamchai et al. (1991). Prevalence is 0.5-2%. It appears as a separate, smaller turbinate medial to the regular middle turbinate.")
    
    pdf.subheading("3.5.3 Ethmoid Sinus Variations")
    
    pdf.subheading("3.5.3.1 Agger Nasi Cells")
    pdf.body("The agger nasi (\"nasal mound\") cells are the most anterior ethmoid air cells, located anterior and superior to the attachment of the middle turbinate. They are formed by pneumatization of the lacrimal bone and frontal process of maxilla.")
    
    pdf.body("Prevalence (essentially universal):")
    pdf.bullet("Bolger et al. (1991): 98.5%")
    pdf.bullet("Stammberger (1991): 89%")
    pdf.bullet("Wormald (2003): 96%")
    pdf.bullet("Jain et al. (2012 - India): 92%")
    pdf.bullet("Sharma et al. (2014): 89%")
    
    pdf.body("Clinical Significance:")
    pdf.bullet("Forms the anterior boundary of frontal recess")
    pdf.bullet("Surgical landmark for frontal sinus drainage")
    pdf.bullet("Large agger nasi cells can compress and obstruct frontal recess")
    pdf.bullet("Important target during frontal sinusotomy")
    
    pdf.subheading("3.5.3.2 Haller Cells (Infraorbital Ethmoid Cells)")
    pdf.body("First described by Albrecht von Haller in 1765, these are ethmoid air cells that pneumatize the orbital floor (medial part) and may extend into the maxillary sinus roof. They are positioned along the medial floor of the orbit, adjacent to the maxillary sinus ostium.")
    
    pdf.body("Prevalence:")
    pdf.bullet("Bolger et al. (1991): 10.3%")
    pdf.bullet("Stackpole and Edelstein (1997): 18%")
    pdf.bullet("Kantarci et al. (2004): 16%")
    pdf.bullet("Bademci et al. (2005): 15.7%")
    pdf.bullet("Jain et al. (2012 - India): 15.8%")
    pdf.bullet("Sharma et al. (2016 - India): 18.2%")
    
    pdf.body("Clinical Significance:")
    pdf.bullet("Can obstruct or narrow the maxillary sinus ostium")
    pdf.bullet("Associated with chronic and recurrent maxillary sinusitis")
    pdf.bullet("May be confused with periorbital cellulitis on imaging")
    pdf.bullet("Need to be addressed during FESS for adequate maxillary sinus drainage")
    pdf.bullet("Risk of orbital injury during surgical removal")
    
    pdf.subheading("3.5.3.3 Onodi Cells (Sphenoethmoidal Cells)")
    pdf.body("Onodi cells, named after Adolph Onodi (1903), are the most posterior ethmoid cells that pneumatize superolaterally to the sphenoid sinus, often coming into close relation with the optic nerve and internal carotid artery.")
    
    pdf.body("Prevalence:")
    pdf.bullet("Weinberger et al. (1996): 8-14%")
    pdf.bullet("Driben et al. (1998): 7%")
    pdf.bullet("DeLano et al. (1996): 12%")
    pdf.bullet("Wormald (2003): 14%")
    pdf.bullet("Jang et al. (2008 - Korean): 60% (highest reported)")
    pdf.bullet("Jain et al. (2012 - India): 10.5%")
    
    pdf.body("Clinical Significance:")
    pdf.bullet("Optic nerve runs through or adjacent to the lateral wall")
    pdf.bullet("Risk of optic nerve injury during posterior ethmoidectomy")
    pdf.bullet("Can be mistaken for sphenoid sinus on imaging")
    pdf.bullet("Approach to sphenoid sinus may need modification")
    pdf.bullet("Cause of optic neuritis or visual loss in sphenoethmoid sinusitis")
    
    pdf.subheading("3.5.3.4 Frontal Cells (Kuhn Classification)")
    pdf.body("Bent and Kuhn (1994) classified frontal recess cells into four types based on their relationship with the agger nasi cell and frontal sinus:")
    pdf.bullet("Type I: Single frontal recess cell above agger nasi, below frontal sinus")
    pdf.bullet("Type II: Tier (multiple) of frontal recess cells above agger nasi, below frontal sinus")
    pdf.bullet("Type III: Single large cell extending from agger nasi into frontal sinus")
    pdf.bullet("Type IV: Isolated cell within the frontal sinus")
    
    pdf.body("Prevalence:")
    pdf.bullet("Type I: 33%")
    pdf.bullet("Type II: 9.5%")
    pdf.bullet("Type III: 9.5%")
    pdf.bullet("Type IV: 1%")
    
    pdf.subheading("3.5.3.5 Supraorbital Ethmoid Cells")
    pdf.body("These ethmoid cells extend laterally over the orbital roof. They have a prevalence of 7.2-15% (Bolger et al., 1991; DelGaudio et al., 2005). Important to differentiate from frontal sinus on CT.")
    
    pdf.subheading("3.5.3.6 Lamina Papyracea Variations")
    pdf.bullet("Dehiscence: 0.5-1%")
    pdf.bullet("Medial bowing/displacement")
    pdf.bullet("Pneumatization defects")
    pdf.body("Clinical importance: Risk of orbital injury during ethmoidectomy")
    
    pdf.add_page()
    pdf.subheading("3.5.4 Maxillary Sinus Variations")
    
    pdf.subheading("3.5.4.1 Maxillary Sinus Hypoplasia")
    pdf.body("Maxillary sinus hypoplasia is characterized by underdevelopment of the maxillary sinus, often associated with abnormal uncinate process.")
    
    pdf.body("Bolger Classification (1990):")
    pdf.bullet("Type I: Mild hypoplasia with normal uncinate process")
    pdf.bullet("Type II: Significant hypoplasia with hypoplastic/absent uncinate process")
    pdf.bullet("Type III: Severe (cleft-like) hypoplasia with absent uncinate process")
    
    pdf.body("Prevalence:")
    pdf.bullet("Bolger et al. (1990): Type I 7.2%, Type II 0.6%, Type III 0.4%")
    pdf.bullet("Sirikci et al. (2000): 1.7-10.4% overall")
    pdf.bullet("Jain et al. (2012 - India): 4.3%")
    
    pdf.subheading("3.5.4.2 Underwood Septa")
    pdf.body("First described by Arthur Underwood in 1910, these are bony septa that partially or completely divide the maxillary sinus into compartments. They are clinically important during sinus lift procedures and dental implant placement.")
    
    pdf.body("Classification (Velasquez-Plata et al., 2002):")
    pdf.bullet("Type I (Anterior): Between first and second molar")
    pdf.bullet("Type II (Middle): Between second molar and tuberosity")
    pdf.bullet("Type III (Posterior): Posterior to maxillary tuberosity")
    
    pdf.body("Prevalence:")
    pdf.bullet("Velasquez-Plata et al. (2002): 21.6%")
    pdf.bullet("Kim et al. (2006): 26.5%")
    pdf.bullet("Maestre-Ferrin et al. (2011): 32.7%")
    pdf.bullet("Park et al. (2011): 41.7%")
    
    pdf.subheading("3.5.4.3 Accessory Maxillary Ostium")
    pdf.body("Additional opening in the lateral nasal wall, separate from the natural ostium. First described by Giraldes (1840). Located in the posterior fontanelle (between the inferior turbinate and uncinate process).")
    
    pdf.body("Prevalence:")
    pdf.bullet("Van Alyea (1936): 23%")
    pdf.bullet("Stammberger (1991): 10-30%")
    pdf.bullet("Earwaker (1993): 15%")
    pdf.bullet("Jain et al. (2012 - India): 18.4%")
    
    pdf.body("Significance: May lead to mucus recirculation and chronic sinusitis. Single AMO drainage is less effective than functional natural ostium.")
    
    pdf.subheading("3.5.5 Frontal Sinus Variations")
    
    pdf.subheading("3.5.5.1 Frontal Sinus Aplasia/Hypoplasia")
    pdf.bullet("Aplasia: 5-15%")
    pdf.bullet("Hypoplasia: 5-10%")
    pdf.bullet("Bilateral aplasia: 1-4%")
    pdf.bullet("Indian studies (Ponde 2003, Nikam 2015): 3.8-4.2%")
    
    pdf.body("Frontal sinus development is the most variable. Higher altitude populations show smaller frontal sinuses. Genetic and environmental factors influence size.")
    
    pdf.subheading("3.5.5.2 Frontal Sinus Asymmetry")
    pdf.body("Asymmetry between right and left frontal sinuses is common (Harris et al., 1987: 85%). This forms the basis for forensic identification using frontal sinus radiographs - the pattern is unique to each individual, comparable to fingerprints.")
    
    pdf.subheading("3.5.5.3 Interfrontal Septal Cell")
    pdf.body("Cell within the interfrontal septum, prevalence 12-36% (McLaughlin et al., 2001). May obstruct frontal recess.")
    
    pdf.subheading("3.5.6 Sphenoid Sinus Variations")
    
    pdf.subheading("3.5.6.1 Sphenoid Sinus Pneumatization (Hamberger Classification)")
    pdf.bullet("Conchal type (2-3%): Solid bone, surgically challenging")
    pdf.bullet("Presellar type (11-24%): Limited pneumatization")
    pdf.bullet("Sellar type (73-86%): Most common, ideal for transsphenoidal surgery")
    
    pdf.body("Indian Studies:")
    pdf.bullet("Vaishya et al. (2015): Sellar 76%, Presellar 20%, Conchal 4%")
    pdf.bullet("Naveen et al. (2018): Sellar 82.5%")
    
    pdf.subheading("3.5.6.2 ICA Dehiscence")
    pdf.body("Bony dehiscence over the internal carotid artery in the lateral wall of sphenoid sinus.")
    pdf.bullet("Fujii et al. (1979): 4-8%")
    pdf.bullet("Renn and Rhoton (1975): 4%")
    pdf.bullet("Sirikci et al. (2000): 5.5%")
    pdf.bullet("Sethi et al. (1995): 22%")
    pdf.bullet("Vaishya et al. (2015 - India): 7.5%")
    
    pdf.body("Critical surgical importance - injury can be catastrophic with mortality rates up to 50%.")
    
    pdf.subheading("3.5.6.3 Optic Nerve Variations")
    pdf.body("DeLano et al. (1996) classified the optic nerve relationship with sphenoid sinus into four types:")
    pdf.bullet("Type I (76%): Adjacent to sphenoid sinus, no indentation")
    pdf.bullet("Type II (15%): Indents sphenoid sinus, no contact with posterior ethmoid")
    pdf.bullet("Type III (6%): Passes through sphenoid sinus")
    pdf.bullet("Type IV (3%): Adjacent to both sphenoid and posterior ethmoid (Onodi cell)")
    
    pdf.body("Optic nerve dehiscence (4-12%) increases the risk of visual loss during surgery.")
    
    pdf.subheading("3.5.7 Anterior Skull Base Variations")
    
    pdf.subheading("3.5.7.1 Keros Classification of Olfactory Fossa")
    pdf.body("Keros (1962) classified the depth of the olfactory fossa into three types based on the difference in height between the cribriform plate and the fovea ethmoidalis:")
    pdf.bullet("Type I (1-3 mm): Shallow olfactory fossa, lowest risk (12-26%)")
    pdf.bullet("Type II (4-7 mm): Moderate depth (52-73%, most common)")
    pdf.bullet("Type III (8-16 mm): Deep olfactory fossa, highest surgical risk (8-26%)")
    
    pdf.body("Type III configuration significantly increases the risk of CSF leak during ethmoidectomy due to the long, thin lateral lamella of the cribriform plate.")
    
    pdf.subheading("3.5.7.2 Cribriform Plate Asymmetry")
    pdf.body("Asymmetry between right and left sides is reported in 10-20% (Meloni et al., 1992). The lower side is at higher risk of inadvertent skull base injury during surgery.")
    
    pdf.subheading("3.5.8 Other Variations")
    pdf.bullet("Pneumatized crista galli")
    pdf.bullet("Frontal sinus septation")
    pdf.bullet("Pneumatized anterior clinoid process")
    pdf.bullet("Pneumatized pterygoid process")
    pdf.bullet("Pneumatized vomer")
    pdf.bullet("Vomeral spurs")
