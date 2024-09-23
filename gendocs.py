import docx

# Function to create a Word document with given paragraphs
def create_sample_doc(filename, paragraphs):
    doc = docx.Document()
    for paragraph in paragraphs:
        doc.add_paragraph(paragraph)
    doc.save(filename)

# Function to generate the source and target documents
def main():
    # Source legal text paragraphs on parking violations
    source_paragraphs = [
        "Parking in a designated no-parking zone shall result in a fine not exceeding $200.00. The vehicle may be towed at the owner's expense if parked for more than 2 hours in such zones.",
        "Vehicles that obstruct pedestrian pathways or cause significant disruption to traffic flow may be subject to immediate towing. Fines for such violations range from $100.00 to $500.00, depending on the severity of the obstruction.",
        "It is prohibited to park any vehicle within 10 feet of a fire hydrant or designated emergency zone. Violation of this rule will incur penalties, including a fine of up to $300.00 and potential towing.",
        "Failure to pay parking fines within 30 days of issuance will result in an additional penalty of $50.00, with the possibility of further legal action if left unresolved beyond 90 days.",
        "The use of residential parking permits is restricted to vehicles registered to residents of the designated area. Unauthorized use of such permits will lead to a fine of $150.00 and revocation of the permit."
    ]

    # Target legal text paragraphs with slight differences
    target_paragraphs = [
        "Parking in a no-parking zone will incur a fine of up to $200.00. The vehicle may be towed at the owner's cost if parked for more than 3 hours in these zones.",
        "Vehicles obstructing pedestrian pathways or causing traffic disruptions may be towed immediately. Fines for such violations range from $120.00 to $450.00 based on the severity of the case.",
        "Parking any vehicle within 12 feet of a fire hydrant or emergency zone is strictly prohibited. Violators will face fines up to $350.00 and possible towing.",
        "Failure to pay fines within 30 days will result in a penalty of $50.00, and legal action may be pursued after 60 days of non-payment.",
        "Residential parking permits are limited to vehicles registered to area residents. Unauthorized permit use will result in a $100.00 fine and permit cancellation."
    ]

    # Generate the sample documents
    create_sample_doc("source.docx", source_paragraphs)
    create_sample_doc("target.docx", target_paragraphs)

# Run the main function to create the documents
if __name__ == "__main__":
    main()
