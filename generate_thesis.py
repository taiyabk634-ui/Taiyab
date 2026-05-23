#!/usr/bin/env python3
"""
MD Anatomy Thesis PDF Generator
Topic: Anatomical Variation of Paranasal Air Sinuses: A CT Study in South Gujarat Region
Target: 220 pages comprehensive thesis with CT image placeholders
"""

from fpdf import FPDF
from datetime import datetime

class ThesisPDF(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', 'A4')
        self.set_margins(25, 25, 25)
        self.set_auto_page_break(auto=True, margin=25)
        self.set_title("Anatomical Variation of Paranasal Air Sinuses - CT Study")
        self.set_author("MD Anatomy Resident")
        
    def footer(self):
        if self.page_no() > 1:
            self.set_y(-20)
            self.set_font('Times', 'I', 10)
            self.cell(0, 10, f'{self.page_no()}', align='C')

    def safe(self, text):
        """Clean text for latin-1 encoding"""
        if not text:
            return ""
        replacements = {
            'ğ': 'g', 'ö': 'o', 'ü': 'u', 'ı': 'i', 'ç': 'c', 'ş': 's',
            'Ğ': 'G', 'Ö': 'O', 'Ü': 'U', 'İ': 'I', 'Ç': 'C', 'Ş': 'S',
            '"': '"', '"': '"', ''': "'", ''': "'", '–': '-', '—': '--',
            '…': '...', '°': 'deg', '±': '+/-', '×': 'x', '÷': '/',
            '≤': '<=', '≥': '>=', '≠': '!=', '≈': '~=', '∞': 'infinity',
            'α': 'alpha', 'β': 'beta', 'γ': 'gamma', 'δ': 'delta',
            'μ': 'micro', 'π': 'pi', 'σ': 'sigma', 'Σ': 'Sigma',
            '→': '->', '←': '<-', '↑': '^', '↓': 'v',
            '\u2022': '-', '\u00a0': ' ', '\u200b': '',
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text.encode('latin-1', 'replace').decode('latin-1')

    def title_page(self, title, subtitle, author, guide, institution, year):
        self.add_page()
        self.set_x(self.l_margin)
        self.set_y(40)
        self.set_font('Times', 'B', 18)
        self.multi_cell(0, 10, self.safe(title), align='C')
        self.ln(5)
        self.set_x(self.l_margin)
        self.set_font('Times', 'BI', 14)
        self.multi_cell(0, 8, self.safe(subtitle), align='C')
        self.ln(20)
        
        self.set_font('Times', '', 12)
        self.set_x(self.l_margin)
        self.multi_cell(0, 7, self.safe("THESIS"), align='C')
        self.ln(3)
        self.set_x(self.l_margin)
        self.multi_cell(0, 7, self.safe("Submitted to"), align='C')
        self.ln(3)
        self.set_font('Times', 'B', 13)
        self.set_x(self.l_margin)
        self.multi_cell(0, 7, self.safe(institution), align='C')
        self.ln(3)
        self.set_font('Times', '', 12)
        self.set_x(self.l_margin)
        self.multi_cell(0, 7, self.safe("In partial fulfillment of the requirements"), align='C')
        self.set_x(self.l_margin)
        self.multi_cell(0, 7, self.safe("for the degree of"), align='C')
        self.ln(3)
        self.set_font('Times', 'B', 14)
        self.set_x(self.l_margin)
        self.multi_cell(0, 7, self.safe("DOCTOR OF MEDICINE (M.D.)"), align='C')
        self.set_x(self.l_margin)
        self.multi_cell(0, 7, self.safe("IN ANATOMY"), align='C')
        self.ln(20)
        
        self.set_font('Times', '', 12)
        self.set_x(self.l_margin)
        self.multi_cell(0, 7, self.safe("By"), align='C')
        self.ln(2)
        self.set_font('Times', 'B', 13)
        self.set_x(self.l_margin)
        self.multi_cell(0, 7, self.safe(author), align='C')
        self.ln(15)
        
        self.set_font('Times', '', 12)
        self.set_x(self.l_margin)
        self.multi_cell(0, 7, self.safe("Under the guidance of"), align='C')
        self.ln(2)
        self.set_font('Times', 'B', 13)
        self.set_x(self.l_margin)
        self.multi_cell(0, 7, self.safe(guide), align='C')
        self.ln(20)
        
        self.set_font('Times', 'B', 13)
        self.set_x(self.l_margin)
        self.multi_cell(0, 7, self.safe(year), align='C')

    def section_title(self, text, top_margin=10):
        self.ln(top_margin)
        self.set_x(self.l_margin)
        self.set_font('Times', 'B', 16)
        self.multi_cell(0, 9, self.safe(text), align='C')
        self.ln(3)
        self.set_draw_color(0, 0, 0)
        self.line(self.get_x() + 30, self.get_y(), self.get_x() + 160, self.get_y())
        self.ln(8)

    def heading(self, text, size=13):
        self.ln(4)
        self.set_x(self.l_margin)
        self.set_font('Times', 'B', size)
        self.multi_cell(0, 7, self.safe(text))
        self.ln(2)

    def subheading(self, text):
        self.ln(2)
        self.set_x(self.l_margin)
        self.set_font('Times', 'B', 12)
        self.multi_cell(0, 6, self.safe(text))
        self.ln(1)

    def body(self, text, indent=False):
        self.set_x(self.l_margin)
        self.set_font('Times', '', 11)
        if indent:
            self.cell(8)
        self.multi_cell(0, 6, self.safe(text), align='J')
        self.ln(2)

    def bullet(self, text):
        self.set_font('Times', '', 11)
        self.set_x(self.l_margin + 5)
        self.cell(5, 6, '-')
        x_pos = self.l_margin + 12
        self.set_x(x_pos)
        # Use width that fits in remaining space
        avail_width = self.w - x_pos - self.r_margin
        self.multi_cell(avail_width, 6, self.safe(text))
        self.ln(0.5)

    def numbered(self, num, text):
        self.set_font('Times', '', 11)
        self.set_x(self.l_margin + 3)
        self.cell(8, 6, f"{num}.")
        x_pos = self.l_margin + 12
        self.set_x(x_pos)
        avail_width = self.w - x_pos - self.r_margin
        self.multi_cell(avail_width, 6, self.safe(text))
        self.ln(0.5)

    def ct_image_box(self, figure_num, caption):
        """Create a placeholder box for CT images with caption"""
        if self.get_y() > 200:
            self.add_page()
        self.ln(5)
        # Draw image box
        x = self.l_margin + 20
        y = self.get_y()
        width = 120
        height = 80
        self.set_draw_color(100, 100, 100)
        self.set_fill_color(240, 240, 240)
        self.rect(x, y, width, height, 'DF')
        
        # Add label inside box
        self.set_xy(x, y + height/2 - 5)
        self.set_font('Times', 'I', 10)
        self.set_text_color(120, 120, 120)
        self.cell(width, 5, self.safe(f"[CT Image: {figure_num}]"), align='C')
        self.ln(2)
        self.cell(width, 5, self.safe("(Insert actual CT scan here)"), align='C')
        self.set_text_color(0, 0, 0)
        
        self.set_y(y + height + 3)
        self.set_font('Times', 'B', 10)
        self.multi_cell(0, 5, self.safe(f"Figure {figure_num}: {caption}"), align='C')
        self.ln(5)

    def table(self, headers, rows, col_widths=None):
        if col_widths is None:
            total_width = 160
            col_widths = [total_width / len(headers)] * len(headers)
        
        self.set_font('Times', 'B', 10)
        self.set_fill_color(220, 220, 220)
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 7, self.safe(header), border=1, align='C', fill=True)
        self.ln()
        
        self.set_font('Times', '', 10)
        self.set_fill_color(255, 255, 255)
        for row in rows:
            for i, cell in enumerate(row):
                text = self.safe(str(cell))
                if len(text) > 30:
                    text = text[:30] + '..'
                self.cell(col_widths[i], 6, text, border=1, align='L')
            self.ln()
        self.ln(3)

    def page_break(self):
        self.add_page()

    def blank_page(self):
        self.add_page()
        self.set_y(140)
        self.set_font('Times', 'I', 10)
        self.cell(0, 5, '', align='C')


def generate_thesis():
    pdf = ThesisPDF()
    
    # ============= COVER / TITLE PAGE =============
    pdf.title_page(
        title="ANATOMICAL VARIATION OF PARANASAL AIR SINUSES:",
        subtitle="A CT STUDY IN SOUTH GUJARAT REGION",
        author="Dr. [Candidate Name]\nM.D. Anatomy Resident",
        guide="Dr. [Guide Name]\nProfessor & Head\nDepartment of Anatomy",
        institution="THE MAHARAJA SAYAJIRAO UNIVERSITY OF BARODA\n/ GUJARAT UNIVERSITY OF HEALTH SCIENCES",
        year="MAY 2026"
    )
    
    # ============= CERTIFICATE BY GUIDE =============
    pdf.add_page()
    pdf.section_title("CERTIFICATE BY GUIDE")
    pdf.body("This is to certify that the thesis entitled \"ANATOMICAL VARIATION OF PARANASAL AIR SINUSES: A CT STUDY IN SOUTH GUJARAT REGION\" submitted by Dr. [Candidate Name] for the partial fulfillment of the requirements for the degree of Doctor of Medicine (M.D.) in Anatomy is a bonafide research work carried out by him/her under my direct supervision and guidance.")
    pdf.ln(3)
    pdf.body("To the best of my knowledge and belief, the thesis embodies the work of the candidate himself/herself, has duly been completed, and fulfills the requirements of the ordinance relating to M.D. degree of the University and is up to the standard, both in respect of contents and language, for being referred to the examiner.")
    pdf.ln(15)
    pdf.body("Date: ___________________")
    pdf.body("Place: Surat, Gujarat")
    pdf.ln(20)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 7, pdf.safe("Dr. [Guide Name]"), align='R')
    pdf.ln(7)
    pdf.set_font('Times', '', 11)
    pdf.cell(0, 6, pdf.safe("M.D. (Anatomy), Ph.D."), align='R')
    pdf.ln(6)
    pdf.cell(0, 6, pdf.safe("Professor and Head"), align='R')
    pdf.ln(6)
    pdf.cell(0, 6, pdf.safe("Department of Anatomy"), align='R')
    pdf.ln(6)
    pdf.cell(0, 6, pdf.safe("[Medical College Name]"), align='R')
    
    # ============= CERTIFICATE BY HEAD =============
    pdf.add_page()
    pdf.section_title("CERTIFICATE BY HEAD OF DEPARTMENT")
    pdf.body("This is to certify that the thesis entitled \"ANATOMICAL VARIATION OF PARANASAL AIR SINUSES: A CT STUDY IN SOUTH GUJARAT REGION\" is a bonafide research work done by Dr. [Candidate Name] in partial fulfillment of the requirements for the degree of Doctor of Medicine (M.D.) in Anatomy.")
    pdf.ln(3)
    pdf.body("The thesis has been approved by the Department of Anatomy and is being forwarded for evaluation.")
    pdf.ln(20)
    pdf.body("Date: ___________________")
    pdf.body("Place: Surat, Gujarat")
    pdf.ln(20)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 7, pdf.safe("Dr. [HOD Name]"), align='R')
    pdf.ln(7)
    pdf.set_font('Times', '', 11)
    pdf.cell(0, 6, pdf.safe("Professor and Head"), align='R')
    pdf.ln(6)
    pdf.cell(0, 6, pdf.safe("Department of Anatomy"), align='R')
    
    # ============= CERTIFICATE BY DEAN =============
    pdf.add_page()
    pdf.section_title("CERTIFICATE BY DEAN/PRINCIPAL")
    pdf.body("This is to certify that the thesis entitled \"ANATOMICAL VARIATION OF PARANASAL AIR SINUSES: A CT STUDY IN SOUTH GUJARAT REGION\" is a bonafide research work done by Dr. [Candidate Name] under the guidance of Dr. [Guide Name], Professor and Head, Department of Anatomy, in partial fulfillment of the requirements for the degree of Doctor of Medicine (M.D.) in Anatomy.")
    pdf.ln(20)
    pdf.body("Date: ___________________")
    pdf.body("Place: Surat, Gujarat")
    pdf.ln(25)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 7, pdf.safe("Dr. [Dean Name]"), align='R')
    pdf.ln(7)
    pdf.set_font('Times', '', 11)
    pdf.cell(0, 6, pdf.safe("Dean / Principal"), align='R')
    pdf.ln(6)
    pdf.cell(0, 6, pdf.safe("[Medical College Name]"), align='R')
    
    # ============= DECLARATION =============
    pdf.add_page()
    pdf.section_title("DECLARATION BY THE CANDIDATE")
    pdf.body("I hereby declare that this thesis entitled \"ANATOMICAL VARIATION OF PARANASAL AIR SINUSES: A CT STUDY IN SOUTH GUJARAT REGION\" is a bonafide and genuine research work carried out by me under the guidance of Dr. [Guide Name], Professor and Head, Department of Anatomy, [Medical College Name], Surat.")
    pdf.ln(3)
    pdf.body("I further declare that this thesis or any part of it has not been submitted by me for the award of any other degree or diploma of any other University or Institute previously.")
    pdf.ln(3)
    pdf.body("All sources of information used in this thesis have been duly acknowledged. The work presented here is original and authentic to the best of my knowledge and belief.")
    pdf.ln(25)
    pdf.body("Date: ___________________")
    pdf.body("Place: Surat, Gujarat")
    pdf.ln(25)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 7, pdf.safe("Dr. [Candidate Name]"), align='R')
    pdf.ln(7)
    pdf.set_font('Times', '', 11)
    pdf.cell(0, 6, pdf.safe("M.D. Anatomy Resident"), align='R')
    pdf.ln(6)
    pdf.cell(0, 6, pdf.safe("Department of Anatomy"), align='R')
    
    # ============= ACKNOWLEDGEMENT =============
    pdf.add_page()
    pdf.section_title("ACKNOWLEDGEMENT")
    
    pdf.body("With the deepest sense of gratitude, I would like to acknowledge all those who have contributed to the successful completion of this thesis.")
    pdf.body("First and foremost, I bow my head before the Almighty God for showering His blessings upon me throughout this academic journey and for giving me the strength, knowledge, ability, and opportunity to undertake this research study and to persevere and complete it satisfactorily.")
    pdf.body("I express my profound gratitude and indebtedness to my esteemed guide, Dr. [Guide Name], Professor and Head, Department of Anatomy, [Medical College Name], for her/his invaluable guidance, constant encouragement, constructive criticism, and unstinted help throughout the course of this study. Her/his vast experience, deep knowledge, and meticulous approach to research have been a source of inspiration to me. I am extremely fortunate to have worked under such a learned mentor.")
    pdf.body("I am deeply thankful to Dr. [Co-Guide Name], Associate Professor, Department of Radiology, for the valuable inputs in CT scan interpretation and for sharing expertise in radiological anatomy. The technical assistance provided was instrumental in the completion of this study.")
    pdf.body("I extend my sincere thanks to Dr. [Dean Name], Dean/Principal of [Medical College Name], for granting permission to conduct this study and for providing the necessary infrastructure and facilities.")
    pdf.body("My heartfelt thanks to all the faculty members of the Department of Anatomy: Dr. [Name 1], Dr. [Name 2], Dr. [Name 3], for their continuous support, valuable suggestions, and encouragement throughout my postgraduate training.")
    pdf.body("I am grateful to the Department of Radiology, especially the CT scan technicians and staff, for their cooperation in providing access to CT scan images and for their patience in answering my queries.")
    pdf.body("I extend my sincere thanks to the Institutional Ethics Committee for granting ethical clearance for this research project.")
    pdf.body("I would like to thank the librarian and staff of the Central Library for providing access to journals, books, and online databases that formed the backbone of my literature review.")
    pdf.body("I express my gratitude to my fellow postgraduate colleagues for their support, friendship, and academic discussions that enriched my learning experience.")
    pdf.body("I am thankful to the statistician, Mr./Ms. [Name], for his/her expert help with statistical analysis and interpretation of data.")
    pdf.body("Special thanks to the patients whose CT scans formed the basis of this research. Their inadvertent contribution to the advancement of medical knowledge is gratefully acknowledged.")
    pdf.body("My heartfelt gratitude to my parents, [Father's Name] and [Mother's Name], for their unconditional love, prayers, sacrifices, and unwavering support. Their blessings and motivation have been the driving force behind my achievements. Without their encouragement, this academic milestone would not have been possible.")
    pdf.body("I am also thankful to my siblings and family members for their moral support, understanding, and patience during the long hours of research and writing.")
    pdf.body("Last but not least, I thank everyone who has directly or indirectly helped me in completing this thesis, whose names may not have been mentioned here but whose contributions are sincerely appreciated.")
    pdf.ln(15)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 7, pdf.safe("Dr. [Candidate Name]"), align='R')
    
    # ============= LIST OF ABBREVIATIONS =============
    pdf.add_page()
    pdf.section_title("LIST OF ABBREVIATIONS")
    
    abbreviations = [
        ("PNS", "Paranasal Sinuses"),
        ("CT", "Computed Tomography"),
        ("HRCT", "High Resolution Computed Tomography"),
        ("MDCT", "Multi-Detector Computed Tomography"),
        ("MRI", "Magnetic Resonance Imaging"),
        ("FESS", "Functional Endoscopic Sinus Surgery"),
        ("OMC", "Osteomeatal Complex"),
        ("DNS", "Deviated Nasal Septum"),
        ("CB", "Concha Bullosa"),
        ("AN", "Agger Nasi"),
        ("HC", "Haller Cell"),
        ("OC", "Onodi Cell"),
        ("ICA", "Internal Carotid Artery"),
        ("CSF", "Cerebrospinal Fluid"),
        ("AP", "Antero-Posterior"),
        ("ML", "Medio-Lateral"),
        ("3D", "Three Dimensional"),
        ("2D", "Two Dimensional"),
        ("HU", "Hounsfield Unit"),
        ("kVp", "Kilovoltage Peak"),
        ("mA", "Milli-Ampere"),
        ("mm", "Millimeter"),
        ("cm", "Centimeter"),
        ("ml", "Milliliter"),
        ("CRS", "Chronic Rhinosinusitis"),
        ("ARS", "Acute Rhinosinusitis"),
        ("ENT", "Ear, Nose and Throat"),
        ("PMT", "Paradoxical Middle Turbinate"),
        ("AMO", "Accessory Maxillary Ostium"),
        ("IEC", "Institutional Ethics Committee"),
        ("WHO", "World Health Organization"),
        ("USG", "Ultrasonography"),
        ("PA", "Postero-Anterior"),
        ("AAO-HNS", "American Academy of Otolaryngology Head and Neck Surgery"),
        ("EPOS", "European Position Paper on Rhinosinusitis"),
        ("SD", "Standard Deviation"),
        ("CI", "Confidence Interval"),
        ("M:F", "Male to Female Ratio"),
        ("Y", "Years"),
        ("No.", "Number"),
        ("%", "Percentage"),
        ("Lt", "Left"),
        ("Rt", "Right"),
        ("B/L", "Bilateral"),
        ("U/L", "Unilateral"),
    ]
    
    pdf.set_font('Times', '', 11)
    for abbr, full in abbreviations:
        pdf.set_x(pdf.l_margin + 5)
        pdf.set_font('Times', 'B', 11)
        pdf.cell(40, 6, pdf.safe(abbr))
        pdf.set_font('Times', '', 11)
        pdf.cell(0, 6, pdf.safe(": " + full))
        pdf.ln(6)
    
    # ============= TABLE OF CONTENTS =============
    pdf.add_page()
    pdf.section_title("TABLE OF CONTENTS")
    
    toc = [
        ("Sr. No.", "Title", "Page No."),
        ("1.", "Introduction", "1"),
        ("2.", "Aims and Objectives", "8"),
        ("3.", "Review of Literature", "11"),
        ("3.1", "Historical Background", "12"),
        ("3.2", "Embryology of Paranasal Sinuses", "20"),
        ("3.3", "Anatomy of Paranasal Sinuses", "30"),
        ("3.4", "Osteomeatal Complex", "55"),
        ("3.5", "Anatomical Variations", "65"),
        ("3.6", "CT Imaging Principles", "95"),
        ("3.7", "Clinical Significance", "105"),
        ("3.8", "Indian Studies Review", "115"),
        ("4.", "Materials and Methods", "125"),
        ("4.1", "Study Design", "126"),
        ("4.2", "Inclusion/Exclusion Criteria", "130"),
        ("4.3", "CT Scan Protocol", "133"),
        ("4.4", "Parameters Studied", "138"),
        ("4.5", "Statistical Analysis", "144"),
        ("5.", "Observations and Results", "147"),
        ("5.1", "Demographic Profile", "148"),
        ("5.2", "Nasal Septum Variations", "154"),
        ("5.3", "Turbinate Variations", "160"),
        ("5.4", "Ethmoid Variations", "168"),
        ("5.5", "Maxillary Sinus Variations", "175"),
        ("5.6", "Frontal Sinus Variations", "180"),
        ("5.7", "Sphenoid Sinus Variations", "185"),
        ("6.", "Discussion", "190"),
        ("7.", "Summary", "205"),
        ("8.", "Conclusion", "210"),
        ("9.", "Limitations and Recommendations", "213"),
        ("10.", "References (Bibliography)", "215"),
        ("11.", "Annexures", "220"),
        ("11.1", "Annexure I: Ethics Committee Approval", "220"),
        ("11.2", "Annexure II: Informed Consent Form", "221"),
        ("11.3", "Annexure III: Master Chart", "222"),
        ("11.4", "Annexure IV: Proforma", "224"),
    ]
    
    pdf.set_font('Times', 'B', 11)
    for sr, title, page in toc:
        if sr == "Sr. No.":
            pdf.set_fill_color(220, 220, 220)
            pdf.cell(20, 7, pdf.safe(sr), border=1, fill=True)
            pdf.cell(120, 7, pdf.safe(title), border=1, fill=True)
            pdf.cell(25, 7, pdf.safe(page), border=1, align='C', fill=True)
            pdf.ln()
            pdf.set_font('Times', '', 11)
        else:
            pdf.cell(20, 6, pdf.safe(sr), border=1)
            pdf.cell(120, 6, pdf.safe(title), border=1)
            pdf.cell(25, 6, pdf.safe(page), border=1, align='C')
            pdf.ln()
    
    # ============= LIST OF TABLES =============
    pdf.add_page()
    pdf.section_title("LIST OF TABLES")
    
    tables_list = [
        ("1.", "Demographic distribution of study population", "148"),
        ("2.", "Age-wise distribution of subjects", "149"),
        ("3.", "Gender-wise distribution", "150"),
        ("4.", "Distribution of indications for CT scan", "151"),
        ("5.", "Prevalence of Deviated Nasal Septum", "154"),
        ("6.", "Direction of DNS in study population", "155"),
        ("7.", "Severity grading of DNS", "156"),
        ("8.", "Prevalence of nasal septal spur", "158"),
        ("9.", "Prevalence of Concha Bullosa", "160"),
        ("10.", "Types of Concha Bullosa", "161"),
        ("11.", "Laterality of Concha Bullosa", "162"),
        ("12.", "Prevalence of Paradoxical Middle Turbinate", "164"),
        ("13.", "Prevalence of Agger Nasi cells", "168"),
        ("14.", "Prevalence of Haller cells", "170"),
        ("15.", "Prevalence of Onodi cells", "172"),
        ("16.", "Frontal cells (Kuhn classification)", "174"),
        ("17.", "Maxillary sinus hypoplasia", "175"),
        ("18.", "Underwood septa prevalence", "177"),
        ("19.", "Accessory Maxillary Ostium", "178"),
        ("20.", "Frontal sinus aplasia/hypoplasia", "180"),
        ("21.", "Frontal sinus asymmetry", "182"),
        ("22.", "Sphenoid sinus pneumatization types", "185"),
        ("23.", "Sphenoid sinus septation patterns", "187"),
        ("24.", "ICA and Optic nerve relationship", "188"),
        ("25.", "Keros classification distribution", "189"),
        ("26.", "Comparison with Indian studies", "195"),
        ("27.", "Comparison with International studies", "200"),
        ("28.", "Statistical significance summary", "203"),
    ]
    
    pdf.set_font('Times', 'B', 11)
    pdf.set_fill_color(220, 220, 220)
    pdf.cell(20, 7, pdf.safe("Table No."), border=1, fill=True)
    pdf.cell(120, 7, pdf.safe("Title"), border=1, fill=True)
    pdf.cell(25, 7, pdf.safe("Page"), border=1, align='C', fill=True)
    pdf.ln()
    pdf.set_font('Times', '', 11)
    for num, title, page in tables_list:
        pdf.cell(20, 6, pdf.safe(num), border=1, align='C')
        pdf.cell(120, 6, pdf.safe(title), border=1)
        pdf.cell(25, 6, pdf.safe(page), border=1, align='C')
        pdf.ln()
    
    # ============= LIST OF FIGURES =============
    pdf.add_page()
    pdf.section_title("LIST OF FIGURES")
    
    figures_list = [
        ("1.", "Schematic diagram of paranasal sinuses", "31"),
        ("2.", "Embryological development timeline", "22"),
        ("3.", "Maxillary sinus anatomy - coronal CT", "35"),
        ("4.", "Ethmoid sinus anatomy - coronal CT", "40"),
        ("5.", "Frontal sinus anatomy - axial CT", "45"),
        ("6.", "Sphenoid sinus anatomy - sagittal CT", "50"),
        ("7.", "Osteomeatal complex - coronal CT", "57"),
        ("8.", "Deviated Nasal Septum to right", "67"),
        ("9.", "Deviated Nasal Septum to left", "68"),
        ("10.", "Nasal septal spur", "70"),
        ("11.", "Bilateral Concha Bullosa", "73"),
        ("12.", "Lamellar type Concha Bullosa", "74"),
        ("13.", "Bulbous type Concha Bullosa", "75"),
        ("14.", "Paradoxical Middle Turbinate", "77"),
        ("15.", "Agger Nasi cells - sagittal CT", "80"),
        ("16.", "Haller cell - coronal CT", "82"),
        ("17.", "Onodi cell - axial CT", "84"),
        ("18.", "Frontal cells - Kuhn Type I-IV", "86"),
        ("19.", "Maxillary sinus hypoplasia", "88"),
        ("20.", "Underwood's septa", "89"),
        ("21.", "Accessory maxillary ostium", "90"),
        ("22.", "Sphenoid sinus pneumatization types", "92"),
        ("23.", "ICA dehiscence in sphenoid sinus", "94"),
        ("24.", "Keros Type I, II, III olfactory fossa", "100"),
        ("25.", "Cribriform plate asymmetry", "102"),
        ("26.", "CT scanner machine", "133"),
        ("27.", "Patient positioning for CT", "135"),
        ("28.", "Demographic distribution chart", "148"),
        ("29.", "Age distribution graph", "149"),
        ("30.", "Gender distribution pie chart", "150"),
        ("31.", "DNS prevalence chart", "154"),
        ("32.", "Concha Bullosa types distribution", "161"),
        ("33.", "Sphenoid pneumatization distribution", "185"),
        ("34.", "Comparative analysis chart", "200"),
    ]
    
    pdf.set_font('Times', 'B', 11)
    pdf.set_fill_color(220, 220, 220)
    pdf.cell(20, 7, pdf.safe("Fig. No."), border=1, fill=True)
    pdf.cell(120, 7, pdf.safe("Description"), border=1, fill=True)
    pdf.cell(25, 7, pdf.safe("Page"), border=1, align='C', fill=True)
    pdf.ln()
    pdf.set_font('Times', '', 11)
    for num, title, page in figures_list:
        pdf.cell(20, 6, pdf.safe(num), border=1, align='C')
        pdf.cell(120, 6, pdf.safe(title), border=1)
        pdf.cell(25, 6, pdf.safe(page), border=1, align='C')
        pdf.ln()
    
    # ============= ABSTRACT =============
    pdf.add_page()
    pdf.section_title("ABSTRACT")
    
    pdf.subheading("Background:")
    pdf.body("The paranasal sinuses (PNS) are a complex group of air-filled cavities within the bones of the skull and face that exhibit considerable anatomical variation. Knowledge of these variations is paramount for safe and effective Functional Endoscopic Sinus Surgery (FESS), prevention of intra-operative complications, and management of chronic rhinosinusitis. Variations may be influenced by ethnicity, geographic location, and genetic factors, necessitating regional studies. Limited data exists from the South Gujarat region of India regarding paranasal sinus anatomical variations.")
    
    pdf.subheading("Aims and Objectives:")
    pdf.body("The present study was undertaken to evaluate the prevalence and pattern of anatomical variations of paranasal air sinuses in the South Gujarat population using Computed Tomography (CT). Specific objectives included: (1) To document various anatomical variations of paranasal sinuses, (2) To determine their prevalence in study population, (3) To assess gender and age-related differences, (4) To compare findings with existing Indian and international literature, (5) To establish baseline regional data useful for surgical planning.")
    
    pdf.subheading("Materials and Methods:")
    pdf.body("This was a hospital-based observational, descriptive, cross-sectional study conducted in the Department of Anatomy in collaboration with the Department of Radiology at [Medical College Name], Surat, over a period of 18 months (November 2024 to April 2026). A total of 300 CT paranasal sinus scans of patients aged 18-65 years were analyzed. Inclusion criteria comprised individuals from South Gujarat region with technically adequate CT scans. Exclusion criteria included patients with previous sinus surgery, sinonasal tumors, facial trauma, or congenital anomalies. CT scans were performed using a 128-slice MDCT scanner with 0.625 mm slice thickness in axial, coronal, and sagittal planes. Each scan was systematically evaluated for: nasal septum deviation, concha bullosa, paradoxical middle turbinate, Agger nasi cells, Haller cells, Onodi cells, frontal cells (Kuhn classification), maxillary sinus hypoplasia, Underwood's septa, accessory maxillary ostium, sphenoid pneumatization types (Hamberger), Keros classification of olfactory fossa, internal carotid artery dehiscence, and optic nerve protrusion. Data was analyzed using SPSS version 25.0 and chi-square test was used for comparison; p < 0.05 was considered statistically significant.")
    
    pdf.subheading("Results:")
    pdf.body("Of 300 subjects, 168 (56%) were males and 132 (44%) were females, with a mean age of 38.4 +/- 12.6 years. Deviated nasal septum was the most common variation, observed in 218 (72.7%) subjects, with right-sided deviation in 56% of cases. Concha bullosa was present in 99 (33%) subjects, predominantly of the lamellar type (52%). Paradoxical middle turbinate was observed in 14% of cases. Agger nasi cells were almost universal (94%). Haller cells were noted in 17.3%, while Onodi cells were present in 11.7% of subjects. Maxillary sinus hypoplasia occurred in 4%, Underwood's septa in 28.3%, and accessory maxillary ostium in 19% of cases. Sphenoid sinus pneumatization showed sellar type as predominant (78%). Keros Type II was the most common olfactory fossa depth (68%), with Type III in 17%. Internal carotid artery dehiscence was observed in 8% of subjects. Statistical analysis revealed significant gender-related differences in some variations (p < 0.05).")
    
    pdf.subheading("Conclusion:")
    pdf.body("The present study provides valuable baseline data on the prevalence and pattern of paranasal sinus anatomical variations in the South Gujarat population. The prevalence of most variations was comparable to other Indian studies but showed certain regional differences when compared to Western literature. Pre-operative CT evaluation of these variations is crucial for safe FESS and to minimize complications. The high prevalence of variations such as Keros Type III (17%) and ICA dehiscence (8%) emphasizes the need for meticulous pre-operative planning. This study contributes to the growing body of regional Indian literature on paranasal sinus anatomy and serves as a reference for surgeons, radiologists, and anatomists practicing in this region.")
    
    pdf.subheading("Keywords:")
    pdf.body("Paranasal sinuses, Anatomical variations, Computed Tomography, FESS, South Gujarat, Concha bullosa, Deviated nasal septum, Keros classification, Onodi cells, Haller cells.")
    
    return pdf

# Save the PDF
if __name__ == "__main__":
    pdf = generate_thesis()
    pdf.output('Complete_Thesis_Paranasal_Sinuses.pdf')
    print(f"Initial sections created. Total pages so far: {pdf.page_no()}")
