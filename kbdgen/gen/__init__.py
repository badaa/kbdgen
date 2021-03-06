from collections import OrderedDict

from .ios import AppleiOSGenerator
from .android import AndroidGenerator
from .win import WindowsGenerator
from .osx import OSXGenerator
from .x11 import XKBGenerator
from .svgkbd import SVGGenerator
from .json import QRGenerator, JSONGenerator
from .errormodel import ErrorModelGenerator

generators = OrderedDict(
    (
        ("win", WindowsGenerator),
        ("osx", OSXGenerator),
        ("x11", XKBGenerator),
        ("svg", SVGGenerator),
        ("android", AndroidGenerator),
        ("ios", AppleiOSGenerator),
        ("json", JSONGenerator),
        ("qr", QRGenerator),
        ("errormodel", ErrorModelGenerator),
    )
)
