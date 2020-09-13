import xml.etree.ElementTree as ET


def xmlize(obj):
    if hasattr(obj, "xml"):
        return obj.xml()
    tag = obj.__class__.__name__
    e = ET.Element(tag)
