# -- coding: utf-8 --

"""

Created on Wed Apr  8 17:53:04 2020



@author: Klaus Reinold

"""




from graphics_and_games_klassen import Rechteck







class KleineWelt():

    """

    Legt das Spielfeld an und die nicht beweglichen Objekte 

    """

    def __init__(self):

        """

        Baut das Szenario auf.

        """    

        rechteck0 = Rechteck()

        rechteck0.PositionSetzen(2, 2)

        rechteck0.GroesseSetzen(96, 96)

        rechteck0.FarbeSetzen("grün")

        

        rechteck1 = Rechteck()

        rechteck1.PositionSetzen(102, 2)

        rechteck1.GroesseSetzen(96, 96)

        rechteck1.FarbeSetzen("blau")

        

        rechteck2 = Rechteck()

        rechteck2.PositionSetzen(202, 2)

        rechteck2.GroesseSetzen(96, 96)

        rechteck2.FarbeSetzen("blau")



        rechteck3 = Rechteck()

        rechteck3.PositionSetzen(2, 102)

        rechteck3.GroesseSetzen(96, 96)

        rechteck3.FarbeSetzen("rot")



        rechteck4 = Rechteck()

        rechteck4.PositionSetzen(102, 102)

        rechteck4.GroesseSetzen(50, 50)

        rechteck4.FarbeSetzen("blau")



        rechteck5 = Rechteck()

        rechteck5.PositionSetzen(202, 50)

        rechteck5.GroesseSetzen(96, 96)

        rechteck5.FarbeSetzen("blau")

        

        rechteck6 = Rechteck()

        rechteck6.PositionSetzen(2, 202)

        rechteck6.GroesseSetzen(96, 96)

        rechteck6.FarbeSetzen("gelb")

        

        rechteck7 = Rechteck()

        rechteck7.PositionSetzen(102, 202)

        rechteck7.GroesseSetzen(96, 96)

        rechteck7.FarbeSetzen("blau")



        rechteck8 = Rechteck()

        rechteck8.PositionSetzen(202, 202)

        rechteck8.GroesseSetzen(96, 96)

        rechteck8.FarbeSetzen("blau")



KleineWelt()