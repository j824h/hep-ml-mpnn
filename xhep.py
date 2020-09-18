# Independent implementation of xhep.Vec4

import numpy as np

class Vec4:
    def __init__(self, px, py, pz, E):
        self.px = px
        self.py = py
        self.pz = pz
        self.E = E

        pt_squared = px ** 2 + py ** 2
        self.pt = np.sqrt(pt_squared)
        
        p_space_squared = pt_squared + pz ** 2
        self.p_space = np.sqrt(p_space_squared)

        m_squared = E ** 2 - p_space_squared
        if m_squared < 0:
            raise ValueError("The values define spacelike vector")
        self.m = np.sqrt(m_squared)

    @staticmethod
    def delta_R_rapidity(p1, p2):
        eta1 = np.arctanh(p1.pt/p1.p_space)
        eta2 = np.arctanh(p2.pt/p2.p_space)
        delta_eta = eta1 - eta2

        cos_delta_phi = np.dot((p1.px, p1.py), (p2.px, p2.py))/(p1.pt * p2.pt)
        abs_delta_phi = np.arccos(cos_delta_phi)

        return np.hypot(delta_eta, abs_delta_phi)
