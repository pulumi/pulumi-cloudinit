// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudInit.Inputs
{

    public sealed class ConfigPartArgs : global::Pulumi.ResourceArgs
    {
        [Input("content", required: true)]
        public Input<string> Content { get; set; } = null!;

        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        [Input("filename")]
        public Input<string>? Filename { get; set; }

        [Input("mergeType")]
        public Input<string>? MergeType { get; set; }

        public ConfigPartArgs()
        {
        }
        public static new ConfigPartArgs Empty => new ConfigPartArgs();
    }
}
