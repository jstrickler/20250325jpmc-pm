import lxml.etree as et

# et.Elementree obj
doc = et.parse('DATA/solar.xml')

root = doc.getroot()

for planet_tag in doc.findall('.//planet'):
    print(planet_tag.get('planetname'))
    for moon in planet_tag.findall('moon'):
        print(f"     {moon.text}")