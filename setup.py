# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

setup(
    name="proto-breaking-change-detector",
    version="0.1",
    py_modules=["proto-breaking-change-detector"],
    install_requires=[
        "Click",
        "protobuf >= 3.12.0",
        "google-api-core >= 1.17.0",
        "googleapis-common-protos >= 1.6.0",
        "grpcio-tools >= 1.37.0",
    ],
    entry_points="""
        [console_scripts]
        proto-breaking-change-detector=src.cli.detect:detect
    """,
)
