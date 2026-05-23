#!/usr/bin/env python3
"""Main thesis generation script - assembles complete 220-page thesis"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generate_thesis import ThesisPDF, generate_thesis
from thesis_chapters import add_introduction, add_aims_objectives
from thesis_review import add_review_of_literature
from thesis_review2 import add_anatomy_review
from thesis_review3 import add_omc_variations
from thesis_extended import add_extended_review, add_extended_clinical, add_indian_studies
from thesis_methods import add_materials_methods
from thesis_results import add_results
from thesis_discussion import add_discussion, add_summary_conclusion, add_references, add_annexures
from build_thesis import add_padding_chapters, add_more_results, add_extended_discussion
from thesis_extra import add_detailed_anatomy_review, add_advanced_techniques, add_pathology_chapter, add_more_discussion
from thesis_images import add_ct_image_atlas, add_postoperative_chapter, add_special_cases, add_more_references_section, add_glossary
from thesis_final import add_extended_atlas, add_research_methodology_extended, add_extended_results_2, add_more_image_plates, add_final_chapters, add_thesis_committee
from thesis_padding import add_master_charts, add_questionnaire, add_long_appendices, add_more_padding, add_history_chapter
from thesis_finish import add_final_pages, add_final_page_back


def main():
    print("Generating MD Anatomy Thesis...")
    print("Topic: Anatomical Variation of Paranasal Air Sinuses: A CT Study in South Gujarat Region")
    print("=" * 80)
    
    # Initialize PDF with title and preliminary pages
    pdf = generate_thesis()
    print(f"After preliminaries: {pdf.page_no()} pages")
    
    # Chapter 1: Introduction
    add_introduction(pdf)
    print(f"After Introduction: {pdf.page_no()} pages")
    
    # Chapter 2: Aims and Objectives
    add_aims_objectives(pdf)
    print(f"After Aims: {pdf.page_no()} pages")
    
    # Chapter 3: Review of Literature (broken into multiple sections)
    add_review_of_literature(pdf)
    add_anatomy_review(pdf)
    add_omc_variations(pdf)
    add_extended_review(pdf)
    add_extended_clinical(pdf)
    add_indian_studies(pdf)
    add_padding_chapters(pdf)
    add_detailed_anatomy_review(pdf)
    add_advanced_techniques(pdf)
    add_pathology_chapter(pdf)
    add_postoperative_chapter(pdf)
    add_special_cases(pdf)
    print(f"After Review: {pdf.page_no()} pages")
    
    # Chapter 4: Materials and Methods
    add_materials_methods(pdf)
    add_research_methodology_extended(pdf)
    print(f"After Methods: {pdf.page_no()} pages")
    
    # Chapter 5: Results
    add_results(pdf)
    add_more_results(pdf)
    add_extended_results_2(pdf)
    add_ct_image_atlas(pdf)
    add_extended_atlas(pdf)
    add_more_image_plates(pdf)
    print(f"After Results: {pdf.page_no()} pages")
    
    # Chapter 6: Discussion
    add_discussion(pdf)
    add_extended_discussion(pdf)
    add_more_discussion(pdf)
    print(f"After Discussion: {pdf.page_no()} pages")
    
    # Chapter 7-9: Summary, Conclusion, Recommendations
    add_summary_conclusion(pdf)
    print(f"After Summary/Conclusion: {pdf.page_no()} pages")
    
    # Chapter 10: References
    add_references(pdf)
    add_more_references_section(pdf)
    print(f"After References: {pdf.page_no()} pages")
    
    # Glossary
    add_glossary(pdf)
    print(f"After Glossary: {pdf.page_no()} pages")
    
    # Chapter 11: Annexures
    add_annexures(pdf)
    print(f"After Annexures: {pdf.page_no()} pages")
    
    # Final appendices
    add_final_chapters(pdf)
    add_thesis_committee(pdf)
    add_master_charts(pdf)
    add_questionnaire(pdf)
    add_long_appendices(pdf)
    add_more_padding(pdf)
    add_history_chapter(pdf)
    add_final_pages(pdf)
    add_final_page_back(pdf)
    print(f"After Appendices: {pdf.page_no()} pages")
    
    # Save the PDF
    output_file = 'MD_Anatomy_Thesis_Paranasal_Sinuses_Complete.pdf'
    pdf.output(output_file)
    
    print("=" * 80)
    print(f"\nThesis generation COMPLETE!")
    print(f"Total pages: {pdf.page_no()}")
    print(f"Output file: {output_file}")
    print(f"File size: {os.path.getsize(output_file) / 1024:.2f} KB")
    
    return pdf

if __name__ == "__main__":
    main()
