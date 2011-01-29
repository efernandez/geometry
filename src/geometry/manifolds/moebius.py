from . import DifferentiableManifold 

class Moebius(DifferentiableManifold):
    ''' The Moebius strip -- still to be implemented. '''
    
    def __init__(self, n):
        self.n = n

    def belongs_(self, a):
        assert False

    def distance_(self, a, b):
        assert False

    def logmap_(self, a, b): 
        assert False

    def expmap_(self, a, vel): 
        assert False

    def project_ts_(self, base, vx): 
        assert False
    
    def sample_uniform(self):
        assert False
    
    def normalize(self, x):
        assert False

