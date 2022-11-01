class Parameters(object):
    """This class includes all the parameters that form the simulation matrix"""
    def __init__(self):
        self.phaseName=['6.1-Phase1', '6.2-Phase2','6.3-CaseStudy']
        self.vehicleType=["SUT","TST"]
        self.vehicleModel=['01F800Truck.k','0TractorSemi-Trailer.k']
        self.barrierBoundary=["Fixed","Free"]
        self.barrierLength=[20,30]
        self.anglesOfAttack=[15,25]
        self.pierLocation=[[3100,3600,4100],[3100,3600,4100]]
        self.pierLocationCaseStudy=[4100,3100,4100,3100,3600,3600,4100,4100]
