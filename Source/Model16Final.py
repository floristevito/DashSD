"""
Python model "Model16Final.py"
Translated using PySD version 0.10.0
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.py_backend.functions import cache
from pysd.py_backend import functions

_subscript_dict = {}

_namespace = {
    'TIME': 'time',
    'Time': 'time',
    'Agricultural production shortage': 'agricultural_production_shortage',
    'Agricultural water shortage with import': 'agricultural_water_shortage_with_import',
    'Change Nile flow Egypt dry climate': 'change_nile_flow_egypt_dry_climate',
    'Change Nile flow Egypt wet climate': 'change_nile_flow_egypt_wet_climate',
    'Annual Nile waterflow to Egypt': 'annual_nile_waterflow_to_egypt',
    'Normal annual Nile flow to Egypt': 'normal_annual_nile_flow_to_egypt',
    '"External switch 2: wet climate"': 'external_switch_2_wet_climate',
    'Agricultural import': 'agricultural_import',
    'Effect low prices on import rate': 'effect_low_prices_on_import_rate',
    '"External switch 1: dry climate"': 'external_switch_1_dry_climate',
    '"External switch 4: high international food prices"':
    'external_switch_4_high_international_food_prices',
    'Normal import rate Egypt': 'normal_import_rate_egypt',
    'Effect high prices on import rate': 'effect_high_prices_on_import_rate',
    '"External switch 3: low international food prices"':
    'external_switch_3_low_international_food_prices',
    'Effective irrigated land': 'effective_irrigated_land',
    'Percentage of new land surface irrigated': 'percentage_of_new_land_surface_irrigated',
    'Percentage of decreased land localized irrigated':
    'percentage_of_decreased_land_localized_irrigated',
    'Percentage of decreased land sprinkler irrigated':
    'percentage_of_decreased_land_sprinkler_irrigated',
    'Percentage of decreased land surface irrigated':
    'percentage_of_decreased_land_surface_irrigated',
    'Percentage of new land localized irrigated': 'percentage_of_new_land_localized_irrigated',
    'Percentage of new land sprinkler irrigated': 'percentage_of_new_land_sprinkler_irrigated',
    'Sum percentage new land': 'sum_percentage_new_land',
    'Change in area surface irrigated': 'change_in_area_surface_irrigated',
    'Sum percentage decreased land': 'sum_percentage_decreased_land',
    'Change in area sprinkler irrigated': 'change_in_area_sprinkler_irrigated',
    'Change in area localized irrigated': 'change_in_area_localized_irrigated',
    'New water demand per irrigated area': 'new_water_demand_per_irrigated_area',
    'Minimum water demand per irrigated area': 'minimum_water_demand_per_irrigated_area',
    '"Policy switch 1: water demand reduction"': 'policy_switch_1_water_demand_reduction',
    'Additional annual non renewable water resources':
    'additional_annual_non_renewable_water_resources',
    'Additional annual water resources': 'additional_annual_water_resources',
    'Decrease potential irrigated land': 'decrease_potential_irrigated_land',
    'Inital percentage sprinkler': 'inital_percentage_sprinkler',
    'Inital percentage surface': 'inital_percentage_surface',
    'Agricultural production': 'agricultural_production',
    'Direct use rate': 'direct_use_rate',
    'Rel surface irrigated': 'rel_surface_irrigated',
    'Initial percentage localized': 'initial_percentage_localized',
    'Annual internal renewable ground and surface water':
    'annual_internal_renewable_ground_and_surface_water',
    'Irrigated water loss': 'irrigated_water_loss',
    'Efficiency score sprinkler': 'efficiency_score_sprinkler',
    'Efficiency score surface': 'efficiency_score_surface',
    'Efficiency sprinkler': 'efficiency_sprinkler',
    'Direct use of agricultural drainage': 'direct_use_of_agricultural_drainage',
    'Increase potential irrigated land': 'increase_potential_irrigated_land',
    'Average water consumption per kg agricultural production':
    'average_water_consumption_per_kg_agricultural_production',
    'Water demand reduction': 'water_demand_reduction',
    'Potential irrigated land localized irrigated': 'potential_irrigated_land_localized_irrigated',
    'Potential irrigated land sprinkler irrigated': 'potential_irrigated_land_sprinkler_irrigated',
    'Recovered irrigation water': 'recovered_irrigation_water',
    'Rel localized irrigated': 'rel_localized_irrigated',
    'Rel sprinkler irrigated': 'rel_sprinkler_irrigated',
    'Percentage recovered': 'percentage_recovered',
    'Efficiency localized': 'efficiency_localized',
    'Efficiency score localized': 'efficiency_score_localized',
    'Water use for irrigation': 'water_use_for_irrigation',
    'Water consumption from agricultural production':
    'water_consumption_from_agricultural_production',
    'Evapotranspiration': 'evapotranspiration',
    'Efficiency surface': 'efficiency_surface',
    'Sum efficiency': 'sum_efficiency',
    'Sum potential': 'sum_potential',
    'Potential irrigated land surface irrigated': 'potential_irrigated_land_surface_irrigated',
    'Treated municipal wastewater': 'treated_municipal_wastewater',
    'Irrigated water volume': 'irrigated_water_volume',
    'Water supply for irrigation': 'water_supply_for_irrigation',
    'Desalinated water produced': 'desalinated_water_produced',
    'Potential irrigated land': 'potential_irrigated_land',
    'Initial area localized irrigation': 'initial_area_localized_irrigation',
    'Initial area sprinkler irrigation': 'initial_area_sprinkler_irrigation',
    'Initial area surface irrigation': 'initial_area_surface_irrigation',
    'Ini water Egypt': 'ini_water_egypt',
    'Water allocated agriculture': 'water_allocated_agriculture',
    'Usable water volume Egypt': 'usable_water_volume_egypt',
    'Annual external renewable groundwater': 'annual_external_renewable_groundwater',
    'Water allocated other sectors': 'water_allocated_other_sectors',
    'Maximum annual irrigated land decrease': 'maximum_annual_irrigated_land_decrease',
    'Maximum annual irrigated land growth': 'maximum_annual_irrigated_land_growth',
    'Average agricultural production per irrigated land':
    'average_agricultural_production_per_irrigated_land',
    'Agricultural water shortage': 'agricultural_water_shortage',
    'Average food demand per capita': 'average_food_demand_per_capita',
    'Birth rate Egypt': 'birth_rate_egypt',
    'Death rate Egypt': 'death_rate_egypt',
    'Agricultural food demand': 'agricultural_food_demand',
    'Ini potential irrigated land': 'ini_potential_irrigated_land',
    'Ini irrigated water volume': 'ini_irrigated_water_volume',
    'Ini population Egypt': 'ini_population_egypt',
    'Ini water demand per irrigated area': 'ini_water_demand_per_irrigated_area',
    'Ini water supply irrigation': 'ini_water_supply_irrigation',
    'Average evapotranspiration': 'average_evapotranspiration',
    'Population decrease': 'population_decrease',
    'Population Egypt': 'population_egypt',
    'Population increase': 'population_increase',
    'Water allocation rate agriculture': 'water_allocation_rate_agriculture',
    'Water demand per irrigated area': 'water_demand_per_irrigated_area',
    'FINAL TIME': 'final_time',
    'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper',
    'TIME STEP': 'time_step'
}

__pysd_version__ = "0.10.0"

__data = {'scope': None, 'time': lambda: 0}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


def time():
    return __data['time']()


@cache('step')
def agricultural_production_shortage():
    """
    Real Name: b'Agricultural production shortage'
    Original Eqn: b'MAX( 0 , Agricultural food demand-Agricultural production )'
    Units: b'kg/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(0, agricultural_food_demand() - agricultural_production())


@cache('step')
def agricultural_water_shortage_with_import():
    """
    Real Name: b'Agricultural water shortage with import'
    Original Eqn: b'MAX(0, (Agricultural production shortage-Agricultural import)/Average agricultural production per irrigated land\\\\ *Water demand per irrigated area)'
    Units: b'(m*m*m)/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(0, (agricultural_production_shortage() - agricultural_import()) /
                      average_agricultural_production_per_irrigated_land() *
                      water_demand_per_irrigated_area())


@cache('run')
def change_nile_flow_egypt_dry_climate():
    """
    Real Name: b'Change Nile flow Egypt dry climate'
    Original Eqn: b'-0.6'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return -0.6


@cache('run')
def change_nile_flow_egypt_wet_climate():
    """
    Real Name: b'Change Nile flow Egypt wet climate'
    Original Eqn: b'0.45'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.45


@cache('step')
def annual_nile_waterflow_to_egypt():
    """
    Real Name: b'Annual Nile waterflow to Egypt'
    Original Eqn: b'Normal annual Nile flow to Egypt* (1 + ("External switch 1: dry climate"*Change Nile flow Egypt dry climate\\\\ )+("External switch 2: wet climate"*Change Nile flow Egypt wet climate))'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return normal_annual_nile_flow_to_egypt() * (
        1 + (external_switch_1_dry_climate() * change_nile_flow_egypt_dry_climate()) +
        (external_switch_2_wet_climate() * change_nile_flow_egypt_wet_climate()))


@cache('run')
def normal_annual_nile_flow_to_egypt():
    """
    Real Name: b'Normal annual Nile flow to Egypt'
    Original Eqn: b'5.55e+10'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5.55e+10


@cache('run')
def external_switch_2_wet_climate():
    """
    Real Name: b'"External switch 2: wet climate"'
    Original Eqn: b'0'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def agricultural_import():
    """
    Real Name: b'Agricultural import'
    Original Eqn: b'Agricultural food demand*IF THEN ELSE("External switch 3: low international food prices"\\\\ =0 :AND: "External switch 4: high international food prices"=0 , Normal import rate Egypt\\\\ , (("External switch 3: low international food prices"*Effect low prices on import rate\\\\ )+("External switch 4: high international food prices"*Effect high prices on import rate\\\\ )))'
    Units: b'kg/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return agricultural_food_demand() * functions.if_then_else(
        external_switch_3_low_international_food_prices() == 0
        and external_switch_4_high_international_food_prices() == 0, normal_import_rate_egypt(),
        ((external_switch_3_low_international_food_prices() * effect_low_prices_on_import_rate()) +
         (external_switch_4_high_international_food_prices() *
          effect_high_prices_on_import_rate())))


@cache('run')
def effect_low_prices_on_import_rate():
    """
    Real Name: b'Effect low prices on import rate'
    Original Eqn: b'0.59'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.59


@cache('run')
def external_switch_1_dry_climate():
    """
    Real Name: b'"External switch 1: dry climate"'
    Original Eqn: b'0'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def external_switch_4_high_international_food_prices():
    """
    Real Name: b'"External switch 4: high international food prices"'
    Original Eqn: b'0'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def normal_import_rate_egypt():
    """
    Real Name: b'Normal import rate Egypt'
    Original Eqn: b'0.57'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.57


@cache('run')
def effect_high_prices_on_import_rate():
    """
    Real Name: b'Effect high prices on import rate'
    Original Eqn: b'0.15'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.15


@cache('run')
def external_switch_3_low_international_food_prices():
    """
    Real Name: b'"External switch 3: low international food prices"'
    Original Eqn: b'0'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def effective_irrigated_land():
    """
    Real Name: b'Effective irrigated land'
    Original Eqn: b'MIN(Water allocated agriculture/Water demand per irrigated area, Potential irrigated land\\\\ )'
    Units: b'km*km'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(water_allocated_agriculture() / water_demand_per_irrigated_area(),
                      potential_irrigated_land())


@cache('run')
def percentage_of_new_land_surface_irrigated():
    """
    Real Name: b'Percentage of new land surface irrigated'
    Original Eqn: b'0'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def percentage_of_decreased_land_localized_irrigated():
    """
    Real Name: b'Percentage of decreased land localized irrigated'
    Original Eqn: b'0'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def percentage_of_decreased_land_sprinkler_irrigated():
    """
    Real Name: b'Percentage of decreased land sprinkler irrigated'
    Original Eqn: b'0'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def percentage_of_decreased_land_surface_irrigated():
    """
    Real Name: b'Percentage of decreased land surface irrigated'
    Original Eqn: b'100'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 100


@cache('run')
def percentage_of_new_land_localized_irrigated():
    """
    Real Name: b'Percentage of new land localized irrigated'
    Original Eqn: b'50'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('run')
def percentage_of_new_land_sprinkler_irrigated():
    """
    Real Name: b'Percentage of new land sprinkler irrigated'
    Original Eqn: b'50'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('step')
def sum_percentage_new_land():
    """
    Real Name: b'Sum percentage new land'
    Original Eqn: b'Percentage of new land localized irrigated+Percentage of new land sprinkler irrigated\\\\ +Percentage of new land surface irrigated'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return percentage_of_new_land_localized_irrigated(
    ) + percentage_of_new_land_sprinkler_irrigated() + percentage_of_new_land_surface_irrigated()


@cache('step')
def change_in_area_surface_irrigated():
    """
    Real Name: b'Change in area surface irrigated'
    Original Eqn: b'-Increase potential irrigated land*(Percentage of new land surface irrigated/100)+Decrease potential irrigated land\\\\ *(Percentage of decreased land surface irrigated/100)'
    Units: b'(km*km)/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return -increase_potential_irrigated_land() * (
        percentage_of_new_land_surface_irrigated() / 100) + decrease_potential_irrigated_land() * (
            percentage_of_decreased_land_surface_irrigated() / 100)


@cache('step')
def sum_percentage_decreased_land():
    """
    Real Name: b'Sum percentage decreased land'
    Original Eqn: b'Percentage of decreased land localized irrigated+Percentage of decreased land sprinkler irrigated\\\\ +Percentage of decreased land surface irrigated'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return percentage_of_decreased_land_localized_irrigated(
    ) + percentage_of_decreased_land_sprinkler_irrigated(
    ) + percentage_of_decreased_land_surface_irrigated()


@cache('step')
def change_in_area_sprinkler_irrigated():
    """
    Real Name: b'Change in area sprinkler irrigated'
    Original Eqn: b'-Increase potential irrigated land*(Percentage of new land sprinkler irrigated/100)+\\\\ Decrease potential irrigated land*(Percentage of decreased land sprinkler irrigated\\\\ /100)'
    Units: b'(km*km)/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return -increase_potential_irrigated_land() * (
        percentage_of_new_land_sprinkler_irrigated() / 100) + decrease_potential_irrigated_land(
        ) * (percentage_of_decreased_land_sprinkler_irrigated() / 100)


@cache('step')
def change_in_area_localized_irrigated():
    """
    Real Name: b'Change in area localized irrigated'
    Original Eqn: b'-Increase potential irrigated land*(Percentage of new land localized irrigated/100)+\\\\ Decrease potential irrigated land*(Percentage of decreased land localized irrigated\\\\ /100)'
    Units: b'(km*km)/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return -increase_potential_irrigated_land() * (
        percentage_of_new_land_localized_irrigated() / 100) + decrease_potential_irrigated_land(
        ) * (percentage_of_decreased_land_localized_irrigated() / 100)


@cache('step')
def new_water_demand_per_irrigated_area():
    """
    Real Name: b'New water demand per irrigated area'
    Original Eqn: b'Rel surface irrigated*Efficiency surface+Rel sprinkler irrigated*Efficiency sprinkler\\\\ +Rel localized irrigated*Efficiency localized'
    Units: b'(m*m*m)/(km*km)/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return rel_surface_irrigated() * efficiency_surface() + rel_sprinkler_irrigated(
    ) * efficiency_sprinkler() + rel_localized_irrigated() * efficiency_localized()


@cache('step')
def minimum_water_demand_per_irrigated_area():
    """
    Real Name: b'Minimum water demand per irrigated area'
    Original Eqn: b'Irrigated water loss/Effective irrigated land'
    Units: b'(m*m*m)/(km*km)/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return irrigated_water_loss() / effective_irrigated_land()


@cache('run')
def policy_switch_1_water_demand_reduction():
    """
    Real Name: b'"Policy switch 1: water demand reduction"'
    Original Eqn: b'0'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def additional_annual_non_renewable_water_resources():
    """
    Real Name: b'Additional annual non renewable water resources'
    Original Eqn: b'5.8*10^9'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5.8 * 10**9


@cache('step')
def additional_annual_water_resources():
    """
    Real Name: b'Additional annual water resources'
    Original Eqn: b'Annual external renewable groundwater+ Annual internal renewable ground and surface water+ Desalinated water produced+ Direct use of agricultural drainage+ Treated municipal wastewater+ Additional annual non renewable water resources'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return annual_external_renewable_groundwater(
    ) + annual_internal_renewable_ground_and_surface_water() + desalinated_water_produced(
    ) + direct_use_of_agricultural_drainage() + treated_municipal_wastewater(
    ) + additional_annual_non_renewable_water_resources()


@cache('step')
def decrease_potential_irrigated_land():
    """
    Real Name: b'Decrease potential irrigated land'
    Original Eqn: b'IF THEN ELSE(Potential irrigated land > Effective irrigated land, Maximum annual irrigated land decrease\\\\ , 0 )'
    Units: b'km*km/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(potential_irrigated_land() > effective_irrigated_land(),
                                  maximum_annual_irrigated_land_decrease(), 0)


@cache('step')
def inital_percentage_sprinkler():
    """
    Real Name: b'Inital percentage sprinkler'
    Original Eqn: b'INITIAL( 0.115)'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return _initial_0115()


@cache('step')
def inital_percentage_surface():
    """
    Real Name: b'Inital percentage surface'
    Original Eqn: b'INITIAL( 0.77)'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return _initial_077()


@cache('step')
def agricultural_production():
    """
    Real Name: b'Agricultural production'
    Original Eqn: b'Effective irrigated land * Average agricultural production per irrigated land'
    Units: b'kg/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return effective_irrigated_land() * average_agricultural_production_per_irrigated_land()


@cache('run')
def direct_use_rate():
    """
    Real Name: b'Direct use rate'
    Original Eqn: b'11.9*10^9/(11.9*10^9+1800*10^6)'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 11.9 * 10**9 / (11.9 * 10**9 + 1800 * 10**6)


@cache('step')
def rel_surface_irrigated():
    """
    Real Name: b'Rel surface irrigated'
    Original Eqn: b'Potential irrigated land surface irrigated/Sum potential'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return potential_irrigated_land_surface_irrigated() / sum_potential()


@cache('step')
def initial_percentage_localized():
    """
    Real Name: b'Initial percentage localized'
    Original Eqn: b'INITIAL( 0.115)'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return _initial_0115()


@cache('step')
def annual_internal_renewable_ground_and_surface_water():
    """
    Real Name: b'Annual internal renewable ground and surface water'
    Original Eqn: b'Recovered irrigation water*(1-Direct use rate)'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return recovered_irrigation_water() * (1 - direct_use_rate())


@cache('step')
def irrigated_water_loss():
    """
    Real Name: b'Irrigated water loss'
    Original Eqn: b'Evapotranspiration+Water consumption from agricultural production'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return evapotranspiration() + water_consumption_from_agricultural_production()


@cache('run')
def efficiency_score_sprinkler():
    """
    Real Name: b'Efficiency score sprinkler'
    Original Eqn: b'100 - 75'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 100 - 75


@cache('run')
def efficiency_score_surface():
    """
    Real Name: b'Efficiency score surface'
    Original Eqn: b'100 - 70'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 100 - 70


@cache('step')
def efficiency_sprinkler():
    """
    Real Name: b'Efficiency sprinkler'
    Original Eqn: b'Efficiency score sprinkler/Sum efficiency*Ini water demand per irrigated area'
    Units: b'(m*m*m)/(km*km)/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return efficiency_score_sprinkler() / sum_efficiency() * ini_water_demand_per_irrigated_area()


@cache('step')
def direct_use_of_agricultural_drainage():
    """
    Real Name: b'Direct use of agricultural drainage'
    Original Eqn: b'Recovered irrigation water*Direct use rate'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return recovered_irrigation_water() * direct_use_rate()


@cache('step')
def increase_potential_irrigated_land():
    """
    Real Name: b'Increase potential irrigated land'
    Original Eqn: b'IF THEN ELSE(Agricultural production shortage > 0 :AND: Potential irrigated land = Effective irrigated land\\\\ , Maximum annual irrigated land growth ,0)'
    Units: b'km*km/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        agricultural_production_shortage() > 0
        and potential_irrigated_land() == effective_irrigated_land(),
        maximum_annual_irrigated_land_growth(), 0)


@cache('run')
def average_water_consumption_per_kg_agricultural_production():
    """
    Real Name: b'Average water consumption per kg agricultural production'
    Original Eqn: b'0.126'
    Units: b'm*m*m/kg'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.126


@cache('step')
def water_demand_reduction():
    """
    Real Name: b'Water demand reduction'
    Original Eqn: b'IF THEN ELSE(:NOT: New water demand per irrigated area = Water demand per irrigated area\\\\ :AND: Water demand per irrigated area > Minimum water demand per irrigated area :AND: "Policy switch 1: water demand reduction"\\\\ =1, (Water demand per irrigated area-New water demand per irrigated area)/TIME STEP , 0 )'
    Units: b'm*m*m/(year*year*km*km)'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.if_then_else(
        not new_water_demand_per_irrigated_area() == water_demand_per_irrigated_area()
        and water_demand_per_irrigated_area() > minimum_water_demand_per_irrigated_area()
        and policy_switch_1_water_demand_reduction() == 1,
        (water_demand_per_irrigated_area() - new_water_demand_per_irrigated_area()) / time_step(),
        0)


@cache('step')
def potential_irrigated_land_localized_irrigated():
    """
    Real Name: b'Potential irrigated land localized irrigated'
    Original Eqn: b'INTEG ( -Change in area localized irrigated, Initial area localized irrigation)'
    Units: b'km*km'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_potential_irrigated_land_localized_irrigated()


@cache('step')
def potential_irrigated_land_sprinkler_irrigated():
    """
    Real Name: b'Potential irrigated land sprinkler irrigated'
    Original Eqn: b'INTEG ( -Change in area sprinkler irrigated, Initial area sprinkler irrigation)'
    Units: b'km*km'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_potential_irrigated_land_sprinkler_irrigated()


@cache('step')
def recovered_irrigation_water():
    """
    Real Name: b'Recovered irrigation water'
    Original Eqn: b'MAX(0,Water use for irrigation-Irrigated water loss)'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(0, water_use_for_irrigation() - irrigated_water_loss())


@cache('step')
def rel_localized_irrigated():
    """
    Real Name: b'Rel localized irrigated'
    Original Eqn: b'Potential irrigated land localized irrigated/Sum potential'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return potential_irrigated_land_localized_irrigated() / sum_potential()


@cache('step')
def rel_sprinkler_irrigated():
    """
    Real Name: b'Rel sprinkler irrigated'
    Original Eqn: b'Potential irrigated land sprinkler irrigated/Sum potential'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return potential_irrigated_land_sprinkler_irrigated() / sum_potential()


@cache('step')
def percentage_recovered():
    """
    Real Name: b'Percentage recovered'
    Original Eqn: b'Recovered irrigation water/Water use for irrigation *100'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return recovered_irrigation_water() / water_use_for_irrigation() * 100


@cache('step')
def efficiency_localized():
    """
    Real Name: b'Efficiency localized'
    Original Eqn: b'Efficiency score localized/Sum efficiency * Ini water demand per irrigated area'
    Units: b'(m*m*m)/(km*km)/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return efficiency_score_localized() / sum_efficiency() * ini_water_demand_per_irrigated_area()


@cache('run')
def efficiency_score_localized():
    """
    Real Name: b'Efficiency score localized'
    Original Eqn: b'100 - 85'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 100 - 85


@cache('step')
def water_use_for_irrigation():
    """
    Real Name: b'Water use for irrigation'
    Original Eqn: b'Effective irrigated land*Water demand per irrigated area'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return effective_irrigated_land() * water_demand_per_irrigated_area()


@cache('step')
def water_consumption_from_agricultural_production():
    """
    Real Name: b'Water consumption from agricultural production'
    Original Eqn: b'Agricultural production*Average water consumption per kg agricultural production'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return agricultural_production() * average_water_consumption_per_kg_agricultural_production()


@cache('step')
def evapotranspiration():
    """
    Real Name: b'Evapotranspiration'
    Original Eqn: b'Average evapotranspiration*Effective irrigated land'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return average_evapotranspiration() * effective_irrigated_land()


@cache('step')
def efficiency_surface():
    """
    Real Name: b'Efficiency surface'
    Original Eqn: b'Efficiency score surface/Sum efficiency*Ini water demand per irrigated area'
    Units: b'(m*m*m)/(km*km)/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return efficiency_score_surface() / sum_efficiency() * ini_water_demand_per_irrigated_area()


@cache('step')
def sum_efficiency():
    """
    Real Name: b'Sum efficiency'
    Original Eqn: b'Efficiency score localized*Initial percentage localized+(Efficiency score sprinkler)\\\\ *Inital percentage sprinkler+Efficiency score surface*Inital percentage surface'
    Units: b'Dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return efficiency_score_localized() * initial_percentage_localized() + (
        efficiency_score_sprinkler()
    ) * inital_percentage_sprinkler() + efficiency_score_surface() * inital_percentage_surface()


@cache('step')
def sum_potential():
    """
    Real Name: b'Sum potential'
    Original Eqn: b'Potential irrigated land localized irrigated+Potential irrigated land sprinkler irrigated\\\\ +Potential irrigated land surface irrigated'
    Units: b'km*km'
    Limits: (None, None)
    Type: component

    b''
    """
    return potential_irrigated_land_localized_irrigated(
    ) + potential_irrigated_land_sprinkler_irrigated(
    ) + potential_irrigated_land_surface_irrigated()


@cache('step')
def potential_irrigated_land_surface_irrigated():
    """
    Real Name: b'Potential irrigated land surface irrigated'
    Original Eqn: b'INTEG ( -Change in area surface irrigated, Initial area surface irrigation)'
    Units: b'km*km'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_potential_irrigated_land_surface_irrigated()


@cache('run')
def treated_municipal_wastewater():
    """
    Real Name: b'Treated municipal wastewater'
    Original Eqn: b'1.3 * 10^9'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1.3 * 10**9


@cache('step')
def irrigated_water_volume():
    """
    Real Name: b'Irrigated water volume'
    Original Eqn: b'INTEG ( Water use for irrigation-Irrigated water loss-Recovered irrigation water, Ini irrigated water volume)'
    Units: b'm*m*m'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_irrigated_water_volume()


@cache('step')
def water_supply_for_irrigation():
    """
    Real Name: b'Water supply for irrigation'
    Original Eqn: b'INTEG ( Water allocated agriculture-Water use for irrigation, Ini water supply irrigation)'
    Units: b'm*m*m'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_water_supply_for_irrigation()


@cache('run')
def desalinated_water_produced():
    """
    Real Name: b'Desalinated water produced'
    Original Eqn: b'0.2 * 10^9'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.2 * 10**9


@cache('step')
def potential_irrigated_land():
    """
    Real Name: b'Potential irrigated land'
    Original Eqn: b'INTEG ( Increase potential irrigated land-Decrease potential irrigated land, Ini potential irrigated land)'
    Units: b'km * km'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_potential_irrigated_land()


@cache('step')
def initial_area_localized_irrigation():
    """
    Real Name: b'Initial area localized irrigation'
    Original Eqn: b'INITIAL( 0.115*38230)'
    Units: b'km*km'
    Limits: (None, None)
    Type: component

    b''
    """
    return _initial_011538230()


@cache('step')
def initial_area_sprinkler_irrigation():
    """
    Real Name: b'Initial area sprinkler irrigation'
    Original Eqn: b'INITIAL( 0.115*38230)'
    Units: b'km*km'
    Limits: (None, None)
    Type: component

    b''
    """
    return _initial_011538230()


@cache('step')
def initial_area_surface_irrigation():
    """
    Real Name: b'Initial area surface irrigation'
    Original Eqn: b'INITIAL( 0.77*38230)'
    Units: b'km*km'
    Limits: (None, None)
    Type: component

    b''
    """
    return _initial_07738230()


@cache('step')
def ini_water_egypt():
    """
    Real Name: b'Ini water Egypt'
    Original Eqn: b'INITIAL( 77.5 * 10^9)'
    Units: b'm*m*m'
    Limits: (None, None)
    Type: component

    b''
    """
    return _initial_775109()


@cache('step')
def water_allocated_agriculture():
    """
    Real Name: b'Water allocated agriculture'
    Original Eqn: b'Usable water volume Egypt*Water allocation rate agriculture'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return usable_water_volume_egypt() * water_allocation_rate_agriculture()


@cache('step')
def usable_water_volume_egypt():
    """
    Real Name: b'Usable water volume Egypt'
    Original Eqn: b'INTEG ( Additional annual water resources+Annual Nile waterflow to Egypt-Water allocated agriculture\\\\ -Water allocated other sectors, Ini water Egypt)'
    Units: b'm*m*m'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_usable_water_volume_egypt()


@cache('run')
def annual_external_renewable_groundwater():
    """
    Real Name: b'Annual external renewable groundwater'
    Original Eqn: b'1000 * 10^6'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1000 * 10**6


@cache('step')
def water_allocated_other_sectors():
    """
    Real Name: b'Water allocated other sectors'
    Original Eqn: b'Usable water volume Egypt * (1-Water allocation rate agriculture)'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return usable_water_volume_egypt() * (1 - water_allocation_rate_agriculture())


@cache('run')
def maximum_annual_irrigated_land_decrease():
    """
    Real Name: b'Maximum annual irrigated land decrease'
    Original Eqn: b'355'
    Units: b'km*km/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 355


@cache('run')
def maximum_annual_irrigated_land_growth():
    """
    Real Name: b'Maximum annual irrigated land growth'
    Original Eqn: b'355'
    Units: b'km*km/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 355


@cache('run')
def average_agricultural_production_per_irrigated_land():
    """
    Real Name: b'Average agricultural production per irrigated land'
    Original Eqn: b'1.3488e+06'
    Units: b'kg/(km*km)/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1.3488e+06


@cache('step')
def agricultural_water_shortage():
    """
    Real Name: b'Agricultural water shortage'
    Original Eqn: b'MAX(0 , Agricultural production shortage /Average agricultural production per irrigated land\\\\ * Water demand per irrigated area )'
    Units: b'm*m*m/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(
        0,
        agricultural_production_shortage() / average_agricultural_production_per_irrigated_land() *
        water_demand_per_irrigated_area())


@cache('run')
def average_food_demand_per_capita():
    """
    Real Name: b'Average food demand per capita'
    Original Eqn: b'465'
    Units: b'kg/year/person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 465


@cache('run')
def birth_rate_egypt():
    """
    Real Name: b'Birth rate Egypt'
    Original Eqn: b'27.2/1000'
    Units: b'1/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 27.2 / 1000


@cache('run')
def death_rate_egypt():
    """
    Real Name: b'Death rate Egypt'
    Original Eqn: b'4.4/1000'
    Units: b'1/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 4.4 / 1000


@cache('step')
def agricultural_food_demand():
    """
    Real Name: b'Agricultural food demand'
    Original Eqn: b'Population Egypt * Average food demand per capita'
    Units: b'kg/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return population_egypt() * average_food_demand_per_capita()


@cache('step')
def ini_potential_irrigated_land():
    """
    Real Name: b'Ini potential irrigated land'
    Original Eqn: b'INITIAL( 38230)'
    Units: b'km*km'
    Limits: (None, None)
    Type: component

    b''
    """
    return _initial_38230()


@cache('step')
def ini_irrigated_water_volume():
    """
    Real Name: b'Ini irrigated water volume'
    Original Eqn: b'INITIAL( 61.1168 *10^9)'
    Units: b'm*m*m'
    Limits: (None, None)
    Type: component

    b''
    """
    return _initial_611168109()


@cache('step')
def ini_population_egypt():
    """
    Real Name: b'Ini population Egypt'
    Original Eqn: b'INITIAL( 9.44471e+07)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _initial_944471e07()


@cache('step')
def ini_water_demand_per_irrigated_area():
    """
    Real Name: b'Ini water demand per irrigated area'
    Original Eqn: b'INITIAL( 1.6 *10^6)'
    Units: b'(m*m*m)/(km*km)/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return _initial_16106()


@cache('step')
def ini_water_supply_irrigation():
    """
    Real Name: b'Ini water supply irrigation'
    Original Eqn: b'INITIAL( 61.35 * 10^9)'
    Units: b'm*m*m'
    Limits: (None, None)
    Type: component

    b''
    """
    return _initial_6135109()


@cache('run')
def average_evapotranspiration():
    """
    Real Name: b'Average evapotranspiration'
    Original Eqn: b'1.07156e+06'
    Units: b'(m*m*m)/(km*km)/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1.07156e+06


@cache('step')
def population_decrease():
    """
    Real Name: b'Population decrease'
    Original Eqn: b'Population Egypt * Death rate Egypt'
    Units: b'person/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return population_egypt() * death_rate_egypt()


@cache('step')
def population_egypt():
    """
    Real Name: b'Population Egypt'
    Original Eqn: b'INTEG ( Population increase-Population decrease, Ini population Egypt)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_population_egypt()


@cache('step')
def population_increase():
    """
    Real Name: b'Population increase'
    Original Eqn: b'Population Egypt * Birth rate Egypt'
    Units: b'person/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return population_egypt() * birth_rate_egypt()


@cache('run')
def water_allocation_rate_agriculture():
    """
    Real Name: b'Water allocation rate agriculture'
    Original Eqn: b'0.79'
    Units: b'1/year'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.79


@cache('step')
def water_demand_per_irrigated_area():
    """
    Real Name: b'Water demand per irrigated area'
    Original Eqn: b'INTEG ( -Water demand reduction, Ini water demand per irrigated area)'
    Units: b'(m*m*m)/(km*km)/year'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_water_demand_per_irrigated_area()


@cache('run')
def final_time():
    """
    Real Name: b'FINAL TIME'
    Original Eqn: b'2050'
    Units: b'year'
    Limits: (None, None)
    Type: constant

    b'The final time for the simulation.'
    """
    return 2050


@cache('run')
def initial_time():
    """
    Real Name: b'INITIAL TIME'
    Original Eqn: b'2016'
    Units: b'year'
    Limits: (None, None)
    Type: constant

    b'The initial time for the simulation.'
    """
    return 2016


@cache('run')
def saveper():
    """
    Real Name: b'SAVEPER'
    Original Eqn: b'1'
    Units: b'year'
    Limits: (0.0, None)
    Type: constant

    b'The frequency with which output is stored.'
    """
    return 1


@cache('run')
def time_step():
    """
    Real Name: b'TIME STEP'
    Original Eqn: b'0.03125'
    Units: b'year'
    Limits: (0.0, None)
    Type: constant

    b'The time step for the simulation.'
    """
    return 0.03125


_initial_0115 = functions.Initial(lambda: 0.115)

_initial_077 = functions.Initial(lambda: 0.77)

_integ_potential_irrigated_land_localized_irrigated = functions.Integ(
    lambda: -change_in_area_localized_irrigated(), lambda: initial_area_localized_irrigation())

_integ_potential_irrigated_land_sprinkler_irrigated = functions.Integ(
    lambda: -change_in_area_sprinkler_irrigated(), lambda: initial_area_sprinkler_irrigation())

_integ_potential_irrigated_land_surface_irrigated = functions.Integ(
    lambda: -change_in_area_surface_irrigated(), lambda: initial_area_surface_irrigation())

_integ_irrigated_water_volume = functions.Integ(
    lambda: water_use_for_irrigation() - irrigated_water_loss() - recovered_irrigation_water(),
    lambda: ini_irrigated_water_volume())

_integ_water_supply_for_irrigation = functions.Integ(
    lambda: water_allocated_agriculture() - water_use_for_irrigation(),
    lambda: ini_water_supply_irrigation())

_integ_potential_irrigated_land = functions.Integ(
    lambda: increase_potential_irrigated_land() - decrease_potential_irrigated_land(),
    lambda: ini_potential_irrigated_land())

_initial_011538230 = functions.Initial(lambda: 0.115 * 38230)

_initial_07738230 = functions.Initial(lambda: 0.77 * 38230)

_initial_775109 = functions.Initial(lambda: 77.5 * 10**9)

_integ_usable_water_volume_egypt = functions.Integ(
    lambda: additional_annual_water_resources() + annual_nile_waterflow_to_egypt() -
    water_allocated_agriculture() - water_allocated_other_sectors(), lambda: ini_water_egypt())

_initial_38230 = functions.Initial(lambda: 38230)

_initial_611168109 = functions.Initial(lambda: 61.1168 * 10**9)

_initial_944471e07 = functions.Initial(lambda: 9.44471e+07)

_initial_16106 = functions.Initial(lambda: 1.6 * 10**6)

_initial_6135109 = functions.Initial(lambda: 61.35 * 10**9)

_integ_population_egypt = functions.Integ(lambda: population_increase() - population_decrease(),
                                          lambda: ini_population_egypt())

_integ_water_demand_per_irrigated_area = functions.Integ(
    lambda: -water_demand_reduction(), lambda: ini_water_demand_per_irrigated_area())
