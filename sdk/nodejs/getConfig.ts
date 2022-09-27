// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Renders a [multipart MIME configuration](https://cloudinit.readthedocs.io/en/latest/topics/format.html#mime-multi-part-archive)
 * for use with [cloud-init](https://cloudinit.readthedocs.io/).
 *
 * Cloud-init is a commonly-used startup configuration utility for cloud compute
 * instances. It accepts configuration via provider-specific user data mechanisms,
 * such as `userData` for Amazon EC2 instances. Multipart MIME is one of the
 * data formats it accepts. For more information, see
 * [User-Data Formats](https://cloudinit.readthedocs.io/en/latest/topics/format.html)
 * in the cloud-init manual.
 *
 * This is not a generalized utility for producing multipart MIME messages. Its
 * featureset is specialized for the features of cloud-init.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as cloudinit from "@pulumi/cloudinit";
 *
 * const foo = pulumi.output(cloudinit.getConfig({
 *     base64Encode: false,
 *     gzip: false,
 *     parts: [{
 *         content: "baz",
 *         contentType: "text/x-shellscript",
 *         filename: "foobar.sh",
 *     }],
 * }));
 * ```
 */
export function getConfig(args: GetConfigArgs, opts?: pulumi.InvokeOptions): Promise<GetConfigResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("cloudinit:index/getConfig:getConfig", {
        "base64Encode": args.base64Encode,
        "boundary": args.boundary,
        "gzip": args.gzip,
        "parts": args.parts,
    }, opts);
}

/**
 * A collection of arguments for invoking getConfig.
 */
export interface GetConfigArgs {
    /**
     * Base64 encoding of the rendered output. Defaults to `true`,
     * and cannot be disabled if `gzip` is `true`.
     */
    base64Encode?: boolean;
    /**
     * Define the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
     */
    boundary?: string;
    /**
     * Specify whether or not to gzip the rendered output. Defaults to `true`.
     */
    gzip?: boolean;
    /**
     * A nested block type which adds a file to the generated
     * cloud-init configuration. Use multiple `part` blocks to specify multiple
     * files, which will be included in order of declaration in the final MIME
     * document.
     */
    parts: inputs.GetConfigPart[];
}

/**
 * A collection of values returned by getConfig.
 */
export interface GetConfigResult {
    readonly base64Encode?: boolean;
    readonly boundary?: string;
    readonly gzip?: boolean;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly parts: outputs.GetConfigPart[];
    /**
     * The final rendered multi-part cloud-init config.
     */
    readonly rendered: string;
}

export function getConfigOutput(args: GetConfigOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetConfigResult> {
    return pulumi.output(args).apply(a => getConfig(a, opts))
}

/**
 * A collection of arguments for invoking getConfig.
 */
export interface GetConfigOutputArgs {
    /**
     * Base64 encoding of the rendered output. Defaults to `true`,
     * and cannot be disabled if `gzip` is `true`.
     */
    base64Encode?: pulumi.Input<boolean>;
    /**
     * Define the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
     */
    boundary?: pulumi.Input<string>;
    /**
     * Specify whether or not to gzip the rendered output. Defaults to `true`.
     */
    gzip?: pulumi.Input<boolean>;
    /**
     * A nested block type which adds a file to the generated
     * cloud-init configuration. Use multiple `part` blocks to specify multiple
     * files, which will be included in order of declaration in the final MIME
     * document.
     */
    parts: pulumi.Input<pulumi.Input<inputs.GetConfigPartArgs>[]>;
}
