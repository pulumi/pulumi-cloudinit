"""A Python Pulumi program"""

import pulumi
import pulumi_cloudinit as cloudinit

datasource_config = cloudinit.get_config(base64_encode=False,
                                         gzip=False,
                                         parts=[cloudinit.GetConfigPartArgs(
                                             content="baz",
                                             content_type="text/x-shellscript",
                                             filename="foobar.sh",
                                         )])

pulumi.export("ds_conf", datasource_config.rendered)

resource_config = cloudinit.Config("resource", base64_encode=False,
                                   gzip=False,
                                   parts=[cloudinit.GetConfigPartArgs(
                                       content="baz",
                                       content_type="text/x-shellscript",
                                       filename="foobar.sh",
                                   )])

pulumi.export("resource_conf", resource_config.rendered)
