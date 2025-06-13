# -*- coding: utf-8 -*-
"""
Parameters and information for stimulation sties.

:Author: Jessie R. Liu
:Copyright: Copyright (c) 2021, Jessie R. Liu, All rights reserved.
"""

# these are 1-indexed
stim_pairs = {
    'EC260': {
        'FG23-FG14': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : True,
            'motor_deficit'           : False,
            'research_elecs'          : [77, 43],
            'center_research_elec'    : 60
        },
        'FG22-FG23': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'research_elecs'          : [75, 77],
            'center_research_elec'    : 76
        },
        'FG30-FG23': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'higher_amp_motor_deficit': True,
            'research_elecs'          : [107, 77],
            'center_research_elec'    : 92
        },
        'FG23-FG15': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'higher_amp_motor_deficit': True,
            'research_elecs'          : [77, 45],
            'center_research_elec'    : 61
        },
        'FG24-FG15': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'other_deficit'           : 'right hand numbness',
            'research_elecs'          : [79, 45],
            'center_research_elec'    : 62
        },
        'FG11-FG13': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'higher_amp_motor_deficit': False,
            'research_elecs'          : [37, 41],
            'center_research_elec'    : 39
        },
        'TG31-TG23': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'higher_amp_motor_deficit': False,
            'other_deficit'           : 'perceptual',
            'research_elecs'          : [237, 205],
            'center_research_elec'    : 221
        },
        'FG31-FG23': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'higher_amp_motor_deficit': True,
            'research_elecs'          : [109, 77],
            'center_research_elec'    : 93
        },
        'FG19-FG20': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'higher_amp_motor_deficit': False,
            'research_elecs'          : [69, 71],
            'center_research_elec'    : 70
        },
        'FG26-FG18': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'higher_amp_motor_deficit': False,
            'research_elecs'          : [99, 67],
            'center_research_elec'    : 83
        },
        'FG26-FG19': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'higher_amp_motor_deficit': False,
            'research_elecs'          : [99, 69],
            'center_research_elec'    : 84
        },
        'FG11-FG12': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'higher_amp_motor_deficit': False,
            'other_deficit'           : 'visual perceptual',
            'research_elecs'          : [37, 39],
            'center_research_elec'    : 38
        },
        'FG15-FG7': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : True,
            'higher_amp_motor_deficit': True,
            'research_elecs'          : [45, 13],
            'center_research_elec'    : 29
        },
        'TG32-TG24': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'higher_amp_motor_deficit': False,
            'other_deficit'           : 'perceptual',
            'research_elecs'          : [239, 207],
            'center_research_elec'    : 223
        }
    },
    'EC267': {
        'PG27-PG28': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : True,
            'research_elecs'          : [229, 231],
            'center_research_elec'    : 230
        },
        'PG28-PG29': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : True,
            'motor_deficit'           : False,
            'higher_amp_motor_deficit': True,
            'research_elecs'          : [231, 233],
            'center_research_elec'    : 232
        },
        'AG18-AG11': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'research_elecs'          : [67, 37],
            'center_research_elec'    : 52
        },
        'AG18-AG27': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'research_elecs'          : [67, 101],
            'center_research_elec'    : 84
        }
    },
    'EC276': {
        'PG11-PG13': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : True,
            'research_elecs'          : [37, 41],
            'center_research_elec'    : 39
        },
        'PG12-PG14': {
            'inconsistent_seq_deficit' : False,
            'seq_deficit'              : True,
            'motor_deficit'            : False,
            'higher_amp_motor_deficit' : True,
            'motor_deficit_description': 'spontaneous vocalization',
            'research_elecs'           : [39, 43],
            'center_research_elec'     : 41
        },
        'PG19-PG12': {
            'inconsistent_seq_deficit' : False,
            'seq_deficit'              : True,
            'motor_deficit'            : False,
            'higher_amp_motor_deficit' : True,
            'motor_deficit_description': 'spontaneous vocalization',
            'research_elecs'           : [69, 39],
            'center_research_elec'     : 54
        }
    },
    'EC282': {
        'FG1-FG2'  : {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : True,
            'research_elecs'          : [129, 130],
            'center_research_elec'    : 'interpolate'
        },
        'FG16-FG17': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : True,
            'motor_deficit'           : False,
            'higher_amp_motor_deficit': True,
            'research_elecs'          : [144, 145],
            'center_research_elec'    : 'interpolate'
        },
        'FG17-FG12': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : True,
            'motor_deficit'           : False,
            'higher_amp_motor_deficit': True,
            'research_elecs'          : [145, 140],
            'center_research_elec'    : 'interpolate'
        },
        'FG8-FG9'  : {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'other_deficit'           : 'head tingle',
            'research_elecs'          : [136, 137],
            'center_research_elec'    : 'interpolate'
        }
    },
    'EC289': {
        'AG3-AG4'  : {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : True,
            'motor_deficit'           : False,
            'higher_amp_motor_deficit': True,
            'research_elecs'          : [5, 7],
            'center_research_elec'    : 6
        },
        'AG20-AG21': {
            'inconsistent_seq_deficit': False,
            'seq_deficit'             : False,
            'motor_deficit'           : False,
            'higher_amp_motor_deficit': False,
            'research_elecs'          : [71, 73],
            'center_research_elec'    : 72
        }
    }
}
