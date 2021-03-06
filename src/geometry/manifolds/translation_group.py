from . import MatrixLieGroup, R, tran, DifferentiableManifold
from .. import (assert_allclose, pose_from_rotation_translation,
    rotation_translation_from_pose, extract_pieces)

import numpy as np
from contracts import contract

__all__ = ['Tran']


class Tran(MatrixLieGroup):
    ''' 
        The translation subgroup of SE(n). 
    '''

    @contract(n='1|2|3')
    def __init__(self, n):
        algebra = tran[n]
        MatrixLieGroup.__init__(self, n=n + 1, algebra=algebra, dimension=n)
        self.En = R[n]
        DifferentiableManifold.isomorphism(self, algebra,
                            self.algebra_from_group,
                            self.group_from_algebra,
                            itype='lie')

    def __repr__(self):
        # return 'Tran(%s)' % (self.n - 1)
        return 'Tr%s' % (self.n - 1)

    def belongs(self, x):
        # TODO: explicit
        R, t, zero, one = extract_pieces(x)  # @UnusedVariable
        assert_allclose(R, np.eye(self.n - 1))
        assert_allclose(zero, 0, err_msg='I expect the lower row to be 0.')
        assert_allclose(one, 1, err_msg='Bottom-right must be 1.')

    @contract(returns='belongs')
    def sample_uniform(self):
        t = self.En.sample_uniform()
        return pose_from_rotation_translation(np.eye(self.n - 1), t)

    def friendly(self, a):
        t = rotation_translation_from_pose(a)[1]
        return 'Tran(%s)' % (self.En.friendly(t))

    def logmap(self, base, p):
        return base, p - base

    def expmap(self, bv):
        base, vel = bv
        return base + vel

    def algebra_from_group(self, g):
        a = np.zeros((self.n, self.n))
        a[:-1, -1] = g[:-1, -1]
        return a

    def group_from_algebra(self, a):
        g = np.eye(self.n)
        g[:-1, -1] = a[:-1, -1]
        return g

    def interesting_points(self):
        points = []
        for t in self.En.interesting_points():
            p = pose_from_rotation_translation(np.eye(self.n - 1), t)
            points.append(p)

        return points
