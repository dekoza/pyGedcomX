example_json = r"""
{
  "attribution" : {
    "contributor" : {
      "resource" : "#GGG-GGGG"
    }
  },
  "persons" : [ {
    "names" : [ {
      "nameForms" : [ {
        "fullText" : "George Washington",
        "parts" : [ {
          "value" : "George",
          "type" : "http://gedcomx.org/Given"
        }, {
          "value" : "Washington",
          "type" : "http://gedcomx.org/Surname"
        } ]
      } ],
      "id" : "789"
    } ],
    "gender" : {
      "type" : "http://gedcomx.org/Male"
    },
    "facts" : [ {
      "type" : "http://gedcomx.org/Birth",
      "date" : {
        "original" : "February 22, 1732",
        "formal" : "+1732-02-22"
      },
      "place" : {
        "original" : "pope's creek, westmoreland, virginia, united states",
        "description" : "#888"
      },
      "id" : "123"
    }, {
      "type" : "http://gedcomx.org/Death",
      "date" : {
        "original" : "December 14, 1799",
        "formal" : "+1799-12-14T22:00:00"
      },
      "place" : {
        "original" : "mount vernon, fairfax county, virginia, united states",
        "description" : "#999"
      },
      "id" : "456"
    } ],
    "sources" : [ {
      "description" : "#EEE-EEEE"
    } ],
    "id" : "BBB-BBBB"
  }, {
    "names" : [ {
      "nameForms" : [ {
        "fullText" : "Martha Dandridge Custis",
        "parts" : [ {
          "value" : "Martha Dandridge",
          "type" : "http://gedcomx.org/Given"
        }, {
          "value" : "Custis",
          "type" : "http://gedcomx.org/Surname"
        } ]
      } ],
      "id" : "987"
    } ],
    "gender" : {
      "type" : "http://gedcomx.org/Male"
    },
    "facts" : [ {
      "type" : "http://gedcomx.org/Birth",
      "date" : {
        "original" : "June 2, 1731",
        "formal" : "+1731-06-02"
      },
      "place" : {
        "original" : "chestnut grove, new kent, virginia, united states",
        "description" : "#KKK"
      },
      "id" : "321"
    }, {
      "type" : "http://gedcomx.org/Death",
      "date" : {
        "original" : "May 22, 1802",
        "formal" : "+1802-05-22"
      },
      "place" : {
        "original" : "mount vernon, fairfax county, virginia, united states",
        "description" : "#999"
      },
      "id" : "654"
    } ],
    "sources" : [ {
      "description" : "#FFF-FFFF"
    } ],
    "id" : "CCC-CCCC"
  } ],
  "relationships" : [ {
    "facts" : [ {
      "type" : "http://gedcomx.org/Marriage",
      "date" : {
        "original" : "January 6, 1759",
        "formal" : "+1759-01-06"
      },
      "place" : {
        "original" : "White House Plantation"
      }
    } ],
    "person1" : {
      "resource" : "#BBB-BBBB"
    },
    "person2" : {
      "resource" : "#CCC-CCCC"
    },
    "sources" : [ {
      "description" : "#FFF-FFFF"
    } ],
    "id" : "DDD-DDDD"
  } ],
  "sourceDescriptions" : [ {
    "citations" : [ {
      "value" : "\"George Washington.\" Wikipedia, The Free Encyclopedia. Wikimedia Foundation, Inc. 24 October 2012."
    } ],
    "about" : "http://en.wikipedia.org/wiki/George_washington",
    "id" : "EEE-EEEE"
  }, {
    "citations" : [ {
      "value" : "\"Martha Washington.\" Wikipedia, The Free Encyclopedia. Wikimedia Foundation, Inc. 24 October 2012."
    } ],
    "about" : "http://en.wikipedia.org/wiki/Martha_washington",
    "id" : "FFF-FFFF"
  } ],
  "agents" : [ {
    "names" : [ {
      "value" : "Ryan Heaton"
    } ],
    "id" : "GGG-GGGG"
  } ],
  "places" : [ {
    "names" : [ {
      "value" : "Pope's Creek, Westmoreland, Virginia, United States"
    } ],
    "latitude" : 38.192353,
    "longitude" : -76.904069,
    "id" : "888"
  }, {
    "names" : [ {
      "value" : "Mount Vernon, Fairfax County, Virginia, United States"
    } ],
    "latitude" : 38.721144,
    "longitude" : -77.109461,
    "id" : "999"
  }, {
    "names" : [ {
      "value" : "Chestnut Grove, New Kent, Virginia, United States"
    } ],
    "latitude" : 37.518304,
    "longitude" : -76.984148,
    "id" : "KKK"
  } ]
}"""
example_xml = r"""
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<gedcomx xmlns="http://gedcomx.org/v1/">
    <attribution>
        <contributor resource="#GGG-GGGG"/>
    </attribution>
    <person id="BBB-BBBB">
        <source description="#EEE-EEEE"/>
        <gender type="http://gedcomx.org/Male"/>
        <name id="789">
            <nameForm>
                <fullText>George Washington</fullText>
                <part type="http://gedcomx.org/Given" value="George"/>
                <part type="http://gedcomx.org/Surname" value="Washington"/>
            </nameForm>
        </name>
        <fact type="http://gedcomx.org/Birth" id="123">
            <date>
                <original>February 22, 1732</original>
                <formal>+1732-02-22</formal>
            </date>
            <place description="#888">
                <original>pope's creek, westmoreland, virginia, united states</original>
            </place>
        </fact>
        <fact type="http://gedcomx.org/Death" id="456">
            <date>
                <original>December 14, 1799</original>
                <formal>+1799-12-14T22:00:00</formal>
            </date>
            <place description="#999">
                <original>mount vernon, fairfax county, virginia, united states</original>
            </place>
        </fact>
    </person>
    <person id="CCC-CCCC">
        <source description="#FFF-FFFF"/>
        <gender type="http://gedcomx.org/Male"/>
        <name id="987">
            <nameForm>
                <fullText>Martha Dandridge Custis</fullText>
                <part type="http://gedcomx.org/Given" value="Martha Dandridge"/>
                <part type="http://gedcomx.org/Surname" value="Custis"/>
            </nameForm>
        </name>
        <fact type="http://gedcomx.org/Birth" id="321">
            <date>
                <original>June 2, 1731</original>
                <formal>+1731-06-02</formal>
            </date>
            <place description="#KKK">
                <original>chestnut grove, new kent, virginia, united states</original>
            </place>
        </fact>
        <fact type="http://gedcomx.org/Death" id="654">
            <date>
                <original>May 22, 1802</original>
                <formal>+1802-05-22</formal>
            </date>
            <place description="#999">
                <original>mount vernon, fairfax county, virginia, united states</original>
            </place>
        </fact>
    </person>
    <relationship id="DDD-DDDD">
        <source description="#FFF-FFFF"/>
        <person1 resource="#BBB-BBBB"/>
        <person2 resource="#CCC-CCCC"/>
        <fact>
            <date>
                <original>January 6, 1759</original>
                <formal>+01-06-1759</formal>
            </date>
            <place>
                <original>White House Plantation</original>
            </place>
        </fact>
    </relationship>
    <sourceDescription about="http://en.wikipedia.org/wiki/George_washington" id="EEE-EEEE">
        <citation>
            <value>"George Washington." Wikipedia, The Free Encyclopedia. Wikimedia Foundation, Inc. 24 October 2012.</value>
        </citation>
    </sourceDescription>
    <sourceDescription about="http://en.wikipedia.org/wiki/Martha_washington" id="FFF-FFFF">
        <citation>
            <value>"Martha Washington." Wikipedia, The Free Encyclopedia. Wikimedia Foundation, Inc. 24 October 2012.</value>
        </citation>
    </sourceDescription>
    <agent id="GGG-GGGG">
        <name>Ryan Heaton</name>
    </agent>
    <place id="888">
        <name>Pope's Creek, Westmoreland, Virginia, United States</name>
        <latitude>38.192353</latitude>
        <longitude>-76.904069</longitude>
    </place>
    <place id="999">
        <name>Mount Vernon, Fairfax County, Virginia, United States</name>
        <latitude>38.721144</latitude>
        <longitude>-77.109461</longitude>
    </place>
    <place id="KKK">
        <name>Chestnut Grove, New Kent, Virginia, United States</name>
        <latitude>37.518304</latitude>
        <longitude>-76.984148</longitude>
    </place>
</gedcomx>"""
