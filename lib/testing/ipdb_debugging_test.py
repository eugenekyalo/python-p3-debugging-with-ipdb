import ipdb

from ipdb_debugging import plus_two

class TestIpdbDebugging:
    '''ipdb_debugging.py'''
    
    def test_adds_two(self):
        '''adds_two() adds 2 to input arg and returns sum.'''
        # Add the following line where you want to start debugging
        ipdb.set_trace()
        assert plus_two(3) == 5
