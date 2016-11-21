# Copyright (C) 2015 UCSC Computational Genomics Lab
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
SSHs into the toil appliance container running on the leader of the cluster
"""
import logging
from toil import version
from toil.lib.bioio import getBasicOptionParser, parseBasicOptions, setLoggingFromOptions
from toil.provisioners import Cluster

logger = logging.getLogger( __name__ )


def main():
    parser = getBasicOptionParser()
    parser.add_argument("--version", action='version', version=version)
    parser.add_argument('-p', "--provisioner", dest='provisioner', choices=['aws'], required=True,
                        help="The provisioner for cluster auto-scaling. Only aws is currently"
                             "supported")
    parser.add_argument("clusterName", help="The name that the cluster will be identifiable by. "
                                            "Must be lowercase and may not contain the '_' "
                                            "character.")
    config = parseBasicOptions(parser)
    setLoggingFromOptions(config)
    cluster = Cluster(provisioner=config.provisioner, clusterName=config.clusterName)
    cluster.sshCluster()
