from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class CreataCFSTcolumnDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'CFST columns automatic modeling program',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        VFrame_1 = FXVerticalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_3 = FXGroupBox(p=VFrame_1, text='Diagram', opts=FRAME_GROOVE)
        fileName = os.path.join(thisDir, 'S9.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=GroupBox_3, text='', ic=icon)

        VFrame_2 = FXVerticalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_6 = FXGroupBox(p=VFrame_2, text='Model Name', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_6, ncols=20, labelText='Model Name:', tgt=form.keyword06Kw, sel=0)
        
        HFrame_1 = FXHorizontalFrame(p=VFrame_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_4 = FXGroupBox(p=HFrame_1, text='Material Parameter', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_4, ncols=12, labelText='Compressive Strength of Concrete:', tgt=form.keyword01Kw, sel=0)
        AFXTextField(p=GroupBox_4, ncols=12, labelText='Yield Strength of Steel Tube:', tgt=form.keyword02Kw, sel=0)
        GroupBox_5 = FXGroupBox(p=HFrame_1, text='Geometry Parameter', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_5, ncols=15, labelText='H:', tgt=form.keyword05Kw, sel=0)
        AFXTextField(p=GroupBox_5, ncols=15, labelText='D:', tgt=form.keyword03Kw, sel=0)
        AFXTextField(p=GroupBox_5, ncols=15, labelText='t :', tgt=form.keyword04Kw, sel=0)
