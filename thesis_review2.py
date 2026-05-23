#!/usr/bin/env python3
"""Chapter 3 continued: Detailed Anatomy"""

def add_anatomy_review(pdf):
    pdf.add_page()
    pdf.heading("3.3 Detailed Anatomy of Paranasal Sinuses")
    
    pdf.subheading("3.3.1 Maxillary Sinus")
    pdf.body("The maxillary sinus is the largest of the paranasal sinuses, occupying the body of the maxillary bone. It is pyramidal in shape, with its base directed medially toward the nasal cavity and its apex pointing laterally toward the zygomatic process.")
    
    pdf.body("Dimensions and Volume:")
    pdf.bullet("Average anteroposterior diameter: 34 mm (range 23-49 mm)")
    pdf.bullet("Average vertical diameter: 33 mm (range 22-45 mm)")
    pdf.bullet("Average mediolateral width: 25 mm (range 16-40 mm)")
    pdf.bullet("Average volume: 12-15 ml (range 4-35 ml)")
    
    pdf.body("Walls of the Maxillary Sinus:")
    pdf.bullet("Anterior wall: Formed by the anterior surface of the maxilla, contains the infraorbital foramen and canal carrying the infraorbital nerve and vessels")
    pdf.bullet("Posterior wall: Formed by the infratemporal surface of the maxilla, related to the pterygopalatine fossa, infratemporal fossa, and the third division of trigeminal nerve")
    pdf.bullet("Superior wall (roof): Forms the floor of the orbit, contains the infraorbital canal; thin bone may transmit infections to orbit")
    pdf.bullet("Inferior wall (floor): Formed by the alveolar process of maxilla, intimately related to the roots of upper premolar and molar teeth")
    pdf.bullet("Medial wall: Forms the lateral wall of nasal cavity, contains the maxillary ostium opening into the middle meatus through the hiatus semilunaris")
    
    pdf.body("The maxillary ostium, the natural opening of the maxillary sinus, is located in the upper part of the medial wall. This high position is functionally disadvantageous as it requires active mucociliary transport against gravity for sinus drainage. The ostium typically measures 3-5 mm in diameter and opens into the middle meatus through the ethmoidal infundibulum.")
    
    pdf.body("Lining and Innervation:")
    pdf.body("The maxillary sinus is lined by ciliated pseudostratified columnar epithelium (respiratory mucosa) which is thinner and less vascular than the nasal mucosa. The arterial supply comes from branches of the maxillary artery (infraorbital, posterior superior alveolar, and greater palatine arteries). Venous drainage is via the pterygoid venous plexus and facial vein. Innervation is through the maxillary division (V2) of the trigeminal nerve via the infraorbital, posterior superior alveolar, middle superior alveolar, and anterior superior alveolar nerves.")
    
    pdf.body("Clinical Relations:")
    pdf.bullet("Roots of upper teeth (especially second premolar and first molar) may protrude into the sinus floor")
    pdf.bullet("Dental infections can spread to the maxillary sinus (odontogenic sinusitis)")
    pdf.bullet("Tumors of the maxillary sinus may invade the orbit, infratemporal fossa, or oral cavity")
    pdf.bullet("Underwood septa may divide the sinus into compartments")
    
    pdf.subheading("3.3.2 Ethmoid Sinuses")
    pdf.body("The ethmoid sinuses are a complex labyrinth of air cells located within the ethmoid bone, between the nasal cavity (medially) and the orbit (laterally). They are arranged in three rows extending from anterior to posterior.")
    
    pdf.body("Anatomical Boundaries of Ethmoid Labyrinth:")
    pdf.bullet("Superior: Cribriform plate of ethmoid (medial) and fovea ethmoidalis of frontal bone (lateral)")
    pdf.bullet("Inferior: Maxillary sinus and middle/superior turbinate")
    pdf.bullet("Medial: Lateral nasal wall (middle and superior turbinates)")
    pdf.bullet("Lateral: Lamina papyracea (separating it from orbit)")
    pdf.bullet("Anterior: Frontal process of maxilla and lacrimal bone")
    pdf.bullet("Posterior: Sphenoid sinus")
    
    pdf.body("Classification of Ethmoid Cells:")
    pdf.body("The ethmoid air cells are traditionally divided into anterior and posterior groups based on their drainage:")
    pdf.bullet("Anterior ethmoid cells: Drain into the middle meatus, including the ethmoid bulla and uncinate process region")
    pdf.bullet("Posterior ethmoid cells: Drain into the superior meatus and may extend into the sphenoid bone (Onodi cells)")
    
    pdf.body("Anatomical Variations:")
    pdf.bullet("Agger nasi cells (98% prevalence) - most anterior ethmoid cells")
    pdf.bullet("Frontal recess cells (Kuhn types I-IV)")
    pdf.bullet("Haller cells (10-45%) - infraorbital ethmoid cells")
    pdf.bullet("Onodi cells (8-14%) - posterior ethmoid cells extending to sphenoid")
    pdf.bullet("Supraorbital ethmoid cells (7-15%)")
    pdf.bullet("Suprabullar cells")
    pdf.bullet("Retrobullar cells")
    
    pdf.body("Vascular Supply and Innervation:")
    pdf.body("The ethmoid sinuses receive blood supply from the anterior and posterior ethmoidal arteries (branches of the ophthalmic artery) and sphenopalatine artery (branch of maxillary artery). The anterior ethmoidal artery is a critical surgical landmark, lying within the anterior ethmoidal foramen and traversing the ethmoid roof from the orbit to the anterior cranial fossa. Innervation is by the anterior and posterior ethmoidal nerves (branches of the ophthalmic nerve V1) and orbital branches of the pterygopalatine ganglion.")
    
    pdf.body("Clinical Significance:")
    pdf.bullet("Lamina papyracea: Thin medial orbital wall - injury can cause periorbital emphysema or hematoma")
    pdf.bullet("Anterior ethmoidal artery: Injury can cause retro-orbital hematoma and vision loss")
    pdf.bullet("Cribriform plate: Skull base; injury causes CSF leak")
    pdf.bullet("Olfactory fossa depth (Keros classification) - higher Keros types increase surgical risk")
    
    pdf.subheading("3.3.3 Frontal Sinus")
    pdf.body("The frontal sinuses are paired, asymmetric cavities located within the frontal bone, behind the superciliary arches. They are typically separated by an intersinus septum that is rarely in the midline. The frontal sinuses are absent at birth and develop progressively until adolescence.")
    
    pdf.body("Dimensions and Volume:")
    pdf.bullet("Average vertical height: 32 mm (range 17-50 mm)")
    pdf.bullet("Average transverse width: 26 mm (range 14-40 mm)")
    pdf.bullet("Average anteroposterior depth: 19 mm (range 10-28 mm)")
    pdf.bullet("Average volume: 6-7 ml per side")
    
    pdf.body("Walls of the Frontal Sinus:")
    pdf.bullet("Anterior wall: Thick, formed by the outer table of frontal bone")
    pdf.bullet("Posterior wall: Thin, separates sinus from anterior cranial fossa and frontal lobe")
    pdf.bullet("Inferior wall (floor): Forms part of orbital roof and contains the frontal recess opening")
    pdf.bullet("Medial wall: Intersinus septum, often deviated from midline")
    
    pdf.body("Drainage of Frontal Sinus:")
    pdf.body("The frontal sinus drains via the frontal recess (formerly called nasofrontal duct) into the middle meatus. The anatomy of the frontal recess is highly variable and complex, often described as an \"hourglass\" with the narrowest point being the frontal ostium. Understanding this anatomy is crucial for endoscopic frontal sinus surgery.")
    
    pdf.body("Variations:")
    pdf.bullet("Aplasia (absence): 5-15% unilateral, 1-4% bilateral")
    pdf.bullet("Hypoplasia: 5-10%")
    pdf.bullet("Asymmetry: 80-85%")
    pdf.bullet("Bony septations: 10-30%")
    pdf.bullet("Pneumatization extending to orbital roof or temporal bone")
    pdf.bullet("Frontal cells (Kuhn types I-IV)")
    
    pdf.body("Clinical Significance:")
    pdf.bullet("Frontal sinus drainage is the most challenging area in FESS")
    pdf.bullet("Forensic identification using frontal sinus radiographs (highly individual pattern)")
    pdf.bullet("Frontal sinus fractures may require surgical reconstruction")
    pdf.bullet("Mucocele formation due to drainage obstruction")
    
    pdf.subheading("3.3.4 Sphenoid Sinus")
    pdf.body("The sphenoid sinuses are paired cavities located within the body of the sphenoid bone, deep within the skull. They are the most posteriorly placed paranasal sinuses and have important anatomical relationships with critical neurovascular structures.")
    
    pdf.body("Dimensions and Volume:")
    pdf.bullet("Average vertical height: 20 mm (range 10-32 mm)")
    pdf.bullet("Average transverse width: 17 mm (range 9-31 mm)")
    pdf.bullet("Average anteroposterior depth: 23 mm (range 11-43 mm)")
    pdf.bullet("Average volume: 7-8 ml per side")
    
    pdf.body("Walls of the Sphenoid Sinus:")
    pdf.bullet("Anterior wall: Faces the nasal cavity, contains the sphenoid ostium")
    pdf.bullet("Posterior wall: Related to clivus, brainstem, basilar artery")
    pdf.bullet("Superior wall: Related to sella turcica, pituitary gland, optic chiasm")
    pdf.bullet("Inferior wall (floor): Related to nasopharynx and palatine bone")
    pdf.bullet("Lateral wall: Related to cavernous sinus, internal carotid artery, optic nerve, abducens nerve, and oculomotor nerve")
    
    pdf.body("Drainage:")
    pdf.body("The sphenoid sinus drains through the sphenoid ostium, located in the upper part of the anterior wall, into the sphenoethmoidal recess (above the superior turbinate).")
    
    pdf.body("Critical Relations:")
    pdf.bullet("Internal carotid artery (lateral wall)")
    pdf.bullet("Optic nerve (superolateral wall)")
    pdf.bullet("Cavernous sinus (lateral wall)")
    pdf.bullet("Pituitary gland (superior wall)")
    pdf.bullet("Vidian canal (floor)")
    pdf.bullet("Foramen rotundum (lateral wall)")
    pdf.bullet("Maxillary nerve (V2) - in lateral wall")
    
    pdf.body("Septation:")
    pdf.body("The sphenoid sinus is divided into right and left compartments by an intersinus septum that is rarely midline. The septation pattern is highly variable:")
    pdf.bullet("Single midline septum: 32-44%")
    pdf.bullet("Single off-midline septum: 30-50%")
    pdf.bullet("Multiple septa: 18-32%")
    pdf.bullet("Septum attaching to ICA canal: 8-25% (clinically significant)")
    
    pdf.body("Pneumatization Types (Hamberger Classification):")
    pdf.bullet("Conchal type (2-3%): Cancellous bone with no pneumatization")
    pdf.bullet("Presellar type (11-24%): Pneumatization extends to anterior wall of sella")
    pdf.bullet("Sellar type (73-86%): Pneumatization extends below sella")
    pdf.bullet("Postsellar type: Pneumatization extends posterior to sella into clivus")
    
    pdf.body("Clinical Significance:")
    pdf.bullet("Approach for transsphenoidal pituitary surgery")
    pdf.bullet("ICA dehiscence (4-22%) - risk of catastrophic hemorrhage")
    pdf.bullet("Optic nerve dehiscence (4-12%) - risk of vision loss")
    pdf.bullet("Onodi cells overlying sphenoid - alters surgical approach")
    pdf.bullet("Skull base reconstruction after CSF leak")
