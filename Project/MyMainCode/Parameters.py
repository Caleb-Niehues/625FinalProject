class Parameters(object):
    """This class includes all the parameters that form the simulation matrix"""
    def __init__(self):
        pass
    def paper1(self):
        self.phaseName = ['8-Paper1']
        self.vehicleType = ["SUT","TST"]
        self.vehicleModel = ['01F800Truck.k','0TractorSemi-Trailer.k']
        self.barrierBoundary = ["Fixed","Free","Segmented"]
        self.anglesOfAttack = [15]

    def paper2(self):
        self.phaseName = ['8-Paper2']
        self.vehicleType = ["SUT","TST"]
        self.vehicleModel = ['01F800Truck.k','0TractorSemi-Trailer.k']
        self.barrierBoundary = ["Fixed","Free","Segmented"]
        self.barrierShape = ["TL3","TL4","TL5"]
        self.anglesOfAttack = [15]