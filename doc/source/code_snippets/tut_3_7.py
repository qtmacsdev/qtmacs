"""
Tutorial 3: Applet- and macro signatures.
"""

# Import the module with the global variables and the macro base class.
import qtmacs.qte_global as qte_global
from qtmacs.base_macro import QtmacsMacro
from qtmacs.base_applet import QtmacsApplet
from PyQt4 import QtGui

# Get a reference to the main instance of Qtmacs.
qteMain = qte_global.qteMain


class TutorialMulti(QtmacsApplet):
    """
    An applet with multiple widgets.
    """
    def __init__(self, appletID):
        # Initialise the base class.
        super().__init__(appletID)

        # Instantiate three QLineEdit objects.
        line1 = QtGui.QLineEdit(self)
        line2 = QtGui.QLineEdit(self)
        line3 = QtGui.QLineEdit(self)

        # Register them with Qtmacs.
        self.qteLine1 = self.qteAddWidget(line1)
        self.qteLine2 = self.qteAddWidget(line2, autoBind=False)
        self.qteLine3 = self.qteAddWidget(line3, widgetSignature='custom')

        # Register the macro and connect the ``clicked`` signals of
        # the push buttons.
        self.macroName = qteMain.qteRegisterMacro(DemoMacroLineEdit)

        # Bind the 'e' key to all widgets.
        qteMain.qteBindKeyWidget('e', self.macroName, self.qteLine1)
        qteMain.qteBindKeyWidget('e', self.macroName, self.qteLine2)
        qteMain.qteBindKeyWidget('e', self.macroName, self.qteLine3)


class DemoMacroLineEdit(QtmacsMacro):
    """
    Insert the string '|LineEdit|` into a QLineEdit.

    |Signature|

    * *applet*: '*'
    * *widget*: 'QLineEdit'
    """
    def __init__(self):
        super().__init__()
        self.qteSetAppletSignature('*')
        self.qteSetWidgetSignature('QLineEdit')

    def qteRun(self):
        self.qteWidget.insert('|LineEdit|')


# Register the applet with Qtmacs, create an instance of it,
# and make it active immediately.
app_name = qteMain.qteRegisterApplet(TutorialMulti)
app_obj = qteMain.qteNewApplet(app_name)
qteMain.qteMakeAppletActive(app_obj)
