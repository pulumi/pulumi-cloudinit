// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudInit.Inputs
{

    public sealed class ConfigPartGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Body content for the part.
        /// </summary>
        [Input("content", required: true)]
        public Input<string> Content { get; set; } = null!;

        /// <summary>
        /// A MIME-style content type to report in the header for the part. Defaults to `text/plain`
        /// </summary>
        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        /// <summary>
        /// A filename to report in the header for the part.
        /// </summary>
        [Input("filename")]
        public Input<string>? Filename { get; set; }

        /// <summary>
        /// A value for the `X-Merge-Type` header of the part, to control [cloud-init merging behavior](https://cloudinit.readthedocs.io/en/latest/reference/merging.html).
        /// </summary>
        [Input("mergeType")]
        public Input<string>? MergeType { get; set; }

        public ConfigPartGetArgs()
        {
        }
        public static new ConfigPartGetArgs Empty => new ConfigPartGetArgs();
    }
}
