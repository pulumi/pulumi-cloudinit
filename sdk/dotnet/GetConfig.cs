// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudInit
{
    public static class GetConfig
    {
        /// <summary>
        /// Renders a [multi-part MIME configuration](https://cloudinit.readthedocs.io/en/latest/explanation/format.html#mime-multi-part-archive) for use with [cloud-init](https://cloudinit.readthedocs.io/en/latest/).
        /// 
        /// Cloud-init is a commonly-used startup configuration utility for cloud compute instances. It accepts configuration via provider-specific user data mechanisms, such as `user_data` for Amazon EC2 instances. Multi-part MIME is one of the data formats it accepts. For more information, see [User-Data Formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html) in the cloud-init manual.
        /// 
        /// This is not a generalized utility for producing multi-part MIME messages. It's feature set is specialized for cloud-init multi-part MIME messages.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// 
        /// ### Config
        /// ```terraform
        /// data "cloudinit_config" "foobar" {
        ///   gzip          = false
        ///   base64_encode = false
        /// 
        ///   part {
        ///     filename     = "hello-script.sh"
        ///     content_type = "text/x-shellscript"
        /// 
        ///     content = file("${path.module}/hello-script.sh")
        ///   }
        /// 
        ///   part {
        ///     filename     = "cloud-config.yaml"
        ///     content_type = "text/cloud-config"
        /// 
        ///     content = file("${path.module}/cloud-config.yaml")
        ///   }
        /// }
        /// ```
        /// 
        /// ### hello-script.sh
        /// ```shell
        /// #!/bin/sh
        /// echo "Hello World! I'm starting up now at $(date -R)!"
        /// ```
        /// 
        /// ### cloud-config.yaml
        /// ```yaml
        /// #cloud-config
        /// # See documentation for more configuration examples
        /// # https://cloudinit.readthedocs.io/en/latest/reference/examples.html
        /// 
        /// # Install arbitrary packages
        /// # https://cloudinit.readthedocs.io/en/latest/reference/examples.html#install-arbitrary-packages
        /// packages:
        ///   - python
        /// # Run commands on first boot
        /// # https://cloudinit.readthedocs.io/en/latest/reference/examples.html#run-commands-on-first-boot
        /// runcmd:
        ///  - [ ls, -l, / ]
        ///  - [ sh, -xc, "echo $(date) ': hello world!'" ]
        ///  - [ sh, -c, echo "=========hello world=========" ]
        ///  - ls -l /root
        /// ```
        /// 
        /// &lt;!-- This schema was originally generated with tfplugindocs, then modified manually to ensure `part` block list is noted as Required --&gt;
        /// 
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetConfigResult> InvokeAsync(GetConfigArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetConfigResult>("cloudinit:index/getConfig:getConfig", args ?? new GetConfigArgs(), options.WithDefaults());

        /// <summary>
        /// Renders a [multi-part MIME configuration](https://cloudinit.readthedocs.io/en/latest/explanation/format.html#mime-multi-part-archive) for use with [cloud-init](https://cloudinit.readthedocs.io/en/latest/).
        /// 
        /// Cloud-init is a commonly-used startup configuration utility for cloud compute instances. It accepts configuration via provider-specific user data mechanisms, such as `user_data` for Amazon EC2 instances. Multi-part MIME is one of the data formats it accepts. For more information, see [User-Data Formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html) in the cloud-init manual.
        /// 
        /// This is not a generalized utility for producing multi-part MIME messages. It's feature set is specialized for cloud-init multi-part MIME messages.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// 
        /// ### Config
        /// ```terraform
        /// data "cloudinit_config" "foobar" {
        ///   gzip          = false
        ///   base64_encode = false
        /// 
        ///   part {
        ///     filename     = "hello-script.sh"
        ///     content_type = "text/x-shellscript"
        /// 
        ///     content = file("${path.module}/hello-script.sh")
        ///   }
        /// 
        ///   part {
        ///     filename     = "cloud-config.yaml"
        ///     content_type = "text/cloud-config"
        /// 
        ///     content = file("${path.module}/cloud-config.yaml")
        ///   }
        /// }
        /// ```
        /// 
        /// ### hello-script.sh
        /// ```shell
        /// #!/bin/sh
        /// echo "Hello World! I'm starting up now at $(date -R)!"
        /// ```
        /// 
        /// ### cloud-config.yaml
        /// ```yaml
        /// #cloud-config
        /// # See documentation for more configuration examples
        /// # https://cloudinit.readthedocs.io/en/latest/reference/examples.html
        /// 
        /// # Install arbitrary packages
        /// # https://cloudinit.readthedocs.io/en/latest/reference/examples.html#install-arbitrary-packages
        /// packages:
        ///   - python
        /// # Run commands on first boot
        /// # https://cloudinit.readthedocs.io/en/latest/reference/examples.html#run-commands-on-first-boot
        /// runcmd:
        ///  - [ ls, -l, / ]
        ///  - [ sh, -xc, "echo $(date) ': hello world!'" ]
        ///  - [ sh, -c, echo "=========hello world=========" ]
        ///  - ls -l /root
        /// ```
        /// 
        /// &lt;!-- This schema was originally generated with tfplugindocs, then modified manually to ensure `part` block list is noted as Required --&gt;
        /// 
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetConfigResult> Invoke(GetConfigInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetConfigResult>("cloudinit:index/getConfig:getConfig", args ?? new GetConfigInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetConfigArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Specify whether or not to base64 encode the `rendered` output. Defaults to `true`, and cannot be disabled if gzip is `true`.
        /// </summary>
        [Input("base64Encode")]
        public bool? Base64Encode { get; set; }

        /// <summary>
        /// Specify the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
        /// </summary>
        [Input("boundary")]
        public string? Boundary { get; set; }

        /// <summary>
        /// Specify whether or not to gzip the `rendered` output. Defaults to `true`.
        /// </summary>
        [Input("gzip")]
        public bool? Gzip { get; set; }

        [Input("parts")]
        private List<Inputs.GetConfigPartArgs>? _parts;

        /// <summary>
        /// A nested block type which adds a file to the generated cloud-init configuration. Use multiple `part` blocks to specify multiple files, which will be included in order of declaration in the final MIME document.
        /// </summary>
        public List<Inputs.GetConfigPartArgs> Parts
        {
            get => _parts ?? (_parts = new List<Inputs.GetConfigPartArgs>());
            set => _parts = value;
        }

        public GetConfigArgs()
        {
        }
        public static new GetConfigArgs Empty => new GetConfigArgs();
    }

    public sealed class GetConfigInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Specify whether or not to base64 encode the `rendered` output. Defaults to `true`, and cannot be disabled if gzip is `true`.
        /// </summary>
        [Input("base64Encode")]
        public Input<bool>? Base64Encode { get; set; }

        /// <summary>
        /// Specify the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
        /// </summary>
        [Input("boundary")]
        public Input<string>? Boundary { get; set; }

        /// <summary>
        /// Specify whether or not to gzip the `rendered` output. Defaults to `true`.
        /// </summary>
        [Input("gzip")]
        public Input<bool>? Gzip { get; set; }

        [Input("parts")]
        private InputList<Inputs.GetConfigPartInputArgs>? _parts;

        /// <summary>
        /// A nested block type which adds a file to the generated cloud-init configuration. Use multiple `part` blocks to specify multiple files, which will be included in order of declaration in the final MIME document.
        /// </summary>
        public InputList<Inputs.GetConfigPartInputArgs> Parts
        {
            get => _parts ?? (_parts = new InputList<Inputs.GetConfigPartInputArgs>());
            set => _parts = value;
        }

        public GetConfigInvokeArgs()
        {
        }
        public static new GetConfigInvokeArgs Empty => new GetConfigInvokeArgs();
    }


    [OutputType]
    public sealed class GetConfigResult
    {
        /// <summary>
        /// Specify whether or not to base64 encode the `rendered` output. Defaults to `true`, and cannot be disabled if gzip is `true`.
        /// </summary>
        public readonly bool Base64Encode;
        /// <summary>
        /// Specify the Writer's default boundary separator. Defaults to `MIMEBOUNDARY`.
        /// </summary>
        public readonly string Boundary;
        /// <summary>
        /// Specify whether or not to gzip the `rendered` output. Defaults to `true`.
        /// </summary>
        public readonly bool Gzip;
        /// <summary>
        /// [CRC-32](https://pkg.go.dev/hash/crc32) checksum of `rendered` cloud-init config.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// A nested block type which adds a file to the generated cloud-init configuration. Use multiple `part` blocks to specify multiple files, which will be included in order of declaration in the final MIME document.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetConfigPartResult> Parts;
        /// <summary>
        /// The final rendered multi-part cloud-init config.
        /// </summary>
        public readonly string Rendered;

        [OutputConstructor]
        private GetConfigResult(
            bool base64Encode,

            string boundary,

            bool gzip,

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
