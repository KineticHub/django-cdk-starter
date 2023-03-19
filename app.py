#!/usr/bin/env python3
import os
import aws_cdk as cdk
from aws_cdk import (
    Environment,
)
from infrastructure.pipeline_stack import DjangoAppPipelineStack


app = cdk.App()
pipeline = DjangoAppPipelineStack(
    app,
    "DjangoAppPipeline",
    repository="KineticHub/justforfam",
    branch="cdk",
    ssm_gh_connection_param="/Github/Connection",
    env=Environment(
        account=os.getenv('CDK_DEFAULT_ACCOUNT'),
        region=os.getenv('CDK_DEFAULT_REGION')
    ),
)
app.synth()
