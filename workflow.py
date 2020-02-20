from kfp import dsl
from mlrun import mount_v3io

artifacts_path = './'
funcs = {}

def init_functions(functions: dict, params=None, secrets=None):
    pass

@dsl.pipeline(
    name='demo project', description='Shows how to use mlrun project.'
)
def kfpipeline(p1=3):
    # first step build the function container
    builder = funcs['tstfunc'].deploy_step(with_mlrun=False)

    # first step
    s1 = funcs['tstfunc'].as_step(name='step-one', handler='my_func',
         image=builder.outputs['image'],
         params={'p1': p1}, out_path=artifacts_path)

    # todo: 2nd step
