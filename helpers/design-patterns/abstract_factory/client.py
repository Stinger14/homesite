from re import S
from sedecorp_factory import SedecorpFactory

ITEM = SedecorpFactory.get_item("SmallCamera")
print(f'{ITEM.__class__}: {ITEM.get_properties()}')
