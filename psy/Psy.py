class Psy:
    def __init__(self, atm_pressure=101325):
        self.atm_pressure = atm_pressure

    def calc_air_par(self, t_db, phi, t_wb=None, t_d=None, w=None, h=None,
                     v=None):
        """
        Takes 2 any air parameters and calculates the rest.
        
        All values in SI
        :param t_db: dry-bulb temperature
        :param phi: relative humidity
        :param t_wb: wet-bulb temperature
        :param t_d: dew-point temperature
        :param w: humidity ratio
        :param h: enthalpy
        :param v: specific volume (1/density)
        :return: dictionary of the rest parameters
        """
        pass

    def calc_process(self, m, air_state1, air_state2, process=None, **kwargs):
        """
        Claculates thermodynamic processes
        :param m: mass airflow of the air
        :param air_state1: dict of at least two parameters of air in state
        one
        :param air_state2: None or dict of either one air parameter if process
        is not None, or two air parameters otherwise. None value can be if 
        'sens_heat_gain', 'latent_heat_gain' is in kwargs
        :param process: None - free process,
        'sensible_heating' - sensible heating , sens_heat_gain should be in 
            kwargs
        :return: air_state1, air_state2, sensible_heat, latent_heat
        """
        pass
