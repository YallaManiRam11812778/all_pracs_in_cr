import xml.etree.ElementTree as ET

# Define namespaces
namespaces = {
    "": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
    "sig": "urn:oasis:names:specification:ubl:schema:xsd:CommonSignatureComponents-2",
    "sac": "urn:oasis:names:specification:ubl:schema:xsd:SignatureAggregateComponents-2",
    "sbc": "urn:oasis:names:specification:ubl:schema:xsd:SignatureBasicComponents-2",
    "cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
    "ds": "http://www.w3.org/2000/09/xmldsig#",
    "xades": "http://uri.etsi.org/01903/v1.3.2#"
}

for prefix, uri in namespaces.items():
    ET.register_namespace(prefix, uri)

# Create the root element
UBLExtensions = ET.Element("{urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}UBLExtensions")

# Create UBLExtension
UBLExtension = ET.SubElement(UBLExtensions, "UBLExtension")

# Add ExtensionURI
ExtensionURI = ET.SubElement(UBLExtension, "ExtensionURI")
ExtensionURI.text = "urn:oasis:names:specification:ubl:dsig:enveloped:xades"

# Add ExtensionContent
ExtensionContent = ET.SubElement(UBLExtension, "ExtensionContent")
UBLDocumentSignatures = ET.SubElement(
    ExtensionContent,
    "{urn:oasis:names:specification:ubl:schema:xsd:CommonSignatureComponents-2}UBLDocumentSignatures"
)

# Add SignatureInformation
SignatureInformation = ET.SubElement(
    UBLDocumentSignatures,
    "{urn:oasis:names:specification:ubl:schema:xsd:SignatureAggregateComponents-2}SignatureInformation"
)

cbc_ID = ET.SubElement(SignatureInformation, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID")
cbc_ID.text = "urn:oasis:names:specification:ubl:signature:1"

sbc_ReferencedSignatureID = ET.SubElement(
    SignatureInformation,
    "{urn:oasis:names:specification:ubl:schema:xsd:SignatureBasicComponents-2}ReferencedSignatureID"
)
sbc_ReferencedSignatureID.text = "urn:oasis:names:specification:ubl:signature:Invoice"

# Add Signature
Signature = ET.SubElement(
    SignatureInformation,
    "{http://www.w3.org/2000/09/xmldsig#}Signature",
    Id="signature"
)

SignedInfo = ET.SubElement(Signature, "{http://www.w3.org/2000/09/xmldsig#}SignedInfo")
CanonicalizationMethod = ET.SubElement(
    SignedInfo,
    "{http://www.w3.org/2000/09/xmldsig#}CanonicalizationMethod",
    Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"
)
SignatureMethod = ET.SubElement(
    SignedInfo,
    "{http://www.w3.org/2000/09/xmldsig#}SignatureMethod",
    Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"
)

# Add References
Reference1 = ET.SubElement(SignedInfo, "{http://www.w3.org/2000/09/xmldsig#}Reference", Id="id-doc-signed-data", URI="")
Transforms = ET.SubElement(Reference1, "{http://www.w3.org/2000/09/xmldsig#}Transforms")

Transform1 = ET.SubElement(
    Transforms,
    "{http://www.w3.org/2000/09/xmldsig#}Transform",
    Algorithm="http://www.w3.org/TR/1999/REC-xpath-19991116"
)
XPath1 = ET.SubElement(Transform1, "{http://www.w3.org/2000/09/xmldsig#}XPath")
XPath1.text = "not(//ancestor-or-self::ext:UBLExtensions)"

Transform2 = ET.SubElement(
    Transforms,
    "{http://www.w3.org/2000/09/xmldsig#}Transform",
    Algorithm="http://www.w3.org/TR/1999/REC-xpath-19991116"
)
XPath2 = ET.SubElement(Transform2, "{http://www.w3.org/2000/09/xmldsig#}XPath")
XPath2.text = "not(//ancestor-or-self::cac:Signature)"

Transform3 = ET.SubElement(
    Transforms,
    "{http://www.w3.org/2000/09/xmldsig#}Transform",
    Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"
)

DigestMethod1 = ET.SubElement(
    Reference1,
    "{http://www.w3.org/2000/09/xmldsig#}DigestMethod",
    Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"
)
DigestValue1 = ET.SubElement(Reference1, "{http://www.w3.org/2000/09/xmldsig#}DigestValue")
DigestValue1.text = "fRaWJINS9sB9aSl/MhCjMsdVMFpLwnxstpPhJkJwkU4="

# Add additional elements as needed...

# Write the tree to a file
a = ET.ElementTree(UBLExtensions)

# Convert ElementTree to string and print it
print(ET.tostring(a.getroot(), encoding='unicode'))