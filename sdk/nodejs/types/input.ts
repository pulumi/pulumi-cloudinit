// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";

export interface ConfigPart {
    content: pulumi.Input<string>;
    contentType?: pulumi.Input<string>;
    filename?: pulumi.Input<string>;
    mergeType?: pulumi.Input<string>;
}

export interface GetConfigPart {
    /**
     * Body content for the part.
     */
    content: string;
    /**
     * A MIME-style content type to report in the header for the part.
     */
    contentType?: string;
    /**
     * A filename to report in the header for the part.
     */
    filename?: string;
    /**
     * A value for the `X-Merge-Type` header of the part,
     * to control [cloud-init merging behavior](https://cloudinit.readthedocs.io/en/latest/topics/merging.html).
     */
    mergeType?: string;
}
