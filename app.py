#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk.aws_cdk_stack import AwsCdkStack


app = cdk.App()
var = "testing"
AwsCdkStack(app, "AwsCdkStack")

app.synth()
