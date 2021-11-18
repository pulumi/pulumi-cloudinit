// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi.Utilities;

namespace Pulumi.CloudInit
{
    public static class GetConfig
    {
        /// <summary>
        /// Renders a [multipart MIME configuration](https://cloudinit.readthedocs.io/en/latest/topics/format.html#mime-multi-part-archive)
        /// for use with [cloud-init](https://cloudinit.readthedocs.io/).
        /// 
        /// Cloud-init is a commonly-used startup configuration utility for cloud compute
        /// instances. It accepts configuration via provider-specific user data mechanisms,
        /// such as `user_data` for Amazon EC2 instances. Multipart MIME is one of the
        /// data formats it accepts. For more information, see
        /// [User-Data Formats](https://cloudinit.readthedocs.io/en/latest/topics/format.html)
        /// in the cloud-init manual.
        /// 
        /// This is not a generalized utility for producing multipart MIME messages. Its
        /// featureset is specialized for the features of cloud-init.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using CloudInit = Pulumi.CloudInit;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var foo = Output.Create(CloudInit.GetConfig.InvokeAsync(new CloudInit.GetConfigArgs
        ///         {
        ///             Base64Encode = false,
        ///             Gzip = false,
        ///             Parts = 
        ///             {
        ///                 new CloudInit.Inputs.GetConfigPartArgs
        ///                 {
        ///                     Content = "baz",
        ///                     ContentType = "text/x-shellscript",
        ///                     Filename = "foobar.sh",
        ///                 },
        ///             },
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetConfigResult> InvokeAsync(GetConfigArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetConfigResult>("cloudinit:index/getConfig:getConfig", args ?? new GetConfigArgs(), options.WithVersion());

        /// <summary>
        /// Renders a [multipart MIME configuration](https://cloudinit.readthedocs.io/en/latest/topics/format.html#mime-multi-part-archive)
        /// for use with [cloud-init](https://cloudinit.readthedocs.io/).
        /// 
        /// Cloud-init is a commonly-used startup configuration utility for cloud compute
        /// instances. It accepts configuration via provider-specific user data mechanisms,
        /// such as `user_data` for Amazon EC2 instances. Multipart MIME is one of the
        /// data formats it accepts. For more information, see
        /// [User-Data Formats](https://cloudinit.readthedocs.io/en/latest/topics/format.html)
        /// in the cloud-init manual.
        /// 
        /// This is not a generalized utility for producing multipart MIME messages. Its
        /// featureset is specialized for the features of cloud-init.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using CloudInit = Pulumi.CloudInit;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var foo = Output.Create(CloudInit.GetConfig.InvokeAsync(new CloudInit.GetConfigArgs
        ///         {
        ///             Base64Encode = false,
        ///             Gzip = false,
        ///             Parts = 
        ///             {
        ///                 new CloudInit.Inputs.GetConfigPartArgs
        ///                 {
        ///                     Content = "baz",
        ///                     ContentType = "text/x-shellscript",
        ///                     Filename = "foobar.sh",
        ///                 },
        ///             },
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetConfigResult> Invoke(GetConfigInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetConfigResult>("cloudinit:index/getConfig:getConfig", args ?? new GetConfigInvokeArgs(), options.WithVersion());
    }


    public sealed class GetConfigArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Base64 encoding of the rendered output. Defaults to `true`,
        /// and cannot be disabled if `gzip` is `true`.
        /// </summary>
        [Input("base64Encode")]
        public bool? Base64Encode { get; set; }

        /// <summary>
        /// Define the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
        /// </summary>
        [Input("boundary")]
        public string? Boundary { get; set; }

        /// <summary>
        /// Specify whether or not to gzip the rendered output. Defaults to `true`.
        /// </summary>
        [Input("gzip")]
        public bool? Gzip { get; set; }

        [Input("parts", required: true)]
        private List<Inputs.GetConfigPartArgs>? _parts;

        /// <summary>
        /// A nested block type which adds a file to the generated
        /// cloud-init configuration. Use multiple `part` blocks to specify multiple
        /// files, which will be included in order of declaration in the final MIME
        /// document.
        /// </summary>
        public List<Inputs.GetConfigPartArgs> Parts
        {
            get => _parts ?? (_parts = new List<Inputs.GetConfigPartArgs>());
            set => _parts = value;
        }

        public GetConfigArgs()
        {
        }
    }

    public sealed class GetConfigInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Base64 encoding of the rendered output. Defaults to `true`,
        /// and cannot be disabled if `gzip` is `true`.
        /// </summary>
        [Input("base64Encode")]
        public Input<bool>? Base64Encode { get; set; }

        /// <summary>
        /// Define the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
        /// </summary>
        [Input("boundary")]
        public Input<string>? Boundary { get; set; }

        /// <summary>
        /// Specify whether or not to gzip the rendered output. Defaults to `true`.
        /// </summary>
        [Input("gzip")]
        public Input<bool>? Gzip { get; set; }

        [Input("parts", required: true)]
        private InputList<Inputs.GetConfigPartInputArgs>? _parts;

        /// <summary>
        /// A nested block type which adds a file to the generated
        /// cloud-init configuration. Use multiple `part` blocks to specify multiple
        /// files, which will be included in order of declaration in the final MIME
        /// document.
        /// </summary>
        public InputList<Inputs.GetConfigPartInputArgs> Parts
        {
            get => _parts ?? (_parts = new InputList<Inputs.GetConfigPartInputArgs>());
            set => _parts = value;
        }

        public GetConfigInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetConfigResult
    {
        public readonly bool? Base64Encode;
        public readonly string? Boundary;
        public readonly bool? Gzip;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.GetConfigPartResult> Parts;
        /// <summary>
        /// The final rendered multi-part cloud-init config.
        /// </summary>
        public readonly string Rendered;

        [OutputConstructor]
        private GetConfigResult(
            bool? base64Encode,

            string? boundary,

            bool? gzip,

            string id,

            ImmutableArray<Outputs.GetConfigPartResult> parts,

            string rendered)
        {
            Base64Encode = base64Encode;
            Boundary = boundary;
            Gzip = gzip;
            Id = id;
            Parts = parts;
            Rendered = rendered;
        }
    }
}
