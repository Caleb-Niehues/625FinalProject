import argparse

class Parameters:
    def __init__(self, commandLine):
        parser = argparse.ArgumentParser(commandLine)
        parser.add_argument('phaseName', nargs=2)
        parser.add_argument('vehicleType', nargs=2)
        parser.add_argument('vehicleModel', nargs=2)
        parser.add_argument('barrierBoundary', nargs=3)
        parser.add_argument('barrierShape', nargs=3)
        parser.add_argument('anglesOfAttack')
        parser.add_argument('purpose')
        
        args = parser.parse_args()
        self.phaseName = args.phaseName
        self.vehicleType = args.vehicleType
        self.vehicleModel = args.vehicleModel
        self.barrierBoundary = args.barrierBoundary
        self.barrierShape = args.barrierShape
        self.anglesOfAttack = args.anglesOfAttack
        self.purpose = args.purpose