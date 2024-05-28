import numpy as np
import control as ctrl

def define_system():
    m_s = 234
    m_us = 43
    k_s = 26000
    k_us = 100000
    b_s = 1544
    b_us = 0

    AA = np.array([
        [0, 1, 0, -1],
        [-k_s/m_s, -b_s/m_s, 0, b_s/m_s],
        [0, 0, 0, 1],
        [k_s/m_us, (b_s)/m_us, -k_us/m_us, (-b_s-b_us)/m_us]
    ])

    B = np.array([
        [0, 1/m_s, 0, -1/m_us]
    ]).T

    C = np.array([[1, 0, 0, 0],
                  [0, 1, 0, 0]])

    D = np.array([[0],
                  [0]])

    sys = ctrl.ss(AA, B, C, D)
    dt = 1/10
    sys_discrete = ctrl.c2d(sys, dt, method='zoh')

    return sys_discrete.A, sys_discrete.B
