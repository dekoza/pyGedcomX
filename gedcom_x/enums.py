from enum import Enum

from .basetypes import GedcomXIdentifier


class Confidence(GedcomXIdentifier, Enum):
    high = "http://gedcomx.org/High"
    medium = "http://gedcomx.org/Medium"
    low = "http://gedcomx.org/Low"


class IdentifierType(GedcomXIdentifier, Enum):
    primary = "http://gedcomx.org/Primary"
    authority = "http://gedcomx.org/Authority"
    deprecated = "http://gedcomx.org/Deprecated"


class RelationshipType(GedcomXIdentifier, Enum):
    couple = "http://gedcomx.org/Couple"
    parent_child = "http://gedcomx.org/ParentChild"


class GenderType(GedcomXIdentifier, Enum):
    male = "http://gedcomx.org/Male"
    female = "http://gedcomx.org/Female"
    unknown = "http://gedcomx.org/Unknown"
    intersex = "http://gedcomx.org/Intersex"


class NameType(GedcomXIdentifier, Enum):
    birth_name = "http://gedcomx.org/BirthName"
    married_name = "http://gedcomx.org/MarriedName"
    also_known_as = "http://gedcomx.org/AlsoKnownAs"
    nickname = "http://gedcomx.org/Nickname"
    adoptive_name = "http://gedcomx.org/AdoptiveName"
    formal_name = "http://gedcomx.org/FormalName"
    religious_name = "http://gedcomx.org/ReligiousName"


class BaseFactType(GedcomXIdentifier, Enum):
    pass


class PersonalFactMixin:
    adoption = "http://gedcomx.org/Adoption"
    adult_christening = "http://gedcomx.org/AdultChristening"
    amnesty = "http://gedcomx.org/Amnesty"
    ancestral_hall = "http://gedcomx.org/AncestralHall"
    ancestral_poem = "http://gedcomx.org/AncestralPoem"
    apprenticeship = "http://gedcomx.org/Apprenticeship"
    arrest = "http://gedcomx.org/Arrest"
    award = "http://gedcomx.org/Award"
    baptism = "http://gedcomx.org/Baptism"
    bar_mitzvah = "http://gedcomx.org/BarMitzvah"
    bat_mitzvah = "http://gedcomx.org/BatMitzvah"
    birth = "http://gedcomx.org/Birth"
    birth_notice = "http://gedcomx.org/BirthNotice"
    blessing = "http://gedcomx.org/Blessing"
    branch = "http://gedcomx.org/Branch"
    burial = "http://gedcomx.org/Burial"
    caste = "http://gedcomx.org/Caste"
    census = "http://gedcomx.org/Census"
    christening = "http://gedcomx.org/Christening"
    circumcision = "http://gedcomx.org/Circumcision"
    clan = "http://gedcomx.org/Clan"
    confirmation = "http://gedcomx.org/Confirmation"
    court = "http://gedcomx.org/Court"
    cremation = "http://gedcomx.org/Cremation"
    death = "http://gedcomx.org/Death"
    education = "http://gedcomx.org/Education"
    education_enrollment = "http://gedcomx.org/EducationEnrollment"
    emigration = "http://gedcomx.org/Emigration"
    enslavement = "http://gedcomx.org/Enslavement"
    ethnicity = "http://gedcomx.org/Ethnicity"
    excommunication = "http://gedcomx.org/Excommunication"
    first_communion = "http://gedcomx.org/FirstCommunion"
    funeral = "http://gedcomx.org/Funeral"
    gender_change = "http://gedcomx.org/GenderChange"
    generation_number = "http://gedcomx.org/GenerationNumber"
    graduation = "http://gedcomx.org/Graduation"
    heimat = "http://gedcomx.org/Heimat"
    immigration = "http://gedcomx.org/Immigration"
    imprisonment = "http://gedcomx.org/Imprisonment"
    inquest = "http://gedcomx.org/Inquest"
    land_transaction = "http://gedcomx.org/LandTransaction"
    language = "http://gedcomx.org/Language"
    living = "http://gedcomx.org/Living"
    marital_status = "http://gedcomx.org/MaritalStatus"
    medical = "http://gedcomx.org/Medical"
    military_award = "http://gedcomx.org/MilitaryAward"
    military_discharge = "http://gedcomx.org/MilitaryDischarge"
    military_draft_registration = "http://gedcomx.org/MilitaryDraftRegistration"
    military_induction = "http://gedcomx.org/MilitaryInduction"
    military_service = "http://gedcomx.org/MilitaryService"
    mission = "http://gedcomx.org/Mission"
    move_from = "http://gedcomx.org/MoveFrom"
    move_to = "http://gedcomx.org/MoveTo"
    multiple_birth = "http://gedcomx.org/MultipleBirth"
    national_id = "http://gedcomx.org/NationalId"
    nationality = "http://gedcomx.org/Nationality"
    naturalization = "http://gedcomx.org/Naturalization"
    number_of_children = "http://gedcomx.org/NumberOfChildren"
    number_of_marriages = "http://gedcomx.org/NumberOfMarriages"
    obituary = "http://gedcomx.org/Obituary"
    official_position = "http://gedcomx.org/OfficialPosition"
    occupation = "http://gedcomx.org/Occupation"
    ordination = "http://gedcomx.org/Ordination"
    pardon = "http://gedcomx.org/Pardon"
    physicalDescription = "http://gedcomx.org/PhysicalDescription"
    probate = "http://gedcomx.org/Probate"
    property = "http://gedcomx.org/Property"
    race = "http://gedcomx.org/Race"
    religion = "http://gedcomx.org/Religion"
    residence = "http://gedcomx.org/Residence"
    retirement = "http://gedcomx.org/Retirement"
    stillbirth = "http://gedcomx.org/Stillbirth"
    tax_assessment = "http://gedcomx.org/TaxAssessment"
    tribe = "http://gedcomx.org/Tribe"
    will = "http://gedcomx.org/Will"
    visit = "http://gedcomx.org/Visit"
    yahrzeit = "http://gedcomx.org/Yahrzeit"


class CoupleRelationshipFactMixin:
    annulment = "http://gedcomx.org/Annulment"
    common_law_marriage = "http://gedcomx.org/CommonLawMarriage"
    civil_union = "http://gedcomx.org/CivilUnion"
    divorce = "http://gedcomx.org/Divorce"
    divorce_filing = "http://gedcomx.org/DivorceFiling"
    domestic_partnership = "http://gedcomx.org/DomesticPartnership"
    engagement = "http://gedcomx.org/Engagement"
    marriage = "http://gedcomx.org/Marriage"
    marriage_banns = "http://gedcomx.org/MarriageBanns"
    marriage_contract = "http://gedcomx.org/MarriageContract"
    marriage_license = "http://gedcomx.org/MarriageLicense"
    marriage_notice = "http://gedcomx.org/MarriageNotice"
    number_of_children = "http://gedcomx.org/NumberOfChildren"
    separation = "http://gedcomx.org/Separation"


class ParentChildRelationshipFactMixin:
    adoptive_parent = "http://gedcomx.org/AdoptiveParent"
    biological_parent = "http://gedcomx.org/BiologicalParent"
    child_order = "http://gedcomx.org/ChildOrder"
    entering_heir = "http://gedcomx.org/EnteringHeir"
    exiting_heir = "http://gedcomx.org/ExitingHeir"
    foster_parent = "http://gedcomx.org/FosterParent"
    guardian_parent = "http://gedcomx.org/GuardianParent"
    step_parent = "http://gedcomx.org/StepParent"
    sociological_parent = "http://gedcomx.org/SociologicalParent"
    surrogate_parent = "http://gedcomx.org/SurrogateParent"


class PersonalFactType(BaseFactType, PersonalFactMixin):
    pass


class CoupleRelationshipFactType(BaseFactType, CoupleRelationshipFactMixin):
    pass


class ParentChildRelationshipFactType(BaseFactType, ParentChildRelationshipFactMixin):
    pass


class FactType(
    BaseFactType,
    PersonalFactMixin,
    CoupleRelationshipFactMixin,
    ParentChildRelationshipFactMixin,
):
    """
    For descriptions please refer to:
    https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md
    """


class NamePartType(GedcomXIdentifier, Enum):
    prefix = "http://gedcomx.org/Prefix"
    suffix = "http://gedcomx.org/Suffix"
    given = "http://gedcomx.org/Given"
    surname = "http://gedcomx.org/Surname"


class ResourceType(GedcomXIdentifier, Enum):
    collection = "http://gedcomx.org/Collection"
    physical_artifact = "http://gedcomx.org/PhysicalArtifact"
    digital_artifact = "http://gedcomx.org/DigitalArtifact"
    record = "http://gedcomx.org/Record"


class BaseEventType(GedcomXIdentifier, Enum):
    """
    https://github.com/FamilySearch/gedcomx/blob/master/specifications/event-types-specification.md
    """


class EventType(BaseEventType):
    adoption = "http://gedcomx.org/Adoption"
    adult_christening = "http://gedcomx.org/AdultChristening"
    annulment = "http://gedcomx.org/Annulment"
    baptism = "http://gedcomx.org/Baptism"
    bar_mitzvah = "http://gedcomx.org/BarMitzvah"
    bat_mitzvah = "http://gedcomx.org/BatMitzvah"
    birth = "http://gedcomx.org/Birth"
    blessing = "http://gedcomx.org/Blessing"
    burial = "http://gedcomx.org/Burial"
    census = "http://gedcomx.org/Census"
    christening = "http://gedcomx.org/Christening"
    circumcision = "http://gedcomx.org/Circumcision"
    confirmation = "http://gedcomx.org/Confirmation"
    cremation = "http://gedcomx.org/Cremation"
    death = "http://gedcomx.org/Death"
    divorce = "http://gedcomx.org/Divorce"
    divorce_filing = "http://gedcomx.org/DivorceFiling"
    education = "http://gedcomx.org/Education"
    engagement = "http://gedcomx.org/Engagement"
    emigration = "http://gedcomx.org/Emigration"
    excommunication = "http://gedcomx.org/Excommunication"
    first_communion = "http://gedcomx.org/FirstCommunion"
    funeral = "http://gedcomx.org/Funeral"
    immigration = "http://gedcomx.org/Immigration"
    land_transaction = "http://gedcomx.org/LandTransaction"
    marriage = "http://gedcomx.org/Marriage"
    military_award = "http://gedcomx.org/MilitaryAward"
    military_discharge = "http://gedcomx.org/MilitaryDischarge"
    mission = "http://gedcomx.org/Mission"
    move_from = "http://gedcomx.org/MoveFrom"
    move_to = "http://gedcomx.org/MoveTo"
    naturalization = "http://gedcomx.org/Naturalization"
    ordination = "http://gedcomx.org/Ordination"
    retirement = "http://gedcomx.org/Retirement"


class RoleType(GedcomXIdentifier):
    principal = "http://gedcomx.org/Principal"
    participant = "http://gedcomx.org/Participant"
    official = "http://gedcomx.org/Official"
    witness = "http://gedcomx.org/Witness"


class DocumentType(GedcomXIdentifier):
    abstract = "http://gedcomx.org/Abstract"
    transcription = "http://gedcomx.org/Transcription"
    translation = "http://gedcomx.org/Translation"
    analysis = "http://gedcomx.org/Analysis"
