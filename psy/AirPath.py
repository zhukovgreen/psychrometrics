from psy.Psy import Psy


class AirPath:
    """Implementation of psychrometrics physics"""

    def __init__(self):
        pass

    def calc(self, air_path):
        """
        Iterates over all AHU components, calculates air parameters and 
        process pressure drop in each
        inlet and outlet. Automatically finds the air path based on inlets and
        outlets ids. It uses class `Psy` to calculate required air processes
        :param air_path: a list of dictionaries. Each dictionary describes
        the air parameters before and after the component.
        :return: updated air_path  
        """
        pass

    def vis(self, data):
        """Visualize the air processes on psychrometric chart"""
        pass


if __name__ == '__main__':
    air_path = [
        {'inlets': {'sup': {10: {'tdb': 5, 'phi': 0.87}}, 'eta': None},
         'process': {'type': None, 'kwargs': None, 'dp': None,
                     'note': 'OA damper'},
         'outlets': {'sup': {11: {'tdb': None, 'phi': None}, 'eta': None}}},
        {'inlets': {'sup': {11: {'tdb': None, 'phi': None}}, 'eta': None},
         'process': {'type': None, 'kwargs': None, 'dp': None,
                     'note': 'filter'},
         'outlets': {12: {'tdb': None, 'phi': None}}},
        {'inlets': {'sup': {12: {'tdb': None, 'phi': None}},
                    'eta': {22: {'tdb': None, 'phi': None}}},
         'process': {'type': 'phex',
                     'kwargs': {
                         'winter': {'sens_eff': 0.81, 'latent_eff': 0.3},
                         'summer': None},
                     'dp': None,
                     'note': 'plate heat exchanger'},
         'outlets': {'sup': {13: {'tdb': None, 'phi': None}},
                     'eta': {23: {'tdb': None, 'phi': None}}},
         },
        {'inlets': {'sup': {13: {'tdb': None, 'phi': None}},
                    'eta': {21: {'tdb': None, 'phi': None}}},
         'process': {'type': 'mixing',
                     'kwargs': {
                         'winter': {'mix_ratio': 0.3},
                         'summer': None},
                     'dp': None,
                     'note': 'mixing chamber'},
         'outlets': {'sup': {14: {'tdb': None, 'phi': None}},
                     'eta': {22: {'tdb': None, 'phi': None}}},
         },
        {'inlets': {'sup': {14: {'tdb': None, 'phi': None}}, 'eta': None},
         'process': {'type': None, 'kwargs': {'heat_gain': None}, 'dp': None,
                     'note': 'supply fan'},
         'outlets': {'sup': {15: {'tdb': None, 'phi': None}, 'eta': None}}},
        {'inlets': {'sup': None, 'eta': {20: {'tdb': 25, 'phi': 0.27}}},
         'process': {'type': None, 'kwargs': {'heat_gain': None}, 'dp': None,
                     'note': 'extract fan'},
         'outlets': {'sup': None, 'eta': {21: {'tdb': None, 'phi': None}}}},

    ]
    t = AirPath()
    t.calc(air_path)
