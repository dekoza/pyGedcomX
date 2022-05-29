import re
from enum import Enum


class GedcomXIdentifier(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not isinstance(value, str):
            raise TypeError("string required")
        pattern = r"^https?://(www\.)?gedcomx.org/"
        if not re.match(pattern, value):
            raise ValueError("invalid GEDCOM X identifier")
        return value


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
    parentChild = "http://gedcomx.org/ParentChild"


class GenderType(GedcomXIdentifier, Enum):
    male = "http://gedcomx.org/Male"
    female = "http://gedcomx.org/Female"
    unknown = "http://gedcomx.org/Unknown"
    intersex = "http://gedcomx.org/Intersex"


class NameType(GedcomXIdentifier, Enum):
    birthName = "http://gedcomx.org/BirthName"
    marriedName = "http://gedcomx.org/MarriedName"
    alsoKnownAs = "http://gedcomx.org/AlsoKnownAs"
    nickname = "http://gedcomx.org/Nickname"
    adoptiveName = "http://gedcomx.org/AdoptiveName"
    formalName = "http://gedcomx.org/FormalName"
    religiousName = "http://gedcomx.org/ReligiousName"


class BaseFactType(GedcomXIdentifier, Enum):
    pass


class PersonalFactMixin:
    adoption = "http://gedcomx.org/Adoption"
    adultChristening = "http://gedcomx.org/AdultChristening"
    amnesty = "http://gedcomx.org/Amnesty"
    ancestralHall = "http://gedcomx.org/AncestralHall"
    ancestralPoem = "http://gedcomx.org/AncestralPoem"
    apprenticeship = "http://gedcomx.org/Apprenticeship"
    arrest = "http://gedcomx.org/Arrest"
    award = "http://gedcomx.org/Award"
    baptism = "http://gedcomx.org/Baptism"
    barMitzvah = "http://gedcomx.org/BarMitzvah"
    batMitzvah = "http://gedcomx.org/BatMitzvah"
    birth = "http://gedcomx.org/Birth"
    birthNotice = "http://gedcomx.org/BirthNotice"
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
    educationEnrollment = "http://gedcomx.org/EducationEnrollment"
    emigration = "http://gedcomx.org/Emigration"
    enslavement = "http://gedcomx.org/Enslavement"
    ethnicity = "http://gedcomx.org/Ethnicity"
    excommunication = "http://gedcomx.org/Excommunication"
    firstCommunion = "http://gedcomx.org/FirstCommunion"
    funeral = "http://gedcomx.org/Funeral"
    genderChange = "http://gedcomx.org/GenderChange"
    generationNumber = "http://gedcomx.org/GenerationNumber"
    graduation = "http://gedcomx.org/Graduation"
    heimat = "http://gedcomx.org/Heimat"
    immigration = "http://gedcomx.org/Immigration"
    imprisonment = "http://gedcomx.org/Imprisonment"
    inquest = "http://gedcomx.org/Inquest"
    landTransaction = "http://gedcomx.org/LandTransaction"
    language = "http://gedcomx.org/Language"
    living = "http://gedcomx.org/Living"
    maritalStatus = "http://gedcomx.org/MaritalStatus"
    medical = "http://gedcomx.org/Medical"
    militaryAward = "http://gedcomx.org/MilitaryAward"
    militaryDischarge = "http://gedcomx.org/MilitaryDischarge"
    militaryDraftRegistration = "http://gedcomx.org/MilitaryDraftRegistration"
    militaryInduction = "http://gedcomx.org/MilitaryInduction"
    militaryService = "http://gedcomx.org/MilitaryService"
    mission = "http://gedcomx.org/Mission"
    moveFrom = "http://gedcomx.org/MoveFrom"
    moveTo = "http://gedcomx.org/MoveTo"
    multipleBirth = "http://gedcomx.org/MultipleBirth"
    nationalId = "http://gedcomx.org/NationalId"
    nationality = "http://gedcomx.org/Nationality"
    naturalization = "http://gedcomx.org/Naturalization"
    numberOfChildren = "http://gedcomx.org/NumberOfChildren"
    numberOfMarriages = "http://gedcomx.org/NumberOfMarriages"
    obituary = "http://gedcomx.org/Obituary"
    officialPosition = "http://gedcomx.org/OfficialPosition"
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
    taxAssessment = "http://gedcomx.org/TaxAssessment"
    tribe = "http://gedcomx.org/Tribe"
    will = "http://gedcomx.org/Will"
    visit = "http://gedcomx.org/Visit"
    yahrzeit = "http://gedcomx.org/Yahrzeit"


class CoupleRelationshipFactMixin:
    annulment = "http://gedcomx.org/Annulment"
    commonLawMarriage = "http://gedcomx.org/CommonLawMarriage"
    civilUnion = "http://gedcomx.org/CivilUnion"
    divorce = "http://gedcomx.org/Divorce"
    divorceFiling = "http://gedcomx.org/DivorceFiling"
    domesticPartnership = "http://gedcomx.org/DomesticPartnership"
    engagement = "http://gedcomx.org/Engagement"
    marriage = "http://gedcomx.org/Marriage"
    marriageBanns = "http://gedcomx.org/MarriageBanns"
    marriageContract = "http://gedcomx.org/MarriageContract"
    marriageLicense = "http://gedcomx.org/MarriageLicense"
    marriageNotice = "http://gedcomx.org/MarriageNotice"
    numberOfChildren = "http://gedcomx.org/NumberOfChildren"
    separation = "http://gedcomx.org/Separation"


class ParentChildRelationshipFactMixin:
    adoptiveParent = "http://gedcomx.org/AdoptiveParent"
    biologicalParent = "http://gedcomx.org/BiologicalParent"
    childOrder = "http://gedcomx.org/ChildOrder"
    enteringHeir = "http://gedcomx.org/EnteringHeir"
    exitingHeir = "http://gedcomx.org/ExitingHeir"
    fosterParent = "http://gedcomx.org/FosterParent"
    guardianParent = "http://gedcomx.org/GuardianParent"
    stepParent = "http://gedcomx.org/StepParent"
    sociologicalParent = "http://gedcomx.org/SociologicalParent"
    surrogateParent = "http://gedcomx.org/SurrogateParent"


class PersonalFactType(PersonalFactMixin, BaseFactType):
    pass


class CoupleRelationshipFactType(CoupleRelationshipFactMixin, BaseFactType):
    pass


class ParentChildRelationshipFactType(ParentChildRelationshipFactMixin, BaseFactType):
    pass


class FactType(
    PersonalFactMixin,
    CoupleRelationshipFactMixin,
    ParentChildRelationshipFactMixin,
    BaseFactType,
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
    physicalArtifact = "http://gedcomx.org/PhysicalArtifact"
    digitalArtifact = "http://gedcomx.org/DigitalArtifact"
    record = "http://gedcomx.org/Record"


class BaseEventType(GedcomXIdentifier, Enum):
    """
    https://github.com/FamilySearch/gedcomx/blob/master/specifications/event-types-specification.md
    """


class EventType(BaseEventType):
    adoption = "http://gedcomx.org/Adoption"
    adultChristening = "http://gedcomx.org/AdultChristening"
    annulment = "http://gedcomx.org/Annulment"
    baptism = "http://gedcomx.org/Baptism"
    barMitzvah = "http://gedcomx.org/BarMitzvah"
    batMitzvah = "http://gedcomx.org/BatMitzvah"
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
    divorceFiling = "http://gedcomx.org/DivorceFiling"
    education = "http://gedcomx.org/Education"
    engagement = "http://gedcomx.org/Engagement"
    emigration = "http://gedcomx.org/Emigration"
    excommunication = "http://gedcomx.org/Excommunication"
    firstCommunion = "http://gedcomx.org/FirstCommunion"
    funeral = "http://gedcomx.org/Funeral"
    immigration = "http://gedcomx.org/Immigration"
    landTransaction = "http://gedcomx.org/LandTransaction"
    marriage = "http://gedcomx.org/Marriage"
    militaryAward = "http://gedcomx.org/MilitaryAward"
    militaryDischarge = "http://gedcomx.org/MilitaryDischarge"
    mission = "http://gedcomx.org/Mission"
    moveFrom = "http://gedcomx.org/MoveFrom"
    moveTo = "http://gedcomx.org/MoveTo"
    naturalization = "http://gedcomx.org/Naturalization"
    ordination = "http://gedcomx.org/Ordination"
    retirement = "http://gedcomx.org/Retirement"


class RoleType(GedcomXIdentifier, Enum):
    principal = "http://gedcomx.org/Principal"
    participant = "http://gedcomx.org/Participant"
    official = "http://gedcomx.org/Official"
    witness = "http://gedcomx.org/Witness"


class DocumentType(GedcomXIdentifier, Enum):
    abstract = "http://gedcomx.org/Abstract"
    transcription = "http://gedcomx.org/Transcription"
    translation = "http://gedcomx.org/Translation"
    analysis = "http://gedcomx.org/Analysis"


class FieldValueType(GedcomXIdentifier, Enum):
    original = "http://gedcomx.org/Original"
    interpreted = "http://gedcomx.org/Interpreted"


class EventTypes(GedcomXIdentifier, Enum):
    # https://github.com/FamilySearch/gedcomx-record/blob/master/specifications/field-types-specification.md
    age = "http://gedcomx.org/Age"
    date = "http://gedcomx.org/Date"
    place = "http://gedcomx.org/Place"
    gender = "http://gedcomx.org/Gender"
    name = "http://gedcomx.org/Name"
    role = "http://gedcomx.org/Role"
    years = "http://gedcomx.org/Years"
    months = "http://gedcomx.org/Months"
    days = "http://gedcomx.org/Days"
    hours = "http://gedcomx.org/Hours"
    minutes = "http://gedcomx.org/Minutes"
    year = "http://gedcomx.org/Year"
    month = "http://gedcomx.org/Month"
    day = "http://gedcomx.org/Day"
    hour = "http://gedcomx.org/Hour"
    minute = "http://gedcomx.org/Minute"
    address = "http://gedcomx.org/Address"
    cemetery = "http://gedcomx.org/Cemetery"
    city = "http://gedcomx.org/City"
    church = "http://gedcomx.org/Church"
    county = "http://gedcomx.org/County"
    country = "http://gedcomx.org/Country"
    district = "http://gedcomx.org/District"
    hospital = "http://gedcomx.org/Hospital"
    island = "http://gedcomx.org/Island"
    militaryBase = "http://gedcomx.org/MilitaryBase"
    mortuary = "http://gedcomx.org/Mortuary"
    parish = "http://gedcomx.org/Parish"
    plotNumber = "http://gedcomx.org/PlotNumber"
    postOffice = "http://gedcomx.org/PostOffice"
    postalCode = "http://gedcomx.org/PostalCode"
    prison = "http://gedcomx.org/Prison"
    province = "http://gedcomx.org/Province"
    section = "http://gedcomx.org/Section"
    ship = "http://gedcomx.org/Ship"
    state = "http://gedcomx.org/State"
    territory = "http://gedcomx.org/Territory"
    town = "http://gedcomx.org/Town"
    township = "http://gedcomx.org/Township"
    ward = "http://gedcomx.org/Ward"
    prefix = "http://gedcomx.org/Prefix"
    suffix = "http://gedcomx.org/Suffix"
    given = "http://gedcomx.org/Given"
    surname = "http://gedcomx.org/Surname"
    abusua = "http://gedcomx.org/Abusua"
    batchNumber = "http://gedcomx.org/BatchNumber"
    caste = "http://gedcomx.org/Caste"
    clan = "http://gedcomx.org/Clan"
    commonLawMarriage = "http://gedcomx.org/CommonLawMarriage"
    education = "http://gedcomx.org/Education"
    ethnicity = "http://gedcomx.org/Ethnicity"
    fatherBirthPlace = "http://gedcomx.org/FatherBirthPlace"
    motherBirthPlace = "http://gedcomx.org/MotherBirthPlace"
    neverHadChildren = "http://gedcomx.org/NeverHadChildren"
    neverMarried = "http://gedcomx.org/NeverMarried"
    numberOfChildren = "http://gedcomx.org/NumberOfChildren"
    numberOfMarriages = "http://gedcomx.org/NumberOfMarriages"
    household = "http://gedcomx.org/Household"
    isHeadOfHousehold = "http://gedcomx.org/IsHeadOfHousehold"
    maritalStatus = "http://gedcomx.org/MaritalStatus"
    multipleBirth = "http://gedcomx.org/MultipleBirth"
    nameSake = "http://gedcomx.org/NameSake"
    nationalId = "http://gedcomx.org/NationalId"
    nationality = "http://gedcomx.org/Nationality"
    occupation = "http://gedcomx.org/Occupation"
    physicalDescription = "http://gedcomx.org/PhysicalDescription"
    property = "http://gedcomx.org/Property"
    race = "http://gedcomx.org/Race"
    religion = "http://gedcomx.org/Religion"
    relationshipToHead = "http://gedcomx.org/RelationshipToHead"
    stillbirth = "http://gedcomx.org/Stillbirth"
    titleOfNobility = "http://gedcomx.org/TitleOfNobility"
    tribe = "http://gedcomx.org/Tribe"
