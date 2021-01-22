// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudInit.Inputs
{

    public sealed class GetConfigPartArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Body content for the part.
        /// </summary>
        [Input("content", required: true)]
        public string Content { get; set; } = null!;

        /// <summary>
        /// A MIME-style content type to report in the header for the part.
        /// </summary>
        [Input("contentType")]
        public string? ContentType { get; set; }

        /// <summary>
        /// A filename to report in the header for the part.
        /// </summary>
        [Input("filename")]
        public string? Filename { get; set; }

        /// <summary>
        /// A value for the `X-Merge-Type` header of the part,
        /// to control [cloud-init merging behavior](https://cloudinit.readthedocs.io/en/latest/topics/merging.html).
        /// </summary>
        [Input("mergeType")]
        public string? MergeType { get; set; }

        public GetConfigPartArgs()
        {
        }
    }
}
