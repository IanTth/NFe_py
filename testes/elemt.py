import xml.etree.ElementTree as ET

from nfe import *
from user import *

tree = ET.parse('ex_NFe.xml')
root = tree.getroot()

print(root.tag)